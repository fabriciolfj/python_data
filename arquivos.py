path = "/Users/fabriciojacob/Documents/teste.txt"

file = open(path)

for linha in file:
    print(linha)


file.close()

temp = "tmp.txt"

with open(temp, "w") as arquivo:
    arquivo.writelines(x for x in open(path) if len(x)  > 1)
