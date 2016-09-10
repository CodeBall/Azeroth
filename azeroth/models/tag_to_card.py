from azeroth.app_runner import mysql_db as db


class TagToCard(db.Model):
    __tablename__ = 'tag_to_card'
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))

    def __init__(self, tag_id, card_id):
        self.tag_id = tag_id
        self.card_id = card_id