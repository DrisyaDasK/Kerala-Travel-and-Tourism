from travelapp.models import Carts

# e code nte context key eth html pagel venamenkilum vilichal data avide kitum
#common ayit pass cheyyenda data
def cart_count_context(request):
    # count=request.user.cart_set.all().exclude(status='order-placed').count
    if request.user.is_authenticated:
        count=Carts.objects.filter(user_id=request.user).exclude(status='booked').count()
        return {'count':count}
        #key here :count
    else:
        return {'count':0}
    

