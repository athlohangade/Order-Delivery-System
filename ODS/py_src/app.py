from flask import Flask, render_template, request, redirect
import sys
sys.path += ['../']
from OdsLib import *

app = Flask(__name__ , template_folder = '../html_src/', static_folder = '../html_src/')
pysql = PySql(app, 'db.yaml')

all_ids = { 'customer_id'           : None,
            'address_id'            : None,
            'deliveryexecutive_id'  : None,
            'payment_method'        : None }


@app.route('/', methods = ['GET', 'POST'])
def index():
    global all_ids
    all_ids = { 'customer_id'           : None,
                'address_id'            : None,
                'deliveryexecutive_id'  : None,
                'payment_method'        : None }

    return render_template('index.html')


#########   CUSTOMER RELATED FUNCTIONS ########

@app.route('/CustomerSignIn', methods = ['GET', 'POST'])
def customer_signin_page():

    pysql.init()
    global all_ids

    if request.method == 'POST' :

        # Check if the button is selected
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

            # Get the details
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


@app.route('/ProductMobile', methods = ['GET', 'POST'])
def product_mobile() :
    pysql.init()

    # Get all the mobiles 
    product_details = Product.get_product_by_category(pysql, 'Mobile')
    global all_ids

    if request.method == 'POST' :

        if 'buy_now' in request.form :
            # get the quantities of product selected by customer
            quantities = request.form.getlist("quantity[]")
            for i in range(len(quantities)) :
                quantities[i] = int(quantities[i])

            # check if the issued quantity is present in product stock
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    if not(Product.check_if_in_stock(pysql, all_ids['customer_id'], product_details[i][0], quantities[i])) :
                        print("Not enough in stock")
                        return render_template('/Product/product_mobile.html', product_details = product_details)

            # check if adding the quantities to the cart doesn't exceed cart limit
            if (Cart.get_no_of_products_in_cart(pysql, all_ids['customer_id']) + sum(quantities)) > 5 :
                print("Max cart limit reached")
                return render_template('/Product/product_mobile.html', product_details = product_details)

            # Add the product to the cart whose quantity value is greater than zero
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    for j in range(0, quantities[i]) :
                        Cart.add_product_to_cart(pysql, all_ids['customer_id'], product_details[i][0])

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

            # check if the issued quantity is present in product stock
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    if not(Product.check_if_in_stock(pysql, all_ids['customer_id'], product_details[i][0], quantities[i])) :
                        print("Not enough in stock")
                        return render_template('/Product/product_mobile.html', product_details = product_details)

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

            # check if the issued quantity is present in product stock
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    if not(Product.check_if_in_stock(pysql, all_ids['customer_id'], product_details[i][0], quantities[i])) :
                        print("Not enough in stock")
                        return render_template('/Product/product_mobile.html', product_details = product_details)

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

            # check if the issued quantity is present in product stock
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    if not(Product.check_if_in_stock(pysql, all_ids['customer_id'], product_details[i][0], quantities[i])) :
                        print("Not enough in stock")
                        return render_template('/Product/product_mobile.html', product_details = product_details)

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

            # check if the issued quantity is present in product stock
            for i in range(0, len(product_details)) :
                if quantities[i] > 0 :
                    if not(Product.check_if_in_stock(pysql, all_ids['customer_id'], product_details[i][0], quantities[i])) :
                        print("Not enough in stock")
                        return render_template('/Product/product_mobile.html', product_details = product_details)

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
    product_details = []
    total = 0


    if request.method == 'POST' :
        # Clear Shopping Cart
        if 'clear_cart' in request.form :
            Cart.clear_cart(pysql, all_ids['customer_id'])

        # If place_order button is pressed
        elif 'place_order' in request.form :
            selected_address_id = request.form['address_radio']
            all_ids['address_id'] = selected_address_id

            selected_payment_method = request.form['payment_method']
            all_ids['payment_method'] = selected_payment_method
            return redirect('/PlaceOrder')

    # Show current products in cart
    else :
        # Get ids of the product currently present in cart
        prodids_incart = Cart.get_prod_in_cart(pysql, all_ids['customer_id'])
        prodids_incart = prodids_incart[0]

        # Get the total price of products in the cart
        total = Cart.get_total(pysql, all_ids['customer_id'])

        # for each product id, get the product details
        for i in prodids_incart :
            if i is not None :
                ans = Product.get_product_details(pysql, i)
                ans = ans[0]
                product_details.append(ans)

    # Choose Address

    address_details = Address.view_all_address_of_customer(pysql, all_ids['customer_id'])
    return render_template('/Cart/cart_info.html', product_details = product_details, total = total, address_details = address_details)


@app.route('/PlaceOrder', methods = ['GET', 'POST'])
def order_success() :

    pysql.init()
    global all_ids

    # If cart is empty, order not to be placed
    if Cart.get_no_of_products_in_cart(pysql, all_ids['customer_id']) == 0 :
        address_details = Address.view_all_address_of_customer(pysql, all_ids['customer_id'])
        return render_template('/Cart/cart_info.html', address_details = address_details, total = 0)

    # Place the order
    order_id = Orders.place_order(pysql, all_ids['customer_id'], all_ids['address_id'], all_ids['payment_method'])
    if order_id != 0 :
        return render_template('/Cart/order_placed.html', order_id = order_id)

    return render_template('/Cart/cart_info.html')


