# 酷狗音乐下载
from pyquery import PyQuery
import requests
import json
import time
import os

# 获取下载地址
# https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19106737800324233885_1548918161847&hash=B8B84C26A105455FF7B7E84768030041&album_id=14819648&_=1548918161848
# 响应
# jQuery19106737800324233885_1548918161847({"status":1,"err_code":0,"data":{"hash":"D92FEC46466FAC0BFC3A6C8DDB66CDB6","timelength":237077,"filesize":3804769,"audio_name":"\u6d1b\u5929\u4f9d - \u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11","have_album":1,"album_name":"\u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11","album_id":"14819648","img":"http:\/\/imge.kugou.com\/stdmusic\/20190125\/20190125165703269535.jpg","have_mv":0,"video_id":0,"author_name":"\u6d1b\u5929\u4f9d","song_name":"\u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11","lyrics":"[00:00.12]\u6d1b\u5929\u4f9d - \u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11\r\n[00:00.58]\u4f5c\u8bcd\uff1a\u5b59\u839e\r\n[00:00.73]\u4f5c\u66f2\uff1a\u5b59\u839e\r\n[00:20.87]\u5929\u7a7a\u7070\u7070\u7684\r\n[00:22.71]\u4f3c\u4e4e\u8981\u4e0b\u96e8\u4e86\r\n[00:24.95]\u6211\u5fc5\u987b\u9762\u5bf9\u7684\r\n[00:29.03]\u7231\u60c5\u79bb\u5f00\u4e86\r\n[00:31.79]\u6211\u77e5\u9053\u4f60\u7684\u5fc3\u60c5\r\n[00:38.83]\u4e45\u4e45\u4e0d\u80fd\u5e73\u9759\r\n[00:41.03]\u6211\u5931\u843d\u7684\u5fc3\u60c5\r\n[00:43.62]\u5982\u679c\u4f60\u8981\u56de\u5230\r\n[00:47.04]\u4ed6\u7684\u8eab\u8fb9\r\n[00:49.94]\u4e00\u5b9a\u8981\u8fc7\u597d\u6bcf\u5929\r\n[00:56.43]\u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11\r\n[01:01.32]\u4f60\u7684\u7f8e\u7ec8\u4e8e\u4e0d\u5728\u6211\u6000\u62b1\r\n[01:06.07]\u539f\u6765\u6211\u7231\u4f60\u65e0\u53ef\u6551\u836f\r\n[01:10.71]\u6211\u7684\u611f\u60c5\u6700\u540e\u4f60\u8fd8\u6ca1\u8981\r\n[01:15.04]\u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11\r\n[01:19.47]\u4f60\u7684\u7f8e\u7ec8\u4e8e\u4e0d\u5728\u6211\u6000\u62b1\r\n[01:24.33]\u5982\u679c\u4f60\u80fd\u5e78\u798f\u6bcf\u5929\r\n[01:28.96]\u6211\u5b64\u72ec\u4e5f\u503c\u5f97\u9a84\u50b2\r\n[01:43.17]\u5929\u7a7a\u7070\u7070\u7684\r\n[01:44.96]\u4f3c\u4e4e\u8981\u4e0b\u96e8\u4e86\r\n[01:47.45]\u6211\u5fc5\u987b\u9762\u5bf9\u7684\r\n[01:51.07]\u7231\u60c5\u79bb\u5f00\u4e86\r\n[01:54.02]\u6211\u77e5\u9053\u4f60\u7684\u5fc3\u60c5\r\n[02:00.71]\u4e45\u4e45\u4e0d\u80fd\u5e73\u9759\r\n[02:03.17]\u6211\u5931\u843d\u7684\u5fc3\u60c5\r\n[02:05.57]\u5982\u679c\u4f60\u8981\u56de\u5230\r\n[02:09.24]\u4ed6\u7684\u8eab\u8fb9\r\n[02:12.20]\u4e00\u5b9a\u8981\u8fc7\u597d\u6bcf\u5929\r\n[02:18.79]\u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11\r\n[02:23.59]\u4f60\u7684\u7f8e\u7ec8\u4e8e\u4e0d\u5728\u6211\u6000\u62b1\r\n[02:28.29]\u539f\u6765\u6211\u7231\u4f60\u65e0\u53ef\u6551\u836f\r\n[02:33.16]\u6211\u7684\u611f\u60c5\u6700\u540e\u4f60\u8fd8\u6ca1\u8981\r\n[02:37.26]\u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11\r\n[02:41.75]\u4f60\u7684\u7f8e\u7ec8\u4e8e\u4e0d\u5728\u6211\u6000\u62b1\r\n[02:46.55]\u5982\u679c\u4f60\u80fd\u5e78\u798f\u6bcf\u5929\r\n[02:51.20]\u6211\u5b64\u72ec\u4e5f\u503c\u5f97\u9a84\u50b2\r\n[02:56.26]\u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11\r\n[02:59.98]\u4f60\u7684\u7f8e\u7ec8\u4e8e\u4e0d\u5728\u6211\u6000\u62b1\r\n[03:04.83]\u539f\u6765\u6211\u7231\u4f60\u65e0\u53ef\u6551\u836f\r\n[03:09.61]\u6211\u7684\u611f\u60c5\u6700\u540e\u4f60\u8fd8\u6ca1\u8981\r\n[03:13.79]\u6211\u7684\u773c\u6cea\u77e5\u9053\u4f60\u7684\u7b11\r\n[03:18.27]\u4f60\u7684\u7f8e\u7ec8\u4e8e\u4e0d\u5728\u6211\u6000\u62b1\r\n[03:23.11]\u5982\u679c\u4f60\u80fd\u5e78\u798f\u6bcf\u5929\r\n[03:27.75]\u6211\u5b64\u72ec\u4e5f\u503c\u5f97\u9a84\u50b2\r\n","author_id":"88936","privilege":8,"privilege2":"1000","play_url":"http:\/\/fs.w.kugou.com\/201901311504\/20b41e3446ddf4c7a79ce7d5fc0be8e7\/G127\/M04\/13\/11\/X5QEAFxK0WuAfzHNADoOYf5iDrg521.mp3","authors":[{"author_id":"88936","sizable_avatar":"http:\/\/singerimg.kugou.com\/uploadpic\/softhead\/{size}\/20160722\/20160722185354390495.jpg","is_publish":"1","author_name":"\u6d1b\u5929\u4f9d","avatar":"http:\/\/singerimg.kugou.com\/uploadpic\/softhead\/400\/20160722\/20160722185354390495.jpg"}],"bitrate":128}});
# 搜索歌曲
# https://songsearch.kugou.com/song_search_v2?callback=jQuery112407406372213107064_1548920473506&keyword=%E4%B8%80%E8%B7%AF%E4%B9%8B%E4%B8%8B&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1548920473508


