# s=input("enter a string")
# i=0
# newstr=""
# while i<len(s):
#     data = s[i]
#     if data==" ":
#         i=i+1
#     else:
#         newstr=newstr+data
#         i=i+1
# print(newstr)
# ------------------------------------------------------------------------------------
# s1=input("enter a string")
# count1=0
# for chr in s1:
#     count1=count1+1
# print(count1,"this is count 1")
# ------------------------------------------------------------------------------------

# s2=input("enter a string")
# count2=0
# i=0
# while i<len(s2):
#     if s2[i]in"aeiouAEIOU":
#         count2=count2+1
#     i=i+1
# print(count2,"this is count 2")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------


s=input("enter value")
# print(s[::-1])
i=len(s)-1
rev =""
while i>=0:
    rev=rev+s[i]
    i=i-1
print(rev)





