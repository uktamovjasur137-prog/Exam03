class Phone:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def show_info(self):
        return f"{self.brand} {self.model}"
    
phone = Phone("Samsung", "Galaxy S21")
print(phone.show_info())