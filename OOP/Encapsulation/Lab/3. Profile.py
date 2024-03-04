class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        check_length = len(value) >= 8
        check_uppercase = any([char for char in value if char.isupper()])
        check_digits = any([char for char in value if char.isdigit()])
        if check_length and check_uppercase and check_digits:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        password = '*' * len(self.__password)
        return f'You have a profile with username: "{self.username}" and password: {password}'




import unittest

class Tests(unittest.TestCase):
    def test_invalid_password(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('My_username', 'My-password')
        self.assertEqual(str(ve.exception), "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def test_invalid_username(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('Too_long_username', 'Any')
        self.assertEqual(str(ve.exception), "The username must be between 5 and 15 characters.")

    def test_correct_profile(self):
        self.profile = Profile("Username", "Passw0rd")
        self.assertEqual(str(self.profile), 'You have a profile with username: "Username" and password: ********')

if __name__ == "__main__":
    unittest.main()
