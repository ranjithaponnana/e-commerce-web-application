import sqlite3


def create_database():

    connection = sqlite3.connect("ecommerce.db")

    cursor = connection.cursor()


    # Users table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        role TEXT DEFAULT 'user'

    )
    """)



    # Products table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        description TEXT,

        price REAL NOT NULL,

        image TEXT

    )
    """)



    # Cart table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        product_id INTEGER,

        quantity INTEGER DEFAULT 1,

        FOREIGN KEY(user_id) REFERENCES users(id),

        FOREIGN KEY(product_id) REFERENCES products(id)

    )
    """)



    # Orders table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        product_id INTEGER,

        status TEXT DEFAULT 'Processing',

        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    connection.commit()

    connection.close()



if __name__=="__main__":

    create_database()

    print("Database created successfully")
