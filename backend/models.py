class User:

    def __init__(
        self,
        username,
        email,
        password,
        role
    ):

        self.username=username

        self.email=email

        self.password=password

        self.role=role



class Product:

    def __init__(
        self,
        name,
        description,
        price,
        image
    ):

        self.name=name

        self.description=description

        self.price=price

        self.image=image



class Order:

    def __init__(
        self,
        user_id,
        product_id,
        status
    ):

        self.user_id=user_id

        self.product_id=product_id

        self.status=status
