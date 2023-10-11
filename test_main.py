#======================================================================================
#                                   Imports
#======================================================================================
from boxSorter import *


#======================================================================================
#                                   Test objects
#======================================================================================
dictlist = [
    {"box_id": 1,   "sortOrder": 3,     "weight": 400,      "dest_id": 1},
    {"box_id": 2,   "sortOrder": 2,     "weight": 600,      "dest_id": 1},
    
    {"box_id": 3,   "sortOrder": 4,     "weight": 200,      "dest_id": 1},
    {"box_id": 4,   "sortOrder": 1,     "weight": 800,      "dest_id": 1},

    {"box_id": 5,   "sortOrder": 8,     "weight": 100,      "dest_id": 2},
    {"box_id": 6,   "sortOrder": 5,     "weight": 800,      "dest_id": 2},

    {"box_id": 7,   "sortOrder": 6,     "weight": 600,      "dest_id": 2},
    {"box_id": 8,   "sortOrder": 7,     "weight": 400,      "dest_id": 2}]


#======================================================================================
#                                   Main Tests
#======================================================================================


# Tests for empty out in case of no input
def test_main_no_in_empty_out():
    assert main() == []


# Tests that output has the expected pallet-distribution between two destinations
def test_main_out_lengths():
    newlist = main(inData=dictlist)
    assert [len(newlist[0]) , len(newlist[1])] == [2 , 2]


#======================================================================================
#                                   Auxiliary Function Tests
#======================================================================================


# Tests that sorting function yields the expected box order
def test_sortData():
    newlist = sortData(dictlist)
    ids = []
    for box in newlist:
        ids.append(box['sortOrder'])
    assert ids == [1, 2, 3, 4, 5, 6, 7, 8]


# Tests that this splitting function yields the expected number of destinations when unsorted and sorted
def test_splitByUnique_unsorted():
    newlist = splitByUnique(dictlist, 'dest_id')
    assert len(newlist) == 2

def test_splitByUnique_sorted():
    newlist = sortData(dictlist)
    newlist = splitByUnique(newlist, 'dest_id')
    assert len(newlist) == 2


# Tests that this splitting function yields the expected number of pallets when unsorted and sorted
def test_splitBySum_unsorted():
    newlist = splitBySum(dictlist, 'weight', 1000)
    assert len(newlist) == 4

def test_splitBySum_sorted():
    newlist = sortData(dictlist)
    newlist = splitBySum(newlist, 'weight', 1000)
    assert len(newlist) == 4


