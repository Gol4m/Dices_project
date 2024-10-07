from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
import json
import random

# Create your views here.

def roll_dice(dice: str):
    highest_number = int(dice.replace('d', ''))
    return str(random.randint(1, highest_number))


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

    if dice_n in type_of_dices.keys():
        data = {
            'dice_name': dice_n,
            'info_about_dice': type_of_dices.get(dice_n),
            'roll_result': roll_dice(dice_n),
            'dices': type_of_dices.keys(),
        }
        return render(request, 'dice/dice_info.html', context=data)
    else:
        return HttpResponseNotFound(f"Увы кубик {dice_n} не найден ;(")


def get_multi_throw(request):
    data = {
        'dices': type_of_dices.keys(),
    }
    return render(request, 'dice/multi_throw.html', context=data)


# Функция для обработки мульти-броска кубиков
def roll_multi_dice(request):
    if request.method == 'POST':
        # Получение данных из запроса в формате JSON
        try:
            body = json.loads(request.body)  # Загружаем JSON из тела запроса
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Некорректный формат JSON'}, status=400)

        dices = body.get('dices', [])

        total_result = 0
        dice_rolls = []

        for dice in dices:
            if dice in type_of_dices.keys():
                result = roll_dice(dice)
                total_result += int(result)
                dice_rolls.append({'dice': dice, 'result': result})

        return JsonResponse({
            'total_result': total_result,
            'dice_rolls': dice_rolls
        })
    else:
        return JsonResponse({'error': 'Некорректный запрос'}, status=400)


def roll_dice_ajax(request, dice_n):
    if dice_n in type_of_dices.keys():
        roll_result = roll_dice(dice_n)
        return JsonResponse({'roll_result': roll_result})
    else:
        return JsonResponse({'error': f'Увы кубик {dice_n} не найден ;('}, status=404)

