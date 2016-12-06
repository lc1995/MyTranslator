import urllib
import json

serviceurl = 'https://translation.googleapis.com/language/translate/v2?'
serviceurl2 = 'https://translation.googleapis.com/language/translate/v2/detect?'

print 'Welcome to My Translator!\n'
print 'Enter word or sentence to translate in Chinese or English.\n'
print 'Enter EnterKey to exit.\n\n'

while True:
	t_text = raw_input('Enter - ')
	if(len(t_text) < 1):
		break
	
	# Detect the language
	parameters = {'key':'AIzaSyCF9-tN_jND33ZqQ697Tfhg0pUTxQ9Bzgw', 'q':t_text}
	url = serviceurl2 + urllib.urlencode(parameters)
	connection = urllib.urlopen(url)
	data = connection.read()
	jsonData = json.loads(data)

	if jsonData['data']['detections'][0][0]['language'] == 'zh-CN':
		parameters = {'key':'AIzaSyCF9-tN_jND33ZqQ697Tfhg0pUTxQ9Bzgw', 'q':t_text, 'source':'zh-CN', 'target':'en', 'format':'text'}
	else:
		parameters = {'key':'AIzaSyCF9-tN_jND33ZqQ697Tfhg0pUTxQ9Bzgw', 'q':t_text, 'source':'en', 'target':'zh-CN', 'format':'text'}

	# Generate Connection
	url = serviceurl + urllib.urlencode(parameters)

	connection = urllib.urlopen(url)
	data = connection.read()
	jsonData = json.loads(data)

	if 'error' in jsonData:
		print 'Error Input!'
		continue

	# print every possible results
	for translation in jsonData['data']['translations']:
		print translation['translatedText']
	print ''

print 'Goodbye!'
