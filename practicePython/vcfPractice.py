import vcf
import sys

def print_vcf():
	filename = raw_input("Enter Filename: ")
	vcf_reader = vcf.Reader(open(filename))
	record = next(vcf_reader)
	print record.ALT
	
def main():
	print_vcf()

if __name__ == "__main__":
	main()
