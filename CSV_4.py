import csv
import os


def classElements(classtag, dataset):
    count = 0

    with open(dataset, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")

        for row in file_reader:
            if (row[2] == ' ' + classtag) and (count < 1000):
                print(row[1])
                count += 1


if __name__ == "__main__":

    classtag = str(input())
    dataset = str(input())
    classElements(classtag, dataset)
