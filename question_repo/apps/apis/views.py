from django.shortcuts import render ,HttpResponse

import logging

#apis 为settings中的logging配置中的loggers
logger = logging.getLogger('apis')


def logtest(request):
    logger.info("欢迎访问")
    return HttpResponse('日志测试')

