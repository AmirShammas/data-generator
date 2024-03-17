import random
import csv
import local_settings


class Order:
    def __init__(self, id: int, user: str, product: str, month: int, price: int, count: int):
        self.id, self.user, self.product, self.month, self.price, self.count = id, user, product, month, price, count

    @property
    def total_price(self) -> int:
        return (self.price * self.count)


class OrderManager:
    def create_orders(number_of_orders: int):
        orders = []
        number_of_users = local_settings.DATABASE['number_of_users']
        number_of_products = local_settings.DATABASE['number_of_products']
        price_min = local_settings.DATABASE['price_min']
        price_max = local_settings.DATABASE['price_max']
        product_count_max = local_settings.DATABASE['product_count_max']
        for i in range(number_of_orders):
            id = i + 1
            user = f"user{random.randint(1, number_of_users)}"
            product = f"product{random.randint(1, number_of_products)}"
            month = random.randint(1, 12)
            price = random.randint(price_min, price_max)
            count = random.randint(1, product_count_max)
            order = Order(id, user, product, month, price, count)
            orders.append(order)
        return orders

    def export_to_csv(file_name: str, orders: list):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "User", "Product", "Month", "Price",
                            "Count", "Total Price"])
            for order in orders:
                writer.writerow([order.id, order.user, order.product, order.month,
                                order.price, order.count, order.total_price])
