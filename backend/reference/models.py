from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Guardian(UserMixin, dict):
    def __init__(self, db_client, email):
        guardian = db_client.find_one({"email": email})
        if guardian is None:
            raise ValueError("Account does not exist.")

        super().__init__()

        self.db_client = db_client
        for key, value in guardian.items():
            self[key] = value


    def set_password(self, password):
        hashed_password = generate_password_hash(password)
        self["password_hash"] = hashed_password
        self.save()

    def check_password(self, password):
        return check_password_hash(self["password_hash"], password)

    def save(self):
        self.db_client.update_one({"_id": self["_id"]}, {"$set": self})

    def get_id(self):
        return self["email"]

    @staticmethod
    def create_user(db_client, email, password, name, phone):
        db_client.insert_one({"email": email, "password_hash": generate_password_hash(password), "name": name, "phone": phone})