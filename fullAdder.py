#Luke McEvoy
#Created on 10/20/18
#HW 7

#I pleadge my honor I have abided by the Stevens Honor System


#returns a string representing the number N in base B 
def numToBaseB(n,b):
    if n == 0:
        return ''
    return str(numToBaseB(n//b,b)) + str(n % b)

#return an integer in base 10 representing the same number as S
def baseBToNum(s, b):
    if len(s) == 0:
        return 0
    return (int(s[0]) * b**(len(s)-1)) + baseBToNum(s[1:len(s)],b)

#return a string representing the same number in base B2'''
def baseToBase(b1, b2, sinb1):
    x = baseBToNum(sinb1, b1)
    return numToBaseB(x, b2)
#two binary strings S and T as input and returns their sum, also in binary
def add(s, t):
    x = baseBToNum(s, 2) + baseBToNum(t, 2)
    return numToBaseB(x, 2)

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = \
    { ('0','0','0') : ('0','0'),
    ('0','0','1') : ('1','0'),
    ('0','1','0') : ('1','0'),
    ('0','1','1') : ('0','1'),
    ('1','0','0') : ('1','0'),
    ('1','0','1') : ('0','1'),
    ('1','1','0') : ('0','1'),
    ('1','1','1') : ('1','1') }

#return a new string representing the sum of the two input strings
def addB(s1,s2):
    def helper(s1,s2, carryin):
        if s1 == '' and s2 == '' and carryin != '0':
            return carryin
        elif s1 == '' and s2 == '':
            return ''
        elif s1 == '' and s2 != '':
            x = FullAdder[('0', s2[-1], carryin)]
            return x[1] + x[0]
        elif s2 == '' and s1 != '':
            x = FullAdder[(s1[-1], '0', carryin)] 
            return x[1] + x[0]
        x = FullAdder[(s1[-1],s2[-1],carryin)]
        #x = (1,0)
        return helper(s1[:-1], s2[:-1], x[1]) + x[0]
    return helper(s1,s2, '0')


