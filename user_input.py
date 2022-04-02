#Find the nth Occurrence of a word in a string!
string = input(' plz enter a string = ')
substring = input('plz enter a substring = ')
occurrenceint = input('plz enter a number')
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




# Repeated Substring

s1 = input('plz enter  sentance = ')

try:
    def f(s1):
        for m in range(1, len(s1) + 1):
            if s1[0:m] * (len(s1) // m) == s1:
                return (s1[0:m], len(s1) // m)

except:
    print('error')
print(f(s1))

# Simple string matching
import re

s2 = input('plz enter element = ')

s3 = input('plz enter element = ')

try:

    def solve(s2, s3):
        pass
        return bool(re.fullmatch(s2.replace('*', '.*'), s3))


    print(solve(s2, s3))

except:
    print('there a problem')



#Is it a palindrome?
ele=input("plz enter you'r word = ")

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
pal=input('plz enter data= ')
if pal==pal[::-1]:
    print('palindrome')
else:
    print('not palindrome')


#Is it a palindrome?
p = input('plz enter sen = ')
l = reversed(p)
if list(p) == list(l):
    print('palindrome')
else:
    print('not palindrome')

