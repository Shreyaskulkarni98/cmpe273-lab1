import heapq
import os
from heapq import merge

nums_listoflist = []
finallist = []

# sorts all the files in give directory and places them in /output dir
def sort(unsorted_filename):
    with open('input/' + unsorted_filename) as fin:
        temp_list = list()
        for line in fin:
            temp_list.append(int(line))
            temp_list.sort(key=int)
        nums_listoflist.append(temp_list)


def write_to_file(listname, output_filename):
    with open('output/' + output_filename, mode='wt') as fout:
        for nums in listname:
            fout.write('%s \n' % nums)
        fout.close()


def merge(*list):
    return heapq.merge(*list)

def main():
    # 1.sorting
    unsorted_filename: str
    for unsorted_filename in os.listdir('input'):
        if unsorted_filename.startswith("unsorted_") and unsorted_filename.endswith(".txt"):
            sort(unsorted_filename)
        else:
            continue

    # 2.merging
    finallist = list(merge(*nums_listoflist))

    # 3.writing to file
    write_to_file(finallist, 'all_sorted_.txt')

    print("Successful! All the unsorted files have beeen sorted and merged into file: all_sorted_.txt")


if __name__ == "__main__":
    main()


