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
            if row[0][i] is None :
                break
            i += 1
        
        if i == 6 :
            return 0

        # Query to add the required product in cart at position 'i'
        sql_stmt =  'UPDATE Cart ' \
                    'SET Prod_ID%s = %s ' \
                    'WHERE Customer_ID = %s'
        try :
            pysql.run(sql_stmt, (i, product_id, customer_id))
            pysql.commit()
            return 1

        except :
            print('Cart is Full')
            return 0

    # @brief This method gives the no. of products in the cart that is assigned 
    #        to the customer. 
    # @retval The function return number of products (0 to 5), if cart is full
    #         then cartsize + 1 (6) is returned
    @staticmethod
    def get_no_of_products_in_cart(pysql, customer_id) :

        # Get the entries of prodID from cart for a particular customer
        sql_stmt =  'SELECT * FROM Cart ' \
                    'WHERE Customer_ID = %s'

        pysql.run(sql_stmt, (customer_id, ))
        row = pysql.result

        # Find out which value of prodID is NULL. At the end of loop, 'i' has the
        # position of prodID attribute that has value NULL.
        # If i is 6, then obviously the cart is full.
        i = 1
        while (i < 6) :
            if row[0][i] is None :
                break
            i += 1
        
        return (i - 1)


    # @brief This method deletes the product from the cart that is assigned to
    #        the customer. 
    # @retval The function return 1, if product is successfully added to the 
    #         cart. It returns 0 then the cart is full
    @staticmethod
    def clear_cart(pysql, customer_id) :

        sql_stmt =  'UPDATE Cart ' \
                    'SET Prod_ID1 = %s, Prod_ID2 = %s, Prod_ID3 = %s, Prod_ID4 = %s, Prod_ID5 = %s ' \
                    'WHERE Customer_ID = %s'

        pysql.run(sql_stmt, (None, None, None, None, None, customer_id))
        pysql.commit()

        return 1

    # @brief This method returns all the product ids in the cart
    @staticmethod
    def get_prod_in_cart(pysql, customer_id) :
        # Get the entries of prodID from cart for a particular customer
        sql_stmt =  'SELECT Prod_ID1, Prod_ID2, Prod_ID3, Prod_ID4, Prod_ID5 ' \
                    'FROM Cart ' \
                    'WHERE Customer_ID = %s'

        pysql.run(sql_stmt, (customer_id, ))
        products = pysql.result
        return products
   
    # @brief This method gives the total of products present in the cart
    @staticmethod
    def get_total(pysql, customer_id) :

        product_ids = Cart.get_prod_in_cart(pysql, customer_id)

        total = 0
        for i in range(0, Cart.get_no_of_products_in_cart(pysql, customer_id)) :

            sql_stmt =  'SELECT Price ' \
                        'FROM Product ' \
                        'WHERE Product_ID = %s'

            pysql.run(sql_stmt, (product_ids[0][i], ))
            ans = pysql.result
            total += int(ans[0][0])
   
        return total 

