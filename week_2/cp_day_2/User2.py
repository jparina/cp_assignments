import datetime

class User:
    user_posts = {
        
    }
    
    def __init__(self, name, email, dl) -> None:
        self.name = name
        self.email = email
        self.license = dl
    
    def __str__(self) -> str:
        return f"My name is {self.name}, my email is {self.email} and my driver's license is {self.license} "

    def post(self, message):
        postid = f"{self.name} {datetime.datetime.now()}"
        self.user_posts[postid] = message
    
kona = User('Kona', 'kona@gmail.com', 'ABC123')
adam = User('Adam', 'adam@gmail.com', 'QWE456')

kona.post("Hello World!")
print(User.user_posts)
kona.post('Hi there')
print(User.user_posts)
adam.post("Hello")
print(User.user_posts)