"""import requests
from django.core.files import File
from category.models import Category
from product.models import Product
from galleryitem.models import GalleryItem"""

#Categories
""" category1 = Category(name="Computadoras", icon="computer", description="Computadoras, Laptops")
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
category11.save() """
category12.save()

# Products
r = requests.get("https://images-na.ssl-images-amazon.com/images/I/41OI4C2VSrL.jpg")
with open("/tmp/product-1.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-1.png", "rb")
product1_file = File(reopen)
product1 = Product(name="ASUS ROG Strix G (2019)", description="Nvidia GeForce GTX 1650 4GB GDDR5,  Intel Core i7-9750h Hexa-Core, 16GB de RAM", brand="ASUS", price=11500, stock=30, weight=2.26)
product1.save()
product1.categories.set([1, 12])
product1.featured_image.save("product-1.png", product1_file, save=True)


r = requests.get("https://www.powerplanetonline.com/cdnassets/Apple_MacBook_Pro_2019_-Plata_01_l.jpeg")
with open("/tmp/product-2.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-2.png", "rb")
product2_file = File(reopen)
product2 = Product(name="MacBook Pro", description="Intel Core i7 7ma gen., Intel UHD Graphics 630, 512 GB SDD, 8GB de RAM", brand="Apple", price=14000, stock=30, weight=2)
product2.save()
product2.categories.set([1])
product2.featured_image.save("product-2.png", product2_file, save=True)


r = requests.get("https://www.asus.com/media/global/products/yxnnaa6rkdb25veg/P_setting_fff_1_90_end_600.png")
with open("/tmp/product-3.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-3.png", "rb")
product3_file = File(reopen)
product3 = Product(name="ASUS ROG Gaming Phone II", description="Qualcomm Snapdragon 855 Plus - Octa-core 2.96GHz, 12GB RAM, Cámara de 48MP, pantalla AMOLED", brand="ASUS", price=7500, stock=30, weight=0.25)
product3.save()
product3.categories.set([2, 12])
product3.featured_image.save("product-3.png", product3_file, save=True)


r = requests.get("https://media.kingston.com/kingston/product/ktc-product-ssd-a400-sa400s37-120gb-1-sm.jpg")
with open("/tmp/product-4.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-4.png", "rb")
product4_file = File(reopen)
product4 = Product(name="SSD Kingston 2.5''SA400S37/120GB", description="Capacidad de 120GB, 10 veces más veloz que un HDD, interfaz SATA", brand="Kingston", price=300, stock=30, weight=0.25)
product4.save()
product4.categories.set([3])
product4.featured_image.save("product-4.png", product4_file, save=True)


r = requests.get("https://i2.wp.com/eolomovil.com/wp-content/uploads/2020/03/0503202019054818168.jpg?fit=530%2C530&ssl=1")
with open("/tmp/product-5.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-5.png", "rb")
product5_file = File(reopen)
product5 = Product(name="RAM HyperX 16GB RGB", description="RAM de 16GB, DDR4, con RGB, 3733 MHz", brand="HyperX", price=500, stock=30, weight=0.04)
product5.save()
product5.categories.set([4])
product5.featured_image.save("product-5.png", product5_file, save=True)


r = requests.get("https://i.dell.com/is/image/DellContent//content/dam/global-site-design/product_images/peripherals/output_devices/dell/monitors/p2719h/spi/monitor-p2719h-hero-504x350-responsive.png?fmt=jpg")
with open("/tmp/product-6.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-6.png", "rb")
product6_file = File(reopen)
product6 = Product(name="Dell 27'' P2719H", description="Monitor Dell 1920x1080px, 27'', 60 Hz, aspecto 16:9", brand="Dell", price=1980, stock=30, weight=4.35)
product6.save()
product6.categories.set([5])
product6.featured_image.save("product-6.png", product6_file, save=True)


