import vcf
import sys
import string

def print_vcf():
	filename = raw_input("Enter Filename: ") #user input for the filename
	vcf_reader = vcf.Reader(open(filename)) #open file
	for record in vcf_reader: #loops through all the records in vcf
		for i in record.ALT: 
			if i == 'T' and record.REF == 'C': #filter out the records with T ALT and C REF
				print record #print out the record if meet the criteria
				
def main():
	print_vcf()	#call print_vcf function

if __name__ == "__main__":
	main()
