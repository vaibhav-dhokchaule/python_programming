# convert from json to python
# import json
# x = '{"name":"vaibhav","age":"21","city":"pune"}'
# y = json.loads(x)
# print(y["age"])


# Convert from python to json..
# import json
# x = {"name":"vaibhav","age":"21","city":"pune"}
# y = json.dumps(x)      # Convert into json.
# print(y)


# Convert python object into json string.
# import json
# print(json.dumps({"name":"vaibhav","age":"21"}))
# print(json.dumps(["apple","banana"]))
# print(json.dumps(("apple","banana")))
# print(json.dumps("hello"))
# print(json.dumps("45"))
# print(json.dumps("45.5"))
# print(json.dumps("True"))
# print(json.dumps("False"))
# print(json.dumps("None"))


# Convert python object containing all the legal data types.
# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(y)


# Use indent parameter to define the number of indents
# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# # use four indents to make it easier to read the result:
# print(json.dumps(x, indent=4))


# Use separator parameters to change the default separator.
# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# # use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
# print(json.dumps(x, indent=4, separators=(". ", " = ")))


# Use the sort_keys parameter to specify if the result should be sorted or not.
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
