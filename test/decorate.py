import time
import json

def get_time(func):
    def wrapper(soup):
        start = time.time()
        result = func(soup)
        use_time = int(time.time() - start)
        print("This function \'{}\', use time {} ".format(func.__name__, use_time))
        return result
    return wrapper


@get_time
def get_plcontent(soup):
    temp_1 = soup.find_all("div", class_="xeditor_content")[0].string
    temp_2 = soup.find_all("div", class_="stockcodec .xeditor")[0].string
    if temp_1:
        cap = temp_1
    else:
        cap = temp_2
    all_pinglun = [cap]
    for line in soup.find_all('div', attrs={'class': "short_text"}):
        pl = line.string.strip()
        all_pinglun.append(pl)
    return all_pinglun


@get_time
def get_infos(soup):
    infos = []
    for line in soup.find_all('div', attrs={'class': "data"}):
        info = json.loads(line['data-json'])
        infos.append(info)
    return infos


@get_time
def get_timelist(soup):
    bz_time = soup.find_all("div", class_="zwfbtime")[0].string.split(' ', 1)[1].rsplit(' ', 1)[0]
    time_list = [bz_time]
    for line in soup.find_all("div", class_="zwlitime"):
        time_list.append(line.string.split(' ', 1)[1])
    return time_list


if __name__ == "__main__":
    soup = None
    all_p = get_plcontent(soup)
    infos = get_infos(soup)