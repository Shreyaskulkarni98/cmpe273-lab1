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


def main():
    # 1.sorting
    unsorted_filename: str
    for unsorted_filename in os.listdir('input'):
        if unsorted_filename.startswith("unsorted_") and unsorted_filename.endswith(".txt"):
            sort(unsorted_filename)
        else:
            continue

    # 2.merging
    list01 = list(merge(nums_listoflist[0], nums_listoflist[1]))
    list23 = list(merge(nums_listoflist[2], nums_listoflist[3]))
    list45 = list(merge(nums_listoflist[4], nums_listoflist[5]))
    list67 = list(merge(nums_listoflist[6], nums_listoflist[7]))
    list89 = list(merge(nums_listoflist[8], nums_listoflist[9]))

    list03 = list(merge(list01, list23))
    list47 = list(merge(list45, list67))
    list07 = list(merge(list03, list47))

    finallist = list(merge(list07, list89))

    # 3.writing to file
    write_to_file(finallist, 'all_sorted_.txt')

    print("Successful! All the unsorted files have beeen sorted and merged into file: all_sorted_.txt")


if __name__ == "__main__":
    main()


