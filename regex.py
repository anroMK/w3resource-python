import re


#a) Check whether the given strings contain 0xB0. Display a boolean result as shown below.



line1 = 'start address: 0xA0, func1 address: 0xC0'
line2 = 'end address: 0xFF, func2 address: 0xB0'

##print(bool(re.search(r'0xB0', line1)))     ##### add your solution here
#print(bool(re.search(r'0xB0', line2)))     ##### add your solution here



#b) Replace all occurrences of 5 with five for the given string.
ip = 'They ate 5 apples and 5 oranges'

#print(re.sub(r'5', r'five', ip))        ##### add your solution here
'They ate five apples and five oranges'


#c) Replace first occurrence of 5 with five for the given string.

ip = 'They ate 5 apples and 5 oranges'

#print(re.sub(r'5', r'five', ip, count=1))     ##### add your solution here
'They ate five apples and 5 oranges'

#d) For the given list, filter all elements that do not contain e.

items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']

#print([w for w in items if not re.search(r'e', w)])        ##### add your solution here
['goal', 'sit']

#e) Replace all occurrences of note irrespective of case with X.

ip = 'This note should not be NoTeD'

#print(re.sub(r'note', r'X', ip, flags = re.IGNORECASE))        ##### add your solution here
'This X should not be XD'

# f) Check if at is present in the given byte input data.

ip = b'tiger imp goat'

#print(bool(re.search(rb'at', ip)))   ##### add your solution here
True

# g) For the given input string, display all lines not containing start irrespective of case.

para = '''good start
Start working on that
project you always wanted
stars are shining brightly
hi there
start and try to
finish the book
bye'''
'''
pat = re.compile(r'^start', flags=re.I)      ##### add your solution here
for line in para.split('\n'):
    if not pat.search(line):
        print(line)
'''


# h) For the given list, filter all elements that contains either a or w.

items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']

##### add your solution here
#print([w for w in items if re.search(r'[a|w]', w) ])
['goal', 'new', 'eat']


# i) For the given list, filter all elements that contains both e and n.

items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']

##### add your solution here
#print([w for w in items if re.search(r'e', w) and re.search(r'n', w)])
['new', 'dinner']

# j) For the given string, replace 0xA0 with 0x7F and 0xC0 with 0x1F.

ip = 'start address: 0xA0, func1 address: 0xC0'

ip = re.sub(r'A0', r'7F', ip)
ip = re.sub(r'C0', r'1F', ip)
##### add your solution here
#print(ip)
'start address: 0x7F, func1 address: 0x1F'

#ANCHORS

# a) Check if the given strings start with be.

line1 = 'be nice'
line2 = '"best!"'
line3 = 'better?'
line4 = 'oh no\nbear spotted'

pat = re.compile('\Abe')       ##### add your solution here

"""
print(bool(pat.search(line1)))
True
print(bool(pat.search(line2)))
False
print(bool(pat.search(line3)))
True
print(bool(pat.search(line4)))
False
"""


# b) For the given input string, change only whole word red to brown


words = 'bred red spread credible'

#print(re.sub(r'\bred\b', r'brown', words))    ##### add your solution here
'bred brown spread credible'

# c) For the given input list, filter all elements that contains 42 surrounded by word characters.

words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']

#print([w for w in words if re.search(r'\B42\B', w)])  ##### add your solution here
['hi42bye', 'nice1423', 'cool_42a']

# d) For the given input list, filter all elements that start with den or end with ly.

items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']

#print([e for e in items if re.search(r'\Aden', e) or re.search(r'ly\Z', e)])
['lovely', '2 lonely', 'dent']

# e) For the given input string, change whole word mall to 1234 only if it is at the start of a line.

para = '''
ball fall wall tall
mall call ball pall
wall mall ball fall
mallet wallet malls'''

#print(re.sub(r'^mall\b', r'1234', para, flags=re.MULTILINE))    ##### add your solution here
'''
ball fall wall tall
1234 call ball pall
wall mall ball fall
mallet wallet malls
'''

# f) For the given list, filter all elements having a line starting with den or ending with ly.

items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']

#print([word for word in items if re.search(r'^den', word, flags=re.MULTILINE) or re.search(r'ly$', word, flags=re.MULTILINE)])
['lovely', '1\ndentist', '2 lonely', 'fly\nfar', 'dent']

# g) For the given input list, filter all whole elements 12\nthree irrespective of case.

items = ['12\nthree\n', '12\nThree', '12\nthree\n4', '12\nthree']
#print([word for word in items if re.search(r'\A12\nthree\Z', word, flags=re.IGNORECASE)])
['12\nThree', '12\nthree']

