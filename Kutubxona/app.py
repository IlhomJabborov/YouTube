import math

# f = math.factorial(10)
# print(f)
# ildiz_kv = math.sqrt(4)
# print(ildiz_kv)

from datetime import date

# d = date(2026,12,11)
# print(type(d))

# t = date.today()
# print(t.day)

from googletrans import Translator

translator = Translator()
matn = str(input("Matn kiriting: "))

natija = translator.translate(matn, dest="en",src="uz")
umumiy_matn = natija.text
print(umumiy_matn)