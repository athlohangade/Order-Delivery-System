# This variable stores the next CustomerID integer
next_customer_id = None
# This variable indicates whether the next_customer_id has been initialized
next_customer_id_read = 0

# @brief This class is used to handle the Customer data in ODS 
# @note  There is not need to create an object of this class as all
#        methods in this class are static
class Customer :

    # @brief The function is used to verify the details entered by the customer
    #        during sign in for allowing the access to the account
    # @param pysql Pysql Object
    # @param email EmailID of the account (string)
    # @param password Password of the account (string)
    # @retval boolean 1 if the entry is found in the database, else 0
    @staticmethod
    def check_customer_signin(pysql, email, password) :
        # Get the email and password entries from database
        sql_stmt =  'SELECT Customer_ID, Email, Password '\
                    'FROM Customer'
        pysql.run(sql_stmt)
        data = pysql.result

        # Check if the database has the required entry 
        for i in data :
            if i[1] == email and i[2] == password :
                return i[0] 
        return False 


    # @brief The function is used to insert the details entered by the customer 
    #        in the mysql database during sign up for the account
    # @param pysql Pysql Object
    # @param Name of the parameter are self-explanatory (string)
    # @retval boolean returns the customer_id allocated for that entry if the 
    #         entry is successfully inserted in the database, else 0
    @staticmethod
    def customer_signup(pysql, firstname, lastname, email, password, phone1, phone2) :
        # Fetch the global variables
        global next_customer_id
        global next_customer_id_read

        # Find the last customer id stored in the database to allocate next id
        # to the next customer. If the number of entries of the customer are not
        # known, then using customer_id_read flag and sql query, we can find it!
        if not next_customer_id_read :
            sql_stmt =  'SELECT COUNT(*) ' \
                        'FROM Customer'
            pysql.run(sql_stmt)
            next_customer_id = pysql.scalar_result
            next_customer_id_read = 1 

        # Now get the customer_id
        customer_id = 'C' + format(next_customer_id, '05d')

        # Make an entry in the database
        sql_stmt =  'INSERT INTO Customer ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, %s)' 

        try : 
            pysql.run(sql_stmt, (customer_id, firstname, lastname, email, password, phone1, phone2))

            # Commit the changes to the remote database
            pysql.commit()
            
            sql_stmt =  'INSERT INTO Cart(Customer_ID) ' \
                        'VALUES (%s)'
            pysql.run(sql_stmt, (customer_id, ))
            pysql.commit()

            # Next customer_id for further sign in
            next_customer_id += 1
            return customer_id

        except :
            return 0


    # @brief The method the profile of the customer.
    # @param pysql Pysql Object
    # @param Name of the parameter are self-explanatory (string)
    # @retval boolean returns the profile is updated sucessfully, else 0
    @staticmethod
    def get_customer_profile(pysql, customer_id) :
        sql_stmt =  'SELECT First_name, Last_name, Email, Phone1, Phone2 ' \
                    'FROM Customer ' \
                    'WHERE Customer_ID = %s'
        try :
            pysql.run(sql_stmt, (customer_id, )) 
            profile = pysql.result
            return profile

        except :
            return 0


    # @brief The method is used to update the profile of the customer.
    # @param pysql Pysql Object
    # @param Name of the parameter are self-explanatory (string)
    # @retval boolean returns the if the profile is updated sucessfully, else 0
    @staticmethod
    def update_customer_profile(pysql, customer_id, first_name, last_name, email, phone1, phone2) :
        sql_stmt =  'UPDATE Customer ' \
                    'SET First_name = %s, Last_name = %s, Email = %s, Phone1 = %s, Phone2 = %s ' \
                    'WHERE Customer_ID = %s'
        try :
            pysql.run(sql_stmt, (first_name, last_name, email, phone1, phone2, customer_id))
            pysql.commit()
            return 1

        except :
            return 0
