"""SQLAlchemy Database"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


# User Table using SQLAlchemy syntax
class User(DB.Model):
    """Twitter Users that correspond to tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return "<User: {}>".format(self.name)


# Tweet Table using SQLAlchemy syntax
class Tweet(DB.Model):
    """Twitter Tweets that corresspond to users"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        "user.id"), nullable=False)
    user = DB.relationship("User", backref=DB.backref("tweets", lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)


def insert_example_users():
    """Will get error ran twice, data to play with"""
    kevin = User(id=48, name="kevin")
    timmy = User(id=97, name="timmy")
    DB.session.add(kevin)
    DB.session.add(timmy)
    DB.session.commit()

# TODO: a function to insert example tweets
def insert_example_tweets():
    tweet1 = Tweet(id=33, text="I love cheeseburgers!", user_id=48)
    tweet2 = Tweet(id=26, text="I love tacos!", user_id=97)
    tweet3 = Tweet(id=55, text="I can't believe Kevin likes cheeseburgers", user_id=97)
    tweet4 = Tweet(id=61, text="I like tacos too, Timmy", user_id=48)
    tweet5 = Tweet(id=74, text="That's good, we should get a pizza", user_id=97)
    tweet6 = Tweet(id=89, text="Sounds like a plan!", user_id=48)
    DB.session.add(tweet1)
    DB.session.add(tweet2)
    DB.session.add(tweet3)
    DB.session.add(tweet4)
    DB.session.add(tweet5)
    DB.session.add(tweet6)
    DB.session.commit()
