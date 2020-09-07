#Python 3.8.5
# Setting up a password in its own environment.



import os

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")

print(db_user)
print(db_password)

