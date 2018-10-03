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
        # file.write('Start here.\n{}\n\n'.format(datetime.now().strftime("%B %d %Y, %H:%M:%S")))

    if counter == 1:
        to_write = 'Start here.\n{}\n\n'.format(datetime.now().strftime("%B %d %Y, %H:%M:%S"))
        file.write(to_write)

    file.write('\n')
    # file.write(datetime.now().strftime("%B %d %Y, %H:%M:%S"))
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
        headr = 'Number;ID;Try;Time\n'
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

    # user_first_name = user_information[0]['first_name']
    # user_last_name = user_information[0]['last_name']

    # try:
    #     user_deactivated = user_information[0]['deactivated']
    #     # user_dead = user_deactivated
    # except KeyError:
    #     # user_dead = 0
    #     user_friends = vk_api.friends.get(user_id=user_id, v=5.89)
    #
    # # return (user_dead, user_first_name, user_last_name, user_sex, user_friends)
    # return (user_first_name, user_last_name, user_friends)
    pass


def can_i_do_this(iteration):

    # dict_of_methods = []
    api = create_session(token=token)
    global counter
    counter = 0
    while True:
        counter += 1
        user_id = randint(1, 999999)
        start_time = time()
        # to_log('Start time {}')
        mini_counter = 0
        while True:
            try:
                mini_counter += 1
                user_info(user_id=user_id, vk_api=api)
                end_time = time()
                break
            except:
                pass
        to_log('{} request for vk.com/id{} complete. Try {}. Time {}.'.format(
            counter,
            user_id,
            mini_counter,
            end_time - start_time
        ))
        to_csv('{};{};{};{}'.format(
            counter,
            user_id,
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
    log = 'log_1000iter'
    token = '1cc8e1444fd1bb6858af1a52c88b34543ab64533e357f146a351dace10154a15e7df18557c041a366c149'
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
