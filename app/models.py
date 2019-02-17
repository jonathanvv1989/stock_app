from app import db


class Trades(db.Model):
    """
    Records transactions in the portfolio
    date: date of the trade (datetime)
    ticker_id: the ticker of the company/fund
    currency_code: currency of the transaction
    type: "BUY" or "SELL"
    quantity: number of shares traded (if sell should be negative)
    price: price per share in hundreds of pence with no decimals.
        e.g. 21595 is £2.1595 (as some AIM listed shares trade below 1p)
    """
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True)
    ticker_id = db.Column(db.String(10), index=True, unique=True)
    currency_code = db.Column(db.String(3))
    type = db.Column(db.String(4))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __repr__(self):
        return "<Quantity {}> on <Ticker {}>".format(
            self.quantity, self.ticker_id
        )
