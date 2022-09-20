#Menu enter all modules
import add_coffee
import delete_coffee
import show_coffee
import modify_coffee
import search_coffee

def main():

    print("Smell Good Coffee Inventory System Menu")
    print('---------------------------------------')
    print('1. Add Records')
    print('2. Show Records')
    print('3. Search for a Records')
    print('4. Modify a Record')
    print('5. Delete a Record')
    print('6. Exit Menu')
    print()
          
    menuNum=int(input("Enter the number on the menu:"))

    while menuNum!='':
        if menuNum==1:
            add_coffee.add_coffee()
            
        if menuNum==2:
            show_coffee.show()
            
        if menuNum==3:
            search_coffee.search()
            
        if menuNum==4:
            modify_coffee.mod()
            
        if menuNum==5:
            delete_coffee.delete()

        if menuNum==6:
            print("You are done!")
            break

    print()
    print("Smell Good Coffee Inventory System Menu")
    print('---------------------------------------')
    print('1. Add Records')
    print('2. Show Records')
    print('3. Search for a Records')
    print('4. Modify a Record')
    print('5. Delete a Record')
    print('6. Exit Menu')
    print()
    menuNum=int(input("Enter the number on the menu"))


if __name__=="__main__":
     main()
