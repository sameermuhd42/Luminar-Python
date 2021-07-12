# Pattern matching
# re - Package for pattern matching

import re

count = 0
matcher = re.finditer('ab', 'abaaabaaab')
print(matcher)
for i in matcher:
    print("Match at:", i.start())
    print('Group:', i.group())
    count += 1
print("count:", count)

# pat = '[abc]'           # either a, b or c
# matcher = re.finditer(pat, 'ab atac@baaab')
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

# pat = '[^abc]'           # except a, b or c
# matcher = re.finditer(pat, 'ab atac@baaab')
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

# pat = '[a-zA-Z]'           # either a to z or A to Z
# matcher = re.finditer(pat, 'ab ataFLgc@bafab')
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

# pat = '[0-9]'           # either 0 to 9
# matcher = re.finditer(pat, 'a1b ataF5c@bafa4b')
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

# pat = '[^a-zA-Z0-9]'           # special symbols
# matcher = re.finditer(pat, 'a1b a/F5c@bafa4b')
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

pat = '\s'           # space
matcher = re.finditer(pat, 'a1b ataF5c@bafa4b')
print(matcher)
for i in matcher:
    print("Match at:", i.start())
    print('Group:', i.group())
