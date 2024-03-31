my_notes = open("my_notes.txt", "w")

my_notes.write("linea 1: hacer los pendientes . \n")
my_notes.write("linea 2: ordenar las cosas .\n")

lineas = ["linea 3: hacer las compras .\n", "linea 4: hacer los trabajos pendientes.\n"]
my_notes.writelines(lineas)

my_notes.close()

my_notes = open("my_notes.txt", "r")

print("método 1: read()")
print("----------------------")
print(my_notes.read())
my_notes.close()

my_notes = open("my_notes.txt", "r")
print("método 2: readlines()")
print("----------------------")
for linea in my_notes.readlines():
    print(linea.rstrip("\n"))
my_notes.close()








