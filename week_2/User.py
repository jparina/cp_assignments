class User:
    def __init__(self, name, email, dl):
        self.name = name
        self.email = email
        self.license = dl
    
    def __str__(self) -> str:
        return f"My name is {self.name}, my email is {self.email} and my driver's license is {self.license} "


kona = User('Kona', 'kona@gmail.com', 'ABC123')
adam = User('Adam', 'adam@gmail.com', 'QWE456')