r = requests.get("https://static.kemikcdn.com/2018/04/88885639-6d2c-4b1a-9cb5-a02d73f55e8c.jpg")
with open("/tmp/product-7.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-7.png", "rb")
product7_file = File(reopen)
product7 = Product(name="Mouse Logitech G203 RGB", description="Mouse ideal para gaming, 8.000 DPI, RGB, una rapidez 8 veces superior a la de los mouse estándar", brand="Logitech", price=300, stock=30, weight=0.08)
product7.save()
product7.categories.set([6, 12])
product7.featured_image.save("product-7.png", product7_file, save=True)


r = requests.get("https://www.macrosistemas.com/images/virtuemart/product/teclado-18.jpg")
with open("/tmp/product-8.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-8.png", "rb")
product8_file = File(reopen)
product8 = Product(name="Teclado Logitech G513 RGB", description="Teclado gaming G513 es un teclado para juegos de alto desempeño con interruptores mecánicos avanzados GX a elegir. Trae RGB", brand="Logitech", price=700, stock=30, weight=1.11)
product8.save()
product8.categories.set([6, 12])
product8.featured_image.save("product-8.png", product8_file, save=True)


r = requests.get("https://cdn.lumingo.com/medias/0100518122-000000000004648235-0-c515Wx515H?context=bWFzdGVyfGltYWdlc3wyNTY0NXxpbWFnZS9qcGVnfGltYWdlcy9oMjcvaDYxLzkwODgwMjczMjg1NDIuanBnfDViOGU5MGU3ZDQ3ZmRjNjY1NzcwNDIxMTg2MWU1YWYyNjliMDBkODEzOTVlNjc2N2M5ZWVmZTQ0MzljNjBlY2Y")
with open("/tmp/product-9.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-9.png", "rb")
product9_file = File(reopen)
product9 = Product(name="SmartTV Samsung UN50RU7100 50''", description="Smart TV Samsung 4K-Ultra HD con Apple AirPlay integrado. Edge LED, 3840x2160 pixels, 50 Hz/60 Hz", brand="Samsung", price=3999, stock=30, weight=1.11)
product9.save()
product9.categories.set([7])
product9.featured_image.save("product-9.png", product9_file, save=True)


r = requests.get("https://media.kingston.com/hyperx/product/hx-product-headset-cloud-core-7.1-2-sm.jpg")
with open("/tmp/product-10.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-10.png", "rb")
product10_file = File(reopen)
product10 = Product(name="Headsets HyperX Cloud 2", description="Audífonos con sonido surround virtual 7.1 para tu PC, gaming, cancelación pasiva del sonido.", brand="HyperX", price=800, stock=30, weight=0.32)
product10.save()
product10.categories.set([8, 12])
product10.featured_image.save("product-10.png", product10_file, save=True)


r = requests.get("https://lh3.googleusercontent.com/proxy/5W4GNQmWR7z9eM88rD8_yBNQuB7FOznd7WFAOJUDmMNendSfAszd4k8CLI5fLpaBdprmfp0gH3inWZdLguSS5U6fJl720GkCE03K3fMlLIoLtUK22Z3sE8zSisg_zd3yOt5x8w")
with open("/tmp/product-11.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-11.png", "rb")
product11_file = File(reopen)
product11 = Product(name="Impresora Canon G1110", description="La Impresora Canon G1110 PIXMA está equipada con tanques de tinta integrados de fácil recarga que proveen una capacidad de tinta mayor y un rendimiento", brand="Canon", price=900, stock=30, weight=4.30)
product11.save()
product11.categories.set([9])
product11.featured_image.save("product-11.png", product11_file, save=True)


r = requests.get("https://images-na.ssl-images-amazon.com/images/I/91JUkwqJhDL._AC_SX466_.jpg")
with open("/tmp/product-12.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-12.png", "rb")
product12_file = File(reopen)
product12 = Product(name="Nvidia GeForce RTX 2080 Ti", description="Su potente arquitectura de GPU NVIDIA Turing ™, tecnologías innovadoras y 11 GB de memoria GDDR6 la convierten en la GPU de juegos más avanzada del mundo", brand="NVIDIA", price=12000, stock=30, weight=4.30)
product12.save()
product12.categories.set([10, 12])
product12.featured_image.save("product-12.png", product12_file, save=True)


