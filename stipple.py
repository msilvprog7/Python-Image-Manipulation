__author__ = "Michael Snider, Kevin Chan"


from PIL import Image
from numpy import *
from random import random


VAR_THRESHOLD = 100				# variance of a quarter must be <= this

MAX_PROB = 0.2					# maximum probability for (pixel value of 0)
MIN_PROB = 0.1					# minimum probability for (pixel value of 255)
OFF_SET = 0.5 					# offset probability


def stipple(img):
	""" Pass Pillow Image in to allow for a pixel by pixel search and 
		quarter the image into fourths, computing the variance and placing
		a stippled dot only when a region has low variance
	"""

	#img = threshold(img, 20)

	# 2d list of pixel values
	originalImg = []
	for x in range(img.size[0]):
		colValues = []
		for y in range(img.size[1]):
			colValues.append(img.getpixel((x, y)))
		originalImg.append(colValues)

	originalImgArray = array(originalImg)
	

	#stippled 2d list of pixels
	pixelValues = []
	for x in range(img.size[0]):
		colValues = []
		for y in range(img.size[1]):
			colValues.append(255)
		pixelValues.append(colValues)


	quarterImage(originalImgArray, pixelValues, (0,0))


	for x in range(img.size[0]):
		for y in range(img.size[1]):
			img.putpixel((x, y), pixelValues[x][y])


	return img



def placeDot(mean):

	return random() > 1 - (MAX_PROB - (mean/255.0) * (MAX_PROB - MIN_PROB))
	#return random() > (mean/255.0) + OFF_SET



def quarterImage(imgArray, pixelValues, (x, y)):
	""" split image array (numpy) into 4ths, pixelValues is in reference to the final stippled image to add dots too,
		(x, y) is in respect to the left-most region of this image for placing dots on the final image
	"""
	centerPoint = (imgArray.shape[0]//2, imgArray.shape[1]//2)



	if centerPoint[0] > 0 and centerPoint[1] > 0:
		firstQuarter = imgArray[:centerPoint[0], :centerPoint[1]]
		#print firstQuarter.shape, var(firstQuarter)

		if var(firstQuarter) > VAR_THRESHOLD:
			quarterImage(firstQuarter, pixelValues, (x, y))
		else:
			firstCenter = (firstQuarter.shape[0]//2 + x, firstQuarter.shape[1]//2 + y)
			if placeDot(mean(firstQuarter)):
				pixelValues[firstCenter[0]][firstCenter[1]] = 0


	if centerPoint[1] > 0:

		secondQuarter = imgArray[centerPoint[0]:, :centerPoint[1]]
		#print secondQuarter.shape, var(secondQuarter)

		if var(secondQuarter) > VAR_THRESHOLD:
			quarterImage(secondQuarter, pixelValues, (x + centerPoint[0], y))
		else:
			secondCenter = (secondQuarter.shape[0]//2 + x + centerPoint[0], secondQuarter.shape[1]//2 + y)
			if placeDot(mean(secondQuarter)):
				pixelValues[secondCenter[0]][secondCenter[1]] = 0


	if centerPoint[0] > 0:

		thirdQuarter = imgArray[:centerPoint[0], centerPoint[1]:]
		#print thirdQuarter.shape, var(thirdQuarter)

		if var(thirdQuarter) > VAR_THRESHOLD:
			quarterImage(thirdQuarter, pixelValues, (x, y + centerPoint[1]))
		else:
			thirdCenter = (thirdQuarter.shape[0]//2 + x, thirdQuarter.shape[1]//2 + y + centerPoint[1])
			if placeDot(mean(thirdQuarter)):
				pixelValues[thirdCenter[0]][thirdCenter[1]] = 0


	fourthQuarter = imgArray[centerPoint[0]:, centerPoint[1]:]
	#print fourthQuarter.shape, var(fourthQuarter)

	if var(fourthQuarter) > VAR_THRESHOLD:
		quarterImage(fourthQuarter, pixelValues, (x + centerPoint[0], y + centerPoint[1]))
	else:
		fourthCenter = (fourthQuarter.shape[0]//2 + x + centerPoint[0], fourthQuarter.shape[1]//2 + y + centerPoint[1])
		if placeDot(mean(fourthQuarter)):
			pixelValues[fourthCenter[0]][fourthCenter[1]] = 0




def threshold(img, value):
	""" Threshold image based on the following rule,
		First go through each column, checking for value differences in pixels.
		Then go through each row, checking for value differences in pixels.
		>= value differences gets assigned a 0 in pixel value
	"""
	pixelValues = []
	for x in range(img.size[0]):
		colValues = []
		for y in range(img.size[1]):
			colValues.append(255)
		pixelValues.append(colValues)


	# column search
	for x in range(img.size[0]):
		for y in range(img.size[1]):

			if y == 0:
				prevYPixel = img.getpixel((x, y))
				continue

			difference = abs(img.getpixel((x, y)) - prevYPixel)
			prevYPixel = img.getpixel((x, y))

			if difference >= value:
				pixelValues[x][y] = 0

	# row search
	for y in range(img.size[1]):
		for x in range(img.size[0]):

			if x == 0:
				prevXPixel = img.getpixel((x, y))
				continue

			difference = abs(img.getpixel((x, y)) - prevXPixel)
			prevXPixel = img.getpixel((x, y))

			if difference >= value:
				pixelValues[x][y] = 0



	for x in range(img.size[0]):
		for y in range(img.size[1]):
			img.putpixel((x, y), pixelValues[x][y])

	return img