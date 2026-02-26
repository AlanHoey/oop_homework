class Product:
    '''
        Code for the Product class goes here
        Product has:
        an id (unique)
        a name
        a cost price
        a retail price
        a quantity
    '''

    def __init__(self, prod_id: str, prod_name: str, cost_price: float, retail_price: float, units_in_stock: int):

        self.prod_id = prod_id
        try:
            if prod_id is None or str(prod_id).strip() == "":
                raise ValueError("Invalid product ID")
        except ValueError:
            print("Invalid product") ID, defaulting to 'unknown_id'")
            self.prod_id = "unknown_id"


        self.prod_name = prod_name
        if prod_name is None or str(prod_name).strip() == "":
            print("Invalid product name, defaulting to 'unknown_product'")
            self.prod_name = "unknown_product"

        self.cost_price = cost_price
        if cost_price is None or str(cost_price).strip() == "":
            print("Invalid cost price, defaulting to 0.0")
            self.cost_price = 0.0

        self.retail_price = retail_price
        if retail_price is None or str(retail_price).strip() == "":
            print("Invalid retail price, defaulting to 0.0")
            self.retail_price = 0.0

        self.units_in_stock = units_in_stock
        if units_in_stock is None or str(units_in_stock).strip() == "":
            print("Invalid units in stock, defaulting to 0")
            self.units_in_stock = 0



class Book(Product):
    '''
        Code for the Book class goes here
        Book has:
        an id (unique)
        a name
        a cost price
        a retail price
        a quantity
        an author
        one or more genres (these should be stored in a list)
    '''