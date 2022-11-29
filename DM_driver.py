from DM import run_DM
import os

def main():
	successes = 0
	failures = 0
	directory = '/mnt/c/RTS_Project'	# Location of where file generator script made input files
	with os.scandir(directory) as it:
		for entry in it:
			if entry.name.endswith('.txt') and entry.is_file():
				rv = run_DM(entry.name)
				if rv == 1:
					successes += 1
				else:
					failures += 1
				print('\n\n')
				print(str(successes) + ' successes and ' + str(failures) + ' failures')

if __name__ == "__main__":
	main()

