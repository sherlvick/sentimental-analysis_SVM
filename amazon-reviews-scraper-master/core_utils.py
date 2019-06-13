import errno
import time
from time import sleep
import json
import logging
import os
import re
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from banned_exception import BannedException
from constants import AMAZON_BASE_URL
import pandas

OUTPUT_DIR = 'comments'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def get_reviews_filename(product_id):
    filename = os.path.join(OUTPUT_DIR, '{}.csv'.format(product_id))
    exist = os.path.isfile(filename)
    return filename, exist


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def persist_comment_to_disk(reviews):
    if len(reviews) == 0:
        return False
    product_id_set = set([r['product_id'] for r in reviews])
    assert len(product_id_set) == 1, 'all product ids should be the same in the reviews list.'
    product_id = next(iter(product_id_set))
    output_filename, exist = get_reviews_filename(product_id)
    if exist:
        print("File with same pid is there...")
        return False
    mkdir_p(OUTPUT_DIR)
    # https://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence/18337754
    with open(output_filename, 'w', encoding='utf-8') as fp:
        json.dump(reviews, fp, sort_keys=True, indent=4, ensure_ascii=False)

    pandas.read_json(output_filename).to_csv(output_filename)
    #return True
    return output_filename


def extract_product_id(link_from_main_page):
    # e.g. B01H8A7Q42
    p_id = -1
    tags = ['/dp/', '/gp/product/']
    for tag in tags:
        try:
            p_id = link_from_main_page[link_from_main_page.index(tag) + len(tag):].split('/')[0]
        except:
            pass
    m = re.match('[A-Z0-9]{10}', p_id)
    if m:
        return m.group()
    else:
        return None


'''
from lxml.html import fromstring
from itertools import cycle
import traceback

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxie = list()
    for i in parser.xpath('//tbody/tr')[:100]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxie.append(proxy)
    return proxie


#If you are copy pasting proxy ips, put in the list below
#proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
proxie = get_proxies()
print(proxie)
#proxy_pool = cycle(proxies)


class myclass:
    c = 7
'''
driver = webdriver.Chrome('D:/chromedriver')

def get_soup(url):
    if AMAZON_BASE_URL not in url:
        url = AMAZON_BASE_URL + url
    #nap_time_sec = 1
    #logging.debug('Script is going to sleep for {} (Amazon throttling). ZZZzzzZZZzz.'.format(nap_time_sec))
    #sleep(nap_time_sec)
    #url = "www.google.com"
    driver.get('https://www.proxysite.com/')
    url_input_box = driver.find_element_by_name('d')
    url_input_box.send_keys(url)
    #time.sleep(10)
    #go_submit_button = driver.find_element_by_xpath('//*[@id="url-form-wrap"]/form/div[2]/button').click()
    try:
        go_submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="url-form-wrap"]/form/div[2]/button')))
        time.sleep(1)
        go_submit_button.click()
        print("YOU link found and returned")
    except TimeoutException:
        print("YOU link not found ... breaking out")
    
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    return soup


'''
def get_soup(url):
    if AMAZON_BASE_URL not in url:
        url = AMAZON_BASE_URL + url
    nap_time_sec = 1
    logging.debug('Script is going to sleep for {} (Amazon throttling). ZZZzzzZZZzz.'.format(nap_time_sec))
    sleep(nap_time_sec)
    #header = requests.utils.default_headers()
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'
    }
    logging.debug('-> to Amazon : {}'.format(url))
    # Get a proxy from the pool
    #proxy = next(proxy_pool)
    m = myclass()
    m.c += 1
    proxy = proxie[m.c]
    print(proxy)
    #proxy = next(i)
    try:
        print('\na')
        sleep(2)
        out = requests.get(url, headers=header ,proxies={'https': 'http://213.32.5.165:443' ,'http': 'http://213.32.5.165:443'})
        assert out.status_code == 200
        soup = BeautifulSoup(out.content, 'lxml')
        if 'captcha' in str(soup):
            raise BannedException('Your bot has been detected. Please wait a while.')
        return soup

    except requests.exceptions.ConnectionError as error:
        print(error)

        
    except BaseException as error:
        print(error)
        # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
        # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
        print("Skipping. Connnection error")
'''
