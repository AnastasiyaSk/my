# Вывод списка файлов в папке в файл list.txt, каждый файл сновой строки
import os

directory = "D:/Spec!Lit/Dispersion+Diffusion+Heterogenity"
files = os.listdir(directory)
f = open("D:/Spec!Lit/Dispersion+Diffusion+Heterogenity/list.doc", "w")
for item in files:
    f.write("%s\n" % item)
f.close()
