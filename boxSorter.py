#======================================================================================
#                                   Imports
#======================================================================================
import json


#======================================================================================
#                                   Auxiliary Functions
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
    
    # Sort after dest_id (first priority)
    # and weight (second priority) with smallest numbers first
    data = sorted(data, key=lambda d: d['weight'], reverse=True)
    data = sorted(data, key=lambda d: d['dest_id'])
    return data


def splitByUnique(data, str): # Split list into list of lists based on unique values of 'str' parameter
    
    newList = [[data[0]]]
    newList.remove([data[0]])
    index = -1
    last_id = -1
    
    # Iterate through items
    for item in data:

        # Check uniqueness criteria (Depends on list being sorted!)
        if last_id != item[str]:
            # Make new sub-list with item and update parameters
            newList.append([item])
            last_id = item[str]
            index += 1
        else:
            # Append item to sub-list else
            newList[index].append(item)

    return newList


def splitBySum(datain, str, max): # Split list into list of lists based on maximum sum of values in 'str' parameter
    
    
    data = datain.copy()
    newList = [[data[0]]]
    newList.remove([data[0]])
    sum = 0
    items = len(data)
    index = -1
    makeNew = True
    
    # Iterate through items as long as there are items
    while items > 0:
    
        # Iterate through items
        noInserts = True
        for item in data:
            
            # If first item or if list has no more applicable items
            if makeNew:

                # Make a new sub-list and update paramaters
                sum = item['weight']
                newList.append([item])
                data.remove(item)
                items -= 1
                index += 1
                noInserts = False
                makeNew = False
                break

            # If sum will not supersed maximum
            elif  sum + item[str] <= max:
                
                # Insert into sub-list and update paramaters
                sum += item['weight']
                newList[index].append(item)
                data.remove(item)
                items -= 1
                noInserts = False
                break

            # Break if list is empty
            if items == 0:
                break
        
        # If list has been looked through with no items applicable for insertion
        if noInserts:
            makeNew = True
    
    return newList



#======================================================================================
#                                   Main Function
#======================================================================================
def main(inData = [], infilename = '', outfilename = ''):
    
    # Load data on boxes depending on given input parameters
    if infilename != '':
        data = loadBoxesData(infilename)
    elif inData != []:
        data = inData
    else:
        print("\nError: No input given.\nEither use 'infilename' parameter to declare path of input JSON file,\nor input list of dicts directly via the 'inData' parameter.")
        return []

    # Sort boxes
    data = sortData(data)
    
    # Split boxes by destination
    data = splitByUnique(data, 'dest_id')

    # Split box-destinations by pallet
    for dest in data:
        split_result = splitBySum(dest, 'weight', 1000)
        dest.clear()
        dest.extend(split_result)
    

    # Print palleting solution to terminal
    for dest in data: # Iterate through destinations
        dest_id = dest[0][0]['dest_id']
        print(f'\nTo destination with ID {dest_id} goes these pallets:')
        
        pallet_index = 0
        for pallet in dest: # Iterate through pallets
            pallet_index += 1
            print(f'\tPallet {pallet_index} with boxes:')
            weight = 0
            for box in pallet: # Iterate through boxes
                print(f'\t\t{box}')
                weight += box['weight']
            print(f'\t\t- Total weight: {weight:.2f} kg -')
    print('\n')

    # Output palleting solution to JSON file if output destination is declared
    if outfilename != '':
        outputData(data, outfilename)
    
    # Return palleting solution
    return data


#======================================================================================
#                                   Execute
#======================================================================================
if __name__=="__main__": 
    main(infilename='boxesIn.json', outfilename='boxesOut.json') 

