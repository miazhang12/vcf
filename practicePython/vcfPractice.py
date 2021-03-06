import vcf
import json
import string
import argparse

#transform the vcf file into JSON format by one line
def vcfToJSON_line(record):
	recordinJSON = ''
	if len(record.ALT) == 1: #change format of record.ALT depending on the length of the content
		alt = str(record.ALT[0])
	else:
		alt = ''.join(str(record.ALT))
		alt = alt.replace('[', '')
		alt = alt.replace(']', '')				
	recordinJSON = recordinJSON + ('{"CHROM":"'+ record.CHROM + '", "POS":' + str(record.POS) + ', "REF":"' + record.REF + '", "ALT":"' + alt + '" }') #transform the vcf data into json format
	return recordinJSON

def allvcfToJSON(filename):
	with open(filename, 'r') as fi: #open file
		vcf_reader = vcf.Reader(fi)
		first = True
		allinJSON = '';
		for record in vcf_reader:
			content = vcfToJSON_line(record)
			if first:
				allinJSON += '['
				allinJSON += content
				#print('['),
				print(content)
				print(json.dumps(content, indent=1))
				first = False
			else:
				allinJSON += ','
				allinJSON += content
				#print(',')
				#print(vcfToJSON_line(record))
		allinJSON += ']'
		return json.dumps(allinJSON, sort_keys = True, indent=4)

#transform the vcf file into JSON format
#does transformations all at once, and writes it to output file rather than printing
def vcfToJSON(filename):
	with open(filename, 'r') as fi: #open file
		vcf_reader = vcf.Reader(fi)
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
	with open("output.txt", "w") as fout:
		json.dump(content, fout, indent=1)

def main():
	parser = argparse.ArgumentParser()
	
	parser.add_argument('filename', help='filename to transform into JSON format')
	
	args = parser.parse_args()
	
	allvcfToJSON(args.filename)
	#vcfToJSON_line(args.filename)
	#vcfToJSON(args.filename)	#call vcfToJSON function

if __name__ == "__main__":
	main()
