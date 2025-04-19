from fake_data_generator import FakeDataGenerator


def main():
    """
    Entry point for the fake data generator application.
    """
    print("Welcome to the Fake Data Generator!")

    # Create an instance of FakeDataGenerator
    generator = FakeDataGenerator()

    # Generate fake data
    fake_data = generator.generate_fake_data()

    # Display the fake data
    print("\nFake Data Generated:")
    for key, value in fake_data.items():
        print(f"{key}: {value}")

    print("\nThank you for using the Fake Data Generator!")


if __name__ == "__main__":
    main()