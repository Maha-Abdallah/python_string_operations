#Find the nth Occurrence of a word in a string!
string = 'This is an example. Return the nth occurrence of example in this example string.'
substring = 'example'
occurrenceint = 1
try:
    tmp = int(occurrenceint)
    print('excellent')
except:
    print('Error')

def find_nth_occurrence(substring, string, occurrenceint):
    o = -1
    for j in range(occurrenceint):
        o = string.find(substring, o+1)
        if o == -1:
            return -1
    return o
print(find_nth_occurrence(substring, string, tmp))

#Find the nth Occurrence of a word in a string!
s = 'This is an example. Return the nth occurrence of example in this example string.'
su = 'example'
oc = 4
try:
    tm = int(oc)
    print('excellent')
except:
    print('Error')

def findnthoccurrence(su, s, o):
    p = -1
    for m in range(oc):
        p = s.find(su, p+1)
        if p == -1:
            return -1
    return p
print(findnthoccurrence(su, s, tm))


# Repeated Substring

s1 = 'ababab'

try:
    def f(s1):
        for l in range(1, len(s1) + 1):
            if s1[0:l] * (len(s1) // l) == s1:
                return (s1[0:l], len(s1) // l)

except:
    print('error')
print(f(s1))

# Repeated Substring

s11 = 'abcde'

try:
    def f(s11):
        for i in range(1, len(s11) + 1):
            if s11[0:i] * (len(s11) // i) == s11:
                return (s11[0:i], len(s11) // i)

except:
    print('error')
print(f(s11))
# Simple string matching
import re

s2 = 'code*s'

s3 = 'codewars'

try:

    def solve(s2, s3):
        pass
        return bool(re.fullmatch(s2.replace('*', '.*'), s3))


    print(solve(s2, s3))

except:
    print('there a problem')

# Simple string matching
import re

s22 = 'a'

s33 = 'b'

try:

    def solve(s22, s33):
        pass
        return bool(re.fullmatch(s22.replace('*', '.*'), s33))


    print(solve(s22, s33))

except:
    print('there a problem')



#Is it a palindrome?
ele='bro'

try:
    def is_palindrome(ele):
        is_palindrome = ele.find(ele[::-1])
        if is_palindrome == 0:
            return True
        else:
            return False

except:
    print('error')

print(is_palindrome(ele))



#Is it a palindrome?
e='sis'

try:
    def ispalindrome(e):
        ispalindrome = e.find(e[::-1])
        if ispalindrome == 0:
            return True
        else:
            return False

except:
    print('error')

print(ispalindrome(e))


#Is it a palindrome?
pal='121'
if pal==pal[::-1]:
    print('palindrome')
else:
    print('not palindrome')

#Is it a palindrome?
f='123'
if f==f[::-1]:
    print('palindrome')
else:
    print('not palindrome')
#Is it a palindrome?
p = 'sweet'
l = reversed(p)
if list(p) == list(l):
    print('palindrome')
else:
    print('not palindrome')
#Is it a palindrome?
pa = 'anime'
lm = reversed(pa)
if list(pa) == list(lm):
    print('palindrome')
else:
    print('not palindrome')
