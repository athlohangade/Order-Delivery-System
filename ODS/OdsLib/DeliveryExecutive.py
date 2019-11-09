# This variable stores the next DeliveryExecutiveID integer
next_deliveryexecutive_id = None
# This variable indicates whether the next_deliveryexecutive_id has been initialized
next_deliveryexecutive_id_read = 0

# @brief This class is used to handle the Delivery Executive data in ODS 
# @note  There is not need to create an object of this class as all
#        methods in this class are static
class DeliveryExecutive :

    # @brief The function is used to verify the details entered by the deliveryexecutive
    #        during sign in for allowing the access to the account
    # @param pysql Pysql Object
    # @param email EmailID of the account (string)
    # @param password Password of the account (string)
    # @retval boolean 1 if the entry is found in the database, else 0
    @staticmethod
    def check_deliveryexecutive_signin(pysql, email, password) :
        # Get the email and password entries from database
        sql_stmt =  'SELECT Email, Password '\ 
                    'FROM Delivery_Executive'
        pysql.run(sql_stmt)
        data = pysql.result

        # Check if the database has the required entry 
        for i in data :
            if i[0] == email and i[1] == password :
                return True 
        return False 