r = requests.get("https://images-na.ssl-images-amazon.com/images/I/61I%2B8Nw4xYL._AC_SX522_.jpg")
with open("/tmp/product-13.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/product-13.png", "rb")
product13_file = File(reopen)
product13 = Product(name="Escritorio en L", description="Marco blanco de acero /Madera color Negro, 118x82x16 ", brand="XTech", price=1000, stock=30, weight=20)
product13.save()
product13.categories.set([11])
product13.featured_image.save("product-13.png", product13_file, save=True)

# Gallery Items

product = Product.objects.filter(id=1).first()

r = requests.get("https://images-na.ssl-images-amazon.com/images/I/811QpiYXe-L._AC_SL1500_.jpg")
with open("/tmp/gallery-1.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-1.png", "rb")
gallery1_file = File(reopen)
gallery_item_1 = GalleryItem(product=product)
gallery_item_1.save()
gallery_item_1.image.save("gallery-1.png", gallery1_file, save=True)

r = requests.get("https://geekzilla.tech/home/wp-content/uploads/2020/04/Screen-Shot-2020-04-08-at-12.58.29-PM.png")
with open("/tmp/gallery-2.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-2.png", "rb")
gallery2_file = File(reopen)
gallery_item_2 = GalleryItem(product=product)
gallery_item_2.save()
gallery_item_2.image.save("gallery-2.png", gallery2_file, save=True)



product = Product.objects.filter(id=2).first()

r = requests.get("https://www.souqbaba.com/wp-content/uploads/2018/12/APPLE-MACBOOK-PRO-2018-MR9R2-SPACE-GREY-I5-8TH-GEN.-2.3-QUAD-CORE-8GB-512GB.png")
with open("/tmp/gallery-3.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-3.png", "rb")
gallery3_file = File(reopen)
gallery_item_3 = GalleryItem(product=product)
gallery_item_3.save()
gallery_item_3.image.save("gallery-3.png", gallery3_file, save=True)

r = requests.get("https://www.pclinks.com.bd/website/image/product.product/1562/image/2000x2000")
with open("/tmp/gallery-4.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-4.png", "rb")
gallery4_file = File(reopen)
gallery_item_4 = GalleryItem(product=product)
gallery_item_4.save()
gallery_item_4.image.save("gallery-2.png", gallery4_file, save=True)





product = Product.objects.filter(id=3).first()

r = requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQDAwxQ363OHCv8hwLG6k4qUHV5Z6d4Rghz5q2zxVdmhQkTCnde&usqp=CAU")
with open("/tmp/gallery-5.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-5.png", "rb")
gallery5_file = File(reopen)
gallery_item_5 = GalleryItem(product=product)
gallery_item_5.save()
gallery_item_5.image.save("gallery-5.png", gallery5_file, save=True)

r = requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR3F5uHDS0trmscIAORJF9144HbV-i_bZxlLRqOO0eFqB0VRkPl&usqp=CAU")
with open("/tmp/gallery-6.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-6.png", "rb")
gallery6_file = File(reopen)
gallery_item_6 = GalleryItem(product=product)
gallery_item_6.save()
gallery_item_6.image.save("gallery-6.png", gallery6_file, save=True)






product = Product.objects.filter(id=4).first()

r = requests.get("https://static.kemikcdn.com/2017/06/sa400s37-120gb-422x571.jpg")
with open("/tmp/gallery-7.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-7.png", "rb")
gallery7_file = File(reopen)
gallery_item_7 = GalleryItem(product=product)
gallery_item_7.save()
gallery_item_7.image.save("gallery-7.png", gallery7_file, save=True)

r = requests.get("https://media.kingston.com/kingston/product/ktc-product-ssd-a400-sa400s37-120gb-1-sm.jpg")
with open("/tmp/gallery-8.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-8.png", "rb")
gallery8_file = File(reopen)
gallery_item_8 = GalleryItem(product=product)
gallery_item_8.save()
gallery_item_8.image.save("gallery-8.png", gallery8_file, save=True)






