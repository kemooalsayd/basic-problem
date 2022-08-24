# monthsObject={
#     "1":"يناير",
#     "2":"فبراير",
#     "3":"مارس",
#     "4":"ابريل",
#     "5":"مايو",
#     "6":"يونيو",
#     "7":"يوليو",
#     "8":"اغسطس",
#     "9":"سبتمبر",
#     "10":"اكتوبر",
#     "11":"نوفمبر",
#     "12":"ديسمبر",
# }
# userInput=input("enter month number:")
# print(monthsObject[userInput])
# rabea=[1,2,3]
# seaf=[4,5,6]
# kharef=[7,8,9]
# sheta=[10,11,12]


# userInput=int(input("enter month number:"))


# if userInput in rabea:
#     print("this month in rabea")
# elif userInput in seaf:
#     print("this month in seaf")
# elif userInput in kharef:
#     print("this month in kharef")
# elif userInput in sheta:
#     print("this month in sheta")
# else:
#     print("this month not real")


# check=["U", "A", "E", "I", "O"]

# userInput=input("enter month number:").upper()

# if userInput in check:
#     print("this letter is movey")
# else:
#     print("this is not movey")



# #############################
# ######## first way ##########
# #############################

# userInput=input("enter word:")

# print(userInput[::-1])







# #############################
# ####### secound way #########
# #############################

# convertToList=list(userInput)
# convertToList.reverse()
# reverseListAndJoin="".join(convertToList)
# print(reverseListAndJoin)









# #############################
# ######## third way ##########
# #############################


# emptyList=[]
# for l in userInput:
#     emptyList.insert(0,l)
#     emptyListAfterJoin="".join(emptyList)
# print(emptyListAfterJoin)






# #############################
# ######## fourd way ##########
# #############################

# emptyValue=""
# for l in userInput:
#     emptyValue=l+emptyValue

# print(emptyValue)



# fN=int(input("enter first number: "))
# unit=input("enter unit: ").strip()
# sN=int(input("enter secound number: "))
# if unit=="+":
#     print(f"{fN}{unit}{sN}=>{fN+sN}")
# elif unit=="-":
#     print(f"{fN}{unit}{sN}=>{fN-sN}")
# elif unit=="*":
#     print(f"{fN}{unit}{sN}=>{fN*sN}")
# elif unit=="/":
#     print(f"{fN}{unit}{sN}=>{fN/sN}")



# userInput=int(input("please enter number only: "))

# if userInput>0:
#     print("this number is positive")
# elif userInput<0:
#     print("this number is negative")
# else:
#     print("this number not positive or negative")













# userInput=int(input("please enter number only: "))

# if userInput>= 80 and userInput<=100:
#     print("your mark is A")
# elif userInput>= 60 and userInput<=100:
#     print("your mark is B")
# elif userInput>= 40 and userInput<=100:
#     print("your mark is C")
# elif userInput< 40 and userInput>=0:
#     print("your mark is F")
# else:
#     print("this is unreal degrea")



# userInput=int(input("please enter watermelon number : "))
# userInputTwo=int(input("please enter boy number : "))
# theFunction=userInput%userInputTwo
# if theFunction==0:
#     print("yes")
# else:
#     print("no")


# x="4.5"
# print(int(float(x)))


# userInput=input("please enter three number between them , : ")


# function=userInput.split(",")
# for n in function:
#     if float(n)/int(float(n))!=1:
#         print(n)
# else:
#     print("not there any floating number")



# userInput=input("please enter three number between them , : ")

# function=userInput.split(",")
# function.sort()
# print(function)
# print(f"min=>{function[0]}")
# print(f"max=>{function[-1]}")


#################################
#  3  \   2   \  erorr  \ erorr #
#################################


# userInput=input("please enter numbers between them ,: ")
# function=userInput.split(",")
# pos=[]
# nag=[]
# for n in function:
#     if int(n)>0:
#         pos.append(n)
#     elif int(n)<0:
#         nag.append(n)
#     else:
#         print("this not number")
# e=[]
# o=[]
# for n in range(len(pos)):
#     g=int(pos[n])
#     e.append(g)
# Sum = sum(e)
# print(Sum)
# for n in range(len(nag)):
#     g=int(nag[n])
#     o.append(g)
# Sumt = sum(o)
# print(Sumt)


# userInput=input("enter the radius value: ")

# pi=3.14
# print(f"the erea of circle=> {pi*(int(userInput)**2)}")
# print(f"the ocean of circle=> {2*pi*(int(userInput))}")

#########################################################
#########################################################
#########################################################

# for o in range(99):
#     if o%5==0:
#         print(o)





# for o in range(100):
#         print(o)



# empty=[]
# for o in range(100):
#     empty.append(o)
# empty.reverse()
# for n in empty:
#     print(n)


# user=input("enter base: ")
# usert=input("enter power: ")

# print(int(user)**int(usert))


####### maltiple the all before numbers ###########

# user=input("enter number: ")
# li=[]
# for n in range(1,int(user)+1):
#     li.append(n)
# result=1
# for l in li:
#     result = result * l
# print(result)

####### mltiple of number 7 ###########

# k=0
# for n in range(100):
#     k+=7
#     if k==98+7:
#         break
#     print(k)


####### mltiple of numbers ###########

# k=1
# for l in range(0,10):
#     k=k*2
#     print(k)


####### knowon problem probably in for loop file ###########

# result=1
# for p in range(16):
#     if p%2!=0:
#         result= result * p
#         print(result)


####### average of numbers ###########
# inputU=input("pleace enter numbers between them , : ")

