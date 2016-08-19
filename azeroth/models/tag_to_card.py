from azeroth.app_runner import mysql_db as db


class TagToCard(db.Model):
    __tablename__ = 'tag_to_card'
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), primary_key=True)

    def __init__(self, tag_id, card_id):
        self.tag_id = tag_id
        self.card_id = card_id