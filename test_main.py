#======================================================================================
#                                   Imports
#======================================================================================
from main import *


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
#                                   Tests
#======================================================================================


def test_main_noerr():
    assert main() == 0


def test_sortData():
    newlist = sortData(dictlist)
    ids = []
    for box in newlist:
        ids.append(box['sortOrder'])
    assert ids == [1, 2, 3, 4, 5, 6, 7, 8]


def test_splitByUnique():
    newlist = splitByUnique(dictlist, 'dest_id')
    assert len(newlist) == 2

def test_splitBySum():
    newlist = splitBySum(dictlist, 'weight', 1000)
    assert len(newlist) == 4









