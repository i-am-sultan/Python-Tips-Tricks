#checking for anagrams

a = 'lost'
b = 'tsol'
if sorted(a) == sorted(b):
    print('anagram')
else:
    print('not anagram')