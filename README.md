# APU-Inventory-Management-System
Python, Inventory Management System for Personal Protective Equipment | 2024

# Project Overview 
This Python project is made for Asia Pacific University PWP Python Programming assignment, The system is to manage the inventory of PPE that it

# Key Features
The application supports 1 user roles with distinct functionalities:

## 1. User Menu
Log in with username and password
- Inventory Info Service (Distribute PPE/Recieve PPE)
- Item Inventory Tracking
- Search Inventory
- Generate Report

## Inventory List
These are the list of PPE items the department recieves are listed:
| Item Code | Item Name |
|---------:|--------|
| HC | Head Cover  |
| FS | Face Shield |
| MS |   Mask      |
| GL |   Gloves    |
| GW |    Gown     |
| SC | Show Covers |

## Feature Declaration
The inventory system has to be programmed in Python. It is required to write the Python program with following features:
- Login Functionality
- Initial inventory Creation
- Item Inventory Update
- Item Inventory Tracking
- Searching Functionality
- Report Functionality

# Database
The system uses text files as the database sequentially detailed in `.txt`. The database includes the following tables:

- suppliers.txt
- supplier_distribution.txt
- ppe.txt
- distribution.txt
- hospital.txt

# Prerequisites
- Visual Studio Code (VSC)
- Basic Python Knowledge
- `.txt` Files as Database

# Installation and Setup
- Clone the repository
- Open the solution in Visual Studio
- Update the SQL connection string in the source code to match your SQL Server configuration // Example connection string (modify as per your setup) string connectionString =  "Server=yourServerName;Database=Users;User Id=yourUsername;Password=yourPassword;";
- Build the solution
- Run the application

# Highlights
- Developed using Python only concepts
- Includes input validation
- Password system allows 3 logins before termination
- Follows coding style guidelines with proper indentation and comments
-	Details of suppliers need to be stored in `suppliers.txt` file. 
-	When testing the program, you should perform adequate updates on each item. This is to prove whether the feature is correctly functioning. 
-	Before distributing any item to hospitals, the program should check for available quantity in stock. User need to be notified if the quantity in stock is insufficient. The program should also indicate the current quantity in stock for the user to retry with appropriate quantity.
- The program should have a feature to create 'hospitals.txt' file for storing and updating hospital details. Include hospital code for each of them.  You can only have 3 or 4 hospitals.
- Record all distributions in `distribution.txt` file.

# Limitations
- Certain features might not be functional, unknown possible errors or incomplete functionality might occur
- Requires thorough testing and validation
- Only accepts integer for selection in menu section

# Contributions
This is a group assignment completed by a team of 5 members, this project was completed with each member assigned to different system functions and documentation.
Feel free to suggest any improvements if you encounter any issues, bugs.

# Diclaimer 
⚠️ IMPORTANT: This project may not function very well. 
The system is not fully maintained, and some features 
may be incomplete or not fully tested.

Note: Without additional development and testing, which was created as for acedemic purposes, could not appropriate for production. 
