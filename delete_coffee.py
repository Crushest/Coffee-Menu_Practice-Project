#Delete an item from the coffee menu

import os #needed to remove the txt file

def delete():
    #create bool switch
    found = False

    search = input('Which coffee do you want to delete?')

    #open original txt file
    coffee=open('coffee.txt','r')
    #create temp file
    temp=open('temp.txt','w')

    #read first line
    descr = coffee.readline()

    while descr != '':
        #read qty field
        qty=float(coffee.readline())
        #strip \n from desc
        descr = descr.rstrip('\n')

        #write to temp file to record
        if descr != search:
            temp.write(descr+ '\n')
            temp.write(str(qty)+'\n')
        else:#do not write if it matches just switched and goes on
            found = True


        #read the next line
        descr = coffee.readline()
    #close files
    coffee.close()
    temp.close()

    #delete original txt file
    os.remove('coffee.txt')
    #rename to takeover deleted file
    os.rename('temp.txt','coffee.txt')

    #end message for if found or not
    if found:
        print('The file has been updated')
    else:
        print('The item does not exist in the file')
if __name__=="__main__":
    delete()
    
        

        
