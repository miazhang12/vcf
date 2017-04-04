import vcf
import json
import string
import argparse

#print out the record in vcf file after filtering
def filter_vcf(filename):
	with open(filename, 'r') as fi: #open file
		vcf_reader = vcf.Reader(fi)
		#ask for what to filter
		ref = input('REF: ')
		alt = input('ALT: ')
		for record in vcf_reader: #loops through all the records in vcf
			for i in record.ALT:
				if i == alt and record.REF == ref:
					return record

def main():
	parser = argparse.ArgumentParser()
	
	parser.add_argument('filename', help='filename to transform into JSON format')
	
	args = parser.parse_args()
	filter_vcf(args.filename)
	
if __name__ == "__main__":
	main()
