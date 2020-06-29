# Order-Delivery-System
Order Delivery System (ODS) for delivering products.
This project is a simple demonstration of mega e-commerce websites like Flipkart.

## Technologies
-   Flask : A micro-web framework for Python
-   MySQL : Database at the backend
-   HTML, CSS, Bootstrap, Jinja : For user interface

## Installation
1. Create virtual environment :
    >   python3 -m venv ods_env

2.  Activate the virtual environment :
    >   source ods_env/bin/activate

3.  Chnage working directory to *ODS* and install the required libraries :
    >   python3 -m pip install -r requirements.txt

## Usage
1.  Update the credentials in *py_src/db.yaml* file to connect to the mysql database. You will need to create a mysql user for this.
2.  Change working directory to *sql_src*.
3.  Open mysql prompt using following command and enter password for the created user.
    >   mysql -u "username" -p

4.  Enter following commands on mysql prompt :
    >   source ods_ddl.sql

    This will create the required database **ODS** on the local system.
    >   source ods_dml.sql

    This command is optional. It adds some dummy data in the tables.
5.  Exit the mysql prompt and change working directory to *py_src*.
6.  Enter the command to run *Flask* :
    >   python3 app.py
