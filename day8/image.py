from PIL import Image, ImageColor

class SpaceImage():
    img_layers = None
    width = None
    height = None

    def __init__(self, input, width, height):
        self.width = width
        self.height = height
        self.img_layers = []
        while len(input) > 0:
            layer = []
            for _ in range(height*width):
                if (len(input) > 0):
                    layer.append(int(input[0]))
                    input = input[1:]
            self.img_layers.append(layer)

    def fewest_zeros(self):
        fewest_zeros = self.width * self.height
        layer_found = None
        for layer in self.img_layers:
            zeros = layer.count(0)
            if zeros < fewest_zeros:
                fewest_zeros = zeros
                layer_found = layer
        return layer_found

    
    def layers(self):
        return self.img_layers
    
    def flatten(self):
        output_layer = [[[] for x in range(self.width)] for y in range(self.height)]
        for i in reversed(range(len(self.img_layers))):
            layer = self.img_layers[i]
            for y in range(self.height):
                for x in range(self.width):
                    pixel = layer[self.width * y + x]
                    if  pixel != 2:
                        output_layer[y][x] = pixel
        return output_layer
    
    def __str__(self):
        im = Image.new('1', (self.width,self.height))
        output_string = "\n"
        output_layer = self.flatten()
        for y in range(self.height):
            for x in range(self.width):
                if output_layer[y][x]:
                    im.putpixel((x,y), ImageColor.getcolor('white', '1'))
                output_string += str(output_layer[y][x])
            output_string += "\n"
        file = "output.png"
        im.save(file)
        return output_string


if __name__ == '__main__':
    file = open("input.txt")
    line = file.readline().rstrip()
    image = SpaceImage(line, 25, 6)
    layer = image.fewest_zeros()
    ones = layer.count(1)
    twos = layer.count(2)
    print("Part 1:", ones * twos)
    print("Part 2:", image)