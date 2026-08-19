import random
CARDS = {
    "1": {
        "name": "Обычный котозаец",
        "description": "Котозаяц сидящий на полке",
        "rarity": "Обычная",
        "image": "images/1.jpg",
        "points": 100,
        "coins": 5500
    },
    "2": {
        "name": "Плачющий котозаец",
        "description": "Плачющий котозаяц.",
        "rarity": "Обычная",
        "image": "images/2.jpg",
        "points": 150,
        "coins": 7700
    },
    "3": {
        "name": "Котозаец-ниндзя",
        "description": "Исчезает ночью и ворует подарки. Никто его никогда не найдет.",
        "rarity": "Редкая",
        "image": "images/3.jpg",
        "points": 500,
        "coins": 10000
    },
    "4": {
        "name": "жирный-котозаец",
        "description": "Много поел",
        "rarity": "Обычная",
        "image": "images/4.jpg",
        "points": 100,
        "coins": 5500
    },
    "5": {
        "name": "Котояцесть",
        "description": "Стримит с бурмалдой",
        "rarity": "Мифическая",
        "image": "images/5.jpg",
        "points": 2000,
        "coins": 20000
    },
	"6": {
        "name": "Тцк котозаяц",
        "description": "Военный котозаяц смотрит телевизор",
        "rarity": "Мифическая",
        "image": "images/6.jpg",
        "points": 2000,
        "coins": 26000
    },
	"7": {
        "name": "Военный котозаяц любит масу чью то",
        "description": "Военный котозаяц",
        "rarity": "Мифическая",
        "image": "images/7.jpg",
        "points": 2000,
        "coins": 20000
    },
    "8": {
        "name": "Котозаяц с своим ребенком",
        "description": "Сыр у котазайца",
        "rarity": "Обычная",
        "image": "images/8.jpg",
        "points": 100,
        "coins": 5000
    },
    "9": {
        "name": "За столом",
        "description": "За столом с друном",
        "rarity": "Редкая",
        "image": "images/9.jpg",
        "points": 500,
        "coins": 10000
    },
    "10": {
        "name": "Котозаяц с девушкой",
        "description": "Котозаяц больше не гэй",
        "rarity": "Обычная",
        "image": "images/10.jpg",
        "points": 500,
        "coins": 10000
    },
    "11": {
        "name": "Дент рождения у котозайца",
        "description": "Др у котозайца",
        "rarity": "Обычная",
        "image": "images/5.jpg",
        "points": 500,
        "coins": 20000
    },
}
RARITY_WEIGHTS = {
    "Обычная": 60,
    "Редкая": 25,
    "Эпическая": 10,
    "Мифическая": 5
}

def get_random_card():
    rarities = list(RARITY_WEIGHTS.keys())
    weights = list(RARITY_WEIGHTS.values())
    chosen_rarity = random.choices(rarities, weights=weights, k=1)[0]
    possible_cards = {k: v for k, v in CARDS.items() if v["rarity"] == chosen_rarity}
    if not possible_cards:
        possible_cards = {k: v for k, v in CARDS.items() if v["rarity"] == "Обычная"}
    card_id = random.choice(list(possible_cards.keys()))
    
    return card_id, possible_cards[card_id]

