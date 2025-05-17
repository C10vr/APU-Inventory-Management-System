import os
import time
import datetime
from datetime import datetime


# Color text
red = "\033[91m"
blue = "\033[96m"


# Bold text
end = "\033[0;0m"


# Return to Main Menu function
def return_main_menu():
    os.system("cls")
    print("Direct back to menu now.")                 
    time.sleep(0.5)
    os.system("cls")
    print("Direct back to menu now..")
    time.sleep(0.5)
    os.system("cls")
    print("Direct back to menu now...")



# ----------------------------------------------------------------- Login Function -----------------------------------------------------------------------------------------------------------------------------


def login():
    
    # Initial username and password (Pre-set)
    credentials = [('user', '123'), ('user2', '123'),
               ('user3', '123'), ('user4', '123'),
               ('user5', '123')]

    count = 1
    
    while True:
        print("Welcome to PPE Inventory Management System")
        print("------------------------------------------\n")
        username = input('Enter your username: ') # Prompt user for username
        password = input('Enter your password: ') # Prompt user for password
        
        for i in credentials:
            if username == i[0] and password == i[1]:  # If user entered username and password match the username and password in credentials, allow user login
                os.system("cls")
                print("Log in.")
                time.sleep(0.5)
                os.system("cls")
                print("Log in..")
                time.sleep(0.5)
                os.system("cls")
                print("Log in...")
                time.sleep(0.5)
                
                os.system('cls')
                print('######################')             
                print(f'# {blue}Log in succesfully{end} #')    
                print('######################')                
                time.sleep(2)
                
                os.system('cls')
                print('Welcome', username)
                return True
            
        if count == 3: # If user enter username or password wrongly 3 times, will immediately terminate user
            os.system('cls')
            print(f'{red}You have entered the wrong password 3 times{end}')
            time.sleep(2)
            
            os.system('cls')
            print(f'{red}Program Has Been Terminated!{end}')
            exit()
            
        else: # Inform user that user has key in wrong username or password
            os.system('cls')
            print(f'{red}You have entered the wrong username or password, please try again{end}')
            time.sleep(2)
            os.system('cls')
            count += 1 # count += 1 mean that the log in attempt increase by 1 time 


# ----------------------------------------------------------------- Initial Inventory Creation Function -----------------------------------------------------------------------------------------------------------------------------

def initial_inventory_creation():
    
    file_path_ppe = "ppe.txt"
    file_path_suppliers = "suppliers.txt"

    if not os.path.exists(file_path_ppe):  # Create ppe.txt file if it does not exist
        print("Initializing Inventory Creation")
        time.sleep(2)
    
        print("This is the first time you are running this program")
        time.sleep(1)
        os.system('cls')
    
        with open(file_path_ppe, "w") as file:  # Ready the file so that can write data into the ppe.txt file
            print("Inserting Item Details\n")
            cont = True
      
            while cont: # When cont is True, ask user for the item information
                item_code = input("Enter the item code: ")
                item_name = input("Enter the item name: ")
                quantity = 100
                supplier_code = input("Enter the supplier code: ")
        
                file.write(f"{item_code},{item_name},{quantity},{supplier_code}\n")  # After received item information, write it into ppe.txt file using specific arrangement and use delimiter (,) to differentiate teh data 
        
                user = input("Added Item Details successfully, would you like to add more (Yes/No)\n>").lower() # Ask useris that user want to continue add new item
        
                if user == "yes":
                    cont = True # Repeat back above code to ask user for the item information
          
                elif user == "no":
                    cont = False # Will stop asking user for the new item information
          
                else:
                    print("Invalid input, please try again")
                    os.system('cls')
                    cont = True  # User will be direct back to asking for insert item information

    if not os.path.exists(file_path_suppliers):  # Create suppliers.txt file if it does not exist
        
        with open(file_path_suppliers,'w') as file:  # Ready the file so that can write data into suppliers.txt file
            os.system('cls')
            print('Insert Supplier details\n')
            cont = True

            num_of_supplier = 0
            
            while cont: # When cont is True, ask user for the supplier information
                
                sup_code = input('Enter supplier code: ')
                sup_name = input('Enter supplier name: ')
                sup_address = input('Enter supplier address: ')
        
                file.write(f"{sup_code},{sup_name},{sup_address}\n") # After received supplier information, write it into suppliers.txt file using specific arrangement and use delimiter (,) to differentiate the data 
        
                user = input('Added supplier details successfully, Would you like to add more? (Yes/No)\n').lower() # Ask useris that user want to continue add new item
        
                if user == 'yes':
                    num_of_supplier += 1  # If user type yes mean user already added one supplier
                    print(f"\nCurrent number of supplier: {num_of_supplier} (Maximum number of supplier is 4)\n")
                    
                    if num_of_supplier >= 4: # If the number of supplier more than 4, system will force stop user to continue insert data
                        cont = False
                    else:
                        cont = True
                    
                elif user == 'no':
                    num_of_supplier += 1
                    print(f"\nCurrent number of supplier: {num_of_supplier} (Minimum number of supplier is 3)\n")
                    
                    if num_of_supplier <= 2: # If the number of supplier below 3, system will force  user to continue insert data
                        cont = True
                    else:
                        cont = False
                    
          
                else:
                    print("Invalid input, please try again")
                    os.system('cls')
                    cont = True  # User will be direct back to asking for insert item information
               
        # Make sure user only enter 3 or 4 supplier only    
        if num_of_supplier < 3:
            print("There are minimum 3 supplier.")
            cont = True
        elif num_of_supplier >= 4:
            print("There are maximum 4 supplier only.")

    return False  # Return False when no more suppliers are being added


