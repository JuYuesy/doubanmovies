import re
from lxml import etree

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
                                <span>1982786人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">希望让人自由。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
'''
# xpath方法
def get_one_page(html):
    html = html.replace('&nbsp;', '')
    html = html.replace('\n', '')

    html = etree.HTML(html)

    for result in html.xpath('*//li'):
        em = result.xpath('.//div[@class="pic"]//em/text()')
        href = result.xpath('.//div[@class="pic"]//a/@href')
        title = result.xpath('.//div[@class="hd"]/a/span/text()')
        actor = result.xpath('.//div[@class="bd"]/p/text()')
        average = result.xpath('//div[@class="star"]/span[2]/text()')
        Num = result.xpath('//div[@class="star"]/span[4]/text()')
        inq = result.xpath('//p[@class="quote"]/span/text()')

    yield {
        "ranking": em,
        "average": average,
        "title": title,
        "number": Num,
        "inq": inq,
        "director&actor": actor,
        "link": href,
        }

#
# def main():
#     for item in get_one_page(html):
#         print(item)
# main()
soup = BeautifulSoup(html, 'lxml')
# for result in soup.find_all('li'):
#     em = result.find('em').get_text()
#     print(em)