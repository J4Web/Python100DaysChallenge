#Data Types
#For int we can't do print(len(2345)) #give out an error message
#Strings
#this extraction of char by char is called subscripting
# print("Hello"[4])


#Fact in python we could write 123456987 if we write it as 
# 123,456,789 its interpreted by python as 123456789 instead


#Float - nums that have decimal points 
#Eg 3.146789 is

#Boolean- True or False 

#Type conversion 
#we use type( ) function to get the type of data type 
#class<int> also with type checking we can change data types 
#called type casting

# new_num_char= str(number_it_is)

from unittest import result


print(70+int("30"))

print("70"+"100")


print(70+float("10.2"))


#So we can't do nums%10 in python ? and num/10 ???
print(70%10)


#doing this gives you a floating point number so we have to convert it to an  integer *****************
print(int(70/10))


print(int("80")/float("1.75")*float("1.75"))


#** -> gives us power

print(2**2)

#PEMDAS

#() ** */ +-

print(3*3+3/3-3)

print(round(8/3))

# // -> this is called floor division 

print(8 // 3)

result=1
result/=3
print(round(result,6))


#FSTRING
print(f"hey here is me {round(result,3)}, here is me and enjoying this learning {3**2}")