__author__ = "Michael Snider, Kevin Chan"


from PIL import Image


def stipple(img):
	""" Pass Pillow Image in to allow for a pixel by pixel search and 
		remove considerably whiter pixels based on our algorithm for stippling
	"""

	img = threshold(img, 20)

	return img



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