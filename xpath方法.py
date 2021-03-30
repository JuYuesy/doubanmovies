import json
import requests
from requests.exceptions import RequestException
from lxml import etree
import time
from xlsxwriter import Workbook
list = []
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) +'
                          'AppleWebKit/537.36 (KHTML, like Gecko) +'
                          'Chrome/81.0.4044.113 Safari/537.36 Edg/81.0.416.58'
        }
        # 添加headers
        response = requests.get(url, headers=headers)
        # 响应状态码查询
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 定义get函数
def parse_one_page(html):

    result = etree.HTML(html)
    em = result.xpath('.//div[@class="pic"]//em/text()')
    href = result.xpath('.//div[@class="pic"]//a/@href')
    title = result.xpath('.//div[@class="hd"]/a/span/text()')
    actor = result.xpath('.//div[@class="bd"]/p/text()')
    average = result.xpath('//div[@class="star"]/span[2]/text()')
    Num = result.xpath('//div[@class="star"]/span[4]/text()')
    inq = result.xpath('//p[@class="quote"]/span/text()')
    for items in range(len(em)):
        yield {
            "ranking": em[items],
            "average": average[items],
            "title": title[items],
            "number": Num[items],
            "inq": inq[items],
            "director&actor": actor[items],
            "link": href[items]
        }



def main(start):
    # 更改链接
    url = 'https://movie.douban.com/top250?start='+str(start)
    print(url)
    html = get_one_page(url)
    html = html.replace('&nbsp;', '')
    for item in parse_one_page(html):
        list.append(item)
        print(item)
        print(len(list))
    if len(list) == 225:
        writeListToExcel(list)


def writeListToExcel(list):
    ordered_list = ["ranking", "average", "title", "number", "inq",  "director&actor", "link", "label"]
    wb = Workbook("豆瓣top250完整(1).xlsx")
    ws = wb.add_worksheet("New Sheet")

    first_row = 0
    for header in ordered_list:
        col = ordered_list.index(header)
        ws.write(first_row, col, header)

    row = 1
    for player in list:
        for _key, _value in player.items():
            col = ordered_list.index(_key)
            ws.write(row, col, _value)
        row += 1  # enter the next row
    wb.close()


if __name__ == '__main__':
    # 更改链接
    for start in range(0, 225, 25):
        main(start)
        #设置延时
        time.sleep(1)