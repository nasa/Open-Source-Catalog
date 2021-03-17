import json
from tools import *

f = open("/Users/etyates/src/github/Open-Source-Catalog/code.json","r")
cod = json.loads(f.read())['releases']
f.close()

f = open("/Users/etyates/src/github/Open-Source-Catalog/catalog.json","r")
cat = json.loads(f.read())
f.close()

def check(n):
	for pr in cod:
		if n == pr['name']:
			# print('YES')
			return True
	print('   NO')
	return False

for p in cat:
	# if p['permissions']['usageType'] == 'openSource':
	check(p['Software'])