product = Product.objects.filter(id=5).first()

r = requests.get("https://www.cyberpuerta.mx/img/product/L/CP-HYPERX-HX432C16PB3A8-3.jpg")
with open("/tmp/gallery-9.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-9.png", "rb")
gallery9_file = File(reopen)
gallery_item_9 = GalleryItem(product=product)
gallery_item_9.save()
gallery_item_9.image.save("gallery-9.png", gallery9_file, save=True)

r = requests.get("https://www.cyberpuerta.mx/img/product/L/CP-HYPERX-HX432C16PB3A8-6.jpg")
with open("/tmp/gallery-10.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-10.png", "rb")
gallery10_file = File(reopen)
gallery_item_10 = GalleryItem(product=product)
gallery_item_10.save()
gallery_item_10.image.save("gallery-10.png", gallery10_file, save=True)






product = Product.objects.filter(id=6).first()

r = requests.get("https://cdn.cnetcontent.com/bf/5f/bf5f8232-afbe-412e-b8bf-e204bdc9173c.jpg")
with open("/tmp/gallery-11.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-11.png", "rb")
gallery11_file = File(reopen)
gallery_item_11 = GalleryItem(product=product)
gallery_item_11.save()
gallery_item_11.image.save("gallery-11.png", gallery11_file, save=True)

r = requests.get("https://www.cyberpuerta.mx/img/product/L/CP-DELL-210-AQCS-6.jpg")
with open("/tmp/gallery-12.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-12.png", "rb")
gallery12_file = File(reopen)
gallery_item_12 = GalleryItem(product=product)
gallery_item_12.save()
gallery_item_12.image.save("gallery-12.png", gallery12_file, save=True)







product = Product.objects.filter(id=7).first()

r = requests.get("https://c1.neweggimages.com/NeweggImage/ProductImage/26-197-252-Z01.jpg")
with open("/tmp/gallery-13.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-13.png", "rb")
gallery13_file = File(reopen)
gallery_item_13 = GalleryItem(product=product)
gallery_item_13.save()
gallery_item_13.image.save("gallery-13.png", gallery13_file, save=True)

r = requests.get("https://hardwareviews.com/wp-content/uploads/2020/04/logitech-g203-lightsync.jpg")
with open("/tmp/gallery-14.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-14.png", "rb")
gallery14_file = File(reopen)
gallery_item_14 = GalleryItem(product=product)
gallery_item_14.save()
gallery_item_14.image.save("gallery-14.png", gallery14_file, save=True)





product = Product.objects.filter(id=8).first()

r = requests.get("https://www.macrosistemas.com/images/virtuemart/product/teclado-18.jpg")
with open("/tmp/gallery-15.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-15.png", "rb")
gallery15_file = File(reopen)
gallery_item_15 = GalleryItem(product=product)
gallery_item_15.save()
gallery_item_15.image.save("gallery-15.png", gallery15_file, save=True)

r = requests.get("https://resources.claroshop.com/medios-plazavip/mkt/5ca62e799ad2b_4jpg.jpg")
with open("/tmp/gallery-16.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-16.png", "rb")
gallery16_file = File(reopen)
gallery_item_16 = GalleryItem(product=product)
gallery_item_16.save()
gallery_item_16.image.save("gallery-16.png", gallery16_file, save=True)






product = Product.objects.filter(id=9).first()

r = requests.get("https://cdn.lumingo.com/medias/0100124913-000000000004649641-0-c515Wx515H?context=bWFzdGVyfGltYWdlc3wxODkzNHxpbWFnZS9qcGVnfGltYWdlcy9oN2YvaDQ3LzkwOTI5NzUxOTgyMzguanBnfGZhYTY4MTg1YTAzZDhiMmZlODhmNDA0NjczNGE5NDZlNWRhOTk1MmYzMzEwZTY3NTc5ZDI4NmI3N2MzZDE3YTU")
with open("/tmp/gallery-17.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-17.png", "rb")
gallery17_file = File(reopen)
gallery_item_17 = GalleryItem(product=product)
gallery_item_17.save()
gallery_item_17.image.save("gallery-17.png", gallery17_file, save=True)

