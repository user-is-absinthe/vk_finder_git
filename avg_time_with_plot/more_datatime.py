from datetime import datetime
from random import choice
from time import time, sleep
from sys import exit

from vk import Session, API, exceptions
import matplotlib.pyplot as plt


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


def can_i_do_this(delay):
    counter = 0
    all_time = []

    first_write_text = '\nStart here.\n{}\n\n'.format(datetime.now().strftime("\t%B %d %Y, %H:%M:%S"))
    to_log(info=first_write_text)

    first_write_csv = 'Now,Method,Delay,Try,Time'
    to_csv(first_write_csv)
    to_csv(datetime.now().strftime("Start at %B %d %Y %H:%M:%S.,,,,"))
    while True:
        counter += 1

        now_choice = choice(all_methods)
        mini_iter = 0
        start_mini = time()
        error_iter = 0
        while True:
            mini_iter += 1
            try:
                sleep(delay)
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
                    ban_to_scv = 'BANNED,FROM,VK,!!!,\n'
                    write_to_csv = 'End at {}.,,,,\nAll elapsed time: {}.,Max: {}.,Min: {}.,Avg: {}.,'.format(
                        datetime.now().strftime("%B %d %Y %H:%M:%S"),
                        time_error - start_program_time,
                        max(all_time) - delaY,
                        min(all_time) - delaY,
                        sum(all_time) - delaY / len(all_time)
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
        print('Now delay {} - {} (step {}) from {}, test n{}, iteration {}.'.format(
            delay,
            all_delays[-1],
            steP,
            len(all_delays),
            all_delays.index(delaY),
            ind
        ))
        print('\t[\t{}\t]\t\t'.format(datetime.now().strftime("%B %d %Y, %H:%M:%S")) + write_to_text)

        write_to_csv = '{},{},{},{},{}'.format(
            datetime.now().strftime("%B %d %Y %H:%M:%S"),
            now_choice,
            delay,
            mini_iter,
            end_mini - start_mini - delaY
        )
        to_csv(info=write_to_csv)

        if counter == iterALL:
            time_now = time()
            date1 = datetime.now().strftime("%B %d %Y, %H:%M:%S")
            write = 'Now, it`s the end. Elapsed time {}.\n{}'.format(time_now - start_program_time, date1)
            to_log(write)
            write_to_csv = 'End at {}.,,,\nAll elapsed time: {}.,Max: {}.,Min: {}.,Avg: {}.,'.format(
                datetime.now().strftime("%B %d %Y %H:%M:%S"),
                time_now - start_program_time,
                max(all_time) - delaY,
                min(all_time) - delaY,
                sum(all_time) / len(all_time) - delaY,
            )
            to_csv(info=write_to_csv)
            print('End. Elapsed time {}.\n {}'.format(time_now - start_program_time, date1))
            return sum(all_time) - delaY / len(all_time)


if __name__ == '__main__':
    tokenVK = '123456798'
    userID_1 = 123456789  # S
    userID_2 = 123456789  # Il
    all_methods = [
        'users.get',
        'friends.getMutual',
        'friends.get',
        'wall.get',
        'photos.getAlbums'
    ]

    vk_API = create_session()

    if len(tokenVK) != 85:
        print('Check token.')
        exit(1)

    iter_BIG = 3
    # iterALL = 1000
    iterALL = 100
    steP = 0.01
    # all_delays = [x * 0.05 for x in range(61)]
    # all_delays = [x * 0.05 for x in range(3)]
    # all_delays = [x * steP for x in range(46)]
    # all_delays = all_delays[15:]
    all_delays = [x * 0.01 for x in range(26)]
    all_delays = all_delays[10:]

    log = 'check_log_{}_{}_iter_with_delay_near_{}'.format(iterALL, iter_BIG, sum(all_delays) / len(all_delays))
    start_program_time = time()
    log_file_txt = log + '.txt'
    log_file_csv = log + '.csv'

    delay_to_time = {}  # delay: avg_time

    for delaY in all_delays:
        pr_delay_to_time = []
        for ind in range(iter_BIG):
            avg_time = can_i_do_this(delay=delaY)
            pr_delay_to_time.append(avg_time)
        delay_to_time[delaY] = sum(pr_delay_to_time) / len(pr_delay_to_time)

    array_X = list(delay_to_time.keys())
    array_Y = []

    for i in array_X:
        array_Y.append(delay_to_time[i])

    figure = plt.figure()
    plt.plot(array_X, array_Y, color='red', linestyle='dashed')  # marker='o',
    plt.title('График зависимости ответов от задержки в окрестности {}.\nОт {} до {} с шагом в {}.'.format(
        sum(all_delays) / len(all_delays),
        all_delays[0],
        all_delays[-1],
        steP
    ))
    plt.xlabel('Время задержки, с.')
    plt.ylabel('Время ответа, с.')
    # plt.show()
    figure.savefig('{}_{}_iter_with_delay_near_{}.png'.format(iterALL, iter_BIG, sum(all_delays) / len(all_delays)))
