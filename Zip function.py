set1={2,6,9}
set2={'b','n','o'}
set3=list(zip(set1,set2))
print(set3,'\n')
list1=[100,345,678]
list2=[245,356,789]
for x,y in zip(list1,list2[ ::-1]):
    print(x,y)
stock=['nvidea','goggle','s&p500']
price=[234.5,132.4,567.9]
newdic={stock:price for stock,price in zip(stock,price)}
print('\n{}'.format(newdic))