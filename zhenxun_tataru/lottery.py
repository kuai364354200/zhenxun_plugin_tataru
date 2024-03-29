# -*- coding: utf-8 -*-
"""
仙人仙彩
"""

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

import random


__zx_plugin_name__ = "帮你选每周仙人仙彩数字"
__plugin_usage__ = """
usage：
    帮你选每周仙人仙彩数字
    指令：
        仙人彩
""".strip()
__plugin_des__ = "仙人彩：帮你选每周仙人仙彩数字"
__plugin_cmd__ = ["仙人彩"]
__plugin_version__ = 0.1
__plugin_type__ = ("一些工具",)
__plugin_author__ = "Tataru"
__plugin_settings__ = {
    "level": 1,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["仙人彩"],
}

this_command = "仙人彩"
lottery = on_command(this_command, priority=5, block=True)


async def lottery_help():
    return this_command + "：帮你选每周仙人仙彩数字"


async def random_lottery():
    last_num_list = []
    lottery_list = []
    for _ in range(3):
        while True:
            last_num = random.randint(0, 9)
            if last_num not in last_num_list:
                last_num_list.append(last_num)
                break
        lottery_list.append(str(random.randint(0, 9)) + " " +
                            str(random.randint(0, 9)) + " " +
                            str(random.randint(0, 9)) + " " +
                            str(last_num))
    return "\n".join(lottery_list)


@lottery.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args == this_command:
        lottery_num_str = await random_lottery()
        await lottery.finish("塔塔露觉得这个可以！\n" + lottery_num_str)
    else:
        return
