# check if the string if its starts with "The" and End with "Spain"
# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$",txt)
# if x :
#     print("YES! We have a match!")
# else:
#     print("No Match")


# Using the findall() function return a list containing every occurrence of "ai":
# import re
# text="The rain in Spain"
# x = re.findall("ai",text)
# print(x)


# Using the search() function .
# import re
# text = "The rain in Spain"
# x = re.search("\s",text)
# print("The first white-space character is located in position:",x.start())


# Using the split() function. Split the string at every white-space character.
# import re
# text = "The rain in Spain"
# x = re.split("\s",text)
# print(x)


# Using the sub() function. Replace all the white-space characters with the digit "9":
import re
text="The rain in Spain" 
x=re.sub("\s","7",text)
print(x)



