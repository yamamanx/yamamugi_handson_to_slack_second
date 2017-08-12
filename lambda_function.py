# coding:utf-8


import requests
import json
import os
import logging
import traceback


slack_url = os.environ['SLACK_URL']


def sendMessage(content, channel):
    payload_dic = {
        "text": content,
        "channel": channel,
    }
    requests.post(slack_url, data=json.dumps(payload_dic))


def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    try:
        kintone_url = event.get('kintone_url','')
        message_template = u':telephone:申込受付レコードを作成しました\n{url}'
        sendMessage(
            message_template.format(url=kintone_url),
            '#general'
        )
        return event

    except Exception as e:
        sendMessage(traceback.format_exc(), '#general')
        logger.error(traceback.format_exc())
        raise(traceback.format_exc())
