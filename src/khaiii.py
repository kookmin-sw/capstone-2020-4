
from khaiii import KhaiiiApi

api = KhaiiiApi("", "")

for word in api.analyze('안녕, 세상.'):
    print(word)
