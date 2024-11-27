# Steps to Run
# Standalone Interactive Session
1] Clone this repo 
    git clone https://github.com/thisisbillall/supermarket-checkout-assignment.git <br/>
2] cd supermarket-checkout-assignment <br/>
3] Run checkout.py as <br/>
    python -i checkout.py 

4] once the interactive session has opened, create object for SupermarketCheckout class as:<br/>
>>> checkout = SupermarketCheckout()<br/>

5] Test with your cart items string as below<br/>
>>> checkout.calculate_total("AABC")<br/>

# Docker Interactive Session
1] Clone this repo 
    git clone https://github.com/thisisbillall/supermarket-checkout-assignment.git
2] cd supermarket-checkout-assignment
3] run: 
  docker-compose build
4] then run: 
  docker-compose run checkout
5] once the interactive session has opened, create object for SupermarketCheckout class as:
>>> checkout = SupermarketCheckout()

6] Test with your cart items string as below
>>> checkout.calculate_total("AABX")
