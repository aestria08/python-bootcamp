# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

colours={
    "apple":"red",
    "pear":"green",
    "banana":"yellow,"

}

print(colours)
print(colours["apple"])
colours["peach"]="pink"
print(colours)
colours["apple"]="blue"
print(colours)

for key in colours:
    print(key)
for key in colours:
    print(colours[key])