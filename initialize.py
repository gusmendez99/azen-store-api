import requests
from django.core.files import File
from category.models import Category
from product.models import Product

#Categories
category1 = Category(name="Computadoras", icon="computer", description="Computadoras, Laptops")
category2 = Category(name="Telefonos", icon="smartphone", description="Android y iOS")
category3 = Category(name="Disco Duro", icon="storage", description="HDD y SSD")
category4 = Category(name="Memorias", icon="memory", description="RAM")
category5 = Category(name="Monitores", icon="monitor", description="IPS, Curvos, ...")
category6 = Category(name="Accesorios de Computadora", icon="mouse", description="Mouse, Teclado, ...")
category7 = Category(name="TV", icon="tv", description="LED, Smart, ...")
category8 = Category(name="Audio", icon="headset", description="Bocinas, Headsets, ...")
category9 = Category(name="Impresoras", icon="printer", description="Matriz, Laser, ...")
category10 = Category(name="Tarjetas de video", icon="gpu", description="NVIDIA, AMD, ...")
category11 = Category(name="Mobiliario", icon="home", description="Escritorios, sillas, ...")
category12 = Category(name="Gaming", icon="videogame-asset", description="Todo relacionado a gaming, con RGB ...")

category1.save()
category2.save()
category3.save()
category4.save()
category5.save()
category6.save()
category7.save()
category8.save()
category9.save()
category10.save()
category11.save()
category12.save()
