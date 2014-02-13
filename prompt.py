__author__ = "Michael Snider, Kevin Chan"



def getSingleString(outputMsg = ""):
	""" Prompt outputMsg and accept input
		for the first string entered.
	"""
	retStr = ""

	while retStr == "":
		retStr = raw_input(outputMsg + ": ")
		retStr = retStr.strip()

	retStr = retStr.split()[0]
	return retStr

def yes_no_choice(outputMsg = ""):
	""" Prompt user with a yes/no ([y/n])
		choice, repeating the question until
		the first non-whitespace character entered
		in the user's response is either 'y' or 'n'.
		Returns True for a 'y' response and False for a 'n' response.
	"""
	retSuccess = False
	strResponse = ""

	while strResponse == "":
		strResponse = getSingleString(outputMsg + "[y/n]")
		strResponse = strResponse.strip().lower()

		if strResponse[0] == 'y':
			return True
		elif strResponse[0] != 'n':
			strResponse = ""

	return False


