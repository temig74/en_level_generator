import requests
from bs4 import BeautifulSoup


def get_auth_session(domain, login, password):
    my_session = requests.session()
    try:
        auth_request_json = my_session.post(f'https://{domain}/login/signin?json=1', data={'Login': login, 'Password': password}).json()
    except:
        print('Ошибка запроса авторизации, возможно неверно указан домен')
        return
    if auth_request_json['Error'] == 0:
        print('Авторизация успешна')
        return my_session
    else:
        print('Ошибка авторизации')
        return


def task_upload(auth_session, input_task, level_num, game_id, domain):
    # payload = {'inputTask': input_task, 'chkReplaceNlToBr': 'off'}
    auth_session.post(f'https://{domain}/Administration/Games/TaskEdit.aspx?gid={game_id}&level={level_num}', data={'inputTask': input_task})


def sector_upload(auth_session, txt_sector_name, answer_list, level_num, game_id, domain):
    payload = {'txtSectorName': txt_sector_name, 'savesector': ' '}
    for i, elem in enumerate(answer_list):
        payload[f'txtAnswer_{i + 1}'] = elem
        payload[f'ddlAnswerFor_{i + 1}'] = '0'
    auth_session.post(f'https://{domain}/Administration/Games/LevelEditor.aspx?gid={game_id}&level={level_num}', data=payload)


def bonus_upload(auth_session, txt_bonus_name, txt_task, txt_help, level_id, answer_list, txt_hours, txt_minutes, txt_seconds, domain, level_num, game_id):
    payload = {
        'txtBonusName': txt_bonus_name,
        'txtTask': txt_task,
        'ddlBonusFor': '',
        'rbAllLevels': '1',
        'txtHelp': txt_help,
        f'level_{level_id}': 'on',
        'txtHours': txt_hours,
        'txtMinutes': txt_minutes,
        'txtSeconds': txt_seconds}
    for i, elem in enumerate(answer_list):
        payload[f'answer_-{i+1}'] = elem
    auth_session.post(f'https://{domain}/Administration/Games/BonusEdit.aspx?gid={game_id}&level={level_num}&bonus=0&action=save', data=payload)


def get_level_id(auth_session, domain, game_id, level_num):
    r = auth_session.get(f'https://{domain}/Administration/Games/LevelManager.aspx?gid={game_id}')
    html = BeautifulSoup(r.content, 'html.parser')
    parse_set = html.find('select', id='ddlCopyFrom').find_all('option')
    lvl_d = {int(elem.text): elem.get('value') for elem in parse_set}
    return lvl_d[level_num]
