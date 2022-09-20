#Show records on the txt file

def show():
    #open file
    coffee_file = open('coffee.txt', 'r')

    #read first line
    descr=coffee_file.readline()
    #read the rest of the file
    while descr != '':
        #read quantity
        qty = float(coffee_file.readline())

        #strip new line
        descr = descr.rstrip('\n')

        #display record
        print('Description:', descr)
        print('Quantity:', qty)

        #read descr
        descr = coffee_file.readline()

    #close file
    coffee_file.close()

if __name__=="__main__":
    show()
    
