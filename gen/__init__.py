import os
from generators import generate_fake_db


def Anonymize(path: str):
    # Генерируем фейковые данные
    generate_fake_db("gen.csv")

    hasher = DbHasher('gen.csv')

    # Вот тут надо будет сделать построчную запись для MySQL, TODO
    # Именно для этого сделан итератор
    # Но так как тут пока только csv то
    with open('tmp.csv', "w", encoding="utf-8") as out_file:
        out_file.write("")
    with open("gen.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open('tmp.csv', "a", encoding="utf-8") as out_file:
        for i in hasher:
            if not i:
                break
            out_file.write(lines[i].strip() + "\n")
    os.rename("tmp.csv", path)
