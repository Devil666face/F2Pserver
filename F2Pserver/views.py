from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import pytz

#http://127.0.0.1:8000/?bus=204&busName=&number=0+790+%D0%99%D0%AE&time=10:11,+13.04.2022&startStation=1-%D0%B0%D1%8F+%D0%BC%D0%B5%D0%B4%D1%81%D0%B0%D0%BD%D1%87%D0%B0%D1%81%D1%82%D1%8C&stopStation=%D0%92%D0%B0%D0%B3%D0%BE%D0%BD%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B7%D0%B0%D0%B2%D0%BE%D0%B4
def about(request):
    return HttpResponse('<h1>Сервер отображения qr кодов. (c)King Midas<h1>')

def answer(request):
    bus = request.GET['bus']
    bus_name = request.GET['busName']
    number = request.GET['number']
    time = request.GET['time']
    start_station = request.GET['startStation']
    stop_station = request.GET['stopStation']

    print(time.split(',')[0])
    minuts_ago = f'{get_time_ago(time.split(",")[0])} минут назад'
    return render(request, 'index.html', {'bus': bus,
                                          'bus_name': bus_name,
                                          'number': number,
                                          'minuts_ago':minuts_ago,
                                          'time':time,
                                          'start_station':start_station,
                                          'stop_station':stop_station})
def get_time_ago(now_time_str):
    tz = pytz.timezone('Europe/Moscow')
    cur_hour = datetime.now(tz).hour
    cur_min = datetime.now(tz).minute
    print(f'сейчас {cur_hour}:{cur_min}')
    return -(int(now_time_str.split(':')[0])*60+int(now_time_str.split(':')[1])-cur_hour*60-cur_min)