# h) For the given input list, replace hand with X for all elements that start with hand followed by at least one word character.

items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']

#print([re.sub(r'\bhand\B', r'X', word) for word in items])
['Xed', 'hand', 'Xy', 'unhanded', 'Xle', 'hand-2']

# i) For the given input list, filter all elements starting with h. Additionally, replace e with X for these filtered elements.

items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']

#print([re.sub(r'e', r'X', word) for word in items if re.search(r'\bh', word)])
['handXd', 'hand', 'handy', 'handlX', 'hand-2']



#ALTERNATION AND GROUPING

# a) For the given input list, filter all elements that start with den or end with ly


items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']

#print([word for word in items if re.search(r'(\Aden|ly\Z)', word)])
['lovely', '2 lonely', 'dent']


# b) For the given list, filter all elements having a line starting with den or ending with ly.

items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']

#print([word for word in items if re.search(r'^den|ly$', word, flags=re.MULTILINE)])
['lovely', '1\ndentist', '2 lonely', 'fly\nfar', 'dent']


# c) For the given input strings, replace all occurrences of removed or reed or received or refused with X.


s1 = 'creed refuse removed read'
s2 = 'refused reed redo received'

pat = re.compile(r'removed|reed|recived|refused')        ##### add your solution here

#print(pat.sub('X', s1))
'cX refuse X read'
#print(pat.sub('X', s2))
'X X redo X'

# d) For the given input strings, replace all matches from the list words with A.


s1 = 'plate full of slate'
s2 = "slated for later, don't be late"
words = ['late', 'later', 'slated']

pat = re.compile('|'.join(words))        ##### add your solution here

#print(pat.sub('A', s1))
'pA full of sA'
#print(pat.sub('A', s2))
"A for A, don't be A"


# e) Filter all whole elements from the input list items based on elements listed in words.

items = ['slate', 'later', 'plate', 'late', 'slates', 'slated ']
words = ['late', 'later', 'slated']

pat = re.compile('|'.join(words))       ##### add your solution here

#print([word for word in items if pat.fullmatch(word)])
['later', 'late']


# Escaping metacharacters

# a) Transform the given input strings to the expected output using same logic on both strings.

str1 = '(9-2)*5+qty/3'
str2 = '(qty+4)/2-(9-2)*5+pq/4'

pat = re.compile(re.escape('(9-2)*5'))
##### add your solution here for str1
#print(re.sub(pat, r'35', str1))
'35+qty/3'
##### add your solution here for str2
#print(re.sub(pat, r'35', str2))
'(qty+4)/2-35+pq/4'

# b) Replace (4)\| with 2 only at the start or end of given input strings.

s1 = r'2.3/(4)\|6 foo 5.3-(4)\|'
s2 = r'(4)\|42 - (4)\|3'
s3 = 'two - (4)\\|\n'

pat = re.compile(r'\A\(4\)\\\||\(4\)\\\|\Z')        ##### add your solution here

#print(pat.sub('2', s1))
'2.3/(4)\\|6 foo 5.3-2'
#print(pat.sub('2', s2))
'242 - (4)\\|3'
#print(pat.sub('2', s3))
'two - (4)\\|\n'

#c c) Replace any matching element from the list items with X for given the input strings. Match the elements from items literally. Assume no two elements of items will result in any matching conflict.

items = ['a.b', '3+n', r'x\y\z', 'qty||price', '{n}']
pat = re.compile('|'.join([re.escape(word) for word in items]))      ##### add your solution here

#print(pat.sub('X', '0a.bcd'))
'0Xcd'
#print(pat.sub('X', 'E{n}AMPLE'))
'EXAMPLE'
#print(pat.sub('X', r'43+n2 ax\y\ze'))
'4X2 aXe'

# d) Replace backspace character \b with a single space character for the given input string.

ip = '123\b456'
"""
>>> ip
'123\x08456'
>>> print(ip)
12456
"""


#print(re.sub('\x08', ' ', ip))      ##### add your solution here
'123 456'

# e) Replace all occurrences of \e with e.

ip = r'th\er\e ar\e common asp\ects among th\e alt\ernations'

#print(ip)
#print(re.sub(r'\\e', r'e', ip))    ##### add your solution here
'there are common aspects among the alternations'

# f) Replace any matching item from the list eqns with X for given the string ip. Match the items from eqns literally.


ip = '3-(a^b)+2*(a^b)-(a/b)+3'
eqns = ['(a^b)', '(a/b)', '(a^b)+2']

##### add your solution here
eqns = sorted(eqns, key=len, reverse=True)
pat = re.compile('|'.join([re.escape(word) for word in eqns]))
#print(pat)

