I first tryed to use **Binary Ninja** to look into the binary but the binary is clearly obfuscated so I used **DIE** to see the obfuscation methon and sure enought the obfuscation method is **UPX** 

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/exatlon/images/1.png?raw=true)

So I hopped into a Linux Machine to try and de obfuscate it and I used **upx -d exatlon_v1 -o exatlon_v1_clear** and got a clear code so I opened this one and tryed ot see what is going on.
But **Binary Ninja** did not done the trick for me so I hopped into **IDA** and sure enought I got some constant strings. 
And we got some sort of password but it seams to be crypted in some way

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/exatlon/images/2.png?raw=true)

but let's try 

```
1152 1344 1056 1968 1728 816 1648 784 1584 816 1728 1520 1840 1664 784 1632 1856 1520 1728 816 1632 1856 1520 784 1760 1840 1824 816 1584 1856 784 1776 1760 528 528 2000```

and as I said it is not correct 

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/exatlon/images/3.png?raw=true)

So it seams that we need to decrypt it (somehow).
First thing that I belived that is was a Oct Encoding but it is not. After a lot of trouble with using the Remote Linux Debugger form IDA I finaly got the debuger working and got the encription. 
I entered **A** adn the result was **1040**
So I decided to create a list and try to decode the password

Password
```
1152 -> H
1344 -> T
1056 -> B
1968 -> {
1728 -> l
816  -> M
1648 -> g
784  -> K
1584 -> c  
816  -> M
1728 -> l 
1520 -> _
1840 -> S 
1664 -> h 
784  -> K
1632 -> f
1856 -> t 
1520 -> _ 
1728 -> l 
816  -> M
1632 -> f
1856 -> T
1520 -> _ 
784  -> K
1760 -> n
1840 -> s
1824 -> r
816  -> M
1584 -> c
1856 -> t 
784  -> K
1776 -> o 
1760 -> n
528  -> !
528  -> !
2000 -> }
```

What I found
```
A = 1040 a = 1552
B = 1056 b = 1568
C = 1072 c = 1584
D = 1088 d = 1600
E = 1104 e = 1616
F = 1120 f = 1632
G = 1136 g = 1648
H = 1152 h = 1664
I = 1168 i = 1680
J = 1184 j = 1696
K = 1200 k = 1712
L = 1216 l = 1728
M = 1232 m = 
N = 1248 n =
O = 1264 o = 
P = 1280 p = 
Q = 1296 q = 
R = 1312 r = 
S = 1328 s = 


```

*After 10 or so minutes I discovered that the patern is that each increment on A-Z and a-z is 16*
*After 10 more minutes I decided that I will witte a program to do this for me because it seemed preaty ez to do so*
Here is my script
```
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


```

and here is the flag **HTB▢l3g1c3l▢sh1ft▢l3ft▢1nsr3ct1on▢▢▢**
We can see that is has some missing characters but I can find it myself
Because it is a flag it will have **{** and **}** so not it looks like **HTB{l3g1c3l▢sh1ft▢l3ft▢1nsr3ct1on▢▢}**
It needs to have some **_** so here is the updated one **HTB{l3g1c3l_sh1ft_l3ft_1nsr3ct1on▢▢}**
And it seems like **528** is **!** so here is the final flag **HTB{l3g1c3l_sh1ft_l3ft_1nsr3ct1on!!}**












