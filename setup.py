from setuptools import setup
import os

# Fayl yaratish funksiyasi
def create_file():
    with open("created_by_setup.txt", "w") as f:
        f.write("Setup ishga tushdi!\n")
    print("File created_by_setup.txt created!")

# Faylni yaratish darhol setup.py ishlaganda
create_file()

setup(
    name="mytestscript",
    version="0.1",
    py_modules=["test"],  # test.py modul sifatida
)
