from dict import dict

with open('main.damajogu', 'r', encoding="utf-8") as file:
    convert = file.read()

print("ENTRADA\nVVVVVVV\n")
print(convert)
print("^^^^^^^\n")

for i in dict:
    convert = convert.replace(dict[i],i)

print("\nSAIDA\nVVVVV\n")
exec(convert)
print("\n^^^^^")
