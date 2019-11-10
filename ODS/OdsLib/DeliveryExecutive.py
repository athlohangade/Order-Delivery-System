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
        sql_stmt =  'SELECT Email, Password ' \
                    'FROM DeliveryExecutive'
        pysql.run(sql_stmt)
        data = pysql.result

        # Check if the database has the required entry 
        for i in data :
            if i[0] == email and i[1] == password :
                return True 
        return False 


    # @brief The function is used to add delivery executive to the sql database.
    #        This is used by ADMIN
    # @param pysql Pysql Object
    # @param Name of the parameter are self-explanatory (string)
    # @retval boolean returns the deliveryexecutive_id allocated for that entry 
    #         if the entry is successfully inserted in the database, else 0
    @staticmethod
    def add_deliveryexecutive(pysql, firstname, lastname, email, password, worktime, salary, phone1, phone2) :
        # Fetch the global variables
        global next_deliveryexecutive_id
        global next_deliveryexecutive_id_read

        # Find the last deliveryexecutive id stored in the database to allocate next id
        # to the next deliveryexecutive. If the number of entries of the deliveryexecutive are not
        # known, then using deliveryexecutive_id_read flag and sql query, we can find it!
        if not next_deliveryexecutive_id_read :
            sql_stmt =  'SELECT COUNT(*) ' \
                        'FROM DeliveryExecutive'
            pysql.run(sql_stmt)
            next_deliveryexecutive_id = pysql.scalar_result
            next_deliveryexecutive_id_read = 1 

        # Now get the deliveryexecutive_id
        deliveryexecutive_id = 'D' + format(next_deliveryexecutive_id, '05d')

        # Make an entry in the database
        sql_stmt =  'INSERT INTO DeliveryExecutive ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)' 

        try : 
            pysql.run(sql_stmt, (deliveryexecutive_id, firstname, lastname, email, password, worktime, salary, phone1, phone2))

            # Commit the changes to the remote database
            pysql.commit()

            # Next deliveryexecutive_id for further sign in
            next_deliveryexecutive_id += 1
            return deliveryexecutive_id

        except :
            return 0

    # @brief This method returns the orders that are delivered or to be
    #        delivered by the executive
    # @retval List containing orderid, customername, address details (pincode,
    #         street, landmark, city, state), orderstatus.
    @staticmethod
    def get_orders_details(pysql, deliveryexecutive_id) :
        sql_stmt =  'WITH T1 AS ( ' \
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
    def get_all_deliveryexecutives(pysql) :
        sql_stmt =  'SELECT ID, First_name, Last_name, Email, Password, Salary, Phone1, Phone2, WorkTime ' \
                    'FROM DeliveryExecutive'

        pysql.run(sql_stmt)
        rows = pysql.result

        return rows 

    # @brief This method changes the status of Order from "Not Delivered" to
    #        "Delivered"
    # @param Order_id (BUT HOW TO GET THE ORDER_ID FROM THE HTML PAGE!!!!)
    # @retval 1 if success, else 0
    @staticmethod
    def change_delivery_status(pysql, order_id) :

        sql_stmt =  'UPDATE Orders ' \
                    'SET Status = "Delivered" ' \
                    'WHERE Order_ID = %s' \

        try :
            pysql.run(sql_stmt, (order_id, ))
            pysql.commit()
            return 1

        except :
            return 0
