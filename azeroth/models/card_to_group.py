from azeroth.app_runner import mysql_db as db


class CardToGroup(db.Model):
    __tablename__ = 'card_to_group'
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('card_group.id'))

    def __init__(self, card_id, group_id):
        self.card_id = card_id
        self.group_id = group_id