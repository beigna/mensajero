# coding: utf-8

import requests
from base64 import b64encode
from datetime import datetime

gsm = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
       "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ`¿abcdefghijklmnopqrstuvwxyzäöñüà")
ext = ("````````````````````^```````````````````{}`````\\````````````[~]`"
       "|````````````````````````````````````€``````````````````````````")

ENDPOINT = 'http://192.168.150.1/goform/goform_set_cmd_process'
HEADERS = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'es-AR,en-US;q=0.7,en;q=0.3',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Host': '192.168.150.1',
    'Origin': 'http://192.168.150.1',
    'Pragma': 'no-cache',
    'Referer': 'http://192.168.150.1/index.html',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0', # noqa
    'X-Requested-With': 'XMLHttpRequest'
}
DATA_LOGOUT = {
    'isTest': 'false',
    'goformId': 'LOGOUT'
}


def _encode_message(plaintext):
    res = bytearray()
    for c in plaintext:
        idx = gsm.find(c)
        if idx != -1:
            res.append(idx)
            continue
        idx = ext.find(c)
        if idx != -1:
            res.append(27)
            res.append(idx)

    out = []
    for index, char in enumerate(res.hex()):
        if index % 2 == 0:
            out.append(char.zfill(3))
        else:
            out.append(char)

    return ''.join(out)


def _data_login(user, passwd):
    return {
        'isTest': 'false',
        'goformId': 'LOGIN',
        'password': b64encode(passwd.encode('utf-8')),
        'username': b64encode(user.encode('utf-8'))
    }


def _data_sms(to, message):
    return {
        'isTest': 'false',
        'goformId': 'SEND_SMS',
        'notCallback': 'true',
        'Number': to,
        'sms_time': datetime.now().strftime('%y;%m;%d;%H;%M:%S;-3'),
        'MessageBody': _encode_message(message),
        'ID': '-1',
        'encode_type': 'GSM7_default'
    }


def send_sms(to, message):
    requests.post(ENDPOINT, headers=HEADERS,
                  data=_data_login('admin', 'admin'))
    requests.post(ENDPOINT, headers=HEADERS,
                  data=_data_sms(to, message))
    requests.post(ENDPOINT, headers=HEADERS, data=DATA_LOGOUT)
