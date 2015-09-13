'''
The Long Way...
===============
'''
def isPhoneNumber(text):
	'''
	Takes a string and searches it for a XXX-XXX-XXXX phone number

	This function as described in the book used str.isDecimal(), which is
	only available in Python3. str.isDigit() is almost always equivolent,
	with rare exceptions including superscript digits (e.g. number squared)
	'''
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdigit():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdigit():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdigit():
			return False
	return True

# message = 'call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
# 	chunk = message[i:i+12]
# 	print chunk
# 	if isPhoneNumber(chunk):
# 		print 'Phone number found ' + chunk
# print 'Done'

'''
And Now... Regular Expressions
==============================
'''
# the regular expressions module (std lib)
import re

# creates a regex object
# using r'string' (raw) format so I don't have to type the escape '\' ten times
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# match object is returned
mo = phoneNumRegex.search('My number is 415-555-4242.')

# match object can return actual string using group() method
# is search() doesnt find a match, mo = None
# if mo:
# 	print 'Phone number found: ' + mo.group()

'''
Groups with ()
==============
'''
# note the parentheses
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('my number is 404-123-8472.')

# can select specific grouping to return
# for i in range(0, 3):
# 	print mo.group(i)

# note the plural form
# returns all groups as a tuple
# areaCode, mainNumber = mo.groups()
# print areaCode
# print main

# searching for '(' requires escape '\'
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('my number is (404) 555-9999')
# print mo.group(1)
# print mo.group(2)

'''
Pipes (or) with |
=================
'''
# Pipe to search for either item
# note there is no space on either side of '|', else the space
# will be part of the search e.g. 'Batman ' != 'Batman.'
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
#print mo1.group()
mo2 = heroRegex.search('Tina Fey and Batman.')
#print mo2.group()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
# print mo.group()
# print mo.group(1)

# search for '|' by using '\|'

'''
Optional Matching with ?
========================
'''
# ? flags preceding group as optional
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
# print mo1.group(), '\n', mo2.group()

# searching for numbers w/ or w/o an area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo2 = phoneRegex.search('My number is 555-4242')
# print mo1.group(), '\n', mo2.group()

# search for '?' with '\?'

'''
Matching Zero or More with *
============================
'''
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowoman')
# print mo1.group(), '\n', mo2.group(), '\n', mo3.group()

# search for * with \*

'''
Matching One or More with +
===========================
'''
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowoman')
# print mo1 == None
# print mo2.group(), '\n', mo3.group()

# search for + with \+

'''
Matching Repititions with {}
============================
'''
# (Ha){3} is equivolent to:
# (Ha)(Ha)(Ha)

# (Ha){3,5} is equivolent to:
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

# {} are greedy by default; they return the longest possible string
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
# print mo1.group()

# NOTE: The ? here has nothing to do with its optional matching use above.
# This is a completely separate usage of the ? character
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
# print mo2.group()

'''
findall()
=========
'''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print mo.group()
# >>> '415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
# print phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# >>> ['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# print phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# >>> [('415', '555', '9999'), ('212', '555', '0000')]

'''
Character Classes
=================

\d 	numeric digit 0 to 9
\D 	none of the above

\w 	letter, numeric digit, or underscore
\W 	none of the above

\s 	space, tab, or newline character
\S 	none of the above
'''

xmasRegex = re.compile(r'\d+\s\w+')
# print xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# >>> ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

'''
Custom Character Classes with [] and ^
======================================
'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
# print vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
# >>> ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

consonantRegex = re.compile(r'[^aeiouAEIOU]')
# print consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
# >>> ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

'''
Beginning and End of string search with ^ and $
===============================================
'''
beginsWithHello = re.compile(r'^Hello')
# print beginsWithHello.search('Hello world!')
# >>> <_sre.SRE_Match object; span=(0, 5), match='Hello'>
# print beginsWithHello.search('He said hello.') == None
# >>> True

endsWithNumber = re.compile(r'\d$')
# print endsWithNumber.search('Your number is 42')
# >>> <_sre.SRE_Match object; span=(16, 17), match='2'>
# print endsWithNumber.search('Your number is forty two.') == None
# >>> True

wholeStringIsNum = re.compile(r'^\d+$')
# print wholeStringIsNum.search('1234567890')
# >>> <_sre.SRE_Match object; span=(0, 10), match='1234567890'>
# print wholeStringIsNum.search('12345xyz67890') == None
# >>> True
# print wholeStringIsNum.search('12 34567890') == None
# >>> True

'''
Wildcard with .
===============
'''
# matches anything but newline
atRegex = re.compile(r'.at')
# print atRegex.findall('The cat in the hat sat on the flat mat.')
# >>> ['cat', 'hat', 'sat', 'lat', 'mat']

# matches everything and anything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# print mo.group(1)
# >>> 'Al'
# print mo.group(2)
# >>> 'Sweigart'

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print mo.group()
# >>> '<To serve man>'

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
# print mo.group()
# '<To serve man> for dinner.>'

# matching \n
noNewlineRegex = re.compile('.*')
# print noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# >>>'Serve the public trust.'
newlineRegex = re.compile('.*', re.DOTALL)
# print newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# >>> 'Serve the public trust.\nProtect the innocent.\nUphold the law.'

'''
Review
======
? matches zero or one of the preceding group.
* matches zero or more of the preceding group.
+ matches one or more of the preceding group.
{n} matches exactly n of the preceding group.
{n,} matches n or more of the preceding group.
{,m} matches 0 to m of the preceding group.
{n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
. matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn't between the brackets
'''

'''
Case-Insensitive Matching
=========================
'''
robocop = re.compile(r'robocop', re.I)
# print robocop.search('Robocop is part man, part machine, all cop.').group()
# >>> 'Robocop'

# print robocop.search('ROBOCOP protects the innocent.').group()
# >>> 'ROBOCOP'

# print robocop.search('Al, why does your programming book talk about robocop so much?').group()
# >>> 'robocop'

'''
sub()
=====
'''
namesRegex = re.compile(r'Agent \w+')
# print namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# >>> 'CENSORED gave the secret documents to CENSORED.'

agentNamesRegex = re.compile(r'Agent (\w)\w*')
# print agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# >>> 'A**** told C**** that E**** knew B**** was a double agent.'

'''
Complex Regexes
===============
'''
# hard to read
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# much better
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

'''
Using IGNORCASE, DOTALL, and VERBOSE together
=============================================
'''
# compile() takes only two arguments
# can use | as bitwise operator to get around this
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)












