from types import NotImplementedType


class Product:
    def __init__(self, product_id: int, product_name: str,
                 unit_price: float, units_in_stock: int):
        """
        Initialises a Product object.

        Args:
            product_id (int): Unique identifier for the product (must be >= 0)
            product_name (str): Name of the product (cannot be blank)
            unit_price (float): Price per unit (must be >= 0)
            units_in_stock (int): Number of units available (must be >= 0)
        """

        if product_id is None or product_id < 0:
            raise ValueError("Product ID must be >= 0")

        if product_name is None or product_name.strip() == "":
            raise ValueError("Product name cannot be blank")

        if unit_price is None or unit_price < 0:
            raise ValueError("Unit price must be >= 0")

        if units_in_stock is None or units_in_stock < 0:
            raise ValueError("Units in stock must be >= 0")

        self._product_id = product_id
        self._product_name = product_name
        self._unit_price = unit_price
        self._units_in_stock = units_in_stock

    def product_id(self) -> int:
        """Returns the product ID."""
        return self._product_id

    def product_name(self) -> str:
        """Returns the product name."""
        return self._product_name

    def unit_price(self) -> float:
        """Returns the unit price."""
        return self._unit_price

    def units_in_stock(self) -> int:
        """Returns number of units in stock."""
        return self._units_in_stock

    def reduce_stock(self, quantity: int) -> None:
        """
        Reduces stock when an order is placed.

        Args:
            quantity (int): Number of units to remove from stock
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if quantity > self._units_in_stock:
            raise ValueError("Not enough stock available")

        self._units_in_stock -= quantity

    def __str__(self) -> str:
        return f"{self._product_name} (€{self._unit_price}) - Stock: {self._units_in_stock}"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"[product_id={self._product_id}, "
                f"name={self._product_name}, "
                f"price={self._unit_price}, "
                f"stock={self._units_in_stock}]")

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Product):
            return NotImplemented
        return self._product_id == other._product_id

    def __ne__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Product):
            return NotImplemented
        return not self == other

    def __hash__(self) -> int:
        return hash(self._product_id)
