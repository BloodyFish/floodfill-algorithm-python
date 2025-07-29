from PIL import Image

class FloodFill:
    def __init__(self, image_path):
        self.img = Image.open(image_path)
        self.center_pixel = (int(self.img.size[0] / 2), int(self.img.size[1] / 2))
        self.center_pixel_color = self.img.getpixel(self.center_pixel)
        self.visited = set()
        print(f"The color to be replaced is {self.center_pixel_color}")
        

    def floodfill(self, color):
        stack = []
        stack.append((self.center_pixel[0], self.center_pixel[1]))

        while len(stack) > 0:
            pixel = stack.pop()

            if pixel in self.visited:
                 continue
            
            self.visited.add(pixel)


            if 0 <= pixel[0] < self.img.size[0] and 0 <= pixel[1] < self.img.size[1]:
                if self.img.getpixel((pixel[0], pixel[1])) == self.center_pixel_color:
                        self.img.putpixel((pixel[0], pixel[1]), color)
                        stack.append((pixel[0], pixel[1] + 1))
                        stack.append((pixel[0], pixel[1] - 1))
                        stack.append((pixel[0] + 1, pixel[1]))
                        stack.append((pixel[0] - 1, pixel[1]))

    def saveOutput(self, output_path):
        self.img.save(output_path)