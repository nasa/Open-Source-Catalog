import os
import subprocess
import json

process = subprocess.Popen(["git", "diff", "--name-only", os.environ['TRAVIS_COMMIT_RANGE']], stdout=subprocess.PIPE)
files = process.communicate()[0].decode("utf-8")

# Check if changes were made to code.json
if 'code.json' in files.split():
	print("REGENERATING CATALOG.JSON")
	f = open("./catalog.json", "r")

else:
	print("NO CODE.JSON DIFFS")
	print(json.loads(f.read())[0]['Software'])



