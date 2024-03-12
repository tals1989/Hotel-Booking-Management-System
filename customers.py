class Customer:
    def __init__(self, id, name, address, city, email, age):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.email = email
        self.age = age

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "email": self.email,
            "age": self.age
        }

class CustomerManager:
    def __init__(self):
        self.customers = []

    def load_customers(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                customer = Customer(*data)
                self.customers.append(customer)

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer_id):
        self.customers = [customer for customer in self.customers if customer.id != customer_id]

    def find_customer_by_name(self, name):
        return [customer for customer in self.customers if customer.name == name]

    def display_all_customers(self):
        for customer in self.customers:
            print(customer.to_dict())
