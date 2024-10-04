from django.http import HttpResponseNotFound
from django.shortcuts import render

import random

def roll_d4():
    return str(random.randint(1, 4))

def roll_d6():
    return str(random.randint(1, 6))

def roll_d8():
    return str(random.randint(1, 8))

def roll_d10():
    return str(random.randint(1, 10))

def roll_d12():
    return str(random.randint(1, 12))

def roll_d20():
    return str(random.randint(1, 20))

# Create your views here.

type_of_dices = {
    'd4': 'Каждая грань имеет три числа, расположенных таким образом, что вертикальное число, расположенное либо около вершины, либо около противоположного края, одинаково на всех трех видимых гранях. Вертикальные числа представляют собой значение броска. Эта кость плохо катится, и поэтому ее обычно подбрасывают в воздух.',
    'd6': 'Обычная игральная кость. Сумма чисел на противоположных гранях равна 7.',
    'd8': 'Каждая грань треугольная, а игральная кость напоминает две квадратные пирамиды, соединенные основанием к основанию. Обычно сумма противоположных граней равна 9.',
    'd10': 'Каждая грань — воздушный змей. У игральной кости два острых угла, где сходятся пять воздушных змеев, и десять тупых углов, где сходятся три воздушных змея. Десять граней обычно имеют числа от нуля до девяти, а не от одного до десяти (ноль читается как «десять» во многих приложениях). Часто все нечетные грани сходятся в одном остром углу, а четные — в другом. Сумма чисел на противоположных гранях обычно равна 9 (если пронумерованы от 0 до 9) или 11 (если пронумерованы от 1 до 10).',
    'd12': 'Каждая грань — правильный пятиугольник. Сумма чисел на противоположных гранях обычно равна 13.',
    'd20': 'Грани представляют собой равносторонние треугольники. Икосаэдры были найдены во времена Римской империи/Птолемеев, но неизвестно, использовались ли они в качестве игральных костей. Современные кости с 20 гранями иногда пронумерованы дважды от 0 до 9 в качестве альтернативы 10-гранным костям. Сумма чисел на противоположных гранях равна 21, если пронумерованы от 1 до 20.',
}


def get_main_page(request):
    data = {
        'dices': type_of_dices.keys(),
    }

    return render(request, 'dice/main_page.html', context=data)


def get_info_dice(request, dice_n):
    if dice_n == 'd4':
        result = roll_d4()
    elif dice_n == 'd6':
        result = roll_d6()
    elif dice_n == 'd8':
        result = roll_d8()
    elif dice_n == 'd10':
        result = roll_d10()
    elif dice_n == 'd12':
        result = roll_d12()
    elif dice_n == 'd20':
        result = roll_d20()
    else:
        result = "lmao what"

    if dice_n in type_of_dices.keys():
        data = {
            'dice_name': dice_n,
            'info_about_dice': type_of_dices.get(dice_n),
            'result': result,
            'dices': type_of_dices.keys(),
        }
        return render(request, 'dice/dice_info.html', context=data)
    else:
        return HttpResponseNotFound(f"Увы кубик {dice_n} не найден ;(")

