API_KEY = "sk_live_test_key"

def getUserData(userId):
    import sqlite3
    query = "SELECT * FROM users WHERE id='" + userId + "'"
    conn = sqlite3.connect("app.db")
    return conn.execute(query).fetchone()