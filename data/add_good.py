from data import db_session
from data.good import Good

db_session.global_init("../db/base.db")
session = db_session.create_session()

good = Good()
# good.price = 1400
# good.name = 'Tetramorium cf. bicarinatum'
# good.image_name = 'Tetramorium cf. bicarinatum.jpg'
# good.type = 'ant'
# good.description = 'Хардкорные муравьи c внутригнездовым размножением, уничтожающие всё на своём пути!'


# good.price = 1300
# good.name = 'Lasius cf. niger'
# good.image_name = 'Lasius cf. niger.jpg'
# good.description = 'Латинское название - Lasius niger, в народе известен как черный садовый муравей. Несмотря на свое ' \
#                    'название, это не абсолютно черные, а скорее тёмно-бурые муравьи. Обитает в полях и садах. Очень ' \
#                    'известный и распространенный муравей, является серьезным конкурентом для других видов средней ' \
#                    'полосы России. '
# good.type = 'ant'


# good.price = 3500
# good.name = 'AntPlanet СТАНДАРТ v.2'
# good.image_name = 'AntPlanet СТАНДАРТ v.2.jpg'
# good.description = 'Муравьиная ферма AntPlanet "Белый Стандарт" v.2 подходит для небольшой муравьиной колонии. Очень ' \
#                    'удобно наблюдать за муравьями за счёт горизонтального расположения системы ходов. '
# good.type = 'farm'


# good.price = 1200
# good.name = 'Camponotus cf. fellah'
# good.image_name = 'Camponotus cf. fellah.jpg'
# good.description = 'Африканские хищные муравьи. Настоящие бойцы! Есть каста крупных солдат-охранников'
# good.type = 'ant'


# good.price = 900
# good.name = 'Messor cf. ebeninus'
# good.image_name = 'Messor cf. ebeninus.jpg'
# good.description = 'Шустрые и агрессивные муравьи-жнецы с Ближнего Востока. Подходят новичкам, есть солдаты!'
# good.type = 'ant'


# good.price = 3000
# good.name = 'Messor cf. denticulatus'
# good.image_name = 'Messor cf. denticulatus.jpg'
# good.description = 'Красногрудые хранители зерна. Отличные муравьи для новичков, есть каста солдат!'
# good.type = 'ant'


# good.price = 3100
# good.name = 'Messor cf. barbarus'
# good.image_name = 'Messor cf. barbarus.jpg'
# good.description = 'Красноголовые муравьи с крупными солдатами. Новорождённые жёлтоголовые превращаются в красноголовых!'
# good.type = 'ant'


# good.price = 3500
# good.name = 'AntPlanet КОВЧЕГ'
# good.image_name = 'AntPlanet КОВЧЕГ.jpg'
# good.description = 'Муравьиная ферма AntPlanet КОВЧЕГ "Аквамарин" имеет вертикальное расположение.  Вместимость ' \
#                    'особей вида Messor Structor (муравьи-жнецы) ~ до 1100.За счет расположения ходов под небольшим ' \
#                    'углом, наблюдение за муравьиной семьей становится более удобным, чем в обычных вертикальных ' \
#                    'фермах. '
# good.type = 'farm'


# good.price = 3500
# good.name = 'AntPlanet МИНИ'
# good.image_name = 'AntPlanet МИНИ.jpg'
# good.description = 'Муравьиная ферма AntPlanet "Белый" подходит для небольшой муравьиной колонии. Очень удобно ' \
#                    'наблюдать за муравьями за счёт горизонтального расположения системы ходов. Вместимость особей ' \
#                    'вида Messor Structor (муравьи-жнецы) ~ 600-700. '
# good.type = 'farm'

session.add(good)
session.commit()