# ----------------------------------------------------------------- Item Inventory Update Function - Distribute PPE-----------------------------------------------------------------------------------------------------------------------------


def distribute_ppe():
    
    # Create hospitals.txt file if it does not exits
    if not os.path.exists("hospitals.txt"):
        
        file = open("hospitals.txt", "w")  # Ready the file so that can write data into hospitals.txt file
        cont = True
        print("Please insert hospital details\n")
        
        num_of_hospital = 0
        
        # If it is True, run below code
        while cont:
            hospital_code = input("Enter hospital code: ")
            hospital_name = input("Enter hospital name: ")
            hospital_address = input("Enter hospital address: ")
            
            file.write(f"{hospital_code},{hospital_name},{hospital_address}\n") # After received hospital information, write it into hospitals.txt file using specific arrangement and use delimiter (,) to differentiate the data
            
            continue_or_not = input('Added supplier details successfully, Would you like to add more? (Yes/No)\n').lower() # Ask useris that user want to continue add new item
            
            if continue_or_not == "yes":
                num_of_hospital += 1
                print(f"\nCurrent number of hospital: {num_of_hospital} (Maximum number of hospital is 4)\n")
                
                if num_of_hospital >= 4: # If the number os hospital more than 4, system will force stop user to continue insert data
                    cont = False
                else:
                    cont = True 
                
            elif continue_or_not == "no": 
                num_of_hospital += 1
                print(f"\nCurrent number of hospital: {num_of_hospital} (Minimum number of hospital is \n)")
                
                if num_of_hospital <=2: # If the number of hospital is below 3, system will force user to insert more information
                    cont = True
                else:
                    cont = False
                
                                
            else:
                print("Invalid input, please try again")
                os.system('cls')
                cont = True  # User will be direct back to asking for insert item information
        
        return False # Return False when no more hospital to be add
        
    
    # Open ppe.txt file and read the data inside the file
    file = open("ppe.txt", "r")
    lines = file.readlines() # Assign all the data into variable lines
    
    print("Current inventory list: ")
    print("I.Code, I.Name, Quantity, S.Code")  # I.Code = Item Code    I.Name = Item Name    S.Code = Supplier Code
    print("................................")
    for line in lines:
        print(line.strip())  # Display all the PPE item
    
    file.close()  # Close file after used
    
    user_enter_item_code = input("Please enter the item code of the item you want to distribute: ") # Prompt the user for the item to update
    
    updated_lines = [] # Create a empty list for storing updated lines
    
    item_found = False
    continue_or_not = False
    
    for line in lines:
        part = line.strip().split(',') # Seperate the data inside ppe.txt file and set it to variable - part
        
        if user_enter_item_code in part:
            item_found = True  # If user entered item code match the variable part, then assign true to variable - item_found for further process
            
            if int(part[2]) < 50: # If the quantity of user enter item code is less than 50, system will prompt a warning to user
                print("\n###########################################")
                print(f"# The stock of {part[1]} is less than 50 #")
                print("###########################################\n")
                time.sleep(2) # Wait for 2 seconds then continue for another program
            
            while not continue_or_not:
                
                quantity_distributed_to_hospital = int(input("How many item you want to distribute? : "))
                hospital_receive_ppe = input("Which hospital (hospital code) have received the distributed PPE item : ")  # Example hospital code is H01, H02
                time_distribution = datetime.now() # Set the time distribution to the time that user update the item
            
                updated_line1 = list()
            
                            
            
                if (int(part[2]) - quantity_distributed_to_hospital) < 0:
                    print("\nInsufficient stock available, please try with less distribute amount.")
                    time.sleep(2)
                    continue_or_not = False
                else:
                    part[2] = str(int(part[2]) - quantity_distributed_to_hospital) # The initial quantity will minus the quantity that has been distributed to hospital
                    continue_or_not = True
                    
            
            updated_line = ','.join(part)  # Join back the part using comma (,)
            updated_lines.append(updated_line + '\n')  # Add the updated line into the updated lines along with a new line (\n)
            updated_line1.append(updated_line) # Add the updated line into updated line1
        
        else:
            updated_lines.append(line)
    
    if item_found:
        # Update the ppe.txt file
        file = open("ppe.txt", "w") 
        file.writelines(updated_lines)  # Write all the data inside updated_lines into the ppe.txt file  
        print(f"\ninventory distributed successfully on {time_distribution.strftime("%d %b - %H:%m")}.")  # Inform user that the distribution process has successful   
        file.close()
        
        # insert the record into the distribution file
        distribution_file = open("distribution.txt", "a")
        distribution_file.writelines(f"{hospital_receive_ppe},{user_enter_item_code},{quantity_distributed_to_hospital},{time_distribution}\n")
        distribution_file.close()
        
    else:
        print("Item not found in the inventory.")
    
    time.sleep(2) # Wait for 2 seconds    
        
    os.system('cls') # Clear all the previous output
    
    file = open("ppe.txt", "r")
    print("Below is new inventory list: ")
    print(".............................")
    for data in file:  # Display the updated ppe.txt file
        data = data.strip()  # Remove any leading, and trailing whitespaces for each data inside the file
        print(data)
        
    time.sleep(5)
    
    print(f"\nPress enter for return back to menu. {red}IF NOT{end}, just leave it.")  # Allow user to control go back to main menu
    z = input("> ") # variable z have no actual use and meaning, just for user to press enter and it will direct back to main menu
    return_main_menu()
    