@app.route('/YourAccount', methods = ['GET', 'POST'])
def profile_view_and_updation() :

    pysql.init()
    global all_ids

    # get the user account details (name, email, etc)
    profile = Customer.get_customer_profile(pysql, all_ids['customer_id'])

    first_name = profile[0][0]
    last_name = profile[0][1]
    email = profile[0][2]
    phone1 = profile[0][3]
    phone2 = profile[0][4]

    # get all the address that are linked with customer account
    address_details = Address.view_all_address_of_customer(pysql, all_ids['customer_id'])

    if request.method == 'POST' :
        if 'update' in request.form :
            profile_details = request.form
            first_name = profile_details['first_name']
            last_name = profile_details['last_name']
            email = profile_details['email']
            phone1 = profile_details['phone1']
            phone2 = profile_details['phone2']

        # Update the profile 
        ans = Customer.update_customer_profile(pysql, all_ids['customer_id'], first_name, last_name, email, phone1, phone2)
        if ans :
            print("Profile Updated Successfully!")
        else :
            print("Profile Updation Failed")

    return render_template('/CustomerSignIn/your_account.html', customer_id = all_ids['customer_id'], first_name = first_name, last_name = last_name, email = email, phone1 = phone1, phone2 = phone2, address_details = address_details)


@app.route('/YourOrders', methods = ['GET', 'POST'])
def show_orders() :
    pysql.init()
    global all_ids

    # Display all the order history of the customer 
    order_details = Orders.get_order_details(pysql, all_ids['customer_id'])
    return render_template('/CustomerSignIn/your_orders.html', order_details = order_details)


@app.route('/AddAddress', methods = ['GET', 'POST'])
def add_address() :

    pysql.init()
    global all_ids

    if request.method == 'POST' :
        if 'add_address' in request.form :

            addr_details = request.form
            street = addr_details['street']
            landmark = addr_details['landmark']
            city = addr_details['city']
            state = addr_details['state']
            pincode = addr_details['pincode']
            address_type = addr_details['address_type']

            # Add the address to the customer account
            ans = Address.add_customer_address(pysql, all_ids['customer_id'], pincode, street, landmark, city, state, address_type)
            print(ans)

            if ans :
                print("Address Added")
                return redirect('/ProductCategory')
            else :
                print("Adding Address Failed")

    return render_template('/CustomerSignIn/add_address.html')


#########   ADMIN RELATED FUNCTIONS ########

@app.route('/AdminSignIn', methods = ['GET', 'POST'])
def admin_signin_page():

    if request.method == 'POST' :
        if 'admin_login' in request.form :
            email = request.form['admin_email']
            password = request.form['admin_password']

            # Check here the email-id and password entered
            if email == 'root' and password == 'admin' :
                print("Logged In")
                return redirect('/AdminActions')
            else :
                print("Invalid Email or Password")

    return render_template('/Admin/admin_signin.html')


@app.route('/AdminActions', methods = ['GET', 'POST'])
def select_admin_action() :

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

    # Display all the products in the database
    product_details = Product.get_all_products(pysql)
    return render_template('/Admin/show_all_products.html', product_details = product_details)


@app.route('/ShowAllDeliveryExecutives', methods = ['GET', 'POST'])
def show_all_deliveryexecutives() :
    pysql.init()

    # Display all the delivery executives currently in work
    delivery_executive_details = DeliveryExecutive.get_all_deliveryexecutives(pysql)
    return render_template('/Admin/show_all_delivery_executives.html', delivery_executive_details = delivery_executive_details)


#########   DELIVERY EXECUTIVE RELATED FUNCTIONS ########

@app.route('/DeliveryExecutiveSignIn', methods = ['GET', 'POST'])
def deliveryexecutive_signin_page() :
    pysql.init()
    global all_ids
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

    # find all undelivered and delivered orders
    undelivered_details = DeliveryExecutive.get_orders_details(pysql, all_ids['deliveryexecutive_id'], 0)
    delivered_details = DeliveryExecutive.get_orders_details(pysql, all_ids['deliveryexecutive_id'], 1)

    if request.method == 'POST' :

        # Get the ids of orders that are undelivered
        order_ids = []
        for i in undelivered_details:
            order_ids.append(i[0])

        # Get the order id that is selected and compare it with all the
        # undelivered order ids. Change the status of the selected order id.
        # Again find all the undelivered and delivered orders and display them
        selected_order_id = request.form["delivered"]
        for i in order_ids:
            if selected_order_id == i:
                DeliveryExecutive.change_delivery_status(pysql, selected_order_id)
                undelivered_details = DeliveryExecutive.get_orders_details(pysql, all_ids['deliveryexecutive_id'], 0)
                delivered_details = DeliveryExecutive.get_orders_details(pysql, all_ids['deliveryexecutive_id'], 1)
                break

    return render_template('/DeliveryExecutiveSignIn/delivery_details.html', delivery_id = all_ids['deliveryexecutive_id'], undelivered_details = undelivered_details, delivered_details = delivered_details)

if __name__ == "__main__" :
    app.run(debug = True)
