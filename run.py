if __name__ == "__main__":
    try:
        tickets = int(input('Введите количество билетов: '))
        if tickets > 20:
            raise RuntimeError('Не больше 20 билетов за один заказ')
        ages = [int(input('Введите возраст: ')) for t in range(tickets)]
        result = []
        for a in ages:
            if a in range(19):
                result.append(0)
            elif a in range(19, 26):
                result.append(990)
            elif a <= 120:
                result.append(1390)
            else:
                raise RuntimeError('Люди пока что столько не живут')
        price = sum(result)
        if tickets > 3:
            print('Сумма к оплате: ', price*0.9)
            print('Сумма скидки: ', price*0.1)
        else:
            print('Сумма к оплате: ', price)
    except ValueError:
        print('Возникла ошибка: количество билетов и возраст нужно указывать числом')
    except RuntimeError as e:
        print('Возникла ошибка: ', e)