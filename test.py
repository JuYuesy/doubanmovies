import re
list = []
html = '''
 <li>
            <div class="item">
                <div class="pic">
                    <em class="">1</em>
                    <a href="https://movie.douban.com/subject/1292052/">
                        <img width="100" alt="肖申克的救赎" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292052/" class="">
                            <span class="title">肖申克的救赎</span>
                                    <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
                                <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.7</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2028559人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">希望让人自由。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        '''
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
    url = 'https://movie.douban.com/top250?start='
    print(url)

    html = html.replace(' ', '')
    for item in parse_one_page(html):
        # 将数据存储在列表中
        list.append(item)
        print(item)
        print(len(list))
    # 判断列表长度进行写入
