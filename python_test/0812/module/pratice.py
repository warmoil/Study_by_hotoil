
# import theater_module
# theater_module.price(3) #3명에서 영화보러갔을때 가격
# theater_module.price_morning(4) #4명에서 조조할인 영화 보러갔을때
# theater_module.price_soldier(5) #5명의 군이이 영화 보러갔을때


# import theater_module as mv #별칭 붙여주기
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# #from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price,price_morning
# price(5)
# price_morning(6) 
# #선택해서 하는것

from theater_module import price_soldier as price
price(5)
#1개만골를건데 그걸 as >>뒤에걸로 별칭지음