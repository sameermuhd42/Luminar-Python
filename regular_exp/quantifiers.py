import re

# pat = 'a+'
# s = 'aaa abc aaaa cga'
# matcher = re.finditer(pat, s)
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

# pat = 'a*'
# s = 'aaa abc aaaa cga'
# matcher = re.finditer(pat, s)
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

# pat = 'a?'
# s = 'aaa abc aaaa cga'
# matcher = re.finditer(pat, s)
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

# pat = 'a{4}'
# s = 'aaa abc aaaa cga'
# matcher = re.finditer(pat, s)
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

# pat = 'a{2,3}'
# s = 'aaa abc aaaa cga'
# matcher = re.finditer(pat, s)
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

# pat = '^a'
# s = 'aaa abc aaaa cga'
# matcher = re.finditer(pat, s)
# print(matcher)
# for i in matcher:
#     print("Match at:", i.start())
#     print('Group:', i.group())

pat = 'a$'
s = 'aaa abc aaaa cga'
matcher = re.finditer(pat, s)
print(matcher)
for i in matcher:
    print("Match at:", i.start())
    print('Group:', i.group())
