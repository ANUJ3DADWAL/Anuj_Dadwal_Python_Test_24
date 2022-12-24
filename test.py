# Question 15
# n=int(input("Enter Your Number: "))
# ndic = {}
# for i in range(1,n+1):
#     ndic[i] = i*i
# print( ndic)    

# Question 14
# lower=int(input("Enter your lower range: "))
# upper=int(input("Enter Your upper range: "))
# result=[(i,i**3) for i in range(lower,upper+1)]
# print(result)

# Question-13
# n=int(input())
# l=[]
# for i in range(1,n+1):
#     if i%3==0:
#         l.append("Fizz")
#     elif i%5==0:
#         l.append("Buzz")
#     elif i%3==0 and i%5==0:
#         l.append("FizzBuzz")
#     else:
#         l.append(str(i))
# print(l) 
#  
# Q-8
# def move(arr):
#   arr.sort()

# arr = [-12,11,-13,-5,6,-7,5,-3,-6]
# move(arr)
# for e in arr:
#     print(e , end = " ")

# Question 4
# ini_dic={
#     "name":"Kelly",
#     "age":25,
#     "salary":8000,
#     "city":"New york"
# }
# ini_dic["location"]=ini_dic.pop("city")
# print(str(ini_dic))

# Question-2

# def show_excitement():
#     return "I am super excited for this course! "*5
# print(show_excitement())

# Question-10

# l=list(map(int,input("List: ").split(",")))
# l.sort()
# print((l[-1]*l[-2])-(l[0]*l[1]))

# Question-6

# l=list(map(int,input().split(",")))
# ind=int(input("K= "))
# l.sort()
# print(l[ind-1])




