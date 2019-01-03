def cost_ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
    
  return (weight * price_per_pound) + 20.00

print(cost_ground_shipping(8.4))

cost_premium_ground_shipping = 125.00

def cost_drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
    
  return (weight * price_per_pound)

print(cost_drone_shipping(1.5))

def cheapest_shipping(weight):
  ground = cost_ground_shipping(weight)
  premium = cost_premium_ground_shipping
  drone = cost_drone_shipping(weight)
  
  if ground < premium and ground < drone:
    method = "Ground Shipping"
    cost = ground
  elif premium < ground and premium < drone:
    method = "Premium Shipping"
    cost = premium
  else:
    method = "Drone Shipping"
    cost = drone
    
  print("The cheapest shipping method possible is " + str(method) + " and it costs " + str(cost))
  
cheapest_shipping(4.8)
cheapest_shipping(41.5)
