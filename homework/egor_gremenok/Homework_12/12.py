class Flower:
    def __init__(self, name, color, freshness, stem_length, cost, lifespan):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.cost = cost
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifespan):
        super().__init__("Роза", color, freshness, stem_length, cost, lifespan)


class Tulip(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifespan):
        super().__init__("Тюльпан", color, freshness, stem_length, cost, lifespan)


class Daisy(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifespan):
        super().__init__("Ромашка", color, freshness, stem_length, cost, lifespan)


class Lilac(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifespan):
        super().__init__("Сирень", color, freshness, stem_length, cost, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_cost(self):
        total = 0
        for flower in self.flowers:
            total += flower.cost
        return total

    def get_remaining_time(self):
        if not self.flowers:
            return 0
        total_lifespan = 0
        for flower in self.flowers:
            total_lifespan += flower.lifespan
        return total_lifespan / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda x: x.cost)

    def find_by_lifespan(self, min_lifespan, max_lifespan):
        result = []
        for flower in self.flowers:
            if min_lifespan <= flower.lifespan <= max_lifespan:
                result.append(flower)
        return result


rose1 = Rose("Красный", 1, 47, 2.2, 7)
rose2 = Rose("Белый", 4, 52, 4.50, 6)
tulip1 = Tulip("Желтый", 2, 34, 3, 5)
daisy1 = Daisy("Белый", 3, 22, 1.99, 4)
lilac1 = Lilac("Сиреневый", 6, 13, 4.79, 9)

bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(tulip1)
bouquet.add_flower(daisy1)
bouquet.add_flower(lilac1)

print("Стоимость букета:", bouquet.calculate_cost())
print("Среднее время жизни букета:", bouquet.get_remaining_time(), "дней")

bouquet.sort_by_freshness()
print("\nСортировка по свежести:")
for flower in bouquet.flowers:
    print(f"{flower.name}, Свежесть (в днях): {flower.freshness}")

bouquet.sort_by_color()
print("\nСортировка по цвету:")
for flower in bouquet.flowers:
    print(f"{flower.name}, Цвет: {flower.color}")

bouquet.sort_by_stem_length()
print("\nСортировка по длине стебля:")
for flower in bouquet.flowers:
    print(f"{flower.name}, Длина стебля: {flower.stem_length} см")

bouquet.sort_by_cost()
print("\nСортировка по стоимости:")
for flower in bouquet.flowers:
    print(f"{flower.name}, Цена: {flower.cost} руб")

found_flowers = bouquet.find_by_lifespan(5, 7)
print("\nЦветы с временем жизни от 5 до 7 дней:")
for flower in found_flowers:
    print(f"{flower.name}, Время жизни: {flower.lifespan} дней")
