print('Введите радиус круга в см ')
a = input()
b = int(a)
pi = 3.14
c = 2*b*pi # Длина окружности см
d = pi*(b**2) # Площадь круга см**
e = b/100 # Перевод из см в м
f = 2*e*pi # Длина окружности м
g = pi*(e**2) # Площадь круга м**2
print ('Длина окружности',c,'см,',f,'м')
print (' Площадь круга ',d,'см**2,',g,'м**2')

 #b = x*2**0.5
x = b*2**0.5  # x см - сторона вписаного квадрата
y = b*3**0.5 # y cv - сторона равностороннего треугольника
print ('Сторона вписанаго квадрата ',x,'см') 
print ('Сторона вписаного равностороннего треугольника ',y,'см') 

print (' Сторона описаного квадрата',2*b,'см') 
i = b*2*3**0.5 # Сторона вписаного треугоольника
print (' Сторона описаного треугольника',i,'см')

p = b * 2 * (2**0.5 - 1)
print (' Сторона описаного восьмиугольника',p,'см')