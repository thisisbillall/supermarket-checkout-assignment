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
1] Clone this repo <br/>
    git clone https://github.com/thisisbillall/supermarket-checkout-assignment.git<br/>
2] cd supermarket-checkout-assignment<br/>
3] run: <br/>
  docker-compose build<br/>
4] then run: <br/>
  docker-compose run checkout<br/>
5] once the interactive session has opened, create object for SupermarketCheckout class as:<br/>
>>> checkout = SupermarketCheckout()<br/>

6] Test with your cart items string as below<br/>
>>> checkout.calculate_total("AABX")<br/>
