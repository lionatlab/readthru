from openpyxl import load_workbook
import datetime

path = 'C:/Users/CMES/PycharmProjects/readthru/server/bible.xlsx'
load_wb = load_workbook(path, data_only = True)

load_ws = load_wb['Sheet1']
load_date = load_wb['Date']
def Read_Part(month, date):
    BibleList = list()
    for r in load_date.rows:
        if(r[0].value == month and r[1].value == date):
            ChapList = r[3].value.split(',')
            for c in ChapList:
                BibleList.append([r[2].value, str(c)])
    return BibleList
def Read_Chapter(name, chapter):
    script = name + ' ' + str(chapter) + '\n'
    for r in load_ws.rows:
        bible = r[0].value
        chap = r[1].value
        if bible == name and chap == chapter:
            verse = str(r[2].value) + '. ' + r[3].value
            script = script + verse + '\n'
    script = script + '\n'
    return script

def Send_Bible(BibleList):
    dt = datetime.datetime.now()
    date = dt.strftime("%Y.%m.%d\n")
    whole_bible = date
    for b,c in BibleList:
        whole_bible = whole_bible + Read_Chapter(b,int(c))
    #print(whole_bible)
    return whole_bible





