
#生成短信验证码，并写入cache

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from libs import sms
import random
from django.core.cache import cache
import random
import logging
logger = logging.getLogger("apis")


def get_mobile_captcha(request):
    ret = {"code": 200, "msg": "验证码发送成功！"}
    try:
        # 获取ajax-用户提交的数据
        mobile = request.GET.get("mobile")
        if mobile is None:
            raise ValueError("手机号不能为空！")
        # 生成随机验证码
        mobile_captcha = "".join(random.choices('0123456789', k=6))

        # 将短信验证码写入redis, 300s 过期
        # key = mobile ,value = mobile_captcha ,300是时间
        cache.set(mobile, mobile_captcha, 300)
        logger.info(f"验证码是{mobile_captcha}")
        # 发送短信
        if not sms.send_sms(mobile, mobile_captcha):
            raise ValueError('发送短信失败')
    except Exception as ex:
        logger.error(ex)
        ret = {"code": 400, "msg": "验证码发送失败！"}
        # jsonresponese等同于httpresponse做了一层json.dumps的封装
    return JsonResponse(ret)
