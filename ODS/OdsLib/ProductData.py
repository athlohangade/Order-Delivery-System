# @brief This class is used to handle the Product details in ODS 
# @note  There is not need to create an object of this class as all
#        methods in this class are static
class ProductData:

    @staticmethod
    def get_product_by_category(pysql, category) :
        sql_stmt =  'SELECT Name, Price ' \
                    'FROM Product ' \
                    'WHERE Category = %s'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products

    @staticmethod
    def get_product_sorted_by_price_asc(pysql) :
        sql_stmt =  'SELECT Name, Price ' \
                    'FROM Product ' \
                    'ORDER BY Price ASC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products

    @staticmethod
    def get_product_sorted_by_price_desc(pysql) :
        sql_stmt =  'SELECT Name, Price ' \
                    'FROM Product ' \
                    'ORDER BY Price DESC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products

    @staticmethod
    def get_product_sorted_by_rating_asc(pysql) :
        sql_stmt =  'SELECT Name, Price ' \
                    'FROM Product ' \
                    'ORDER BY Rating ASC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products

    @staticmethod
    def get_product_sorted_by_rating_desc(pysql) :
        sql_stmt =  'SELECT Name, Price ' \
                    'FROM Product ' \
                    'ORDER BY Rating DESC'

        pysql.run(sql_stmt, (category, ))
        products = pysql.result

        return products


