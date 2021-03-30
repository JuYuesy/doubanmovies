import requests
from requests.exceptions import RequestException
import re
import time
# from xlsxwriter import Workbook

list = []

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) +'
                          'AppleWebKit/537.36 (KHTML, like Gecko) +'
                          'Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'
        }
        # 添加headers
        response = requests.get(url, headers=headers)
        # 响应状态码查询
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):

    # 正则表达式
    pattern = re.compile('<li>.*?<em class="">(.*?)</em>.*?href="(.*?)".*?"title">(.*?)</span>.*?<p class="">\n\s+(.*?)...<br>\n +'
                     '(.*?)\s.*?age">(.*?)<.*?<span>(.*?)<.*?"inq">(.*?)<', re.S)
    items = re.findall(pattern, html)

    for item in items:
        print(item[2])
        yield {
            "ranking": str(item[0]),
            "average": item[5],
            "title": item[2],
            "number": item[6],
            "inq": item[7],
            "director&actor": item[3],
            "link": item[1],
            "label": item[4],

        }


def main(start):
    # 更改链接
    url = 'https://movie.douban.com/top250?start=' + str(start)
    print(url)
    html = get_one_page(url)
    html = html.replace(' ', '')
    for item in parse_one_page(html):
        # 将数据存储在列表中
        list.append(item)
        print(item)
        print(len(list))
    # 判断列表长度进行写入
    # if len(list) == 225:
    #     writeListToExcel(list)


# def writeListToExcel(list):
#     # 设置表头
#     ordered_list = ["ranking", "average", "title", "number", "inq", "director&actor", "link", "label"]
#     # 新建工作簿
#     wb = Workbook("豆瓣top250完整(1).xlsx")
#     ws = wb.add_worksheet("New Sheet")

#     first_row = 0
#     # 循环写入表头
#     for header in ordered_list:
#         col = ordered_list.index(header)
#         ws.write(first_row, col, header)

#     row = 1
#     # 写入内容
#     for player in list:
#         for _key, _value in player.items():
#             col = ordered_list.index(_key)
#             ws.write(row, col, _value)
#         row += 1  # enter the next row
#     # 关闭文件
#     wb.close()


if __name__ == '__main__':
    # 更改链接
    for start in range(0, 225, 25):
        main(start)
        # 设置延时
        time.sleep(1)