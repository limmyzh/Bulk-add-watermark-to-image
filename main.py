from PIL import Image, ImageOps
import os


# Watermark filename: in root folder
watermarkFile = "water.png"
# the input folder name
inputFolder = "images"
# the output folder name
outputFolder = "images_output"
# suffix for watermarking
outputSuffix = "_watermarked"
#position of the watermark
posx = 50
posy = 1500

# load the watermark image
watermark = Image.open(watermarkFile) 

# get files in inputFolder
for filename in os.listdir(inputFolder):
    # if it is a jpg
    if filename.endswith(".jpg"):
        # get the full input file path
        inputFilePath = os.path.join(inputFolder, filename)
        # load the image
        currentImage = Image.open(inputFilePath)
        currentImage = ImageOps.expand(currentImage,border=200,fill='white')
        # paste the watermark
        currentImage.paste(watermark, (posx, posy), watermark)
        # and save final image as PNG
        print("Generating : " + outputFolder + "/" + filename + outputSuffix + ".png")
        currentImage.save(outputFolder + "/" + filename + outputSuffix + ".png" , "PNG", optimize=False, compress_level = 9)

print("==> Process finished")