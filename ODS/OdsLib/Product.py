import random
# This variable stores the next ProductID integer
next_product_id = None
# This variable indicates whether the next_product_id has been initialized
next_product_id_read = 0
product_shortforms = {'Mobile'  : 'MOB', 
                      'Laptop'  : 'LAP', 
                      'Books'   : 'BOK',
                      'Sports'  : 'SPT',
                      'Clothing': 'CLT'}

# @brief This class is used to handle the product details and updation
# @note  There is not need to create an object of this class as all
#        methods in this class are static
class Product :

    # @brief The function is used to insert the product details entered by the
    #        admin in the mysql database
    # @param pysql Pysql Object
    # @param Name of the parameter are self-explanatory (string)
    # @retval boolean returns the 1 if the entry is successfully inserted in the
    #         database, else 0
    @staticmethod
    def add_product(pysql, name, category, price, seller, quantity) :

        # First check if the product already present in the table. If yes, then
        # just increment its quantity. Else, assign a new productID and add
        # the given quantity
        sql_stmt =  'SELECT * ' \
                    'FROM Product'
        pysql.run(sql_stmt)
        row = pysql.result

        if row[1] == name and row[2] == category and row[5] ==  seller :
            sql_stmt =  'UPDATE Product ' \
                        'SET Quantity = Quantity + %s ' \
                        'WHERE Product_ID = %s'
            pysql.run(sql_stmt, (quantity, row[0]))
            return 1

        # If the execution reaches here implies there is no entry for the
        # required product in the product. So assign an id and make an entry

        # Fetch the global variables
        global next_product_id
        global next_product_id_read

        # Find the last product id stored in the database to allocate next id
        # to the next product. If the number of entries of the product are not
        # known, then using product_id_read flag and sql query, we can find it!
        if not next_product_id_read :
            sql_stmt =  'SELECT COUNT(*) ' \
                        'FROM Product'
            pysql.run(sql_stmt)
            next_product_id = pysql.scalar_result
            next_product_id_read = 1

        # Now get the product_id 
        product_id = product_shortforms[category] + format(next_product_id, '06d')

        # Assign a random rating at start
        rating = random.uniform(0,5)
        rating = '%.1f'%(rating)

        # Make an entry in the database
        sql_stmt =  'INSERT INTO Product ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, %s)'
        try :
            pysql.run(sql_stmt, (product_id, name, category, price, rating, seller, quantity))

            # Commit the changes to the remote database
            pysql.commit()

            # Next address_id for further addition of product
            next_product_id += 1
            return 1
        except :
            return 0


    @staticmethod
    def get_product_by_category(pysql, category) :
        sql_stmt =  'SELECT Name, Seller, Rating, Price ' \
                    'FROM Product ' \
                    'WHERE Category = %s'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products

    @staticmethod
    def get_product_sorted_by_price_asc(pysql) :
        sql_stmt =  'SELECT Name, Seller, Rating, Price ' \
                    'FROM Product ' \
                    'ORDER BY Price ASC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products

    @staticmethod
    def get_product_sorted_by_price_desc(pysql) :
        sql_stmt =  'SELECT Name, Seller, Rating, Price ' \
                    'FROM Product ' \
                    'ORDER BY Price DESC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products

    '''@staticmethod
    def get_product_sorted_by_rating_asc(pysql) :
        sql_stmt =  'SELECT Name, Seller, Rating, Price ' \
                    'FROM Product ' \
                    'ORDER BY Rating ASC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products
    '''

    @staticmethod
    def get_product_sorted_by_rating_desc(pysql) :
        sql_stmt =  'SELECT Name, Seller, Rating, Price ' \
                    'FROM Product ' \
                    'ORDER BY Rating DESC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products

    # Gives highest rated product having minimum price
    # I think this one is to be employed
    @staticmethod
    def get_product_sorted_by_price_asc_rating_desc(pysql) :
        sql_stmt =  'SELECT Name, Seller, Rating, Price ' \
                    'FROM Product ' \
                    'ORDER BY Rating DESC, Price ASC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products

    # Gives least cost product having maximum rating
    @staticmethod
    def get_product_sorted_by_rating_desc_price_asc(pysql) :
        sql_stmt =  'SELECT Name, Seller, Rating, Price ' \
                    'FROM Product ' \
                    'ORDER BY Price ASC, Rating DESC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products
