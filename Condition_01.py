#This code is to find the persons eligibilty to vote


x=int(input("enter the age of the person:"))
if x>=18 :
  print("yes the person is eligible to vote")
elif x<0:
  print("Invalid age")
else :
  print("No,the person is not eligible to vote")
