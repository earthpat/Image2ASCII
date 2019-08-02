from PIL import Image
from numpy import*
import math

asciiVals = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

print(len(asciiVals))

im = Image.open("image.png")
print("Success!")
width, height = im.size
print("The height and width of this image is: " + str(width) + " " + str(height))

rgb_im = im.convert('RGB')

arr = [[] for x in range(width)]

for x in range(width):
    for y in range(height):
        arr[x].append(rgb_im.getpixel((x, y)))

widthCounter = 0
for x in range(width):
    for y in range(height):
        r, g, b = rgb_im.getpixel((x, y))
        arr[x][y] = asciiVals[math.floor(
            65*(((math.floor(((r + g + b) / 3))) - 1)/255))]
        widthCounter += 1
        if (widthCounter == width):
            widthCounter = 0
            print(arr[x][y])
        else:
            print(arr[x][y], end=" ")
