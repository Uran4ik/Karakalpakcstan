from flask import Flask
from model import log, db, Cuisine, Attractions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        cuisine1 = Cuisine(name='Баурсак', short_description='Ромбики из теста обжаренные во фритюре', price=10200)
        cuisine2 = Cuisine(name='Жуэре гуртик',
                           short_description='Блюдо относится к числу старинных видов пищи, готовят до сих пор '
                                             'Это блюдо характерно лишь для кулинарии каракалпаков', price=24200)
        cuisine3 = Cuisine(name='Плов', short_description='Самый лучший плов в мире - каракалпакский. Шикарное блюдо от шикарных людей.', price=20200)
        cuisine4 = Cuisine(name='Манты',
                           short_description='Манты - это несомненно восхитительное лакомство, представляющее из себя традиционное '
                                             'блюдо восточной кухни, имеющее определенную сложность и изысканность',
                           price=20200)

        attract1 = Attractions(name='Музей искусств имени И.В.Савицкого', short_description='Государственный музей искусств Республики Каракалпакстан'
                                                                                            ' им. И.Савицкого является самым притягательным местом в Каракалпакстане.'
                                                                            'Он носит имя своего основателя и первого директора — художника Игоря Витальевича Савицкого'
                                                                            'Музей расположен в центре Нукуса. Его коллекция насчитывает около 100 000 экспонатов',price=103190)
        attract2 = Attractions(name='Mizdakhan Necropolis',
                           short_description='Миздакхан – это целый комплекс историко-археологических памятников, вершина западного холма увенчана руинами крепости Гяур-кала,'
                                            'построенной в IV веке до нашей эры. Миздакхан – ранее древний город, ныне археологический и архитектурный комплекс.'
                                             'Мировые часы или часы Апокалипсиса.', price=245200)
        attract3 = Attractions(name='Муйнак', short_description='В начале XX века Муйнак был крупным портовым селением здесь кипела жизнь. Рыбная промышленность в Муйнаке процветала.'
                               'Сюда приезжали рыбаки из других республик Советского Союза и закупались. На территории бывшего моря возникла пустыня Аралкум', price=128209)
        attract4 = Attractions(name='Дахма Чилпык',
                           short_description='Дахма Чилпык, возраст которой составляет более 2 000 лет, является символом древней истории и изображена на гербе республики Каракалпакстан. '
                                            'Её название до сих пор окончательно не расшифровано. Одни считают, что это просто аллитерация, отражение плеска волн Аму-Дарьи,' 
                                            'другие склоняются к персидской трактовке, по которой Чилпык переводится как «сорок праведников»', price=176299)

        db.session.add_all([cuisine4, cuisine2, cuisine3, cuisine1, attract1, attract4, attract2, attract3])
        db.session.commit()

    print('Создана база данных нац. кухни Каракапакстана')