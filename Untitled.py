import urllib
import re
f = urllib.urlopen("https://www.life-moon.pp.ru")
c = int(re.findall('<a href="/moon-days/9/">(\d+) лунного дня</a>', f.read())[0])
print c
while True:
    a = input("Какой лунный день ? 0 - автоматически: ")
    if a == 0:
        a = c
    if a>0 and a<29:
        if a >16:
            a = 29 - a
        b = ((a-1) * 50) / 15
        print "Очень примерное расстояние от земли до луны: "+ str(356 + b) + ".000 тысяч км"
    else:
        print "не правильно"
