class PasswordManager:
    def __init__(self, __password: str) -> None:
        self.__password = __password  
    
    # TODO: Implement the verify_password method
    def verify_password(self, candidate: str) -> bool:
        return candidate == self.__password



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
