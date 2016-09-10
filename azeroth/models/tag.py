from azeroth.app_runner import mysql_db as db

from sqlalchemy.dialects.mysql import TINYINT


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(100), index=True, default='default', nullable=False, unique=True)
    nick_name = db.Column(db.String(100), index=True, default='default')
    use_group = db.Column(TINYINT, default=True)
    about = db.Column(db.String(255))

    def __init__(self, name, nickname, use_group=True, about=None):
        self.name = name
        self.nick_name = nickname
        self.use_group = use_group
        self.about = about
