from datetime import datetime
from random import randint
from time import time
from sys import exit

from vk import Session, API


def create_session(token):
    session = Session(access_token=token)
    vk_api = API(session)
    return vk_api


def to_log(info):
    try:
        file = open(log_file_txt, 'a')
    except FileNotFoundError:
        file = open(log_file_txt, 'w')

    if counter == 1:
        to_write = 'Start here.\n{}\n\n'.format(datetime.now().strftime("%B %d %Y, %H:%M:%S"))
        file.write(to_write)

    file.write('\n')
    file.write('\t')
    file.write(info)
    file.write('\n')
    file.close()


def to_csv(info):
    try:
        file = open(log_file_csv, 'a')
    except FileNotFoundError:
        file = open(log_file_csv, 'w')
        # file.write('Number;ID;Try;Time\n')
        # file.write(datetime.now().strftime("%B %d %Y, %H:%M:%S"))
        # file.write('\n')

    if counter == 1:
        headr = 'Number;ID;Method;Try;Time\n'
        file.write(headr)
        date1 = datetime.now().strftime("%B %d %Y, %H:%M:%S")
        file.write(date1)
        file.write('\n')

    file.write('\n')
    file.write(info)
    file.close()


def user_info(user_id, vk_api):
    user_information = vk_api.users.get(
        user_id=user_id,
        fields='first_name, last_name, is_closed, can_access_closed, deactivated',
        v=5.89
    )
    return user_information


def mutual_friends(one_user_id, two_user_id, api):
    information = api.friends.getMutual(
        source_uid=one_user_id,
        target_uid=two_user_id,
        v=5.89
    )
    return information


def get_wall(user_id, api):
    post_on_wall = api.wall.get(
        owner_id=user_id,
        v=5.89
    )
    return post_on_wall


def get_friends(user_id, api):
    more_friends = api.friends.get(
        user_id=user_id,
        v=5.89
    )
    return more_friends


def docs_get(api):
    docs = api.docs.get(
        v=5.89
    )
    return docs


def can_i_do_this(iteration):

    # dict_of_methods = []
    api = create_session(token=token)
    global counter
    counter = 0
    while True:
        counter += 1
        bone = randint(0, len(methods_list))
        # if methods_list[bone] == 'user.get':
        # user_id = randint(1, 999999)
        start_time = time()
        # to_log('Start time {}')
        mini_counter = 0
        user_id = randint(1, 999999)
        user_id_2 = randint(1, 999999)
        while True:
            try:
                mini_counter += 1

                if methods_list[bone] == 'user.get':
                    user_info(user_id=user_id, vk_api=api)
                elif methods_list[bone] == 'get.mutual':
                    # user_id_1 = randint(1, 999999)
                    mutual_friends(
                        one_user_id=user_id,
                        two_user_id=user_id_2,
                        api=api
                    )
                    user_id = str(user_id) + '/' + str(user_id_2)
                elif methods_list[bone] == 'get.wall':
                    get_wall(user_id=user_id, api=api)
                elif methods_list[bone] == 'friends.get':
                    get_friends(user_id=user_id, api=api)
                elif methods_list[bone] == 'docs.get':
                    docs_get(api=api)

                end_time = time()
                break
            except:
                pass
        to_log('{} request for vk.com/id{} with {} methods complete. Try {}. Time {}.'.format(
            counter,
            user_id,
            methods_list[bone],
            mini_counter,
            end_time - start_time
        ))
        to_csv('{};{};{};{};{}'.format(
            counter,
            user_id,
            methods_list[bone],
            mini_counter,
            end_time - start_time
        ))

        print('Request n{} for vk.com/id{} complete. Try {}. Time {}.'.format(
            counter,
            user_id,
            mini_counter,
            end_time - start_time
        ))

        if counter == iteration:
            time_now = time()
            date1 = datetime.now().strftime("%B %d %Y, %H:%M:%S")
            write = 'Now, it`s the end. Elapsed time {}.\n{}'.format(time_now - start_program_time, date1)
            to_log(write)
            to_csv(write)
            print('End. Elapsed time {}.\n {}'.format(time_now - start_program_time, date1))
            break

    pass


if __name__ == '__main__':
    log = 'log_dict_test'
    token = 'tkn'
    iteration = 1000

    '''
    https://vk.com/id1
    https://vk.com/id12356
    https://vk.com/id999999
    '''

    if len(token) != 85:
        print('Check token.')
        exit(1)

    start_program_time = time()
    log_file_txt = log + '.txt'
    log_file_csv = log + '.csv'
    can_i_do_this(iteration)
    methods_list = [
        'user.get',
        'get.mutual',
        'get.wall',
        'friends.get',
        'docs.get'
    ]
