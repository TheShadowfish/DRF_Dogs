import stripe
from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_dollars(amount):
    """Конвертирует рубли в доллары"""

    # Отказывается работать
    c = CurrencyRates()
    rate = c.get_rate("RUB", "USD")
    return int(amount * rate)

    # а так - все работает. Что с theforexapi.com?
    # return int(amount/85.875)


def create_stripe_price(amount):
    """Создает цену в страйпе"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Donation"},
    )


def create_stripe_session(price):
    """Создание сессии страйп"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
