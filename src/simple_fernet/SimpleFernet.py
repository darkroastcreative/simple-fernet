import os

from cryptography.fernet import Fernet

class SimpleFernet:
    """A wrapper around the `fernet` module from the `cryptography` package
    designed to simplify the process of using Fernet.
    """

    def __init__(self, key_environment_variable: str = None):
        """Initializes an instance of SimpleFernet.
        
        ## Arguments
        - `key_environment_variable`: A string representing the name of an
        environment variable that contains a Fernet key.
        
        ## Notes
        - It is assumed that you have already created a Fernet key and stored
        its value in an environment variable. This is due to limitations related
        to setting environment variables with Python code.
        """
        self.key_environment_variable = key_environment_variable

        if self.key_environment_variable is None:
            raise ValueError('key_environment_variable is not set. Please provide a valid environment variable name.')
        elif self.key_environment_variable is not None and os.getenv(self.key_environment_variable) is None:
            # TODO: Consider adding logic to set the environment variable such that it persists.
            raise ValueError(f'The environment variable "{self.key_environment_variable}" is not set. Please set its value to a Fernet key.')
        else:
            try:
                Fernet(key=os.getenv(self.key_environment_variable))
            except:
                raise ValueError(f'The Fernet key in the environment variable "{self.key_environment_variable}" is invalid. Please confirm the value is a valid Fernet key and try again.')
    
    def encrypt(self, data) -> bytes:
        """Converts the provided data to bytes and encrypts it using Fernet.
        
        ## Arguments
        - `data`: The data to be encrypted.
        
        ## Returns
        A `bytes` object representing the encrypted data.
        
        ## Notes
        - The data passed into this method must implement the 
        """
        # TODO: Need to determine the best way to convert most/all objects to bytes for encryption.
        pass
    
    def decrypt(self, encrypted_data: bytes|str) -> bytes:
        """Decrypts the provided encrypted data using Fernet.
        
        ## Arguments
        - `encrypted_data`: A `bytes` or `str` object representing the data to
        decrypt with Fernet.
        
        ## Returns
        A `bytes` object representing the decrypted data.
        
        ## Notes
        - The value passed in as `encrypted_data` must be of type `bytes` or
        `str`. If not, a `TypeError` will be raised.
        - This function does not perform any type conversion on the decrypted
        data. Rather, it returns the decrypted data as `bytes` and leaves the
        responsibility of converting the data to the user. This is done
        intentionally to ensure the data is not converted to the wrong type
        after decryption.
        """
        # Declare and initialize a variable to represent the decrypted data.
        decrypted_data: bytes|None = None
        
        # Attempt to decrypt the encrypted data based on its type. If the type
        # of encrypted_data is not bytes or str, a TypeError will be raised.
        if type(encrypted_data) is bytes:
            decrypted_data = Fernet(key=os.getenv(self.key_environment_variable)).decrypt(token=encrypted_data)
        elif type(encrypted_data) is str:
            decrypted_data = Fernet(key=os.getenv(self.key_environment_variable)).decrypt(token=encrypted_data.encode())
        else:
            raise TypeError('encrypted_data must be either bytes or str.')
            
        return decrypted_data