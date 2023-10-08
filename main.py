
import json

# Load data from JSON file
def loadBoxesData(infilename):
    
    # Read from JSON file
    with open(infilename, "r") as infile:
        data = json.load(infile)
    
    return data

# Output data to JSON file
def outputData(data, outfilename):

    # Format data to JSON object
    json_object = json.dumps(data, indent=4)

    # Write to file
    with open(outfilename, "w") as outfile:
        outfile.write(json_object)



# Defining main function
def main():

    # Hyperparameters
    infilename = 'boxes.json'
    outfilename = 'out.json'

    # Load data on boxes
    data = loadBoxesData(infilename)




    # Iterating through the json list
    for box in data:
        print(box)



    
    # Output palleting solution
    outputData(data, outfilename)
    
    return 0
  
  
# Execute main function
if __name__=="__main__": 
    main() 