r = requests.get("https://resources.claroshop.com/medios-plazavip/s2/10180/1221795/5da3dc0a5427f-2_un50ru7100-1600x1600.jpg")
with open("/tmp/gallery-18.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-18.png", "rb")
gallery18_file = File(reopen)
gallery_item_18 = GalleryItem(product=product)
gallery_item_18.save()
gallery_item_18.image.save("gallery-18.png", gallery18_file, save=True)







product = Product.objects.filter(id=10).first()

r = requests.get("https://m.media-amazon.com/images/I/71eSPhz0IjL.jpg")
with open("/tmp/gallery-19.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-19.png", "rb")
gallery19_file = File(reopen)
gallery_item_19 = GalleryItem(product=product)
gallery_item_19.save()
gallery_item_19.image.save("gallery-19.png", gallery19_file, save=True)

r = requests.get("https://static.kemikcdn.com/2016/04/0dd8c853-3f34-4f58-a360-b076e6db3d8f.jpg")
with open("/tmp/gallery-20.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-20.png", "rb")
gallery20_file = File(reopen)
gallery_item_20 = GalleryItem(product=product)
gallery_item_20.save()
gallery_item_20.image.save("gallery-20.png", gallery20_file, save=True)





product = Product.objects.filter(id=11).first()

r = requests.get("https://www.tiendacanon.com.mx/wcsstore/CMEXCatalogAssetStore/G1110_AS_FR_cl_xl.jpg")
with open("/tmp/gallery-21.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-21.png", "rb")
gallery21_file = File(reopen)
gallery_item_21 = GalleryItem(product=product)
gallery_item_21.save()
gallery_item_21.image.save("gallery-21.png", gallery21_file, save=True)

r = requests.get("https://www.intelcomphonduras.com/wp-content/uploads/2018/10/impresora-canon-g1110-pixmainyeccion-de-tinta-D_NQ_NP_863784-MRD27406393430_052018-F.jpg")
with open("/tmp/gallery-22.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-22.png", "rb")
gallery22_file = File(reopen)
gallery_item_22 = GalleryItem(product=product)
gallery_item_22.save()
gallery_item_22.image.save("gallery-22.png", gallery22_file, save=True)





product = Product.objects.filter(id=12).first()

r = requests.get("https://easetec.com.pk/wp-content/uploads/2019/05/91Qg5K-cmfL._SL1500_.jpg")
with open("/tmp/gallery-23.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-23.png", "rb")
gallery23_file = File(reopen)
gallery_item_23 = GalleryItem(product=product)
gallery_item_23.save()
gallery_item_23.image.save("gallery-23.png", gallery23_file, save=True)

r = requests.get("https://c1.neweggimages.com/ProductImage/14-137-338-V19.jpg")
with open("/tmp/gallery-24.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-24.png", "rb")
gallery24_file = File(reopen)
gallery_item_24 = GalleryItem(product=product)
gallery_item_24.save()
gallery_item_24.image.save("gallery-24.png", gallery24_file, save=True)








product = Product.objects.filter(id=13).first()

r = requests.get("https://my.accvent.com/images/stories/virtuemart/product/xtf-cd4333.png")
with open("/tmp/gallery-25.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-25.png", "rb")
gallery25_file = File(reopen)
gallery_item_25 = GalleryItem(product=product)
gallery_item_25.save()
gallery_item_25.image.save("gallery-25.png", gallery25_file, save=True)

r = requests.get("https://www.xtechamericas.com/media/XTF-CD433-002.jpg")
with open("/tmp/gallery-26.png", "wb") as f:
    f.write(r.content)
reopen = open("/tmp/gallery-26.png", "rb")
gallery26_file = File(reopen)
gallery_item_26 = GalleryItem(product=product)
gallery_item_26.save()
gallery_item_26.image.save("gallery-26.png", gallery26_file, save=True)

 """