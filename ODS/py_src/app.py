from flask import Flask, render_template, request, redirect
import sys
sys.path += ['../']
from OdsLib import *

app = Flask(__name__ , template_folder = '../html_src/', static_folder = '../html_src/')
pysql = PySql(app, 'db.yaml')

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

all_ids = {'customer_id' : None }




#########   CUSTOMER RELATED FUNCTIONS ########

@app.route('/CustomerSignIn', methods = ['GET', 'POST'])
def customer_signin_page():

    pysql.init()
    if request.method == 'POST' :
        if 'customer_login' in request.form :
            email = request.form['customer_email']
            password = request.form['customer_password']

            # Check here the email-id and password entered with the sql database
            ans = Customer.check_customer_signin(pysql, email, password)
            all_ids['customer_id'] = ans

            if ans :
                print("Logged In")
                return redirect('/ProductCategory')
            else :
                print("Invalid Email or Password")

    return render_template('/CustomerSignIn/customer_signin.html')


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

            if password == confirmpassword :

                # Add the details to the sql database
                customer_id = Customer.customer_signup(pysql, firstname, lastname, email, password, phone1, phone2)
                if customer_id != 0 :
                    return render_template('/CustomerSignIn/customer_signup_success.html', customer_id = customer_id)

    return render_template('/CustomerSignIn/customer_signup.html')


@app.route('/ProductCategory', methods = ['GET', 'POST'])
def user_page() :
    return render_template('/Product/product_category.html')


#@app.route('/YourOrders', methods = ['GET', 'POST'])
#def show_orders() :



@app.route('/ProductMobile', methods = ['GET', 'POST'])
def product_mobile() :
    pysql.init()
    product_details = Product.get_product_by_category(pysql, 'Mobile')
    global all_ids

    if request.method == 'POST' :

        if 'buy_now' in request.form :
            # get the quantities of product selected by customer
            quantities = request.form.getlist("quantity[]")
            for i in range(len(quantities)) :
                quantities[i] = int(quantities[i])

            # check if adding the quantities to the cart doesn't exceed cart limit
            if (Cart.get_no_of_products_in_cart(pysql, all_ids['customer_id']) + sum(quantities)) > 5 :
                print("Max cart limit reached")
                return render_template('/Product/product_mobile.html', product_details = product_details)

            # Add the product to the cart whose quantity value is greater than zero
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    for j in range(0, quantities[i]) :
                        Cart.add_product_to_cart(pysql, all_ids['customer_id'],
                                product_details[i][0])

            return redirect('/CartInfo')

    return render_template('/Product/product_mobile.html', product_details = product_details)


@app.route('/ProductLaptop', methods = ['GET', 'POST'])
def product_laptop() :
    pysql.init()
    product_details = Product.get_product_by_category(pysql, 'Laptop')
    global all_ids

    if request.method == 'POST' :

        if 'buy_now' in request.form :
            # get the quantities of product selected by customer
            quantities = request.form.getlist("quantity[]")
            for i in range(len(quantities)) :
                quantities[i] = int(quantities[i])

            # check if adding the quantities to the cart doesn't exceed cart limit
            if (Cart.get_no_of_products_in_cart(pysql, all_ids['customer_id']) + sum(quantities)) > 5 :
                print("Max cart limit reached")
                return render_template('/Product/product_laptop.html', product_details = product_details)

            # Add the product to the cart whose quantity value is greater than zero
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    for j in range(0, quantities[i]) :
                        Cart.add_product_to_cart(pysql, all_ids['customer_id'],
                                product_details[i][0])

            return redirect('/CartInfo')

    return render_template('/Product/product_laptop.html', product_details = product_details)



