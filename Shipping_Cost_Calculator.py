# Shipping Cost Calulator 

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calulate shipping cost 
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
