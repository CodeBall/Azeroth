from azeroth.models.tag import Tag
from azeroth.app_runner import mysql_db as db


class TagController:

    def add_tag(self, data):
        try:
            name = data["name"]
            nickname = data["nickname"]
            use_group = data.get("use_group")
            about = data.get("about")
        except:
            return {"status": "failure"}

        tag_obj = Tag(name, nickname, use_group, about)

        try:
            db.session.add(tag_obj)
            db.session.commit()
            data["id"] = tag_obj.id
            return {"status": "success", "data": data}
        except Exception as es:
            print(es)
            return {"status": "failure"}

    def get_all_tags(self):

        all_tags = Tag.query.all()

        results = []
        for one_tag in all_tags:
            results.append({
                'name': one_tag.name,
                'nickname': one_tag.nick_name,
                'use_group': one_tag.use_group,
                'about': one_tag.about
            })

        return results

    def get_tag_by_name(self, name):
        return Tag.query.filter_by(name=name).first()