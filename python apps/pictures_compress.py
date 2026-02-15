from PIL import Image
import ast
from pathlib import Path
import struct
from itertools import product

def encode(path, newfilename):
    im = Image.open(path).convert("RGB")
    width, height = im.size
    pixels = im.load()

    # We use integer division // 2 to define the new dimensions
    new_width, new_height = width // 2, height // 2

    with open(newfilename + ".qwertyuiop", "w") as file:
        file.write(f"[{new_width},{new_height}]\n")

        for y in range(0, new_height * 2, 2):
            row = []
            for x in range(0, new_width * 2, 2):
                # Get the 4 pixels in the 2x2 block
                p1 = pixels[x, y]
                p2 = pixels[x + 1, y]
                p3 = pixels[x, y + 1]
                p4 = pixels[x + 1, y + 1]

                # Average the Red, Green, and Blue channels
                avg_r = (p1[0] + p2[0] + p3[0] + p4[0]) // 4
                avg_g = (p1[1] + p2[1] + p3[1] + p4[1]) // 4
                avg_b = (p1[2] + p2[2] + p3[2] + p4[2]) // 4
                
                row.append(f"({hex(avg_r)},{hex(avg_g)},{hex(avg_b)})")
            
            file.write("[ " + " , ".join(row) + " ] \n")

def decode(path):
    with open(path, "r") as file:
        size_line = file.readline()
        size = ast.literal_eval(size_line)
        small_width, small_height = size

        # The output image will be twice the size of the encoded data
        im = Image.new("RGB", (small_width * 2, small_height * 2))
        pixels = im.load()

        for y in range(small_height):
            row_line = file.readline().strip()
            row_data = ast.literal_eval(row_line)
            
            for x in range(small_width):
                r, g, b = row_data[x]
                # Values are already integers after ast.literal_eval
                # Fill a 2x2 block in the output image with the averaged color
                pixels[x * 2, y * 2] = (r, g, b)
                pixels[x * 2 + 1, y * 2] = (r, g, b)
                pixels[x * 2, y * 2 + 1] = (r, g, b)
                pixels[x * 2 + 1, y * 2 + 1] = (r, g, b)

    im.show()

# Execution
# encode("./imagepants.jpg", "testfilecomp")
# decode("testfilecomp.qwertyuiop")

def binaryCompressedEncode(path, newfilename):
    pathToFile = Path(path)
    encoding = struct.Struct('>BBB')
    image = Image.open(pathToFile)
    image = image.convert("RGB")
    width, height = image.size

    if( height % 2 == 1 or width % 2 == 1):
        raise ValueError('The file cannot be evenly compressed into squares')
    height, width = height //2 , width // 2
    pixels = image.load()
    with open(newfilename + ".qwertcompbin", "wb") as file:
        file.write(struct.pack('>II', height , width))
 
        for position in product(range(0, height * 2,2) , range(0, width * 2, 2)):
            y = position[0]
            x = position[1]
            
            
            # Get the 4 pixels in the 2x2 block
            p1 = pixels[x, y]
            p2 = pixels[x + 1, y]
            p3 = pixels[x, y + 1]
            p4 = pixels[x + 1, y + 1]

            # Average the Red, Green, and Blue channels
            avg_r = (p1[0] + p2[0] + p3[0] + p4[0]) // 4
            avg_g = (p1[1] + p2[1] + p3[1] + p4[1]) // 4
            avg_b = (p1[2] + p2[2] + p3[2] + p4[2]) // 4

            data = encoding.pack(avg_r, avg_g, avg_b)
            file.write(data)
            
def binaryCompDecode(fileName):
    path = Path(fileName)
    if not path.suffix == ".qwertcompbin":
        raise ValueError("Wrong type of file")
    with open(path, "rb") as file:
        height, width = struct.unpack('>II', file.read(8))
        image = Image.new("RGB", (width * 2, height * 2))
        pixels = image.load()
        encoding = struct.Struct('>BBB')
        for y in range(height):
            for x in range(width):
                data = file.read(3)
                avg_r, avg_g, avg_b = encoding.unpack(data)
                pixels[x * 2, y * 2] = (avg_r, avg_g, avg_b)
                pixels[x * 2 + 1, y * 2] = (avg_r, avg_g, avg_b)
                pixels[x * 2, y * 2 + 1] = (avg_r, avg_g, avg_b)
                pixels[x * 2 + 1, y * 2 + 1] = (avg_r, avg_g, avg_b)
    image.show()
    



if(__name__ == "__main__"):
    binaryCompressedEncode("./imagepants.jpg", "testfilecompbin")
    
    binaryCompDecode("testfilecompbin.qwertcompbin")



