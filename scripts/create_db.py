from azeroth.app_runner import mysql_db as db, app


from azeroth.models.card import Card
from azeroth.models.card_group import CardGroup
from azeroth.models.card_to_group import CardToGroup
from azeroth.models.tag import Tag
from azeroth.models.tag_to_card import TagToCard
from azeroth.models.tag_to_group import TagToGroup

if __name__ == '__main__':
    with app.app_context():
        db.create_all()