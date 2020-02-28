from opcodes import Processor, get_program
from keyboard import Keyboard
import sys
import itertools

bad_items = ["escape pod","infinite loop","giant electromagnet","molten lava","photons"]

def is_command_prompt(result):
    return "".join(result[-8:]).find("Command?") >= 0

def stripped(result):
    return "".join(result[:-8]).strip()

def keypin_from_output(result):
    last_bit = "".join(result[-50:])
    start = last_bit.find("typing ") + 4
    return last_bit[start:start+10]


class ZorkDroid():
    def __init__(self, file_name, input):
        self.program = get_program(file_name)
        self.input_device = input
        self.proc = Processor(self.program, 4096)
        self.proc.set_std_input(self.input_device)
        self.inventory = set()
        self.rooms = {}
        self.current_room = None
    
    def move(self):
        result = []
        while True:
            output = self.proc.run_to_output()
            if output:
                result.append(chr(output))
                if is_command_prompt(result):
                    return False, stripped(result)
            else: break
        return True, keypin_from_output(result)
    
    def action(self, text):
        finished = False
        room, desc, doors, items = self.parse(text)
        commands = []
        self.update_room(room, desc, doors)
        
        if self.current_room == "Security Checkpoint" and len(self.inventory) == 8:
            return self.pass_security()
        
        for item in items:
            self.take_item(item, commands)
        self.choose_direction(commands)
        return False, commands

    def update_room(self, room, desc, doors):
        if room:
            self.current_room = room
            if room not in self.rooms:
                self.rooms[room] = {"desc":desc,"doors":doors,"choice":0}
    
    def take_item(self, item, commands):
        if item not in bad_items:
            self.inventory.add(item)
            commands.append("take " + item + "\n")
    
    def drop_item(self, item, commands):
        commands.append("drop " + item + "\n")
        self.inventory.discard(item)
    
    def choose_direction(self, commands):
        directions = self.rooms[self.current_room]["doors"]
        choice = (self.rooms[self.current_room]["choice"] + 1) % len(directions)
        self.rooms[self.current_room]["choice"] = choice
        direction = directions[choice]
        commands.append(direction + "\n")

    def follow_commands(self, commands):
        while commands:
            command = commands.pop(0)
            self.input_device.append(command)
            finished, output = self.move()
            if finished:
                return finished, output
        return False, output

    def pass_security(self):
        print("Collected all items and at Security Gate")
        commands = []
        finished = False
        for permutation in self.all_item_combinatins():
            for item in set(self.inventory):
                self.drop_item(item, commands)
            for item in permutation:
                self.take_item(item, commands)
            commands.append("west\n")
            print("Trying to pass with ", permutation)
            finished, output = self.follow_commands(commands)
            if finished: break
        return finished, output
    
    def all_item_combinatins(self):
        combinations = []
        for i in range(2,len(self.inventory)):
            combinations.extend(list(itertools.combinations(self.inventory, i)))
        return combinations
    
    def parse(self, text):
        if text.find("== Pressure-Sensitive Floor ==") >= 0:
            text = text[210:]
        doors = []
        items = []
        lines = text.splitlines()
        if len(lines) < 3:
            return None, None, [],[]
        room = lines.pop(0)[3:-3]
        desc = lines.pop(0)
        while lines:
            line = lines.pop(0)
            if line.find("Doors") >= 0:
                doors = self.get_list(lines)
            if line.find("Items") >= 0:
                items = self.get_list(lines)
        return room, desc, doors, items
    
    def get_list(self, lines):
        things = []
        line = lines.pop(0)
        while line.find("-") >= 0:
            things.append(line[2:])
            if lines:
                line = lines.pop(0)
            else:
                break
        return things


if __name__ == '__main__':
    program = "input.txt"
    interactive = False
    if len(sys.argv) > 1: interactive = True
    droid = ZorkDroid(program, Keyboard())
    finished, output = droid.move()
    commands = []
    while not finished:
        if interactive:
            print(output)
            finished, output = droid.move()
        else:
            finished, commands = droid.action(output)
            if finished: 
                output = commands
                break
            finished, output = droid.follow_commands(commands)
    print("Part 1: PIN code is ",output)