# ----------------------------------------------------------------- Item Inventory Update - Receive PPE Function -----------------------------------------------------------------------------------------------------------------------------


def receive_ppe():
    # Open ppe.txt file and read the data inside the file
    file = open("ppe.txt", "r")
    lines = file.readlines() # Assign all the data into variable lines
    
    print("Current inventory list: ")
    print("I.Code, I.Name, Quantity, S.Code")  # I.Code = Item Code    I.Name = Item Name    S.Code = Supplier Code
    print("................................")
    for line in lines:
        print(line.strip())  # Display all the PPE item
    
    file.close()  # Close file after used
    
    user_enter_item_code = input("Please enter the item code of the item you want to increase the stock: ")

    updated_lines = [] # Create a empty list for storing updated lines
    
    item_found = False  # First assign the item_found to False, it will be change after found the item by using item code

    for line in lines:
        part = line.strip().split(',') # Seperate the data inside ppe.txt file and set it to variable - part
        
        if user_enter_item_code in part:
            item_found = True  # If user entered item code match the variable part, then assign true to variable - item_found for further process
            
            if int(part[2]) < 50: # If the quantity of user enter item code is less than 50, system will prompt a warning to user
                print("\n###########################################")
                print(f"# The stock of {part[1]} is less than 50 #")
                print("###########################################\n")
                time.sleep(2) # Wait for 2 seconds then continue for another program
            
            quantity_received_from_supplier = int(input("How many item you have received? : "))
            supplier_supply_item = input("Which supplier (supplier code) have send the PPE item : ")  # Example hospital code is H01, H02
            time_distribution = datetime.now() # Set the time distribution to the time that user update the item
            
            updated_line1 = list()
            
            part[2] = str(int(part[2]) + quantity_received_from_supplier) # The initial quantity will minus the quantity that has been distributed to hospital
            
            updated_line = ','.join(part)  # Join back the part using comma (,)
            updated_lines.append(updated_line + '\n')  # Add the updated line into the updated lines along with a new line (\n)
            updated_line1.append(updated_line)  # Add the updated line into updated line1
        
        else:
            updated_lines.append(line)
            
    if item_found:
        # Update the ppe.txt file 
        file = open("ppe.txt", "w") 
        file.writelines(updated_lines)
        print(f"\nReceived inventory successfully on {time_distribution.strftime("%d %b - %H:%m")}.")
        file.close()
        
        # insert the record into supplier_distribution to store history for supplier send inventory
        supplier_distribution_file = open("supplier_distribution.txt", "a")
        supplier_distribution_file.writelines(f"{supplier_supply_item},{user_enter_item_code},{quantity_received_from_supplier},{time_distribution}\n")
        supplier_distribution_file.close()
    
    else:
        print("Item not found in the inventory")
    
    
    time.sleep(2)
    
    file = open("ppe.txt", "r")
    
    os.system('cls')
    print("Below is new inventory list: ")
    print(".............................")
    for data in file:  # Display the updated ppe.txt file
        data = data.strip()  # Remove any leading, and trailing whitespaces for each data inside the file
        print(data)
        
    time.sleep(5)
    
    print(f"\nPress enter for return back to menu. {red}IF NOT{end}, just leave it.") # Allow user to control go back to main menu
    z = input("> ") # variable z have no actual use and meaning, just for user to press enter and it will direct back to main menu
    return_main_menu()
    

