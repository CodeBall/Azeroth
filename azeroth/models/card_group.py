from azeroth.app_runner import mysql_db as db


class CardGroup(db.Model):
    __tablename__ = 'card_group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True, default='default')
    nick_name = db.Column(db.String(200), index=True, default='default')
    content = db.Column(db.Text)

    def __init__(self, name, nickname, content = None):
        self.name = name
        self.nick_name = nickname
        self.content = content