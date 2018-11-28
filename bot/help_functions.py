from bot.database import Pet
from bot.languages import DICTIONARY


def get_string_current_user_pet(user):
    pet = Pet.objects(pet_id=user.current_pet).first()
    if pet.kind == 'dog':
        message_answer = '\n' + '\n' + DICTIONARY[user.language]['dog'] + '\n'
    elif pet.kind == 'cat':
        message_answer = '\n' + '\n' + DICTIONARY[user.language]['cat'] + '\n'
    else:
        message_answer = '\n' + '\n' + pet.kind + '\n'

    message_answer += DICTIONARY[user.language]['sex'] + (DICTIONARY[user.language]['female_pet_btn']
                                                          if pet.sex else DICTIONARY[user.language]['male_pet_btn']) + \
                      '\n' + \
                      DICTIONARY[user.language]['breed'] + pet.breed + '\n' + \
                      DICTIONARY[user.language]['age'] + pet.age + '\n' + \
                      DICTIONARY[user.language]['description'] + pet.description + '\n' + \
                      '<a href="tg://user?id=%d">%s</a>' % (user.user_id, DICTIONARY[user.language]['owner_user'])
    return message_answer


def get_string_all_pet(user, pet):
    if pet.kind == 'dog':
        message_answer = '\n' + '\n' + DICTIONARY[user.language]['dog'] + '\n'
    elif pet.kind == 'cat':
        message_answer = '\n' + '\n' + DICTIONARY[user.language]['cat'] + '\n'
    else:
        message_answer = '\n' + '\n' + pet.kind + '\n'

    message_answer += DICTIONARY[user.language]['sex'] + (DICTIONARY[user.language]['female_pet_btn']
                                                          if pet.sex else DICTIONARY[user.language]['male_pet_btn']) + \
                      '\n' + \
                      DICTIONARY[user.language]['breed'] + pet.breed + '\n' + \
                      DICTIONARY[user.language]['age'] + pet.age + '\n' + \
                      DICTIONARY[user.language]['description'] + pet.description + '\n' + \
                      '<a href="tg://user?id=%d">%s</a>' % (user.user_id, DICTIONARY[user.language]['owner_user'])
    return message_answer