@app.route('/ProductClothing', methods = ['GET', 'POST'])
def product_clothing() :
    pysql.init()
    product_details = Product.get_product_by_category(pysql, 'Clothing')
    global all_ids

    if request.method == 'POST' :

        if 'buy_now' in request.form :
            # get the quantities of product selected by customer
            quantities = request.form.getlist("quantity[]")
            for i in range(len(quantities)) :
                quantities[i] = int(quantities[i])

            # check if adding the quantities to the cart doesn't exceed cart limit
            if (Cart.get_no_of_products_in_cart(pysql, all_ids['customer_id']) + sum(quantities)) > 5 :
                print("Max cart limit reached")
                return render_template('/Product/product_clothing.html', product_details = product_details)

            # Add the product to the cart whose quantity value is greater than zero
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    for j in range(0, quantities[i]) :
                        Cart.add_product_to_cart(pysql, all_ids['customer_id'],
                                product_details[i][0])

            return redirect('/CartInfo')

    return render_template('/Product/product_clothing.html', product_details = product_details)


@app.route('/ProductSport', methods = ['GET', 'POST'])
def product_sport() :
    pysql.init()
    product_details = Product.get_product_by_category(pysql, 'Sport')
    global all_ids

    if request.method == 'POST' :

        if 'buy_now' in request.form :
            # get the quantities of product selected by customer
            quantities = request.form.getlist("quantity[]")
            for i in range(len(quantities)) :
                quantities[i] = int(quantities[i])

            # check if adding the quantities to the cart doesn't exceed cart limit
            if (Cart.get_no_of_products_in_cart(pysql, all_ids['customer_id']) + sum(quantities)) > 5 :
                print("Max cart limit reached")
                return render_template('/Product/product_sport.html', product_details = product_details)

            # Add the product to the cart whose quantity value is greater than zero
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    for j in range(0, quantities[i]) :
                        Cart.add_product_to_cart(pysql, all_ids['customer_id'],
                                product_details[i][0])

            return redirect('/CartInfo')

    return render_template('/Product/product_sport.html', product_details = product_details)


@app.route('/ProductBooks', methods = ['GET', 'POST'])
def product_books() :
    pysql.init()
    product_details = Product.get_product_by_category(pysql, 'Books')
    global all_ids

    if request.method == 'POST' :

        if 'buy_now' in request.form :
            # get the quantities of product selected by customer
            quantities = request.form.getlist("quantity[]")
            for i in range(len(quantities)) :
                quantities[i] = int(quantities[i])

            # check if adding the quantities to the cart doesn't exceed cart limit
            if (Cart.get_no_of_products_in_cart(pysql, all_ids['customer_id']) + sum(quantities)) > 5 :
                print("Max cart limit reached")
                return render_template('/Product/product_books.html', product_details = product_details)

            # Add the product to the cart whose quantity value is greater than zero
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    for j in range(0, quantities[i]) :
                        Cart.add_product_to_cart(pysql, all_ids['customer_id'],
                                product_details[i][0])

            return redirect('/CartInfo')

    return render_template('/Product/product_books.html', product_details = product_details)


@app.route('/CartInfo', methods = ['GET', 'POST'])
def view_cart() :

    pysql.init()
    global all_ids

    prodids_incart = Cart.get_prod_in_cart(pysql, all_ids['customer_id'])
    prodids_incart = prodids_incart[0]
    print(prodids_incart)

    total = Cart.get_total(pysql, all_ids['customer_id'])

    product_details = []
    for i in prodids_incart :
        if i is not None :
            ans = Product.get_product_details(pysql, i)
            ans = ans[0]
            product_details.append(ans)

    return render_template('/Cart/cart_info.html', product_details =
            product_details, total = total)


#########   ADMIN RELATED FUNCTIONS ########

@app.route('/AdminSignIn', methods = ['GET', 'POST'])
def admin_signin_page():

    if request.method == 'POST' :
        if 'admin_login' in request.form :
            email = request.form['admin_email']
            password = request.form['admin_password']

            # Check here the email-id and password entered
            if email == 'atharva' and password == 'atharva' :
                print("Logged In")
                return redirect('/AdminActions')
            else :
                print("Invalid Email or Password")

    return render_template('/Admin/admin_signin.html')


@app.route('/AdminActions', methods = ['GET', 'POST'])
def select_admin_action() :
    '''if request.method == 'POST' :
        # List of options
        options = ['insert_product',
                   'add_delivery_executive',
                   'show_all_products',
                   'show_all_delivery_executives']

        # Check if any option is selected
        for option in options:
            if option in request.form:
                return redirect('/' + option)
                '''
    return render_template('/Admin/admin_actions.html')


