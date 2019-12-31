from openpyxl import load_workbook


# 통독일정 엑셀시트 로딩 / 리스트 저장
def load_schedule(load_wb):
    wsReading = load_wb['reading']
    readingList = list()

    for row in wsReading:
        data = dict()
        data['month'] = row[0].value
        data['day'] = row[1].value
        data['books'] = row[2].value
        readingList.append(data)

    return readingList

# 통독일정 검
def today_schedule(readingList, month, day):
    for data in readingList:
        if data['month'] == month and data['day'] == day:
            todaySchedule = data['books']

    return todaySchedule


# 엑셀파일 불러오기
load_wb = load_workbook("./bible.xlsx", data_only=True)

# 통독일정 엑셀시트 로딩 / 리스트 저장 / 통독일정 검색
month = 12
day = 31
readingList = load_schedule(load_wb)
todaySchedule = today_schedule(readingList, month, day)

print(todaySchedule)
