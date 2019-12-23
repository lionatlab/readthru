from openpyxl import load_workbook
import datetime
import json
import re
from collections import defaultdict

def read_json(path_json):
    with open(path_json, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    return json_data

def get_chapters(chaps):
    chapList = list()
    totalList = list()
    if chaps.find(',') != -1:
        chapList=chaps.split(',')
    else:
        chapList.append(chaps)

    for ch in chapList:
        totalList.extend(job_split(ch))
    return totalList

def job_split(chaps):
    chapList = list()
    chaps = chaps.split(' ')
    if chaps[1].find('-') != -1:
        tmp = chaps[1].split('-')
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
        for i in range(tmp[0], tmp[1]+1):
            chapList.append(chaps[0] + ' ' + str(i))
    else:
        chapList.append(chaps[0] + ' ' + chaps[1])
    return chapList

def jsonMaker(path):
    load_wb = load_workbook(path + 'bible.xlsx', data_only=True)
    exBible = load_wb['Sheet1']
    exDate = load_wb['Date']
    dateList = list()
    bibleList = list()
    for r in exDate:
        data = dict()
        data['month'] = r[0].value
        data['date'] = r[1].value
        data['books'] = r[2].value
        dateList.append(data)
    for r in exBible:
        data = dict()
        data['book'] = r[0].value
        data['chap'] = r[1].value
        data['verse'] = r[2].value
        data['script'] = r[3].value
        bibleList.append(data)
    with open(path + 'bible.json', 'w', encoding='utf-8') as make_file:
        json.dump(bibleList, make_file, ensure_ascii=False, indent='\t')
    with open(path + 'date.json', 'w', encoding='utf-8') as make_file:
        json.dump(dateList, make_file, ensure_ascii=False, indent='\t')
    return bibleList, dateList

def get_chap(bible, name, chap):
    verseList = list()
    for dic in bible:
        if dic['book'] == name and dic['chap'] == chap:
            data = dict()
            data['idx'] = dic['verse']
            data['content'] = dic['script']
            verseList.append(data)
    return verseList

def get_chapterBYdate(date, mm, dd):
    for day in date:
        if day['month'] == mm and day['date'] == dd:
            return day['books']
    return False

def get_contents(bible, book, chap):
    data = dict()
    chapContent = get_chap(bible, book, chap)
    data['chapter_name'] = '{} {}장'.format(book, chap)
    data['verse_num'] = len(chapContent)
    data['verse'] = chapContent
    return data

def get_oneday(bible, date, mm, dd):
    data = dict()
    data['date'] = '{}월 {}일'.format(mm,dd)
    chaps = get_chapterBYdate(date, mm, dd)
    data['chapter'] = chaps
    chaps = get_chapters(chaps)
    data['chapter_num'] = len(chaps)
    contList = list()
    for chap in chaps:
        chap = chap.split(' ')
        book = chap[0]
        chapter = chap[1]
        print('book : {} chapter : {}'.format(book,chapter))
        contList.append(get_contents(bible, book, int(chapter)))
    data['contents'] = contList
    return data

def get_totalday(bible, date):
    data = dict()
    for day in date:
        strkey = 'm{}d{}'.format(day['month'],day['date'])
        data[strkey] = get_oneday(bible,date, int(day['month']),int(day['date']))
        print(strkey)
    return data

def main():
    path = 'C:/Users/CMES/PycharmProjects/readthru/server/'
    jsonMaker(path)
    bible = read_json(path + "bible.json")
    date = read_json(path + "date.json")
    final = get_totalday(bible, date)
    with open(path + 'final.json', 'w', encoding='utf-8') as make_file:
        json.dump(final, make_file, ensure_ascii=False, indent='\t')

if __name__ == "__main__":
    main()

