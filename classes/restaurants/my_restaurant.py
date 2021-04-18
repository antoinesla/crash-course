from restaurant import Restaurant, IceCreamStand



restaurant1 = Restaurant("guggino's", "italian cuisine")
restaurant1.describe_restaurant()

print('\n')

restaurant2 = IceCreamStand('diarhee-land', ['chocolate', 'vanilla'])
restaurant2.describe_restaurant()
restaurant2.describe_flavors_served()

print('\n')

restaurant3 = IceCreamStand(
    'salmonella-land', ['raspberry', 'cookie dough', 'mint', 'lemon'])
restaurant3.describe_restaurant()
restaurant3.describe_flavors_served()