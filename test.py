import os
import subprocess


print(os.environ['TRAVIS_COMMIT_RANGE'])
print("\n\n\n")
process = subprocess.Popen(["git", "diff", "--name-only", os.environ['TRAVIS_COMMIT_RANGE']], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)
# CHANGED_FILES = ($(git diff --name-only $TRAVIS_COMMIT_RANGE))