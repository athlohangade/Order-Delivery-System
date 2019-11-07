from flask import Flask, render_template, request, redirect
import sys
sys.path += ['../']
from OdsLib import *

app = Flask(__name__ , template_folder = '../html_src/', static_folder = '../html_src/')
pysql = PySql(app, 'db.yaml')

@app.route('/', methods = ['GET', 'POST'])
def index():
    pysql.init()
    return render_template('index.html')

@app.route('/CustomerSignIn', methods = ['GET', 'POST'])
def customer_signin_page():
    pysql.init()
    if request.method == 'POST' :
        if 'customer_login' in request.form :
            email = request.form['customer_email']
            password = request.form['customer_password'] 

            # Check here the email-id and password entered with the sql database
            ans = CustomerData.check_customer_signin(pysql, email, password)

            if ans :
                print("Logged In")
                return redirect('/Products')
            else :
                print("Invalid Email or Password")

    return render_template('/CustomerSignIn/customer_signin.html')

@app.route('/Products', methods = ['GET', 'POST'])
def product_page() :
    pass

@app.route('/CustomerSignUp', methods = ['GET', 'POST'])
def customer_signup_page() :
    pysql.init()
    if request.method == 'POST' :
        if 'customer_signup' in request.form:
            userDetails = request.form
            firstname = userDetails['customer_firstname']
            lastname = userDetails['customer_lastname']
            email = userDetails['customer_email']
            password = userDetails['customer_password']
            confirmpassword = userDetails['customer_confirmpassword']
            phone1 = userDetails['customer_phone1']
            phone2 = userDetails['customer_phone2']
         
            print("Check password")
            if password == confirmpassword :

                print("Check password")
                # Add the details to the sql database
                customer_id = CustomerData.enter_customer_data(pysql, firstname, lastname, email, password, phone1, phone2)
                if customer_id != 0 :
                    return render_template('/CustomerSignIn/customer_signup_success.html', customer_id = customer_id)

    return render_template('/CustomerSignIn/customer_signup.html')



@app.route('/DeliveryExecutiveSignIn', methods = ['GET', 'POST'])
def deliveryexecutive_signin_page() :
    pysql.init()
    if request.method == 'POST' :
        if 'deliveryexecutive_login' in request.form:
            email = request.form['deliveryexecutive_email']
            password = request.form['deliveryexecutive_password'] 
            
            # Check here the email-id and password entered with the sql database
            ans = DeliveryExecutiveData.check_deliveryexecutive_signin(pysql, email, password)

            if ans :
                print("Logged In")
                return redirect('DeliveryExecutiveSignIn/DeliveryDetails')
            else :
                print("Invalid Email or Password")

    return render_template('/DeliveryExecutiveSignIn/deliveryexecutive_signin.html')

@app.route('/DeliveryExecutiveSignIn/DeliveryDetails', methods = ['GET', 'POST'])
def delivery_details_page() :
    pass

if __name__ == "__main__" :
    app.run(debug = True)
