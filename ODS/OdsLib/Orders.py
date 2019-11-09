import random
# This variable stores the next OrderID integer
next_order_id = None
# This variable indicates whether the next_order_id has been initialized
next_order_id_read = 0

class Orders :

    # @brief This method is called after the customer has placed the order.
    #        Approriate entries for the given order are made
    # @retval Return 1 if entry added successfully, else 0
    @staticmethod
    def add_order(pysql, customer_id, address_id, payment_method) :
        
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
        order_id = l1 + l2 + format(next_order_id, '07d')
        
        # Find total. Use the cart table
        sql_stmt =  'SELECT * ' \
                    'FROM Cart ' \
                    'WHERE Customer_ID = %s'
        pysql.run(sql_stmt, (customer_id, ))
        row = pysql.result

        total = 0
        for i in range(1, 6) :
            total += row[i]

        # Make an entry in the database
        sql_stmt =  'INSERT INTO Product ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, (SELECT CURRENT_TIMESTAMP))' 

        try :        
            pysql.run(sql_stmt, (order_id, customer_id, address_id, total, payment_method, "Not Delivered"))

            # Commit the changes to the remote database
            pysql.commit()

            # Next order id
            next_order_id += 1
            return 1
        except :
            return 0