#print(pat.sub('X', ip))
'3-X*X-X+3'


# Dot metacharacter and Quantifiers


# a) Replace 42//5 or 42/5 with 8 for the given input.

ip = 'a+42//5-c pressure*3+42/5-14256'

#print(re.sub(r'42//?5', r'8', ip))    ##### add your solution here
'a+8-c pressure*3+8-14256'

# b) For the list items, filter all elements starting with hand and ending with at most one more character or le.


items = ['handed', 'hand', 'handled', 'handy', 'unhand', 'hands', 'handle']

#print([word for word in items if re.search(r'\Ahand(.|le)?\Z', word)])
##### add your solution here
['hand', 'handy', 'hands', 'handle']

# c) Use re.split to get the output as shown for the given input strings.

eqn1 = 'a+42//5-c'
eqn2 = 'pressure*3+42/5-14256'
eqn3 = 'r*42-5/3+42///5-42/53+a'

pat = re.compile(r'42//?5')

#print(re.split(pat, eqn1))
['a+', '-c']
#print(re.split(pat, eqn2))
['pressure*3+', '-14256']
#print(re.split(pat, eqn3))
['r*42-5/3+42///5-', '3+a']

#  d) For the given input strings, remove everything from the first occurrence of i till end of the string.

s1 = 'remove the special meaning of such constructs'
s2 = 'characters while constructing'

pat = re.compile(r'i.+')        ##### add your solution here

#print(pat.sub('', s1))
'remove the spec'
#print(pat.sub('', s2))
'characters wh'

# e) For the given strings, construct a RE to get output as shown.


str1 = 'a+b(addition)'
str2 = 'a/b(division) + c%d(#modulo)'
str3 = 'Hi there(greeting). Nice day(a(b)'

remove_parentheses = re.compile(r'\(.*?\)')     ##### add your solution here

#print(remove_parentheses.sub('', str1))
'a+b'
#print(remove_parentheses.sub('', str2))
'a/b + c%d'
#print(remove_parentheses.sub('', str3))
'Hi there. Nice day'

# f) Correct the given RE to get the expected output.

words = 'plink incoming tint winter in caution sentient'
change = re.compile(r'int|in|ion|ing|inco|inter|ink')

# wrong output
#print(change.sub('X', words))
'plXk XcomXg tX wXer X cautX sentient'

# expected output
change = re.compile(r'in(ter|co|t|g|k)?|ion')      ##### add your solution here
#print(change.sub('X', words))
'plX XmX tX wX X cautX sentient'


# i) For the given input strings, remove everything from the first occurrence of test (irrespective of case) till end of the string, provided test isn't at the end of the string.


s1 = 'this is a Test'
s2 = 'always test your RE for corner cases'
s3 = 'a TEST of skill tests?'

pat = re.compile(r'test.*', re.IGNORECASE)      ##### add your solution here

#print(pat.sub('', s1))
'this is a Test'
#print(pat.sub('', s2))
'always '
#print(pat.sub('', s3))
'a '

# j) For the input list words, filter all elements starting with s and containing e and t in any order.

words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']

#print([word for word in words if re.search(r'\bs.*(e.*t|t.*e)', word)])
##### add your solution here
['subtle', 'sets', 'site']

# k) For the input list words, remove all elements having less than 6 characters.

words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']

#print([word for word in words if re.search('.{6,}', word)])
['sequoia', 'subtle', 'exhibit']

# l) For the input list words, filter all elements starting with s or t and having a maximum of 6 characters.

words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']

#print([w for w in words if re.fullmatch(r'(s|t).{,5}', w)])
['subtle', 'sets', 'tests', 'site']


# m) Can you reason out why this code results in the output shown? The aim was to remove all <characters> patterns but not the <> ones. The expected result was 'a 1<> b 2<> c'.

ip = 'a<apple> 1<> b<bye> 2<> c<cat>'

#print(re.sub(r'<.+?>', '', ip))
'a 1 2'

# n) Use re.split to get the output as shown below for given input strings.

s1 = 'go there  //   "this // that"'
s2 = 'a//b // c//d e//f // 4//5'
s3 = '42// hi//bye//see // carefully'

pat = re.compile(r' +// +')     ##### add your solution here

#print(pat.split(s1, maxsplit=1))     ##### add your solution here for s1
['go there', '"this // that"']
#print(pat.split(s2, maxsplit=1))     ##### add your solution here for s2
['a//b', 'c//d e//f // 4//5']
#print(pat.split(s3, maxsplit=1))     ##### add your solution here for s3
['42// hi//bye//see', 'carefully']







