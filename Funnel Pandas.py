import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print (visits.head())
print (cart.head())
print (checkout.head())
print (purchase.head())

visits_cart = pd.merge (visits,cart, how = 'left')
print (visits_cart)

howlong = len(visits_cart)
print (howlong)

cartnull = visits_cart[visits_cart.cart_time.isnull()]
print (cartnull)
print (len(cartnull))

notcart = float(len(cartnull)) / len(visits_cart)
print (notcart)

cart_checkout = pd.merge (cart, checkout, how='left')
checkout_null = cart_checkout[cart_checkout.checkout_time.isnull()]
not_checkout = float(len(checkout_null))/len(cart_checkout)
print (not_checkout)

checkout_purch = pd.merge (checkout, purchase, how='left')
purchase_null = checkout_purch[checkout_purch.purchase_time.isnull()]
not_purch = float(len(purchase_null))/len(checkout_purch)
print (not_purch)

all_data = visits.merge(cart, how = 'left').merge(checkout, how='left').merge(purchase, how = 'left')

print (all_data.head())

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)

print(all_data.time_to_purchase.mean())



