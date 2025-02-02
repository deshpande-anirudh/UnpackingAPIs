import bcrypt

database = {}


def hash_password(plain_password):
    hashed_password = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt()).decode()
    return hashed_password


def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


if __name__ == "__main__":
    user_name = 'danny'
    plain_password = 'Abc$123'

    database[user_name] = hash_password(plain_password)
    print(
        check_password(plain_password, database[user_name])
    )



