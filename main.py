#======================================================================================
#                                   Imports
#======================================================================================
import json
from operator import attrgetter


#======================================================================================
#                                   Auxiliary functions
#======================================================================================


def loadBoxesData(infilename): # Load data from JSON file
    
    # Read from JSON file
    with open(infilename, "r") as infile:
        data = json.load(infile)
    return data


def outputData(data, outfilename): # Output data to JSON file

    # Format data to JSON object
    json_object = json.dumps(data, indent=4)
    # Write to file
    with open(outfilename, "w") as outfile:
        outfile.write(json_object)


def sortData(data): # Build new sorted list 
    
    # Sort after dest_id first and weight second (largest numbers first)
    dataout = sorted(data, key=attrgetter('dest_id', 'weight'), reverse=True)
    return dataout






#======================================================================================
#                                   Main function
#======================================================================================
def main():

    # Hyperparameters
    infilename = 'boxes.json'
    outfilename = 'out.json'
    

    # Load data on boxes
    data = loadBoxesData(infilename)


    # Sort boxes
    data = sortData(data)


    # Iterate through boxes
    for box in data:
        print(box)



    
    # Output palleting solution
    outputData(data, outfilename)
    

    return 0


#======================================================================================
#                                   Execute
#======================================================================================
if __name__=="__main__": 
    main() 

