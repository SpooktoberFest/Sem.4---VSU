
import json


# Defining main function 
def main(): 
    
    # Open JSON file and load data
    f = open('boxes.json', "r")
    data = json.load(f)







    # Close file and return main function
    f.close()
    
    return 0
  
  
# Execute main function
if __name__=="__main__": 
    main() 



