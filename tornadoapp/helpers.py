import bcrypt

class Password:
    """Wrapper class for hashing and comparing passwords using bcrypt"""

    @staticmethod
    def hash(password):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    @staticmethod
    def compare(password, hashed):
        return bcrypt.hashpw(password, hashed) == hashed

