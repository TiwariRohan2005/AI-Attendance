from app.config import ADMIN_USERNAME, ADMIN_PASSWORD

def validate_admin(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD