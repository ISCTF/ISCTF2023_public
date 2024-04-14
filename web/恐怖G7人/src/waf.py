import re

waf_words = {"setstate","exec","key","os",'system','eval','popen','subprocess','command','run','read','output','cat','ls','grep','global','flag','\\nR','ntimeit'}

def waf(string):
	for i in waf_words:
		if re.findall(i, str(string), re.I):
			print(i)
			return False
	pattern_unicode = r'\\u[0-9a-fA-F]{4}'
	pattern_R1 = r'\\nR'
	pattern_R2 = r'\\ntimeit'
	m1 = re.findall(pattern_unicode,str(string))
	m2 = re.findall(pattern_R1, str(string))
	m3 = re.findall(pattern_R2, str(string))
	if any([m1,m2,m3]):
		print(m1,m2,m3)
		return False
	return True