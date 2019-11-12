import random
from OdsLib.Cart import Cart
# This variable stores the next OrderID integer
next_order_id = None
# This variable indicates whether the next_order_id has been initialized
next_order_id_read = 0

class Orders :

    # @brief This method is called after the customer has placed the order.
    #        Approriate entries for the given order are made
    # @retval Return 1 if entry added successfully, else 0
    @staticmethod
    def place_order(pysql, customer_id, address_id, payment_method) :

        letters = list(map(chr, range(ord('A'), ord('Z')+1)))
        l1 = letters[random.choice([i for i in range(0, 26)])]
        l2 = letters[random.choice([i for i in range(0, 26)])]

        # Fetch the global variables
        global next_order_id
        global next_order_id_read

        # Find the last order id stored in the database to allocate next id
        # to the next order. If the number of entries of the order are not
        # known, then using order_id_read flag and sql query, we can find it!
        if not next_order_id_read :
            sql_stmt =  'SELECT COUNT(*) ' \
                        'FROM Orders'
            pysql.run(sql_stmt)
            next_order_id = pysql.scalar_result
            next_order_id_read = 1

        # Now get the order_id
        order_id = l1 + l2 + '-' + format(next_order_id, '07d')

        # Find total. Use the cart table and product table
        total = Cart.get_total(pysql, customer_id)

        # Make an entry in the database
        sql_stmt =  'INSERT INTO Orders ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, (SELECT CURRENT_TIMESTAMP))'

        try :
            pysql.run(sql_stmt, (order_id, customer_id, address_id, total, payment_method, "Not Delivered"))

            # Commit the changes to the remote database
            pysql.commit()

            # Next order id
            next_order_id += 1

            # Add the (order_id, product_id) combination in OrderDetails Table
            sql_stmt =  'SELECT * ' \
                        'FROM Cart ' \
                        'WHERE Customer_ID = %s'
            pysql.run(sql_stmt, (customer_id, ))
            row = pysql.result


            for i in range(1, 6) :
                if row[0][i] is not None :
                    sql_stmt =  'INSERT INTO OrderDetails ' \
                                'VALUES (%s, %s)'
                    pysql.run(sql_stmt, (order_id, row[0][i]));
                    pysql.commit()

            # Empty the Cart
            Cart.clear_cart(pysql, customer_id)

            # Assign a random Delivery Executive
            sql_stmt =  'SELECT ID ' \
                        'FROM DeliveryExecutive ' \
                        'ORDER BY RAND() ' \
                        'LIMIT 1'
            pysql.run(sql_stmt)
            deliveryexecutive_id = pysql.result
        
            sql_stmt =  'INSERT INTO Delivery ' \
                        'VALUES (%s, %s)'

            pysql.run(sql_stmt, (order_id, deliveryexecutive_id[0][0]))
            pysql.commit()

            return order_id

        except :
            return 0

    # @brief This method gives the orders that have been placed till date
    @staticmethod
    def get_order_details(pysql, customer_id) :

        sql_stmt =  'WITH T1 AS ( ' \
                        'SELECT Orders.Order_ID, Order_Date, Payment_Method, Product_ID ' \
                        'FROM Orders INNER JOIN OrderDetails ' \
                        'ON Orders.Order_ID = OrderDetails.Order_ID ' \
                        'WHERE Customer_ID = %s) ' \
                    'SELECT Order_Date, Order_ID, Product.Product_ID, Name, Payment_Method, Price ' \
                    'FROM Product INNER JOIN T1 ' \
                    'ON T1.Product_ID = Product.Product_ID ' \
                    'ORDER BY Order_ID'

        pysql.run(sql_stmt, (customer_id, ))
        orders = pysql.result

        return orders
