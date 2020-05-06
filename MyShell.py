import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Pizzeria.settings")
import django
django.setup()
from pizzas.models import Pizza,Comment,Topping


pizzas = Pizza.objects.all()
for pizza in pizzas:
    print(pizza.id, pizza)



#if you know the ID of a particular object, you can use the method Topic.object.get()
# to retrieve that object and examin any attribute the object has.
t = Pizza.objects.get(id=1)
print(t.name) 
print(t.date_added)



#To get data through a foreign key relationship, you use the lowercase name of the 
# related model followed  by an underscore and the word set.
Comments = t.Comment_set.all()

for Comment in Comments:
    print(Comment)
    
for pizza in pizzas:
    print (pizza.id, pizza)


