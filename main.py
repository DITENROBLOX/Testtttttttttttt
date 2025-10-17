meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ТРЭШ": "ложная, фиговая информация",
            "DITEN": "сАмОе ВрЕмЯ пОдПиСаТсЯ нА кАнАл: https://www.youtube.com/channel/UCmsA6EruUyu0qLWDEXGFxCQ/",
            "KODLAND": "Вы только что получили скидку 15%!",
            "RIDEACTION": "Вы получили скидку 20% на все товары в магазине RideAction!!!"
            }
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
        print(meme_dict[word])
else:
        print('TAKOГO CЛOBA HET')
