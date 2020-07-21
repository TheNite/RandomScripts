import mariadb
import sys

try:
    conn = mariadb.connect(
        user="phpmyadmin",
        password="password123",
        host="",
        port=3306,
        database='employees',
    )
except mariadb.Error as e:
    print(f'Error connecting to MariaDB Platform: {e}')
    sys.exit(1)
cur = conn.cursor()

cur.execture(
    "SELECT first_name,lastname FROM employees WHERE first_name=?",
    (some_name,))

for (firs_name, last_name) in cur:
    print(f'First Name: {firs_name}, Last Name: {last_name}')