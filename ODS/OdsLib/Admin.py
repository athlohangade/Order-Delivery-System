# This variable stores the next ProductID integer
next_product_id = None
# This variable indicates whether the next_product_id has been initialized
next_product_id_read = 0

class Admin :
    # Check this needed to be done

    # @brief The function is used to insert the product details entered by the
    #        admin in the mysql database
    # @param pysql Pysql Object
    # @param Name of the parameter are self-explanatory (string)
    # @retval boolean returns the 1 if the entry is successfully inserted in the
    #         database, else 0
    @staticmethod
    def add_product(pysql, product_id, name, category, price, rating, seller) :

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

        # Now get the address_id
        product_id = format(next_product_id, '06d')

        # Make an entry in the database
        sql_stmt =  'INSERT INTO Product ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

        try :
            pysql.run(sql_stmt, (customer_id, address_id, pincode, street, landmark, city, state, addr_type))

            # Commit the changes to the remote database
            pysql.commit()

            # Next address_id for further addition of product
            next_product_id += 1
            return 1
        except :
            return 0
