# Part A - String Functions (10 Questions)S
text = "PYTHON"
print(text.lower())
# ans=python


# 2. Write code to remove extra spaces from:
name = " Hello World "
print(name.strip())
    # ans = Hello World

fruit="banana"
print(fruit.count("a"))
#ans=3

sentence="i have a dog"
print(sentence.replace("dog","cat"))
#   ans  = i have a cat


msg="python is fun"
print(msg.split())
# ans = ['python', 'is', 'fun']


text="machine"
print(text.find("i"))
# ans=4


greeting="Good Morning"
print(greeting.startswith("Good"))
# ans=True


word="hello"
print(word.upper())
# ans=HELLO


number="12345"
print(number.isdigit())
# ans=True


items = ['data', 'science']
result = '_'.join(items)
print(result)
# ans=data_science



# Part B - List Functions (12 Questions)
I = [1,2,3]
I.append("10")
print(I)
# ans=[1, 2, 3, '10']

I=[5,6,7]
I.insert(1,"99")
print(I)
# ans=[5, '99', 6, 7]

I=[9,1,3,8]
I.sort()
print(I)
# ans=[1, 3, 8, 9]

I=[10,20,30,40]
I.remove(20)
print(I)
# ans=[10, 30, 40]

I=[1,2,3,4]
I.pop()
print(I)
# ans=[1, 2, 3]

a=[1,2]
b=[3,4]
print(a+b)
# ans=[1, 2, 3, 4]

nums=[2,4,2,2,6]
print(nums.count(2))
# ans=3

I=[5,10,15]
print(sum(I))
# ans=30

marks=[44,72,91,60]
print(max(marks))
# ans=91

nums=[20,18,5,34]
print(min(nums))
# ans=5


I=[8,9,10]
I.clear()
print(I)
# ans=[]

original=[1,2,3]
I=original.copy()
print(I)
# ans=[1, 2, 3]



# Part C - Control Statements (8 Questions)
# 23. Write a program to check if a number is even or odd
num=int(input("enter the number="))
i=0
if (num%2==0):
    print("even")
else:
    print("odd")
#     ans=enter the number=7
# odd

# 24. Use if-elif-else to check whether a number is positive, negative, or zero
num=int(input("enter the number="))
if (num>0):
    print("positive")
elif (num<0):
    print("negative")

elif    (num==0):
    print("zero")
else:
    print("wrong num")
# ans=enter the number=0
# zero

# 25. Write a for loop to print numbers from 1 to 10.
i=0
for i in range (1,11):
    print(i)
#     ans=
# 1    
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 26. Print the multiplication table of 5 using a for loop    
i=0
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

# 27. Use a while loop to print numbers from 10 down to 1.

i=10
while i>0:
    print(i)
    i-=1
# ans=
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1    

# 28. Write code to calculate the sum of digits of a number using a while loop
num=int(input("enter the number for calulate digit="))
sum1=0
while num>0:
    digit=num%10   
    sum1+=digit
    num=num//10
print(sum1)
# ans=
# enter the number for calulate digit=567
# 18

# 29. Count the number of vowels in a given string using for and if

word=input("Enter a word to find vowels in it=")
vowel=0
for i in word:
    if i.lower() in 'aeiou':
       vowel+=1
print(vowel)
# ans=
# let be mayank
# =2


# 30. Check if the string "madam" is a palindrome using indexing and if
string='madam'
if string==string[::-1]:
    print('yes it is polindrome')
else:
    print("nahi hai")
    # ans=yes it is polindrome