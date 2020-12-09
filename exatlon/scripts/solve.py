passwordE = [1152,1344,1056,1968,1728,816,1648,784,1584,816,1728,1520,1840,1664,784,1632,1856,1520,1728,816,1632,1856,1520,784,1760,1840,1824,816,1584,1856,784,1776,1760,528,528,2000]
smallLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
bigLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

offsetNumbers = 768 #code for 1
offsetBigStart = 1040 #code of 'A'
offsetSmallStart = 1552 #code of 'a'
flag = ""

for i in range(0,len(passwordE)):
    letter = passwordE[i]
    try:
        if(letter < offsetBigStart):
            letter = letter - offsetNumbers
            flag = flag + (numbers[int(letter/16)])
        elif(letter - offsetSmallStart <= 0):
            letter = letter - offsetBigStart
            flag = flag + (bigLetters[int(letter/16)])
        else:
            letter = letter - offsetSmallStart
            flag = flag + (smallLetters[int( letter/16)])
    except(IndexError):
        flag = flag + ("▢")
print(flag)
