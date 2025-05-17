# Import extra dictionary
import os
import time


# Import function from other python file
import functionbox as fb


# Color text
red = "\033[91m"
blue = "\033[96m"


# Bold text
end = "\033[0;0m"

# Calling login function
os.system("cls") # Clean all the previous output
fb.login()


# After login, start the program
fb.initial_inventory_creation()


# Chek invalid input for menu
def check_menu(a):
    correct = False
    try:
        a = int(a)
        if a <= 5 and a > 0:  # If the user enter number is not between 1 until 5, it will be reject by system
            correct = True
            return a
        else:
            os.system("cls")
            print(f"{red}Please enter a correct option.{end}")
            time.sleep(1)
                 
    except ValueError:
        os.system("cls")
        print(f"{red}Please enter a valid input given.{end}")
        time.sleep(1)


# Check invalid input for menu4
def check_menu4(a):
    correct = False
    try:
        a = int(a)
        if a <= 4 and a > 0:  # If the user enter number is not between 1 until 4, it will be reject by system
            correct = True
            return a
        else:
            os.system("cls")
            print(f"{red}Please enter a correct option.{end}")
            time.sleep(1)
                 
    except ValueError:
        os.system("cls")
        print(f"{red}Please enter a valid input given.{end}")
        time.sleep(1)

# Check invalid input for menu1 and menu44        
def check_menu1_and_menu44(a):
    correct = False
    try:
        a = int(a)
        if a <= 3 and a > 0:  # If the user enter number is not between 1 until 3, it will be reject by system
            correct = True
            return a
        else:
            os.system("cls")
            print(f"{red}Please enter a correct option.{end}")
            time.sleep(1)
                 
    except ValueError:
        os.system("cls")
        print(f"{red}Please enter a valid input given.{end}")
        time.sleep(1)



while True:
    time.sleep(2)
    os.system('cls')
    print("Inventory Management System : : Main Menu\n")
    print('1. Inventory Update')
    print('2. Item Inventory Tracking')
    print('3. Search Inventory')
    print('4. Generate Report')
    print('5. Exit')

    menu = input("> ")
    
    menu = check_menu(menu)

    if menu == 1: 
        os.system("cls")
        
        print('1. Distribute PPE\n2. Receive PPE\n3. Back?') # Allow user for 3 option
        
        menu1 = input("> ")
        
        menu1 = check_menu1_and_menu44(menu1)
                
        
        if menu1 == 1:  # Distribute PPE Function
            os.system("cls")
            fb.distribute_ppe()  # Will direct user to distribute PPE function in functionbox
        
        elif menu1 == 2:  # Receive PPE from supplier Function
            os.system("cls")
            fb.receive_ppe()
        
        elif menu1 == 3:  # Exit Function
            fb.return_main_menu()
    
    
    elif menu == 2:  # Item Inventory Tracking Function
        os.system("cls")
        fb.item_inventory_tracking()
        
    
    elif menu == 3:  # Search Item Function
        os.system("cls")
        fb.search_item()
        
    
    elif menu == 4:
        os.system("cls")
        print("1. Supplier Report\n2. Hospitals Report\n3. Transaction Report\n4. Back")
        menu4 = input("> ")
        
        menu4 = check_menu4(menu4)
        
        if menu4 == 1:  # Generate Supplier Report Function
            os.system("cls")
            fb.generate_supplier_report()
            
        elif menu4 == 2:  # Generate Hospital Report Function
            os.system("cls") 
            fb.generate_hospitals_report()
            
        elif menu4 == 3:  # Allow User to Choose to Display Different Transaction report
            os.system("cls") 
            print("1. Generate Supplier Transaction Report\n2. Generate Hospital Transaction Report\n3. Back")
            menu44 = input("> ")
            
            menu44 = check_menu1_and_menu44(menu44)
            
            if menu44 == 1:  # Generate Supplier Monthly Transaction Function
                os.system("cls")
                fb.generate_month_report_supplier()
                
            elif menu44 == 2:  # Generate Hospital Monthly Transaction Function
                os.system("cls")
                fb.generate_month_report_hospital()
            
            elif menu44 == 3:
                fb.return_main_menu()

        elif menu4 == 4:
            fb.return_main_menu()
    
    
    elif menu == 5:
        os.system("cls")
        print("Goodbye! Have a nice day ~")
        time.sleep(0.5)
        os.system("cls")
        exit()
    