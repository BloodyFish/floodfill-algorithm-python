import os
from floodfill import FloodFill


script_dir = os.path.dirname(__file__)
filename = "Floodfill_test.png"

img_dir = os.path.join(script_dir, filename)
output_dir = os.path.join(script_dir, "Filoodfill_test_output.png")

flood_fill = FloodFill(img_dir)
flood_fill.floodfill(color=(0, 255, 0, 255))
flood_fill.saveOutput(output_dir)
flood_fill.img.show()