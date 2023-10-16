import sqlite3
from contextlib import closing
import threading
import random
import string

class UserDatabase:
    def __init__(self, db_name: str = 'user_data.db'):
        self.db_name = db_name
        with self._connect() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS users 
                            (username TEXT, 
                             chatid INTEGER PRIMARY KEY, 
                             firstname TEXT, 
                             lastname TEXT,
                             referral_code TEXT,
                             credit INTEGER,
                             money INTEGER)''')
            conn.commit()

    def _connect(self):
        return closing(sqlite3.connect(self.db_name, check_same_thread=False))

    def add_user(self, username: str, chatid: int, firstname: str, lastname: str, credit: int, money: int):
        referral_code = ''.join(random.choices(string.ascii_uppercase, k=10))
        with self._connect() as conn:
            conn.execute('''INSERT INTO users 
                            (username, chatid, firstname, lastname, referral_code, credit, money) 
                            VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                         (username, chatid, firstname, lastname, referral_code, credit, money))
            conn.commit()

    def get_user(self, chatid: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE chatid = ?', (chatid,))
            return cursor.fetchone()

    def get_all_users(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()

    def update_user(self, chatid: int, field: str, value):
        with self._connect() as conn:
            conn.execute(f'UPDATE users SET {field} = ? WHERE chatid = ?', (value, chatid))
            conn.commit()

    def delete_user(self, chatid: int):
        with self._connect() as conn:
            conn.execute('DELETE FROM users WHERE chatid = ?', (chatid,))
            conn.commit()

    def delete_all_users(self):
        with self._connect() as conn:
            conn.execute('DELETE FROM users')
            conn.commit()

if __name__ == "__main__":
    db = UserDatabase()
    
    def worker(thread_id):
        chatid = 12345 + thread_id
        try:
            db.add_user(username=f"User{thread_id}", chatid=chatid, firstname='John', lastname='Doe', credit=400, money=200)
            
            user = db.get_user(chatid)
            print(f"Thread-{thread_id}: {user}")
            
        except Exception as e:
            print(f"Exception in Thread-{thread_id}: {e}")

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All Threads Completed")
    print("All Users:", db.get_all_users())

    db.delete_all_users()
    print("All Users after deletion:", db.get_all_users())