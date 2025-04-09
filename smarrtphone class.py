# Defining the Smartphone class
class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

        # Method to display details of the smartphone
    def display_info(self):
        print(f"Smartphone Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")
        print(f"Color: {self.color}")

        # Method to make a call
    def make_call(self, number):
        print(f"Calling {number}...")

        # Method to send a message
    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

# Defining the SmartphoneWithCamera class that inherits from Smartphone class
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, color, camera_resolution):
        super().__init__(brand, model, storage, color)
        self.camera_resolution = camera_resolution  # Additional attribute for camera 

    # Encapsulation: Hiding camera resolution behind a method
    def get_camera_resolution(self):
        return f"{self.camera_resolution} MP"

    # Overriding the method to display additional info about camera
    def display_info(self):
        super().display_info()
        print(f"Camera Resolution: {self.camera_resolution}")

# Creating an object of the SmartphoneWithCamera class
smartphone = SmartphoneWithCamera("Samsung", "Galaxy S21", 128, "Phantom Gray", 64)

# Calling the display_info method to show smartphone details
smartphone.display_info()
