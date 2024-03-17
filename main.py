from order_manager import OrderManager
import local_settings


if __name__ == "__main__":
    try:
        number_of_orders = local_settings.DATABASE['number_of_orders']
        file_name = local_settings.DATABASE['file_name']
        orders = OrderManager.create_orders(number_of_orders)
        print("Orders created !!")
        OrderManager.export_to_csv(file_name, orders)
        print("Orders exported to csv !!")
    except Exception as error:
        print("Error: ", error)
    finally:
        print("The End !!")
