from database import db 
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    # id, usename(80), password_hash(255)
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False)
    password_hash = db.Column(db.String(255), nullable = False)
    # 특정 사용자가 장바구니에 담은 아이템 목록
    items_in_cart = db.relationship("Cart", back_populates = 'customer', lazy = 'dynamic')
    all_orders = db.relationship("Order", back_populates = 'customer', lazy = 'dynamic')

    # encode password : generate hashed password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    # decode password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    # id, name(81), price(float), description(200)
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(81), nullable = False)
    price = db.Column(db.Float, nullable = False)
    description = db.Column(db.String(200))

class Order(db.Model):
    # id, user_id(foreign key), total_price(float), is_paid(Boolean)
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    total_price = db.Column(db.Float, nullable = False)
    is_paid = db.Column(db.Boolean, nullable = False)
    customer = db.relationship('User', back_populates = 'all_orders')

class OrderDetail(db.Model):
    # id, order_id(from order), product_id, quanity
    __tablename__ = "order_detail"
    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

class Cart(db.Model):
    # id, user_id, product_id, quanity
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    custoemr = db.relationship("User", back_populates = 'items_in_cart')