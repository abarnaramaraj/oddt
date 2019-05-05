numlist=[]
number=int(input("enter the num"))
for i in range(1,number+1):
 value=int(input("enter the value"))
 numlist.append(value)
print("odd number")
for j in range(number):
 if(numlist[j]%2!=0):
print(numlist[j])
