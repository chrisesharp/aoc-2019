from opcodes import Processor, get_program
from keyboard import Keyboard
import sys
import itertools

bad_items = ["escape pod","infinite loop","giant electromagnet","molten lava","photons"]

class ZorkDroid():
    def __init__(self, file_name, input):
        self.program = get_program(file_name)
        self.input_device = input
        self.proc = Processor(self.program, 32768)
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
            else:
                break
            if "".join(result[-8:]).find("Command?") >= 0:
                return False, "".join(result[:-8]).strip()

        last_bit = "".join(result[-50:])
        start = last_bit.find("typing ") + 4
        return True, last_bit[start:start+10]
    
    def action(self, text):
        finished = False
        room, desc, doors, items = self.parse(text)
        commands = []
        self.update_room(room, desc, doors)
        
        if self.current_room == "Security Checkpoint" and len(self.inventory) == 8:
            return self.end_game()
        
        for item in items:
            self.take_item(item, commands)
        
        self.choose_direction(commands)

        while commands:
            command = commands.pop()
            self.input_device.append(command)
        return finished, None

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


    def end_game(self):
        print("Collected all items")
        commands = []
        finished = False
        for permutation in self.all_item_combinatins():
            for item in set(self.inventory):
                self.drop_item(item, commands)
            for item in permutation:
                self.take_item(item, commands)
            commands.append("west\n")
            while commands:
                command = commands.pop(0)
                self.input_device.append(command)
                finished, output = self.move()
                if finished:
                    return finished, output
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
            if line.find("Doors here lead") >= 0:
                line = lines.pop(0)
                while line.find("-") >= 0:
                    doors.append(line[2:])
                    if lines:
                        line = lines.pop(0)
                    else:
                        break
            if line.find("Items here:") >= 0:
                line = lines.pop(0)
                while line.find("-") >= 0:
                    items.append(line[2:])
                    if lines:
                        line = lines.pop(0)
                    else:
                        break
        return room, desc, doors, items

if __name__ == '__main__':
    program = "input.txt"
    interactive = False
    if len(sys.argv) > 1: interactive = True
    droid = ZorkDroid(program, Keyboard())
    finished, output = droid.move()
    while not finished:
        if interactive:
            print(output)
        else:
            finished, output = droid.action(output)
        if finished: break
        finished, output = droid.move()
    print("Part 1:",output)
