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
				if imgArray[x + x_r][y + y_r] == 0:
					num += 1

	return num


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
			if originalImg[x][y] == 0 and numZeroesAround(originalImg, (x,y)) >= 4:
				crossings += 1

	print "Crossings that occur:", crossings




filePath = prompt.getSingleString("Enter path to image")

try:
	fileTmp = open(filePath, "r")
	fileTmp.close()

except IOError:
	print "File not found..."
	sys.exit()


image = Image.open(filePath).convert("L")
print "Image converted to bw..."
print "\t", image.format, image.size, image.mode


# stipple image ****


image = findCrossings(image)


# **********************
