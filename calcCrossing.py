__author__ = "Michael Snider, Kevin Chan"


import prompt
import sys
from PIL import Image


def numZeroesAround(imgArray, (x, y)):
	""" Find number of pixel values of 0 around a given pixel
	"""
	num = 0
	for x_r in range(-1, 2):
		for y_r in range(-1, 2):
			if x_r != 0 or y_r != 0:
				if imgArray[x + x_r][y + y_r] == (0, 0, 0, 255):
					num += 1

	return num

def colorCross(img, (x, y)):
	""" Color the surrounding pixels of a cross red, the center pixel remains black
	"""
	for x_r in range(-1, 2):
		for y_r in range(-1, 2):
			if x_r != 0 or y_r != 0:
					img.putpixel((x + x_r, y + y_r), (255, 0, 0, 0))

	return img


def findCrossings(img):
	""" Calculate the number of crossings on a TSP image
	"""
	crossings = 0

	# 2d list of pixel values
	originalImg = []
	for x in range(img.size[0]):
		colValues = []
		for y in range(img.size[1]):
			colValues.append(img.getpixel((x, y)))
		originalImg.append(colValues)

	# iterate over 9 pixel sections
	for x in range(1, img.size[0] - 1):
		for y in range(1, img.size[1] - 1):
			if originalImg[x][y] == (0, 0, 0, 255) and numZeroesAround(originalImg, (x,y)) >= 4:
				img = colorCross(img, (x, y))
				crossings += 1

	print "Crossings that occur:", crossings
	return img



#prompt for TSP image
filePath = prompt.getSingleString("Enter path to TSP image")

try:
	fileTmp = open(filePath, "r")
	fileTmp.close()

except IOError:
	print "File not found..."
	sys.exit()


image = Image.open(filePath).convert("RGBA")
print "Image converted to rgba..."
print "\t", image.format, image.size, image.mode


# stipple image ****


image = findCrossings(image)


# **********************

print "Saving image..."


# save cross image
separatedFilePath = filePath.rsplit(".", 1)
newFilePath = separatedFilePath[0] + "-cross" + "." + separatedFilePath[1]
try:
	fileTmp = open(newFilePath, "r")
	fileTmp.close()

	if not prompt.yes_no_choice("\tWould you like to overwrite file " + newFilePath):
		print "\tImage was not saved."
		sys.exit()

except IOError:
	pass

image.save(newFilePath)
print "\t", "Saved successfully to", newFilePath
