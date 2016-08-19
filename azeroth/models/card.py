from azeroth.app_runner import mysql_db as db


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(100), index=True, nullable=False, default='default')
    card_nick_name = db.Column(db.String(100), index=True, default='default')
    card_expend = db.Column(db.Integer, index=True, nullable=False) # 消耗
    card_attack = db.Column(db.Integer, index=True, nullable=False) # 攻击力
    card_hp = db.Column(db.Integer, index=True, nullable=False) # 血量
    image_url = db.Column(db.String(300), nullable=False)
    card_about = db.Column(db.String(300))

    def __init__(self, name, expend, attack, hp, image_url, nick_name=None, about=None):
        self.card_name = name,
        self.card_expend = expend,
        self.card_attack = attack,
        self.card_hp = hp,
        self.image_url = image_url,
        self.card_nick_name = nick_name,
        self.card_about = about