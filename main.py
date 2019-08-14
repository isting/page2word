#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
python3
个人学习demo
对指定网页上的单词进行爬取
采用百度翻译进行翻译
数据处理逻辑（单词大于2个字母，去重，移除数字）
data/translate_data.txt 保存原始文件和翻译结果
./url.txt  保存检索到地址
'''

import requests
import re
import time
from utils.translate import translate


class Studye(object):
    def __init__(self):
        self.url = ''
        self.temporary = ''
        print('初始化中')
        print('处理页面信息中...')

    # 获取地址
    def get_url(self):
        # self.url = input('请输入想要检索的网络地址：')
        # return self.url
        with open('./url.txt', 'r', encoding="utf-8") as f:
            url = f.read()
            self.url = url[1:-1]
    # 请求地址
    def query_url(self, url):
        result = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
        })
        print('获取数据完成')
        return result.text

    # 临时读取本地数据
    def data_read(self):
        data = ''
        with open('./data.txt', 'r+', encoding="utf-8") as f:
            data = f.read()
        return data

    # 数据处理
    def data_re_dispose(self, data):
        # 移除style script 尖括号 移除数字 转list 去重 移除简单的内容  根据列表移除内容
        data = re.sub(r'<style>([\s\S]+?)</style>', '', data)
        data = re.sub(r'<script([\s\S]+?)</script>', '', data)
        data = re.sub(r'<[^>]*>', '', data)
        data = re.sub(r'\d', '', data)
        data = re.findall(r'\w+',  data)
        data = list(set(data))
        data = filter(lambda x: len(x) > 2, data)
        print('数据处理完成')
        return data

    # 调用有道翻译
    def data_translate(self, data):
        data = list(data)
        for k in range(len(data)):
            self.temporary += translate(data[k], k, len(data))
            # time.sleep(1)

    # 保存数据
    def save_data(self, data):
        with open('data/original_data.txt', 'w', encoding="utf-8") as f:
            for k in list(data):
                f.write(k + '\n')
        print('保存原始数据完成')

    # 保存带有翻译的数据
    def save_data_translate(self):
        with open('data/translate_data.txt', 'w', encoding="utf-8") as f:
            f.write(self.temporary)
        print('保存翻译数据完成')

    # begin
    def run(self):
        try:
            # 获取地址
            self.get_url()
            if not self.url: return print('地址不正确')
            # 请求数据
            data = self.query_url(self.url)
            # 本地模拟数据
            # data = self.data_read()
            # 数据处理
            data = self.data_re_dispose(data)
            # 保存原始数据
            # self.save_data(data)
            # 翻译
            self.data_translate(data)
            # 保存翻译
            self.save_data_translate()
        except Exception as e:
            print('出错了', e)
        finally:
            print('完成 ^_^ , 10s后退出')
            time.sleep(10)


if __name__ == "__main__":
    Studye().run()
