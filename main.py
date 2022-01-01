import csv


def main():
    with open('data.csv') as f:
        reader = list(csv.DictReader(f))
    items = list(map(item_price_to_int, reader))
    items = sorted(items, key=lambda x: x['price'], reverse=True)
    point = 0
    payment = 0
    for item in items:
        price = item['price']
        got_point = round(price/2.2)
        if item['novel'] == 'o':
            got_point = round(price*0.3/1.1)
        if point >= price:
            point = got_point - price
        else:
            payment += price - point
            point = got_point
        print(f'{item["title"]}({price}円)を購入,{got_point}ポイントを獲得')

    print(f'合計金額: {payment}, 残りポイント: {point}')


def item_price_to_int(x: dict):
    x['price'] = int(x['price'])
    return x


if __name__ == '__main__':
    main()
