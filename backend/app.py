from flask import Flask, request, jsonify
from flask_cors import CORS

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

import sqlite3

from auth import encrypt_password, verify_password


app = Flask(__name__)

CORS(app)


app.config["JWT_SECRET_KEY"] = "ecommerce_secret_key"

jwt = JWTManager(app)



# Home API

@app.route("/")
def home():

    return jsonify(
        {
            "message":"E-Commerce Backend Running"
        }
    )



# -------------------------
# USER REGISTER
# -------------------------

@app.route("/register", methods=["POST"])
def register():

    data = request.json


    username = data["username"]

    email = data["email"]

    password = encrypt_password(
        data["password"]
    )


    connection = sqlite3.connect(
        "ecommerce.db"
    )

    cursor = connection.cursor()


    try:

        cursor.execute(
        """
        INSERT INTO users
        (username,email,password)
        VALUES(?,?,?)
        """,
        (
            username,
            email,
            password
        )
        )


        connection.commit()


        return jsonify(
            {
                "message":"Registration successful"
            }
        )


    except:

        return jsonify(
            {
                "message":"Email already exists"
            }
        )


    finally:

        connection.close()




# -------------------------
# USER LOGIN
# -------------------------

@app.route("/login", methods=["POST"])
def login():

    data=request.json


    email=data["email"]

    password=data["password"]



    connection=sqlite3.connect(
        "ecommerce.db"
    )

    cursor=connection.cursor()



    cursor.execute(
        """
        SELECT * FROM users
        WHERE email=?
        """,
        (email,)
    )


    user=cursor.fetchone()


    connection.close()



    if user and verify_password(
        password,
        user[3]
    ):


        token=create_access_token(
            identity=user[0]
        )


        return jsonify(
            {
                "token":token
            }
        )



    return jsonify(
        {
            "message":"Invalid login details"
        }
    )





# -------------------------
# PRODUCT APIs
# -------------------------


@app.route("/products", methods=["GET"])
def get_products():


    connection=sqlite3.connect(
        "ecommerce.db"
    )

    cursor=connection.cursor()


    cursor.execute(
        "SELECT * FROM products"
    )


    products=cursor.fetchall()


    connection.close()


    return jsonify(products)





@app.route("/products", methods=["POST"])
@jwt_required()
def add_product():


    data=request.json


    connection=sqlite3.connect(
        "ecommerce.db"
    )

    cursor=connection.cursor()



    cursor.execute(
    """
    INSERT INTO products
    (name,description,price,image)
    VALUES(?,?,?,?)
    """,
    (
        data["name"],
        data["description"],
        data["price"],
        data["image"]
    )
    )


    connection.commit()

    connection.close()



    return jsonify(
        {
            "message":"Product added"
        }
    )






@app.route("/products/<int:id>", methods=["PUT"])
@jwt_required()
def update_product(id):


    data=request.json


    connection=sqlite3.connect(
        "ecommerce.db"
    )

    cursor=connection.cursor()


    cursor.execute(
    """
    UPDATE products
    SET name=?, description=?, price=?
    WHERE id=?
    """,
    (
        data["name"],
        data["description"],
        data["price"],
        id
    )
    )


    connection.commit()

    connection.close()


    return jsonify(
        {
            "message":"Product updated"
        }
    )





@app.route("/products/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id):


    connection=sqlite3.connect(
        "ecommerce.db"
    )


    cursor=connection.cursor()


    cursor.execute(
        """
        DELETE FROM products
        WHERE id=?
        """,
        (id,)
    )


    connection.commit()

    connection.close()


    return jsonify(
        {
            "message":"Product deleted"
        }
    )





# -------------------------
# CART APIs
# -------------------------


@app.route("/cart", methods=["POST"])
@jwt_required()
def add_cart():


    user_id=get_jwt_identity()


    data=request.json


    connection=sqlite3.connect(
        "ecommerce.db"
    )

    cursor=connection.cursor()



    cursor.execute(
    """
    INSERT INTO cart
    (user_id,product_id)
    VALUES(?,?)
    """,
    (
        user_id,
        data["product_id"]
    )
    )


    connection.commit()

    connection.close()


    return jsonify(
        {
            "message":"Added to cart"
        }
    )





@app.route("/cart", methods=["GET"])
@jwt_required()
def view_cart():


    user_id=get_jwt_identity()


    connection=sqlite3.connect(
        "ecommerce.db"
    )


    cursor=connection.cursor()


    cursor.execute(
    """
    SELECT products.name,
    products.price
    FROM products
    JOIN cart
    ON products.id=cart.product_id
    WHERE cart.user_id=?
    """,
    (user_id,)
    )


    cart=cursor.fetchall()


    connection.close()


    return jsonify(cart)






# -------------------------
# ORDER API
# -------------------------


@app.route("/orders", methods=["POST"])
@jwt_required()
def place_order():


    user_id=get_jwt_identity()


    data=request.json


    connection=sqlite3.connect(
        "ecommerce.db"
    )


    cursor=connection.cursor()



    cursor.execute(
    """
    INSERT INTO orders
    (user_id,product_id)
    VALUES(?,?)
    """,
    (
        user_id,
        data["product_id"]
    )
    )


    connection.commit()

    connection.close()


    return jsonify(
        {
            "message":"Order placed successfully"
        }
    )





@app.route("/orders", methods=["GET"])
@jwt_required()
def track_order():


    user_id=get_jwt_identity()


    connection=sqlite3.connect(
        "ecommerce.db"
    )


    cursor=connection.cursor()


    cursor.execute(
    """
    SELECT * FROM orders
    WHERE user_id=?
    """,
    (user_id,)
    )


    orders=cursor.fetchall()


    connection.close()


    return jsonify(orders)





if __name__=="__main__":

    app.run(debug=True)
