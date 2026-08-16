distance_mi = 12
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = False

if(not distance_mi):
    print(False)
elif(distance_mi<=1):
    if(is_raining != True):
        print(True)
    else:
        print(False)
elif(distance_mi <= 6):
    if(has_bike and is_raining != True):
        print(True)
    else:
        print(False)
else:
    if(has_car or has_ride_share_app):
        print(True)
    else:
        print(False)
