from openpyxl import load_workbook


# 통독일정 엑셀시트 로딩 / 리스트 저장
def load_schedule(load_wb):
    wsReading = load_wb['reading']
    reading_list = list()

    for row in wsReading:
        data = dict()
        data['month'] = row[0].value
        data['day'] = row[1].value
        data['books'] = row[2].value
        reading_list.append(data)
    return reading_list


# 통독일정 검색
def today_schedule(reading_list, month, day):
    for data in readingList:
        if data['month'] == month and data['day'] == day:
            today_schedule = data['books']

    return today_schedule


# 엑셀파일 불러오기 / 통독일정 엑셀시트 로딩 / 리스트 저장
load_wb = load_workbook("./bible.xlsx", data_only=True)
readingList = load_schedule(load_wb)

# 통독일정 검색
month = 12
day = 30
today_schedule = today_schedule(reading_list, month, day)

print(today_schedule)
