# s = input("enter string: ")
# i = 0
# newstr = ""
#
# while i < len(s):
#     data = s[i]
#     ascii_val = ord(data)
#
#     if ascii_val >= 65 and ascii_val <= 90:
#         newascii = ascii_val + 32
#         con = chr(newascii)
#         newstr = newstr + con
#     else:
#         newstr = newstr + data   # keep other characters same
#
#     i = i + 1
#
# print(newstr)
#
# s = input("enter string: ")
# i = 0
# newstr = ""
#
# while i < len(s):
#     data = s[i]
#     ascii_val = ord(data)
#
#     if ascii_val >= 97 and ascii_val <= 122:
#         newascii = ascii_val - 32
#         con = chr(newascii)
#         newstr = newstr + con
#     else:
#         newstr = newstr + data   # keep other characters same
#
#     i = i + 1
#
# print(newstr)

s = input("enter string: ")
i = 0
newstr = ""

while i < len(s):
    data = s[i]
    ascii_val = ord(data)

    if ascii_val >= 65 and ascii_val <= 90:
        newascii = ascii_val + 32
        con = chr(newascii)
        newstr = newstr + con

    elif ascii_val >= 97 and ascii_val <= 122:
        newascii = ascii_val - 32
        con = chr(newascii)
        newstr = newstr + con
    else:
        newstr = newstr + data   # keep other characters same

    i = i + 1

print(newstr)