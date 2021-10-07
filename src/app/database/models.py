import mongoengine as me

class Example(me.Document):
    example = me.StringField()