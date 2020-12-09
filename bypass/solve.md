First thing that I tryed was decomiling the .exe file and get some source code back.
I done this using **Jetbrains dotPeek** and got some clean looking code

I identilyed the main to be **0.0**
![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/bypass/images/1.png?raw=true)

I see that the function is always returning **false** so I switched to **ILSpy** and its **reflexil** extention to be able to modify the **.exe**

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/bypass/images/2.png?raw=true)

I will change **ldc.i4.0** to **ldc.i4.1** to make it return **true** always

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/bypass/images/3.png?raw=true)

Now I will update the **ILSpy model object**

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/bypass/images/4.png?raw=true)

Now you can see that it will always return **true**

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/bypass/images/5.png?raw=true)

Now I will save the patched .exe and let's run it

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/bypass/images/6.png?raw=true)

Now we can see that we pass the first check and we are requested with a secret key.

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/bypass/images/7.png?raw=true)

Lets modify the .exe again

No I will go in the **0.2()** and modify the **op_Equality** to a an **op_Inequality** and update the object and save the new patched .exe

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/bypass/images/8.png?raw=true)

But now when we enter anything in the scret key the programs return and exits.
My ideea is to force the program to always loop.
I decided to remove the **return** statement and replace it with a **nop**. Updated and saved. it.

![img](https://raw.githubusercontent.com/L1ghtDream/hackthebox/master/bypass/images/9.png?raw=true)

And sure enough here is the flag **HTB{SuP3rC00lFL4g}**