# 获取下载地址
load_down_url = 'https://www.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19106737800324233885_${times}&hash=${hash}&album_id=${id}&_=${times}'

save_path = 'music/'

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9",
           "Upgrade-Insecure-Requests": "1",
           "cookie": "kg_mid=646acf1b184ebb702871180da62a9acd; ",
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


class Kg_music_down:

    def __init__(self):

        pass

    def load_music(self, url):
        request = requests.request("GET", url)
        pq = PyQuery(request.text)
        request.close()
        script_arr = pq("script")
        for script in script_arr:
            if pq(script).text().find("global.features") > 0:
                song_arr_text = pq(script).text()
                print(song_arr_text)
                line = song_arr_text[song_arr_text.find('global.features'):song_arr_text.find('; (function()')]
                if line.find("Hash") > 0:
                    print(line)
                    # print(line[line.find('['):])
                    json_arr = json.loads(line[line.find('['):])
                    return json_arr

    def load_down_music(self, music, rank_title):
        # print(music)
        times = int(time.time() * 1000)
        load_down_url_now = load_down_url.replace("${times}", str(times))
        load_down_url_now = load_down_url_now.replace("${hash}", music['Hash'])
        load_down_url_now = load_down_url_now.replace("${id}", str(music['album_id']))
        # print(load_down_url_now)

        request = requests.get(load_down_url_now, headers=headers, timeout=60)
        # request = requests.request("GET", load_down_url_now, headers=headers)
        result_content = request.text
        # print(result_content)
        request.close()
        music_json = json.loads(result_content[result_content.find("{"):result_content.find(");")])
        # print(music_json['data']['song_name'])
        # print(music_json['data']['lyrics'])
        # print(music_json['data']['play_url'])
        audio_name = music_json['data']['audio_name']
        song_name = music_json['data']['song_name']
        down_url = music_json['data']['play_url']
        if down_url == "":
            print("歌曲下载路劲不存在：" + audio_name)
            return
        lrc = music_json['data']['lyrics']
        path = save_path+rank_title+"/"
        make_save_path(path)
        if not os.path.exists(path + song_name + ".mp3"):
            self.save_music(song_name + ".mp3", down_url, path)
        else:
            print("已存在" + song_name + ".mp3")

        if not os.path.exists(path + song_name + ".lrc"):
            self.save_lyrics(song_name + ".lrc", lrc, path)
        else:
            print("已存在" + song_name + ".lrc")

    def save_music(self, fileName, down_url, path):
        count = 0
        while count < 3:

            # time.sleep(3)
            try:
                r = requests.get(down_url, headers=headers, stream=True, timeout=60)
                # print(r.status_code)
                if (r.status_code == 200):
                    with open(path + fileName, "wb+") as f:
                        for chunk in r.iter_content(1024):
                            f.write(chunk)
                    print("完成下载：" + fileName)
                    break
            except Exception as e:
                print(e)
                print("下载出错：" + fileName + "，3秒后重试")
                if os.path.exists(path + fileName):
                    os.remove(path + fileName)

                time.sleep(3)
            count += 1
        pass

    def save_lyrics(self, fileName, lrc, path):
        try:
            with open(path + fileName, "wb+") as f:
                f.write(lrc.encode(encoding='UTF-8', errors='strict'))
        except Exception as e:
            pass

    def load_top_url(self, url):

        r = requests.get(url, headers=headers, stream=True, timeout=60)
        pq = PyQuery(r.text)
        r.close()
        li_arr = pq(".pc_temp_side li")
        # print(li_arr.length)
        arr_url = []
        for i in range(0, li_arr.length):
            rank ={}
            rank['url'] = pq(li_arr[i]).find('a').attr('href')
            rank['title'] = pq(li_arr[i]).find('a').attr('title')
            arr_url.append(rank)

        return arr_url

    def load_page_url(self, page, page_url):
        urls_end = page_url[page_url.find("-"):]
        urls_start = page_url[:page_url.rfind("/") + 1]
        return urls_start + str(page) + urls_end


def make_save_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':

    make_save_path(save_path)

    kg_music_down = Kg_music_down()

    top_path = 'https://www.kugou.com/yy/html/rank.html'
    pathArr = kg_music_down.load_top_url(top_path)

    for rank in pathArr:

        for i in range(100):
            music_url = kg_music_down.load_page_url(i + 1, rank["url"])
            print(music_url)
            jsonArr = kg_music_down.load_music(music_url)
            if jsonArr:
                for music in jsonArr:
                    kg_music_down.load_down_music(music, rank["title"])
                    # break
            else:
                break
