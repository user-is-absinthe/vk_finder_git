from vk import Session, API


def name_to_id(token_0, long_name_0):
    session = Session(access_token=token_0)
    vk_api = API(session)
    information = vk_api.utils.resolveScreenName(screen_name=long_name_0, v=5.80)
    return information


def main(main_token, main_long_name):
    info_by_user = name_to_id(token_0=main_token, long_name_0=main_long_name)
    print('Full name: ', main_long_name)
    print('Type of object: ', info_by_user['type'])
    print('Object id: ', info_by_user['object_id'])
    print('\nHelp:\nuser — пользователь;\ngroup — сообщество;\napplication — приложение.')


if __name__ == '__main__':
    token = 'tkn'
    long_name = 'name'
    main(main_token=token, main_long_name=long_name)
