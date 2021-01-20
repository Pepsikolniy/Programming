import openpyxl
import datetime
import json
import os.path
from flask import Flask, request

def writeexel():
    global line, buffer
    book = openpyxl.load_workbook('data.xlsx')
    sheet= book.active
    for items in buffer:
        for i in range(5):
            sheet.cell(line,i+1).value = items[i]
        line+=1
    sheet.cell(1,6).value = line-1
    book.save('data.xlsx')
    book.close
    buffer.clear()
    
app = Flask(__name__)   
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        time = datetime.datetime.now().time()
        json_from_post= request.get_json()
        global number, buffer
        for item in json_from_post['cart']:
            buy = [number, json_from_post['user_id'], time, item['item'], item['price']]
            number += 1  
            buffer.append(buy)
        if len(buffer)>5:
            writeexel()
        return 'OK'
    return "Vse rabotayet"
    
if __name__ == "__main__":
    global number, buffer, line
    number = 1
    line = 2
    buffer = []
    if not(os.path.exists('data.xlsx')):    
        book = openpyxl.Workbook()
        sheet = book.active
        sheet.cell(1,1).value = 'N'
        sheet.cell(1,2).value = 'User ID'
        sheet.cell(1,3).value = 'Datetime'
        sheet.cell(1,4).value = 'Item'
        sheet.cell(1,5).value = 'Price'
        sheet.cell(1,6).value = 1
        book.save('data.xlsx')
        book.close
    else:
        book = openpyxl.load_workbook('data.xlsx')
        sheet = book.active
        number = sheet.cell(1,6).value
        book.close
    app.run()
