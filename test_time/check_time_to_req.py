from datetime import datetime
from random import choice  # , randint
from time import time
from sys import exit

from vk import Session, API, exceptions


def create_session():
    session = Session(access_token=tokenVK)
    vk_api = API(session)
    return vk_api


def user_get():
    vk_API.users.get(
        user_id=userID_1,
        fields='first_name, last_name, is_closed, can_access_closed, deactivated',
        v=5.89
    )


def photos_get_albums():
    vk_API.photos.getAlbums(
        user_id=userID_1,
        v=5.89
    )


def wall_get():
    vk_API.wall.get(
        user_id=userID_1,
        v=5.89
    )


def friends_get():
    vk_API.friends.get(
        user_id=userID_1,
        v=5.89
    )


def friends_get_mutual():
    vk_API.friends.getMutual(
        source_uid=userID_1,
        target_uid=userID_2,
        v=5.89
    )


def to_log(info):
    try:
        file = open(log_file_txt, 'a')
    except FileNotFoundError:
        file = open(log_file_txt, 'w')
    # file.write('')
    time_to_write = datetime.now().strftime("\t[%B %d %Y, %H:%M:%S]\t")
    file.write(time_to_write + info)
    file.write('\n')
    file.close()


def to_csv(info):
    try:
        file = open(log_file_csv, 'a')
    except FileNotFoundError:
        file = open(log_file_csv, 'w')
    file.write(info)
    file.write('\n')
    file.close()


def can_i_do_this():
    # dict_of_methods = []
    # global counter
    counter = 0
    all_time = []

    first_write_text = '\nStart here.\n{}\n\n'.format(datetime.now().strftime("\t%B %d %Y, %H:%M:%S"))
    to_log(info=first_write_text)

    '''
            head = 'Now,Method,Try,Time\n'
        file.write(head)
        date1 = datetime.now().strftime("Now %B %d %Y %H:%M:%S.,,,,\n")
        # date1 = date1.replace(',', ' ')
        # file.write('Now ' + date1 + ',,,,\n')
        file.write(date1)
        file.write('\n')
    '''
    first_write_csv = 'Now,Method,Try,Time'
    to_csv(first_write_csv)
    to_csv(datetime.now().strftime("Start at %B %d %Y %H:%M:%S.,,,"))
    while True:
        counter += 1

        now_choice = choice(all_methods)
        mini_iter = 0
        start_mini = time()
        error_iter = 0
        while True:
            mini_iter += 1
            try:
                if now_choice == 'users.get':
                    user_get()
                    break
                elif now_choice == 'friends.getMutual':
                    friends_get_mutual()
                    break
                elif now_choice == 'friends.get':
                    friends_get()
                    break
                elif now_choice == 'wall.get':
                    wall_get()
                    break
                elif now_choice == 'photos.getAlbums':
                    photos_get_albums()
                    break
            except exceptions.VkAPIError:
                error_iter += 1
                # print('catch')
                if error_iter == 100:
                    time_error = time()
                    print(datetime.now().strftime("%B %d %Y %H:%M:%S. ALARM!!! BANNED FROM VK!"))
                    to_log(datetime.now().strftime("%B %d %Y %H:%M:%S. ALARM!!! BANNED FROM VK!"))
                    ban_to_scv = 'BANNED,FROM,VK,!!!\n'
                    write_to_csv = 'End at {}.,,,\nAll elapsed time: {}.,Max: {}.,Min: {}.,Avg: {}.'.format(
                        datetime.now().strftime("%B %d %Y %H:%M:%S"),
                        time_error - start_program_time,
                        max(all_time),
                        min(all_time),
                        sum(all_time) / len(all_time)
                    )
                    to_csv(ban_to_scv + write_to_csv)
                    exit(10)
                pass
        end_mini = time()
        all_time.append(time() - start_mini)

        write_to_text = 'Now {} iteration, used {} method, success on the {} try, spent {} second(-s).'.format(
            counter,
            now_choice,
            mini_iter,
            end_mini - start_mini
        )
        to_log(info=write_to_text)
        print('\t[\t{}\t]\t'.format(datetime.now().strftime("%B %d %Y, %H:%M:%S")) + write_to_text)

        write_to_csv = '{},{},{},{}'.format(
            datetime.now().strftime("%B %d %Y %H:%M:%S"),
            now_choice,
            mini_iter,
            end_mini - start_mini
        )
        to_csv(info=write_to_csv)

        if counter == iterALL:
            time_now = time()
            date1 = datetime.now().strftime("%B %d %Y, %H:%M:%S")
            write = 'Now, it`s the end. Elapsed time {}.\n{}'.format(time_now - start_program_time, date1)
            to_log(write)
            write_to_csv = 'End at {}.,,,\nAll elapsed time: {}.,Max: {}.,Min: {}.,Avg: {}.'.format(
                datetime.now().strftime("%B %d %Y %H:%M:%S"),
                time_now - start_program_time,
                max(all_time),
                min(all_time),
                sum(all_time) / len(all_time)
            )
            to_csv(info=write_to_csv)
            print('End. Elapsed time {}.\n {}'.format(time_now - start_program_time, date1))
            break


if __name__ == '__main__':

    iterALL = 15000

    tokenVK = 'tkn'
    userID_1 = 1  # S
    userID_2 = 2  # Il
    all_methods = [
        'users.get',
        'friends.getMutual',
        'friends.get',
        'wall.get',
        'photos.getAlbums'
    ]

    '''
    https://vk.com/id1
    https://vk.com/id12356
    https://vk.com/id999999
    '''

    vk_API = create_session()

    if len(tokenVK) != 85:
        print('Check token.')
        exit(1)
    log = 'check_log_{}_iter'.format(iterALL)
    start_program_time = time()
    log_file_txt = log + '.txt'
    log_file_csv = log + '.csv'
    can_i_do_this()
