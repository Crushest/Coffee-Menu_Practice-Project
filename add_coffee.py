#Add coffee to inv

def add_coffee():
    #define for loop
    another = 'y'

    #open txt file to add
    coffee_file=open('coffee.txt', 'a')

    #add record to file

    while another == 'y' or another == 'Y':

        print('\nEnter the following coffee data:')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds):'))

        #append data to txt file
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        #determine to continue or not
        print('\nDo you want to add another record?')
        another = input("Y = yes, anything else = no: ")

    #close file
    coffee_file.close()
    print('\nData added to file')

#call
if __name__=="__main__": 
    add_coffee()
        
