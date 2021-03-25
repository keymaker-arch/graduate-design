import requests
import re
import time


def retrieve_BioPepDB(query_para, page_start, page_end, store_path):
    url = 'http://bis.zju.edu.cn/biopepdbr/include/get_list.php'
    info_url = 'http://bis.zju.edu.cn/biopepdbr/'
    header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.183 Safari/537.36',
            'Referer': 'http://bis.zju.edu.cn/biopepdbr/index.php?p=search&field=category&query=' + query_para,
            'Host': 'bis.zju.edu.cn', 'Origin': 'http://bis.zju.edu.cn'}
    post_data = {'field': 'category', 'query': query_para, 'order': 'pepid', 'desc': 'n', 'stp': 0}
    fp = open(store_path, 'w')
    count = 0
    missed_page = []
    missed_pep = []
    for i in range(page_start, page_end):
        print('\nretrieving page: ' + str(i+1))
        post_data['stp'] = 20 * i
        try:
            res = requests.post(url, data=post_data, headers=header, timeout=5)
        except requests.exceptions.RequestException as e:
            print(e)
            missed_page.append(i)
            pass
        href_tag_list = re.findall('<td.*?Go.*?</td>', res.text)
        href_list = []
        for href in href_tag_list:
            match = re.search('href="(.*?)"', href)
            if match:
                href_list.append(match.group(1))

        for href in href_list:
            _url = info_url + href
            try:
                res = requests.get(_url, timeout=5)
            except requests.exceptions.RequestException as e:
                print(e)
                missed_pep.append((i+1, href_list.index(href), href))
                pass
            match = re.search('Sequence</td><td>(.*?)</td>', res.text)
            if match:
                tmp = match.group(1).replace('<br/>', '')
                print(tmp)
                fp.write(tmp)
                fp.write('\n')
                count += 1
            time.sleep(0.1)
        time.sleep(0.1)
    fp.close()
    if missed_page:
        print('pep in following pages missed:')
        print(missed_page)
    if missed_pep:
        print('following peptides missed(page, index, url):')
        for pep in missed_pep:
            print(pep)
    print('\n\ntotal retrieve: ' + str(count))


if __name__ == '__main__':
    # retrieve_BioPepDB('antihypertensive', 0, 83, '/home/han/antihypertensive_1653')
    retrieve_BioPepDB('antimicrobial', 0, 123, '/home/han/antimicrobial_2455')
