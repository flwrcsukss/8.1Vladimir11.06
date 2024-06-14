# class Vehicle:
#     forWheels = {2: 'мотоцикл', 3: 'трицикл', 4: 'автомобиль'}
#     def __init__(self, name, mileage):
#         self.__name = name
#         self.__mileage = mileage
#
#     def get_vehicle_type(self, numOfWheels):
#         if numOfWheels not in Vehicle.forWheels.keys():
#             return 'Я не знаю таких ТС'
#         else:
#             return f'Это {Vehicle.forWheels[numOfWheels]} марки {self.__name}'
#
#     def get_vehicle_advice(self):
#         if self.__mileage < 50001:
#             return f'Неплохо, {self.__name} можно брать.'
#         if 50000 < self.__mileage < 100001:
#             return f'{self.__name} надо внимательно проверить.'
#         if 100000 < self.__mileage < 150001:
#             return f'{self.__name} надо провести полную диагностику.'
#         if self.__mileage > 150000:
#             return f'{self.__name} лучше не покупать.'
#
# car_1 = Vehicle('BMW', 20000)
# car_2 = Vehicle('Audi', 60000)
# car_3 = Vehicle('Lada', 120000)
# car_4 = Vehicle('Lamborghini', 200000)
# print(car_1.get_vehicle_type(3))
# print(car_2.get_vehicle_type(2))
# print(car_3.get_vehicle_type(2))
# print(car_4.get_vehicle_type(4), end='\n\n')
#
# print(car_1.get_vehicle_advice())
# print(car_2.get_vehicle_advice())
# print(car_3.get_vehicle_advice())
# print(car_4.get_vehicle_advice())


class Dota:
    goldForPositions = ['', 600, 500, 475, 230, 230]
    levelForPositions = ['', 0.55, 0.6, 0.5, 0.45, 0.45]
    def __init__(self, hero, currentMinuteOfGame):
        self.__hero = hero
        # self.__totalGold = totalGold
        # self.__totalLevel = totalLevel
        self.__currentMinuteOfGame = currentMinuteOfGame

    def gold_per_minute(self, totalGold):
        return f'Герой {self.__hero} имеет {round(totalGold / self.__currentMinuteOfGame, 2)} золота в минуту'

    def level_per_minute(self, totalLevel):
        return f'Герой {self.__hero} имеет {round(totalLevel / self.__currentMinuteOfGame, 2)} прирост уровня в минуту'

    def good_farm_for_this_minute(self, position, totalGold, totalLevel):
        if not (0 < position < 6):
            return 'Я не знаю такой позиции.'
        if totalGold / self.__currentMinuteOfGame >= Dota.goldForPositions[position] and totalLevel / self.__currentMinuteOfGame >= Dota.levelForPositions[position]:
            return f'Герой {self.__hero} обладает отличным фармом на данной минуте игры.'
        if (totalGold / self.__currentMinuteOfGame >= Dota.goldForPositions[position]) + (totalLevel / self.__currentMinuteOfGame >= Dota.levelForPositions[position]) == 1:
            return f'Герой {self.__hero} обладает нормальным фармом на данной минуте игры.'
        if (totalGold / self.__currentMinuteOfGame >= Dota.goldForPositions[position]) + (totalLevel / self.__currentMinuteOfGame >= Dota.levelForPositions[position]) == 0:
            return f'Герой {self.__hero} обладает ужасным фармом на данной минуте игры.'

hero_1 = Dota('Antimage', 30)
hero_2 = Dota('Invoker', 30)
hero_3 = Dota('Axe', 30)
hero_4 = Dota('Rubick', 30)
hero_5 = Dota('Pudge', 30)
print(hero_1.gold_per_minute(12000))
print(hero_1.level_per_minute(12))
print(hero_1.good_farm_for_this_minute(1, 12000, 12), end='\n\n')

print(hero_2.gold_per_minute(17000))
print(hero_2.level_per_minute(16))
print(hero_2.good_farm_for_this_minute(2, 17000, 16), end='\n\n')

print(hero_3.gold_per_minute(7000))
print(hero_3.level_per_minute(12))
print(hero_3.good_farm_for_this_minute(3, 7000, 12), end='\n\n')

print(hero_4.gold_per_minute(7000))
print(hero_4.level_per_minute(12))
print(hero_4.good_farm_for_this_minute(4, 7000, 12), end='\n\n')

print(hero_5.gold_per_minute(8000))
print(hero_5.level_per_minute(14))
print(hero_5.good_farm_for_this_minute(5, 8000, 14), end='\n\n')

