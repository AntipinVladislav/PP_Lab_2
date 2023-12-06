import csv
import os
import shutil


def createCSV2():
    with open("dataset2.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")

        classtag = "Cat"
        for i in range(1000):
            
            p1 = os.path.abspath(f'dataset/{classtag.lower()}_{str(i).zfill(4)}.jpg')

            p2 = os.path.relpath(f'dataset/{classtag.lower()}_{str(i).zfill(4)}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])
            
        classtag = "Dog"
        for i in range(1000):
            
            p1 = os.path.abspath(f'dataset/{classtag.lower()}_{str(i).zfill(4)}.jpg')

            p2 = os.path.relpath(f'dataset/{classtag.lower()}_{str(i).zfill(4)}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])

def copy():
    classtag = 'Cats'
    for i in range(1000):
        shutil.copyfile(f'dataset/Cats/{str(i).zfill(4)}.jpg', f'dataset/{str(classtag).lower()}_{str(i).zfill(4)}.jpg')
    classtag = 'Dogs'
    for i in range(1000):
        shutil.copyfile(f'dataset/Dogs/{str(i).zfill(4)}.jpg', f'dataset/{str(classtag).lower()}_{str(i).zfill(4)}.jpg')

if __name__ == "__main__":
    copy()
    createCSV2()