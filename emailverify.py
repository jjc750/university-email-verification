import re
import sys
import univerify
def main():
	
	#if there are more than 2 system arguments, run univerify
	if(len(sys.argv) > 2):
		univerify.main()
	
	#sets up variables
	email = sys.argv[1]	
	valid = False
	emailsplit = email.split("@")
	
	#opens domains.txt, checks to see if email domain is a valid one
	domains = open("domains.txt", "r")
	for domain in domains:
		domain = domain.strip()
		if domain == emailsplit[1]:
			valid = True
			
	#prints/returns validity of email
	print("Email valid? ")
	print(valid)
	return valid
	
if __name__== "__main__":
  main()