# fun=inputU.split(",")
# li=[]
# for k in fun:
#     li.append(int(k))
# print(f"the average numbers is {sum(li)/len(li)}")






########## numbers summition ##########

# inputU=input("pleace enter numbers between them , : ")

# fun=inputU.split(",")
# li=[]
# for k in fun:
#     li.append(int(k))
# print(f"the sum of numbers is {sum(li)}")




########## numbers lenght ##########

# inputU=input("pleace enter numbers : ")
# print(f"the sum of numbers is {len(inputU)}")



####### print number of time divide in two##########

# inputU=int(input("pleace enter numbers : "))
# count=1
# if inputU==0:
#     print("enter any number except zero")
# else:
#     while True:
#         if inputU/2==1:
#             break
#         if inputU%2==0:
#             count+=1
#             inputU/=2
#         elif inputU==0:
#             count=0
#             break
#         else:
#             count-=1
#             break
#     print(count)



# c=""
# o=0
# for l in range(100,201):
#     if l%5==0 or l%6==0:
#         o+=1
#         c=f"{c} {str(l)}"
#         if o==10:
#             c=c+"\n"
#             o=0

# print(c)




####### print element summition ##########

# def summ(*li):
#         return sum(*li)
# x=[1,2,3]
# print(summ(x))

####### print elements lenght ##########

# def summ(*li):
#         return len(*li)
# x=[1,2,3]
# print(summ(x))
####### print max value##########

# def summ(*li):
#         return max(*li)
# x=[1,2,3]
# print(summ(x))

####### print min value##########

# def summ(*li):
#         return min(*li)
# x=[1,2,3]
# print(summ(x))

####### print sum elements and lenght ##########

# x=[1,2,3+1]
# def calc(*li):
#     global pos
#     pos=[]
#     for l in li:
#         for k in l:
#             if k%2==0:
#                 pos.append(k)
            

# calc(x)
# print(len(pos))
# print(sum(pos))

####### calc onces of there ##########

# x=[1,2,3+1,2]
# def count(*li):
#     global c
#     c=0
#     for l in li:
#         for k in l:
#             if k==2:
#                 c+=1

# count(x)
# print(c)


####### calc count ##########
# x=[1,2,3,2,1,2,3,2,4,7,4,9-2]
# def count(*li):
#     for l in li:
#         m=list(set(l))
#         for k in m:
#             print(f"{k}=>{l.count(k)}")
# count(x)


###### LINEAR SEARCH  #######

# c=0
# p=[]
# for i in range(pow(10, 6)+1):
#     p.append(i)

# TheNumber=1234
# for k in p:
#     c+=1
#     if k==TheNumber:
#         print("number found")
#         break
# else:
#     print("number not found")
# print(c)




# ##### BINEARY SEARCH  #######
# def binary_search(item_list,item):
# 	first = 0
# 	last = len(item_list)-1
# 	found = False
# 	while( first<=last and not found):
# 		mid = (first + last)//2
# 		if item_list[mid] == item :
# 			found = True
# 		else:
# 			if item < item_list[mid]:
# 				last = mid - 1
# 			else:
# 				first = mid + 1	
# 	return found
	
# print(binary_search([1,2,3,5,6,8], -1))
# print(binary_search([1,2,3,5,8], 5))

# ###### INTERPOLAITION SEARCH  #######

# c=0
# TheNumber=-1
# p=[]
# for i in range(pow(10, 6)+1):
#     p.append(i)
# low=0
# mid=0
# high=len(p)-1
# while low<high:
#     c+=1
#     mid=int(low + (((high - low) / (p[high] - p[low])) *
#                     (TheNumber - p[low])))
#     if TheNumber==p[mid]:
#         print("number found")
#         break
#     elif p[mid]<TheNumber:
#         low=mid-1
#     elif p[mid]>TheNumber:
#         high=mid+1
# else:
#     print("number not found")

# print(c)



####### selection sort##########

# a = [64, 25, 12, 22, 11]

# for i in range(len(a)):

# 	for j in range(i+1, len(a)):

# 		if a[i] > a[j]:
# 			a[i], a[j] = a[j], a[i]
# print(a)

####### selection sort in string ##########

# l=["f","b","c","e","A"]
# for i in range(len(l)):
#     for g in range(i+1,len(l)):
#         if ord(l[g])<ord(l[i]):
#             l[g],l[i]=l[i],l[g]
# print(l)


####### bubble sort  ##########

# a = [64, 25, 12, 22, 11]
# for i in range(len(a)):
#     for k in range(i,len(a)-1):
#         if a[i]<a[k]:
#             a[i],a[k]=a[k],a[i]
# print(a)






















##################################
##################################
#########   FINISHED   ###########
##################################
##################################


# def cleanword(word):

#         if len(word)==1:

#             return word
#         if word[0]==word[1]:

#             return cleanword(word[1:])

#         return word[0] + cleanword(word[1:])


# print(cleanword('wwoorlld'))


# f = open(r"D:\for learning\py\the months calc\t.txt", "w")
# print(f.write("kemoo\n")

####### map#########
# def i(v):

#         return  v>10

# n=(12,23,10,32,5,76,6,3)
# m=map(i, n)
# for b in m:
#     print(b)

######### filter #######
# def i(v):

#         return  v>10

# n=(12,23,10,32,5,76,6,3)
# m=filter(i, n)
# for b in m:
#     print(b)

########## reduce #########
# from functools import reduce
# def i(v,f):

#         return  v+f

# n=[12,23,10,32,5,76,6,3]
# m=reduce(i, n)

# print(m)











