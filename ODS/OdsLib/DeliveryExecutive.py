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

    # @brief This method returns the orders that are delivered or to be
    #        delivered by the executive
    # @retval List containing orderid, customername, address details (pincode,
    #         street, landmark, city, state), orderstatus.
    @staticemethod
    def get_orders_details(pysql, deliveryexecutive_id) :
        sql_stmt =  'WITH T1 AS ('
                        'SELECT Order_ID, Address_ID, Status ' \
                        'FROM Orders ' \
                        'WHERE Order_ID in ( ' \
                            'SELECT Order_ID from Delivery ' \
                            'WHERE ID = %s)) ' \
                    'SELECT Order_ID, First_name, Pincode, Street, Landmark, City, State, Status ' \ 
                    'FROM  Customer INNER JOIN ' \
                    '(SELECT Order_ID, Customer_ID, Pincode, Street, Landmark, City, State, Status, ' \
                    'FROM Address INNER JOIN T1 ' \
                    'ON Address.Address_ID=T1.Address_ID) AS T2 ' \
                    'WHERE Customer.Customer_ID=T2.Customer_ID'
        pysql.run(sql_stmt, (deliveryexecutive_id, ))
        row = pysql.result
        return row

    # @brief This method gives all the delivery executive of the system.
    #        Normally used by ADMIN
    @staticmethod
    def get_all_deliveryexecutive(pysql) :
        sql_stmt =  'SELECT ID, Name, Email, Salary, Phone1, Phone2, WorkTime ' \
                    'FROM Product'

        pysql.run(sql_stmt)
        rows = pysql.result

        return rows 
