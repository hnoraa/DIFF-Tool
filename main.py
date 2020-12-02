#!/usr/bin/python3
import sys
import files as f

def main():
	if len(sys.argv) == 1 or len(sys.argv) > 3:
		print('Usage: python3 main.py sourceFile targetFile')
	else:
		# compare the two files
		src = sys.argv[1]
		tar = sys.argv[2]

		if not (f.file_exists(src) or f.file_exists(tar)):
			print('Usage: python3 main.py sourceFile targetFile\nERROR: Cannot find one or both files!')
			return None

		if not (f.is_file(src) or f.is_file(tar)):
			print('Usage: python3 main.py sourceFile targetFile\nERROR: One or both files is a directory!')
			return None
	 
		print('Comparing Source: {:s} with Target: {:s}\nAnalysis:'.format(src, tar))

		if src == tar:
			print('Source and Target are the same file!')

		if f.equal_size(src, tar):
			print('Files are the same size')
		elif f.source_larger(src, tar):
			print('Source file is larger than Target')
		else:
			print('Target file is larger than Source')

		print('Source size {:d} bytes\nTarget size {:d} bytes'.format(f.file_size(src), f.file_size(tar)))

if __name__ == '__main__':
	main()