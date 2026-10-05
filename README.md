# Phone Book Management System

A simple desktop-based Phone Book Management System made using Python, Tkinter and MySQL.

The application allows users to add, search, view and delete contacts. Contacts are organized into three city-wise tables: Delhi, Kolkata and Mumbai.

## Features

* Add new contacts
* Search contacts by name
* View all contacts
* Delete contacts
* Automatic contact ID generation
* MySQL database storage
* Simple graphical user interface

## Technologies Used

* Python
* Tkinter
* MySQL
* PyMySQL
* python-dotenv

## Database

The project uses a MySQL database called `phonebook`.

It contains three tables:

phonebook
├── Delhi
├── Kolkata
└── Mumbai

Each table contains:

id
name
addr
phNo

## How to Run

### 1. Clone the repository

git clone <repository-url>

### 2. Install required packages

pip install -r requirements.txt

### 3. Set up MySQL

Create a database named:CREATE DATABASE phonebook;


Then create the Delhi, Kolkata and Mumbai tables with the required columns.

### 4. Create the `.env` file

Create a file named `.env` in the project folder:

MYSQL_PASSWORD=your_mysql_password

Replace `your_mysql_password` with your local MySQL password.

The `.env` file is intentionally not included in GitHub because it contains database credentials.

### 5. Run the application

python phBook.py

## What I Learned

This project helped me understand:

* Python GUI development using Tkinter
* Connecting Python with MySQL
* Executing SQL queries from Python
* Basic CRUD operations
* Input validation
* Using environment variables for sensitive information

## Future Improvements

Some features I would like to add later:

* Edit existing contacts
* User login and authentication
* Better phone number validation
* Import and export contacts
* Improved UI
* Better database design

## Author

**Srijon Nandy**

