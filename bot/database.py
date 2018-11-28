from mongoengine import *
from config import DATABASE_HOST, DATABASE_LOGIN, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_PORT

connect(DATABASE_NAME, host=DATABASE_HOST, port=DATABASE_PORT, username=DATABASE_LOGIN, password=DATABASE_PASSWORD)
print('Connected to {0}'.format(DATABASE_NAME))

LANGUAGES = ('ru', 'ua')


class User(Document):
    user_id = IntField(required=True)
    username = StringField()
    first_name = StringField()
    last_name = StringField()
    state = StringField()
    language = StringField(choices=LANGUAGES, default=LANGUAGES[0])
    current_pet = IntField()
    current_pet_by_filters = ListField(IntField())


class Pet(Document):
    pet_id = SequenceField()
    user_id = IntField(required=True)
    kind = StringField()
    sex = BooleanField(default=False)    # False - мужской, True - женский
    breed = StringField()
    age = StringField()
    description = StringField()
    view = BooleanField(default=False)  # Можно ли отображать
