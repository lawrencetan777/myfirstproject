from PIL import Image
import ast

def encode(path, newfilename):
    im = Image.open(path).convert("RGB")
    pixels = im.load()

    with open(newfilename + ".qwertyuiop", "w") as file:
        file.write(f"[{im.size[0]},{im.size[1]}]\n")

        for y in range(im.size[1]):
            row = []
            for x in range(im.size[0]):
                r, g, b = pixels[x, y]
                row.append(f"({r},{g},{b})")
            tempText = "[ " + " , ".join(row) + " ] \n"
            file.write(tempText)

encode("./imagepants.jpg", "testfile")
encoded_path = "testfile.qwertyuiop"

def decode(path):
    with open(path, "r") as file:
        size_line = file.readline()
        size = ast.literal_eval(size_line)
        width, height = size

        im = Image.new("RGB", (width, height))
        pixels = im.load()

        for y in range(height):
            row_line = file.readline().strip()
            row_data = ast.literal_eval(row_line)
            
            for x in range(width):
                r, g, b = row_data[x]
                pixels[x, y] = (r, g, b)

    im.show()

decode(encoded_path)