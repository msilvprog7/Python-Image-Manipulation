__author__ = "Michael Snider, Kevin Chan"


import prompt, stipple, connect
import sys
from PIL import Image



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


image = stipple.stipple(image)


# **********************


print "Saving image..."


# save stippled image
separatedFilePath = filePath.rsplit(".", 1)
newFilePath = separatedFilePath[0] + "-stipple" + "." + separatedFilePath[1]
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




# connect image ****


image = connect.connect(image)


# **********************


print "Saving image..."


# save tsp image
separatedFilePath = filePath.rsplit(".", 1)
newFilePath = separatedFilePath[0] + "-tsp" + "." + separatedFilePath[1]
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

