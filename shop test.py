from flask import Flask

app = Flask(__name__)

# База данных магазина (вся информация о товарах в одном месте)
products = {
    'oil': {'name': 'Масло (oil)', 'price': 450, 'quantity': 7},
    'wheel': {'name': 'Колесо (wheel)', 'price': 7000, 'quantity': 2}
}


# 1. Главная страница сайта
@app.route('/')
def home():
    oil = products['oil']
    wheel = products['wheel']

    # Возвращаем красивую страницу сразу с синими кнопками для покупки
    return f"""
    <h1>Добро пожаловать в NetworkShop "MotoTyt"!</h1>
    <p><b>Доступные товары:</b></p>
    <ul>
        <li>
            {oil['name']} — Цена: {oil['price']} руб. (В наличии: {oil['quantity']} шт.) 
            — <a href="/buy/oil" style="padding: 3px 8px; background: #007bff; color: white; text-decoration: none; border-radius: 3px;">Купить 1 шт.</a>
        </li>
        <br>
        <li>
            {wheel['name']} — Цена: {wheel['price']} руб. (В наличии: {wheel['quantity']} шт.) 
            — <a href="/buy/wheel" style="padding: 3px 8px; background: #007bff; color: white; text-decoration: none; border-radius: 3px;">Купить 1 шт.</a>
        </li>
    </ul>
    <p style="color: gray; font-size: 14px;">Вы также можете делать ручные запросы в адресной строке: /buy/oil или /buy/wheel</p>
    """


# 2. Страница обработки покупки
@app.route('/buy/<item_name>')
def buy_item(item_name):
    # Говорим Python, что будем изменять наш глобальный словарь с товарами
    global products

    # Проверяем, есть ли вообще такой товар в магазине
    if item_name in products:
        item = products[item_name]

        # Проверяем склад ПЕРЕД покупкой, чтобы не уходить в минус
        if item['quantity'] > 0:
            item['quantity'] -= 1  # Списываем 1 штуку
            return f"""
            <h1>🤖 Успешная покупка!</h1>
            <p>Вы успешно приобрели: <b>{item['name']}</b> за {item['price']} руб.</p>
            <p>Остаток на складе: <b>{item['quantity']} шт.</b></p>
            <br>
            <a href='/' style="display: inline-block; padding: 5px 10px; background: #28a745; color: white; text-decoration: none; border-radius: 3px;">Вернуться в магазин</a>
            """
        else:
            return f"""
            <h1>❌ Ошибка списания</h1>
            <p>Извините, товар <b>{item['name']}</b> закончился на складе!</p>
            <br>
            <a href='/'>Вернуться в магазин</a>
            """
    else:
        return """
        <h1>❌ Ошибка 404</h1>
        <p>Такого товара не существует в нашей системе.</p>
        <br>
        <a href='/'>Вернуться в магазин</a>
        """


if __name__ == '__main__':
    # Запуск веб-сервера в режиме отладки
    app.run(debug=True)