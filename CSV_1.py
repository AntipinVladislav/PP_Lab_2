import csv
import os



def createCSV1():
    with open("dataset1.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")

        classtag = "Cat"
        for i in range(1000):
            
            p1 = os.path.abspath(f'dataset/{classtag}s/{str(i).zfill(4)}.jpg')

            p2 = os.path.relpath(f'dataset/{classtag}s/{str(i).zfill(4)}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])
            
        classtag = "Dog"
        for i in range(1000):
            
            p1 = os.path.abspath(f'dataset/{classtag}s/{str(i).zfill(4)}.jpg')

            p2 = os.path.relpath(f'dataset/{classtag}s/{str(i).zfill(4)}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])






if __name__ == "__main__":

    createCSV1()

    


