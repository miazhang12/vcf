import vcf
import json
import string
import argparse

#print out the records in vcf file
def print_vcf(filename):
	with open(filename, 'r') as fi: #open file
		vcf_reader = vcf.Reader(fi)
		for record in vcf_reader: #loops through all the records in vcf
			for i in record.ALT: 
				if i == 'T' and record.REF == 'C': #filter out the records with T ALT and C REF
					print(record) #print out the record if meet the criteria

#transform the vcf file into JSON format
def vcfToJSON(filename):
	vcf_reader = vcf.Reader(open(filename))
	with open("vcfToJSON.txt","w") as original:
		recordinJSON = ''
		for record in vcf_reader:
			#print type(str(record.ALT[0]))
			if len(record.ALT) == 1:
				alt = str(record.ALT[0])
			else:
				alt = ''.join(str(record.ALT))
				alt = alt.replace('[', '')
				alt = alt.replace(']', '')				
			recordinJSON = recordinJSON + ('{"CHROM":"'+ record.CHROM + '", "POS":' + str(record.POS) + ', "REF":"' + record.REF + '", "ALT":"' + alt + '" },')
		recordinJSON = recordinJSON[:-1]
		recordinJSON = '[' + recordinJSON + ']'
		original.write(recordinJSON)
	with open("vcfToJSON.txt", "r") as fin:
		content = json.load(fin)
	with open("toJSON.txt", "w") as fout:
		json.dump(content, fout, indent=1)
		
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', help='filename to transform into JSON format')
	args = parser.parse_args()
	
	print_vcf(args.filename)	#call print_vcf function
	vcfToJSON(args.filename)	#call vcfToJSON function

if __name__ == "__main__":
	main()
