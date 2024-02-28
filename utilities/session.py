import configparser
import logging
import os


def get_or_create_data():
    config = configparser.ConfigParser(allow_no_value=True)
    if not os.path.exists('data.txt'):
        config.add_section('updater')
        config.set('updater', 'restarts', '0')
        config.write(open('data.txt', 'w'))
        logging.info('Loaded default data file.')
    else:
        config.read('data.txt')
        logging.info('Loaded existing data file.')
    return config


def save_data(data):
    data.write(open('data.txt', 'w'))


def tick_updater():
    data = get_or_create_data()

    data['updater']['restarts'] = str(int(data['updater']['restarts']) + 1)
    save_data(data)
    logging.debug("Ticked updater: " + data['updater']['restarts'])


def is_initial_launch():
    data = get_or_create_data()
    return data['updater']['restarts'] == '0'


def should_update():
    data = get_or_create_data()

    if int(data['updater']['restarts']) <= 3:
        # tick_updater()
        return True
    else:
        return False

    if data['updater']['restarts'] == '0':
        data['updater']['restarts'] = '1'
        save_data(data)
        return True
    elif data['updater']['restarts'] == '1':
        data['updater']['restarts'] = '2'
        save_data(data)
        return True
    elif data['updater']['restarts'] == '2':
        data['updater']['restarts'] = '-1'
        save_data(data)
        return True
    else:
        return False
