import random


class FakeDataGenerator:
    """
    A class to generate and display fake data using built-in Python libraries.
    """

    def __init__(self):
        self.first_names = ["John", "Jane", "Alice", "Bob", "Charlie"]
        self.last_names = ["Doe", "Smith", "Johnson", "Brown", "Williams"]
        self.streets = ["Main St", "High St", "Elm St", "Maple Ave", "Oak Dr"]
        self.domains = ["example.com", "test.com", "demo.com"]

    def generate_name(self):
        """
        Generate a random full name.
        """
        return f"{random.choice(self.first_names)} {random.choice(self.last_names)}"

    def generate_address(self):
        """
        Generate a random address.
        """
        return f"{random.randint(1, 999)} {random.choice(self.streets)}, Cityville, USA"

    def generate_email(self, name):
        """
        Generate a random email address based on the given name.
        """
        return f"{name.replace(' ', '.').lower()}@{random.choice(self.domains)}"

    def generate_phone_number(self):
        """
        Generate a random phone number.
        """
        return f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"

    def generate_fake_data(self):
        """
        Generate and return a dictionary containing fake data.
        """
        name = self.generate_name()
        address = self.generate_address()
        email = self.generate_email(name)
        phone_number = self.generate_phone_number()

        return {
            "Name": name,
            "Address": address,
            "Email": email,
            "Phone Number": phone_number,
        }