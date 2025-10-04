from app import create_app
from app.helpers.app_context import AppContext as AC
from app.models import (User, Role, Product, ProductCategory,Article, ArticleCategory, 
ArticleStatus,OrderStatus,Order, OrderItem ,ConfigValues, Voucher, Variation, SubscriptionType, UserSubscription)
import random
from random import randint
import string
from datetime import datetime
import time
from timeloop import Timeloop
from datetime import timedelta

db = AC().db

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == "__main__":
    app = create_app("config.dev")  # start app with config
    with app.app_context():
        db.drop_all()
        db.create_all()
        member = Role("member")
        admin = Role("admin")
        user = User("abc@gmail.com", "1q2w3e4r")
        user2 = User("abcd@gmail.com", "1q2w3e4r")
        user2.subscribed=True
        user.role = admin
        max_no_products_per_order = ConfigValues('max_no_products_per_order', 4)
        min_duration_of_rental = ConfigValues('min_duration_of_rental', 4)
        max_duration_of_rental = ConfigValues('max_duration_of_rental', 7)
        max_no_of_vouchers = ConfigValues('max_no_of_vouchers', 2)
        MAIL_USERNAME = ConfigValues('MAIL_USERNAME', 'adayahouseshop@gmail.com')
        MAIL_PASSWORD = ConfigValues('MAIL_PASSWORD', 'adaya1234')
        MAIL_SERVER = ConfigValues('MAIL_SERVER', 'smtp.gmail.com')
        MAIL_PORT = ConfigValues('MAIL_PORT', 465)
        MAIL_DEFAULT_SENDER = ConfigValues('MAIL_DEFAULT_SENDER', 'adayahouseshop@gmail.com')
        EMAIL_PASSWORD_RESET_SECRET_KEY= ConfigValues('EMAIL_PASSWORD_RESET_SECRET_KEY', 'Thisisasecret!')
        SIB_KEY = ConfigValues('SIB_KEY', 'gzryVUPZHa1GW7n6')
        for x in range(1, 30):
            variation = Variation('S')
            variation.product_id = x
            variation.price = 10
            variation.stock = 1
            variation1 = Variation('M')
            variation1.product_id = x
            variation1.price = 20
            variation1.stock = 1
            variation2 = Variation('L')
            variation2.product_id = x
            variation2.price = 30
            variation2.stock = 1
            variation3 = Variation('XL')
            variation3.product_id = x
            variation3.price = 40
            variation3.stock = 1
            db.session.add(variation)
            db.session.add(variation1)
            db.session.add(variation2)
            db.session.add(variation3)
        voucher = Voucher('HAO20')
        voucher.discount_fixed_amount = 5
        voucher.product_id = 3
        voucher.redeem_by = datetime.strptime('13-4-2020', '%d-%m-%Y')
        voucher2 = Voucher('LUO20')
        voucher2.discount_fixed_amount = 20
        voucher2.product_id = 5
        voucher2.redeem_by = datetime.strptime('18-4-2020', '%d-%m-%Y')
        subtype = SubscriptionType(duration=1, price=10)
        subtype2 = SubscriptionType(duration=6, price=40)
        usersubscription = UserSubscription()
        usersubscription.user_id=2
        usersubscription.start_date=datetime.now()
        usersubscription.end_date=datetime.strptime('06-02-2020 05:58:00', '%d-%m-%Y %H:%M:%S')
        usersubscription.subscription_type=subtype
        db.session.add(max_no_products_per_order)
        db.session.add(min_duration_of_rental)
        db.session.add(max_duration_of_rental)
        db.session.add(max_no_of_vouchers)
        db.session.add(MAIL_USERNAME)
        db.session.add(MAIL_PASSWORD)
        db.session.add(MAIL_SERVER)
        db.session.add(MAIL_PORT)
        db.session.add(MAIL_DEFAULT_SENDER)
        db.session.add(EMAIL_PASSWORD_RESET_SECRET_KEY)
        db.session.add(SIB_KEY)
        db.session.add(member)
        db.session.add(user)
        db.session.add(user2)
        db.session.add(voucher)
        db.session.add(voucher2)
        db.session.add(subtype)
        db.session.add(subtype2)
        db.session.add(usersubscription)
        food_category = ProductCategory('food')
        clothes_category = ProductCategory('cloth')
        food_article = ArticleCategory('food-article')
        clothes_article = ArticleCategory('cloth-article')
        status = ArticleStatus('draft')
        order_status = OrderStatus('completed')
        db.session.add(order_status)
        db.session.add(food_article)
        db.session.add(clothes_article)
        db.session.add(food_category)
        db.session.add(clothes_category)
        for x in range(10):
            product = Product(randomString(10))            
            article = Article(randomString(10))
            order = Order()
            order_item = OrderItem()
            order_item.quantity = 1
            order_item.start_date = datetime.strptime('1-4-2020', '%d-%m-%Y')
            order_item.end_date = datetime.strptime('8-4-2020', '%d-%m-%Y')
            order.order_items = []
            order.order_items.append(order_item)
            article_category = food_article
            category = food_category
            if x % 2 == 0:
                category = clothes_category
                article_category = clothes_article
            product.category = category
            article.category = article_category
            article.status = status
            db.session.add(order)
            db.session.add(product)
            db.session.add(order_item)
            db.session.add(article)

        db.session.commit()