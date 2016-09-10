from azeroth.app_runner import mysql_db as db


class TagToGroup(db.Model):
    __tablename__ = 'tag_to_group'
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('card_group.id'))

    def __init__(self, tag_id, group_id):
        self.tag_id = tag_id
        self.group_id = group_id