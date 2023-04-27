from chef import Chef
from cont_chef import Cont_chef

cf1=Chef("saran","veg briyani","chicken briyani")
cf2=Chef("siva","veg rice","chicken rice")
# print(cf1.nonveg)    
cf3=Cont_chef("sai","veg noodles","chicken noodles","pasta")
print(cf1.name,cf2.name,cf3.name)
