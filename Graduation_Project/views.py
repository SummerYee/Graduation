# -*- coding: utf-8 -*-
# @Author  : 王小易 / SummerYee
# @Time    : 2020/4/17 17:26
# @File    : views.py
# @Software: PyCharm

from django.shortcuts import render
import time


def index(request):
    predict_label = '待输入'
    your_query_sentence = request.POST.get('input')
    if your_query_sentence is not None:
        f=open('linshi.txt','w',encoding='utf-8')
        f.write(your_query_sentence)
        f.close()
        time.sleep(0.5)
        f2 = open('linshi2.txt',encoding='utf-8')
        predict_label = f2.read()
        f2.close()
    context={
        'inputt':your_query_sentence,
        'result':predict_label
    }
    return render(request,'index.html',context=context)
