import asyncio
import heapq
import os
from heapq import merge

nums_listoflist = []
finallist = []
loop = asyncio.get_event_loop()

async def sort(unsorted_filename):
    with open('input/' + unsorted_filename) as fin:
        temp_list = list()
        for line in fin:
            temp_list.append(int(line))
            temp_list.sort(key=int)
        nums_listoflist.append(temp_list)
    pass

async def get_sorted_lists():
    # 1.Opening, looping, and sorting the input files
    unsorted_filename: str
    async_tracker = list()

    for unsorted_filename in os.listdir('input'):
        if unsorted_filename.startswith("unsorted_") and unsorted_filename.endswith(".txt"):
            # print("loading of " + unsorted_filename + " started")
            task = asyncio.create_task(sort(unsorted_filename))
            async_tracker.append(task)
            # print("sorted " + unsorted_filename)
            # print('\n')
        else:
            continue

    # await async_tracker[0]
    # await async_tracker[1]
    # await async_tracker[2]
    # await async_tracker[3]
    # await async_tracker[4]
    # await async_tracker[5]
    # await async_tracker[6]
    # await async_tracker[7]
    # await async_tracker[8]
    # await async_tracker[9]

    await asyncio.gather(async_tracker[0], async_tracker[1], async_tracker[2], async_tracker[3], async_tracker[4], async_tracker[5], async_tracker[6], async_tracker[7], async_tracker[8], async_tracker[9])


def write_to_file(listname, output_filename):
    with open('output/' + output_filename, mode='wt') as fout:
        for nums in listname:
            fout.write('%s \n' % nums)
        fout.close()


def merge(*list):
    return heapq.merge(*list)


def main():
    # 1. open, run and sort all the files in async
    asyncio.run(get_sorted_lists())

    # 2. merge
    finallist = list(merge(*nums_listoflist))

    # 3.writing to file
    write_to_file(finallist, 'async_all_sorted_.txt')

    print("Successful! All the unsorted files have beeen sorted and merged into file: async_all_sorted_.txt")


if __name__ == "__main__":
    main()
