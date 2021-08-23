

# car_1 = {'model':'ferrari','rang':'qizil'}
# 
# 
# print(car_1['model'])
# print(car_1['rang'])
# 
# # lo'gatni ichiga kalit so'z va malumot qo'shish
# 
# car_1[ 'modeli' ]= 'lambargini'
# 
# # kalit so'z va qiymatni o'chirib tashlash
# del car_1['modeli']
# 
# 
# telefonlar ={
#              
#              'apple':'iphone 12 pro',
#              'samsung':'s21 ultra'
#             }
# print(telefonlar['samsung'])
# 
# #get() metodi
# 
# telefon = telefonlar.get('nokia','bu telefon yo\'q')
# print(telefon)

telefonlar ={
             'samsung':'s21 ultra',
              'apple':'iphone 12 pro',
              'samsung':'s21 ultra'
              }

# for key,value in telefonlar.items():
#     print(f'kalit: {key}')
#     print(f'qiymar: {value}')
    
    
#     #kalitlarni ko'rsatuvchi metod keys() metodi
    
    
#     print(telefonlar.keys())

# print('telefon chiqaradigan kompanjyalar mahsulotlar')
# for mahsulot in telefonlar.keys():
#     print(mahsulot.title())

# alifbo tartibida chiqarish

# print('telefon chiqaradigan kompanjyalar mahsulotlar')
# for mahsulot in sorted(telefonlar.keys()):
#     print(mahsulot.title())    
    


# malumotlarni chiqaruvchi metod values() metodi


# print('telefon chiqaradigan kompanjyalar mahsulotlar')
# for mahsulot in sorted(telefonlar.values()):
#     print(mahsulot.title()) 
    
    
    
    #takrorlanganlarni tozalovchi element
    
    
print('telefon chiqaradigan kompanjyalar mahsulotlar')
for mahsulot in set(sorted(telefonlar.keys())):
    print(mahsulot.title())      