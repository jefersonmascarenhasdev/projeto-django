
from random import randint
from faker import Faker

fake = Faker()

def make_recipe():
    return {
        "title": fake.sentence(nb_words=4),
        "description": fake.text(max_nb_chars=200),
        "preparation_time": randint(1, 240),
        "servings": randint(1, 20),
        "preparation_steps": fake.text(max_nb_chars=500),
        "created_at": fake.date_time_this_year(),
        "author": {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
        },
        "category": {
            "name": fake.word(),
        },
        "cover": {
            "url": fake.image_url(),
            "alt_text": fake.sentence(nb_words=6),
        },
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(make_recipe())
