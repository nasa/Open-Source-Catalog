import os
import subprocess
import json

# process = subprocess.Popen(["git", "diff", "--name-only", os.environ['TRAVIS_COMMIT_RANGE']], stdout=subprocess.PIPE)
process = subprocess.Popen(["git", "diff", "--name-only"], stdout=subprocess.PIPE)
files = process.communicate()[0].decode("utf-8")

# Check if changes were made to code.json
if 'code.json' in files.split():
	print("REGENERATING CATALOG.JSON")
	f = open("./catalog.json", "a")
	f.write("This is a text addition")
	f.close()
	process1 = subprocess.Popen(["git", "add", "*"], stdout=subprocess.PIPE)
	process2 = subprocess.Popen(["git", "commit", "-m", "automatic submit"], stdout=subprocess.PIPE)
	process3 = subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)

else:
	print("NO CODE.JSON DIFFS")
	

