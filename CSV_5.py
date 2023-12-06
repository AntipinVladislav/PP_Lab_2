import csv


def classElements(classtag, dataset):
    my_iter = MyIterator(1000)

    with open(dataset, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")

        for row in file_reader:
            if row[2] == ' ' + classtag:
                print(row[1])
                my_iter.__next__()


class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
        else:
            raise StopIteration


if __name__ == "__main__":

    classtag = str(input())
    dataset = str(input())
    classElements(classtag, dataset)
