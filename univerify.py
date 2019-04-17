import re
import sys

def main():
	#regex for finding emails in the list
	regexes = [
	"\([A-Za-z]+\.edu\)"
	]
	
	#adds all of the emails which follow the regex to a list
	result = []
	for regex in regexes:
		data = open("list.txt", "r")
		for item in data:
			result += re.findall(regex, item)

	#writes list to file
	for data in result:
		file = open('domains.txt', "w")
		file.write(data.replace('(', '').replace(')', '') + "\n")
	
if __name__== "__main__":
  main()