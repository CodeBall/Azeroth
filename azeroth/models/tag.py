from azeroth.app_runner import mysql_db as db


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(100), index=True, default='default', nullable=False)
    nick_name = db.Column(db.String(100), index=True, default='default')
    about = db.Column(db.String(255))

    def __init__(self, name, nickname, about = None):
        self.name = name
        self.nick_name = nickname
        self.about = about
