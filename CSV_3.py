import csv
import os
import shutil
import random


def createCSV3(randlist):
    with open("dataset3.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")

        classtag = "Cat"
        for i in range(1000):

            p1 = os.path.abspath(f'dataset/{randlist[i]}.jpg')

            p2 = os.path.relpath(f'dataset/{randlist[i]}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])

        classtag = "Dog"
        for i in range(1000):

            p1 = os.path.abspath(f'dataset/{randlist[i+1000]}.jpg')

            p2 = os.path.relpath(f'dataset/{randlist[i+1000]}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])


def copyRand(randlist):
    classtag = 'Cats'
    for i in range(1000):
        shutil.copyfile(
            f'dataset/Cats/{str(i).zfill(4)}.jpg', f'dataset/{randlist[i]}.jpg')
    classtag = 'Dogs'
    for i in range(1000):
        shutil.copyfile(
            f'dataset/Dogs/{str(i).zfill(4)}.jpg', f'dataset/{randlist[i+1000]}.jpg')


def randNumberNames():
    randlist = list(range(10000))
    random.shuffle(randlist)
    return randlist


if __name__ == "__main__":

    randlist = randNumberNames()

    copyRand(randlist)
    createCSV3(randlist)
