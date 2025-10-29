from werkzeug.security import check_password_hash, generate_password_hash
import db

def create_user(username, password, timestamp):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO Users (username, password_hash, time_stamp) VALUES (?, ?, ?)"
    db.execute(sql, [username, password_hash, timestamp])

def username_exists(username):
    sql = "SELECT 1 FROM Users WHERE username = ?"
    result = db.query(sql, [username])
    return len(result) > 0

def check_login(username, password):
    sql = "SELECT user_id, password_hash FROM Users WHERE username = ?"
    result = db.query(sql, [username])

    if len(result) == 1:
        user_id, password_hash = result[0]
        if check_password_hash(password_hash, password):
            return user_id

    return None

def get_profile_info(profile_id):
    sql = "SELECT username, time_stamp FROM Users WHERE user_id = ?"
    result = db.query(sql, [profile_id])
    if len(result) == 1:
        return result[0]['username'], result[0]['time_stamp']
    return None, None