# ----------------------------------------------------------------- Item Inventory Tracking Function -----------------------------------------------------------------------------------------------------------------------------


def item_inventory_tracking():   # JS will do
    os.system('cls')
    
    # Read the ppe.txt file and process its content
    inventory = []
    file = open("ppe.txt", "r")
    for line in file:
        parts = line.strip().split(',')  # Split the information of each data using comma (,) and assign it as parts
        item_code = parts[0]
        item_name = parts[1]
        item_quantity = int(parts[2])
        supplier_code = parts[3]
            
        inventory.append({"item_code": item_code, "item_name": item_name, "quantity": item_quantity, "supplier": supplier_code})  # Insert all information into inventory using dictionary

    # Sort inventory by item code
    sorted_inventory = sorted(inventory, key=lambda x: x["item_code"])

    # Print total quantity of all items sorted by item code
    print("Total quantity of all items (sorted by item code):")
    for item in sorted_inventory:
        print(f"{item['item_code']}: {item['quantity']} boxes")

    # Check have item that is below 25 boxes or not, if got then it is True, if not, then it is False
    item_below_25 = [item for item in sorted_inventory if item["quantity"] < 25]
    

    
    if item_below_25:
        # Print items with less than 25 boxes in stock
        print("\nItems with less than 25 boxes in stock:")
        for item in item_below_25:
            print(f"{item['item_code']}: {item['quantity']} boxes")
    else:
        print("\nItems with less than 25 boxes in stock:")
        print("There are no PPE item is less than 25 boxes in stock.\n")
        
    time.sleep(5)
    
    print(f"\nPress enter for return back to menu. {red}IF NOT{end}, just leave it.")  # Allow user to control go back to main menu
    z = input("> ") # variable z have no actual use and meaning, just for user to press enter and it will direct back to main menu
    return_main_menu()
    

# ----------------------------------------------------------------- Search Item Function -----------------------------------------------------------------------------------------------------------------------------


def search_item():   # Joshau will do
    
    os.system('cls')
    
    # Open ppe.txt file and read the data inside the file
    file = open("ppe.txt", "r")
    lines = file.readlines() # Assign all the data into variable lines
    
    print("Current inventory list: ")
    print("I.Code, I.Name, Quantity, S.Code")  # I.Code = Item Code    I.Name = Item Name    S.Code = Supplier Code
    print("................................")
    for line in lines:
        print(line.strip())  # Display all the PPE item
    
    file.close()  # Close file after used
    
    item_code_search = input("\nPlease enter the code of the item want to search: ")
    
    # Read the distribution.txt file and process its content
    distributions = []
    with open('distribution.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')  # Split the information of each data using comma (,) and assign it as parts
            hospital_code = parts[0]
            code = parts[1]
            quantity = int(parts[2])
            distributions.append({"hospital_code": hospital_code, "item_code": code, "quantity": quantity})   # Insert all information into distributions variable using dictionary

    # Filter distributions by the given item code
    filtered_distributions = [d for d in distributions if d["item_code"] == item_code_search]

    if not filtered_distributions:
        print(f"\nNo distributions record found for item code {item_code_search}.")

    # Sum quantities distributed to the same hospital
    hospital_distribution = {}
    for dist in filtered_distributions:
        hospital_code = dist["hospital_code"]
        if hospital_code in hospital_distribution:
            hospital_distribution[hospital_code] += dist["quantity"]
        else:
            hospital_distribution[hospital_code] = dist["quantity"]

    # Print the distribution list
    print(f"\nDistribution list for item code - {item_code_search}:\n")
    for hospital_code, total_quantity in hospital_distribution.items():
        print(f"Hospital {hospital_code}: {total_quantity} boxes")
    
    time.sleep(5)

    print(f"\nPress enter for return back to menu. {red}IF NOT{end}, just leave it.")  # Allow user to control go back to main menu
    z = input("> ") # variable z have no actual use and meaning, just for user to press enter and it will direct back to main menu
    return_main_menu()


