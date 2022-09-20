#Search within the txt file

def search():
    #Create a bool to use as a indicator
    found = False

    #Get the search value
    search = input('Enter a description to search for: ')

    #Open the coffee.txt file
    cofee_file = open('coffee.txt', 'r')

    #read the first record description field
    descr = coffee_file.readling()

    #read rest of the file
    while descr != '':
        #read the quantity area
        qty = float(cofee_file.readling())

        #take out the new line
        descr = descr.rstrip('\n')

        #Determine if it matches the search value
        if descr == search:
            #display
            print('Description:', descr)
            print('Quantity:', qty)
            print() #Blank line here
            #set found as true if it is
            found = True
        #read next line if not a match
        descr = cofee_file.readline()

    #close txt file
    coffee_file.close()

    #if not found then display this message
    if not found:
        print("Item was not found within the file")

if __name__=="__main__":
    search()
    
