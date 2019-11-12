# This variable stores the next AddressID integer
next_address_id = None
# This variable indicates whether the next_address_id has been initialized
next_address_id_read = 0

# @brief This class is used to handle the Customer address in ODS 
# @note  There is not need to create an object of this class as all
#        methods in this class are static
class Address :

    # @brief The function is used to insert the address details entered by the 
    #        customer in the mysql database
    # @param pysql Pysql Object
    # @param Name of the parameter are self-explanatory (string)
    # @retval boolean returns the 1 if the entry is successfully inserted in the 
    #         database, else 0
    @staticmethod
    def add_customer_address(pysql, customer_id, pincode, street, landmark, city, state, addr_type) :

        # Fetch the global variables
        global next_address_id
        global next_address_id_read

        # Find the last address id stored in the database to allocate next id
        # to the next address. If the number of entries of the address are not
        # known, then using address_id_read flag and sql query, we can find it!
        if not next_address_id_read :
            sql_stmt =  'SELECT COUNT(*) ' \
                        'FROM Address'
            pysql.run(sql_stmt)
            next_address_id = pysql.scalar_result
            next_address_id_read = 1 

        # Now get the address_id
        address_id = format(next_address_id, '06d')

        # Make an entry in the database
        sql_stmt =  'INSERT INTO Address ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)' 

        try : 
            pysql.run(sql_stmt, (customer_id, address_id, pincode, street, landmark, city, state, addr_type))

            # Commit the changes to the remote database
            pysql.commit()

            # Next address_id for further addition of address 
            next_address_id += 1
            return 1 
        except :
            return 0

    @staticmethod
    def view_all_address_of_customer(pysql, customer_id) :
            
        sql_stmt =  'SELECT Address_ID, Pincode, Street, Landmark, City, State, Type ' \
                    'FROM Address ' \
                    'WHERE Customer_ID = %s' \

        pysql.run(sql_stmt, (customer_id, ))
        addresses = pysql.result

        return addresses
