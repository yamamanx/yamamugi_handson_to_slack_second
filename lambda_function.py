# coding:utf-8


import requests
import json
import os
import logging
import traceback


slack_url = os.environ['SLACK_URL']
log_level = os.environ.get('LOG_LEVEL', 'INFO')

logger = logging.getLogger()

if log_level == 'ERROR':
    logger.setLevel(logging.ERROR)
elif log_level == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)


def send_message(content, channel):
    payload_dic = {
        "text": content,
        "channel": channel,
    }
    logger.debug(payload_dic)
    response = requests.post(slack_url, data=json.dumps(payload_dic))
    logger.debug(response.text)

def lambda_handler(event, context):

    try:
        kintone_url = event.get('kintone_url','')
        message_template = u':telephone:申込受付レコードを作成しました\n{url}'
        send_message(
            message_template.format(url=kintone_url),
            '#general'
        )
        return event

    except Exception as e:
        send_message(traceback.format_exc(), '#general')
        logger.error(traceback.format_exc())
        raise(traceback.format_exc())
