# @brief This class is to handle the adding and removing from the cart table
# @note  There is not need to create an object of this class as all
#        methods in this class are static

class Cart :

    # @brief This method adds the product to the cart that is assigned to the 
    #        customer. 
    # @retval The function return 1, if product is successfully added to the 
    #         cart. It returns 0 then the cart is full
    @staticmethod
    def add_product_to_cart(pysql, customer_id, product_id) :
        # Get the entries of prodID from cart for a particular customer
        sql_stmt =  'SELECT * FROM Cart ' \
                    'WHERE Customer_ID = %s'

        pysql.run(sql_stmt, (customer_id, ))
        row = pysql.result

        # Find out which value of prodID is NULL. At the end of loop, 'i' has the
        # position of prodID attribute that has value NULL. Then insert at that
        # position. If i is 6, then obviously the cart is full.
        i = 1
        while (i < 6) :
            if row[i] == 'NULL' :
                break
            i += 1
        
        if i == 6 :
            return 0

        # Query to add the required in cart at position 'i'
        sql_stmt =  'UPDATE Cart ' \
                    'SET Prod_ID%s = %s' \
                    'WHERE Customer_ID = %s'
        pysql.run(sql_stmt, (i, product_id, customer_id))

        return 1

    # @brief This method deletes the product from the cart that is assigned to
    #        the customer. 
    # @retval The function return 1, if product is successfully added to the 
    #         cart. It returns 0 then the cart is full
    @staticmethod
    def delete_product_to_cart(pysql, customer_id, product_id) :
        # Get the entries of prodID from cart for a particular customer
        sql_stmt =  'SELECT * FROM Cart ' \
                    'WHERE Customer_ID = %s'

        pysql.run(sql_stmt, (customer_id, ))
        row = pysql.result

        # Find out which value of prodID is equal to product_id. At the end of 
        # loop, 'i' has the position of prodID attribute that has value
        # product_id. Then insert at that position. If i is 6, then the product 
        # is not found in the cart.
        i = 1
        while (i < 6) :
            if row[i] == product_id :
                break
            i += 1
        
        if i == 6 :
            return 0

        # Query to add the required in cart at position 'i'
        sql_stmt =  'UPDATE Cart ' \
                    'SET Prod_ID%s = %s' \
                    'WHERE Customer_ID = %s'
        pysql.run(sql_stmt, (i, 'NULL', customer_id))
        pysql.commit()

        return 1
