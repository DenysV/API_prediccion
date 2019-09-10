from datetime import datetime
from datetime import timedelta
from calendar import monthrange
import re

def check_data(data):
    valid = False
    pattern = '([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'
    if re.findall(pattern, data):
        date_list = [int(el) for el in data.split('-')]
        valid = True if (date_list[-1] <= monthrange(date_list[0], date_list[1])[1]) else False
    return valid

def prediccion(fecha):
    if check_data(fecha):
        res = []
        for i in range(1, 11):
            res.append({"fecha": (datetime.strptime(fecha, '%Y-%m-%d') + timedelta(i)).strftime('%Y-%m-%d'), "Tmax":22.5})
    else:
        res = 'Fecha invalida!'
    return res

#print(prediccion('2019-09-26'))