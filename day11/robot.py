from opcodes import Processor, get_program
from direction import Direction, left, right, next_location
from PIL import Image, ImageColor

class Robot():
    direction = None
    proc = None
    location = None
    top_left = None
    bottom_right = None

    def __init__(self, processor=None):
        self.proc = processor
        self.direction = Direction.UP
        self.location = (0,0)
        self.top_left = (0,0)
        self.bottom_right = (0,0)
    
    def step(self, turn_right):
        if turn_right:
            self.direction = right(self.direction)
        else:
            self.direction = left(self.direction)
        self.location = next_location(self.location, self.direction)
        self.update_extents()
    
    def update_extents(self):
        self.top_left = (min(self.top_left[0],self.location[0]), 
                         min(self.top_left[1],self.location[1]))
        self.bottom_right = (max(self.bottom_right[0], self.location[0]),
                             max(self.bottom_right[1], self.location[1]))
    
    def run(self, panels):
        input = [panels[self.location]]
        self.proc.set_std_input(input)
        outputs = []
        output = None
        while self.proc.step():
            output = self.proc.get_std_output()
            if output != None:
                outputs.append(output)
            if len(outputs) == 2:
                paint, turn = outputs
                outputs.clear()
                panels[self.location] = paint
                self.step(turn)
                input.insert(0,panels.get(self.location,0))
        return panels
    
    def display(self, panels, n):
        width = self.bottom_right[0] - self.top_left[0]
        height = self.bottom_right[1] - self.top_left[1]
        im = Image.new('1', (width+1,height+1))
        output_string = "\n"
        
        for y in range(height+1):
            for x in range(width+1):
                panel = (self.top_left[0] + x, self.top_left[1] + y)
                paint = panels.get(panel,0)
                if paint:
                    im.putpixel((x,y), ImageColor.getcolor('white', '1'))
                    output_string += "#"
                else:
                    output_string += " "
            output_string += "\n"
        im.save("output_" + str(n) + ".png")
        return output_string


if __name__ == '__main__':
    file = "input.txt"
    prog = get_program(file)
    print("Part 1:")
    processor = Processor(prog, 512, True)
    robot = Robot(processor)
    panels = {(0,0):0}
    panels = robot.run(panels)
    print(len(panels.keys()))
    print(robot.display(panels,1))
    
    print("Part 2:")
    processor = Processor(prog, 512, True)
    robot = Robot(processor)
    panels = {(0,0):1}
    panels = robot.run(panels)
    print(robot.display(panels,2))