@app.route('/InsertProduct', methods = ['GET', 'POST'])
def add_products() :
    pysql.init()
    if request.method == 'POST' :
        if 'add_product' in request.form :
            # Take data from page
            name = request.form['product_name']
            category = request.form['product_category']
            price = request.form['product_price']
            seller = request.form['product_seller']
            quantity = request.form['product_quantity']

            # Insert in sql database
            ans = Product.add_product(pysql, name, category, price, seller, quantity)
            if ans :
                print('Successfully Added')
            else :
                print('Error adding product in table')

    return render_template('/Admin/insert_product.html')


@app.route('/AddDeliveryExecutive', methods = ['GET', 'POST'])
def add_deliveryexecutive() :
    pysql.init()
    if request.method == 'POST' :
        if 'add_delivery_executive' in request.form :

            # Take data from page
            firstname = request.form['delivery_executive_first_name']
            lastname = request.form['delivery_executive_last_name']
            email = request.form['delivery_executive_email']
            password = request.form['delivery_executive_password']
            salary = request.form['delivery_executive_salary']
            worktime = request.form['delivery_executive_worktime']
            phone1 = request.form['delivery_executive_phone']
            phone2 = request.form['delivery_executive_alternatephone']

            # Insert in sql database
            ans = DeliveryExecutive.add_deliveryexecutive(pysql, firstname, lastname, email, password, worktime, salary, phone1, phone2 )
            if ans :
                print('Successfully Added')
            else :
                print('Error adding delivery executive in table')

    return render_template('/Admin/add_delivery_executive.html')


@app.route('/ShowAllProducts', methods = ['GET', 'POST'])
def show_all_products() :
    pysql.init()
    product_details = Product.get_all_products(pysql)
    return render_template('/Admin/show_all_products.html', product_details = product_details)


@app.route('/ShowAllDeliveryExecutives', methods = ['GET', 'POST'])
def show_all_deliveryexecutives() :
    pysql.init()
    delivery_executive_details = DeliveryExecutive.get_all_deliveryexecutives(pysql)
    return render_template('/Admin/show_all_delivery_executives.html', delivery_executive_details = delivery_executive_details)


#########   DELIVERY EXECUTIVE RELATED FUNCTIONS ########

@app.route('/DeliveryExecutiveSignIn', methods = ['GET', 'POST'])
def deliveryexecutive_signin_page() :
    pysql.init()
    if request.method == 'POST' :
        if 'deliveryexecutive_login' in request.form:
            email = request.form['deliveryexecutive_email']
            password = request.form['deliveryexecutive_password']

            # Check here the email-id and password entered with the sql database
            ans = DeliveryExecutive.check_deliveryexecutive_signin(pysql, email, password)
            all_ids['deliveryexecutive_id'] = ans
            if ans :
                print("Logged In")
                return redirect('/DeliveryDetails')
            else :
                print("Invalid Email or Password")

    return render_template('/DeliveryExecutiveSignIn/deliveryexecutive_signin.html')


@app.route('/DeliveryDetails', methods = ['GET', 'POST'])
def delivery_details_page() :
    pysql.init()
    undelivered_details = DeliveryExecutive.get_orders_details(pysql, all_ids['deliveryexecutive_id'], 0)
    delivered_details = DeliveryExecutive.get_orders_details(pysql, all_ids['deliveryexecutive_id'], 1)

    if request.method == 'POST' :
        order_ids = []
        for i in undelivered_details:
        order_ids.append(i[0])

        selected_order_id = request.form["delivered"]
        for i in order_ids:
            if selected_order_id == i:
                DeliveryExecutive.change_delivery_status(pysql, selected_order_id)

    return render_template('/DeliveryExecutiveSignIn/delivery_details.html', undelivered_details = undelivered_details, delivered_details = delivered_details)

if __name__ == "__main__" :
    app.run(debug = True)
