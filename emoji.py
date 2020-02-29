# -*- coding:utf-8 -*-
import json
import sys
from datetime import datetime
from workflow import Workflow, web
import random

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')


def main(wf):
    # wf 是一个 Workflow 对象
    # 这个是主函数

    # 引入其他模块

    # 获取参数

    with open("emojis.json") as file:
        data = json.load(file)
    args = wf.args
    input_data = args[0]
    # 自定义的程序
    # 向结果中添加显示内容
    number = 0
    tmp = []
    tmp += wf.filter(input_data, data.keys(), key=lambda x: x, max_results=3)
    raw_data = wf.filter(input_data, data.items(),
                         key=lambda x: u''.join(x[1]['keywords']), max_results=40)
    for i in raw_data:
        tmp.append(i[0])
    for i in tmp:
        number += 1
        wf.add_item(data[i]['char'], i,
                    icon="icon.png", copytext=data[i]['char'], valid=True, arg=data[i]['char'])

    # 让 Alfred 显示结果
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()  # 创建针对 Alfred2 的 Workflow 对象
    # 如果针对的是 Alfred3，那么应该使用 wf = Workflow3()
    # 设置日志对象
    log = wf.logger
    wf.run(main)  # 调用主函数