# ----------------------------------------------------------------- Generate Supplier Report Function -----------------------------------------------------------------------------------------------------------------------------


def generate_supplier_report():
    
    # Read the suppliers.txt file and process its content
    suppliers = {}
    with open('suppliers.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            supplier_code = parts[0]
            supplier_name = parts[1]
            supplier_location = parts[2]               
            suppliers[supplier_code] = {
                "name": supplier_name,
                "location": supplier_location,
                "items": []
            }

    # Read the ppe.txt file and process its content
    with open('ppe.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            item_code = parts[0]
            item_name = parts[1]
            quantity = int(parts[2])
            supplier_code = parts[3]
            if supplier_code in suppliers:
                suppliers[supplier_code]["items"].append(f"{item_code} ({item_name})") # add the item code and item name into the suppliers variable

    # Print the supplier report
    print("Supplier Report:\n")
    print("-----------------------------\n")
    
    for supplier_code, details in suppliers.items():
        print(f"Supplier Code: {supplier_code}")
        print(f"Supplier Name: {details['name']}")
        print(f"Location: {details['location']}")
        print(f"Supplies Item: {', '.join(details['items']) if details['items'] else 'No items supplied'}") # If the supplier got supply any PPE item, it will displat at this output
        print()
        
    time.sleep(5)
    
    print(f"\nPress enter for return back to menu. {red}IF NOT{end}, just leave it.")  # Allow user to control go back to main menu
    z = input("> ") # variable z have no actual use and meaning, just for user to press enter and it will direct back to main menu
    return_main_menu()
    

# ----------------------------------------------------------------- Generate Hospitals Report Function -----------------------------------------------------------------------------------------------------------------------------


def generate_hospitals_report():
    # Read the hospitals.txt file and process its content
    hospitals = {}
    with open('hospitals.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            hospital_code = parts[0]
            hospital_name = parts[1]
            hospital_location = parts[2]
            hospitals[hospital_code] = {
                "name": hospital_name,
                "location": hospital_location,
                "distributions": {}
            }

    # Read the distribution.txt file and process its content
    with open('distribution.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            hospital_code = parts[0]
            item_code = parts[1]
            quantity = int(parts[2])
            if hospital_code in hospitals:
                if item_code in hospitals[hospital_code]["distributions"]:
                    hospitals[hospital_code]["distributions"][item_code] += quantity  # Sum all of the relavent quantity of PPE that has been distributed to hospital
                else:
                    hospitals[hospital_code]["distributions"][item_code] = quantity  # If don't more than one distribution record, it will just maintain the only record

    # Print the hospital report
    print("Hospital Report")
    print("-----------------------------\n")
    
    for hospital_code, details in hospitals.items():
        print(f"Hospital Code: {hospital_code}")
        print(f"Hospital Name: {details['name']}")
        print(f"Location: {details['location']}")
        print("Distributions:")
        if details['distributions']:
            # If there are any distribution, it will print out, else, it will print "No distribution"
            for item_code, total_quantity in details['distributions'].items():  
                print(f"  {item_code}: {total_quantity} boxes")
        else:
            print("  No distributions")
        print()
        
    
    time.sleep(5)
    
    print(f"\nPress enter for return back to menu. {red}IF NOT{end}, just leave it.")  # Allow user to control go back to main menu
    z = input("> ") # variable z have no actual use and meaning, just for user to press enter and it will direct back to main menu
    return_main_menu()


# ----------------------------------------------------------------- Generate Transaction Report - Supplier Transaction Function -----------------------------------------------------------------------------------------------------------------------------


def generate_month_report_supplier():
    
    os.system("cls")
    
    # Prompt user for month and year
    input_date = input("Please key in the month and year (e.g., June, 2024): ")
    
    try:
        # Parse the user input to get the month and year
        month_str, year_str = input_date.split(',')
        month = datetime.strptime(month_str.strip(), '%B').month
        year = int(year_str.strip())
    except ValueError:
        print("Invalid input. Please enter the month and year in the format 'Month, Year' (e.g., June, 2024).")
        return
    
    # Initialize list to store supplier distributed data
    supplier_distribution = []

    with open('supplier_distribution.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            supplier_code = parts[0]
            item_code = parts[1]
            quantity = int(parts[2])
            timestamp = parts[3]
            date_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f') # it will set the date_time to a time value
            
            
            if date_time.year == year and date_time.month == month:
                supplier_distribution.append({
                    "supplier_code": supplier_code,
                    "item_code": item_code,
                    "quantity": quantity,
                    "timestamp": f"  [{date_time.strftime("%d")} {date_time.strftime("%B")} {date_time.strftime("%Y")}  {date_time.strftime("%H")}:{date_time.strftime("%M")}]" # Assign a more suitable format to display time
                })

    # Print the monthly report for supplier
    print(f"\nOverall Transaction Report for {year}-{month:02d}:\n")
    if supplier_distribution:
        print("Supplier Distributed :")
        print("Format : Supplier Code : Item Code - Number Distributed   [Time]")
        print("----------------------------------------------------------------")
        for dist in supplier_distribution:  # For the item inside supplier_distribution.txt file , display the data using below format
            print(f"  Supplier {dist['supplier_code']}: {dist['item_code']} - {dist['quantity']} boxes on {dist['timestamp']}")  # Format to display the information
    else:
        print("No transactions found for the selected month.")
    
    
    time.sleep(5)

    print(f"\nPress enter for return back to menu. {red}IF NOT{end}, just leave it.")  # Allow user to control go back to main menu
    z = input("> ") # variable z have no actual use and meaning, just for user to press enter and it will direct back to main menu
    return_main_menu()
        
        
# ----------------------------------------------------------------- Generate Transaction Report - Hospital Transaction Function -----------------------------------------------------------------------------------------------------------------------------


def generate_month_report_hospital():
    
    os.system("cls")
    
    # Prompt user for month and year
    input_date = input("Please key in the month and year (e.g., June, 2024): ")
    
    try:
        # Parse the user input to get the month and year
        month_str, year_str = input_date.split(',')
        month = datetime.strptime(month_str.strip(), '%B').month
        year = int(year_str.strip())
    except ValueError:
        print("Invalid input. Please enter the month and year in the format 'Month, Year' (e.g., June, 2024).")
        return

    # Initialize list to store distribution data
    distributions = []

    # Read the distribution.txt file and process its content
    with open('distribution.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            hospital_code = parts[0]
            item_code = parts[1]
            quantity = int(parts[2])
            timestamp = parts[3]
            date_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
            
            if date_time.year == year and date_time.month == month:
                distributions.append({
                    "hospital_code": hospital_code,
                    "item_code": item_code,
                    "quantity": quantity,
                    "timestamp": f"  [{date_time.strftime("%d")} {date_time.strftime("%B")} {date_time.strftime("%Y")}  {date_time.strftime("%H")}:{date_time.strftime("%M")}]" 
                })

    # Print the monthly report for hospital
    print(f"\nOverall Transaction Report for {year}-{month:02d}:\n")
    if distributions:
        print("Distributions to Hospitals:")
        print("Format : Hospital Code : Item Code - Number Distributed   [Time]")
        print("----------------------------------------------------------------")
        for dist in distributions:
            print(f"Hospital {dist['hospital_code']} : {dist['item_code']} - {dist['quantity']} boxes on {dist['timestamp']}")
    else:
        print("No transactions found for the selected month.")
    
    
    time.sleep(5)
    
    print(f"\nPress enter for return back to menu. {red}IF NOT{end}, just leave it.")  # Allow user to control go back to main menu
    z = input("> ") # variable z have no actual use and meaning, just for user to press enter and it will direct back to main menu
    return_main_menu()


