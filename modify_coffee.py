#Modify coffee record

import os #needed for the remove and rename of functions

def mod_coffee():
    #Create a bool switch for the search
    found=False

    #get the search value and new quantity
    search = input("Enter description to search for: ")
    new_qty= int(input("Enter new quantity for item described: "))

    #open original txt file
    coffee = open('coffee.txt','r')

    #open/make temp file
    temp = open('temp.txt','w')
    
    #Read the first line 
    descr = coffee.readline()

    #read the rest of the file with a while loop
    while descr != '':
        #read quantity space
        qty = float(coffee.readline())

        #strip  \n for new line
        descr = descr.rstrip('\n')

        #write to temp file,
        #or new record if this is the
        #one that is to be modified
        if descr ==  search:
            temp.write(descr + '\n')
            temp.write(str(new_qty) + '\n')

            found = True

        else:
            temp.write(descr + '\n')
            temp.write(str(qty) + '\n')

        #read the next description
        descr = coffee.readline()
    #close all files
    coffee.close()
    temp.close()

    #delete original coffee file
    os.remove('coffee.txt')
    #rename temp file
    os.rename('temp.txt', 'coffee.txt')
    #if found or not will display these messages
    if found:
        print('The file has been updated')
    else:
        print('That item was not found in the file')

if __name__=="__main__":
    mod_coffee()
              
    
            
