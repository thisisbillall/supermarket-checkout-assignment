
class SupermarketCheckout:
    def __init__(self):
        self.prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        self.discounts = {'A': (3, 130), 'B': (2, 45)}

    def calculate_total(self, items):
        item_count = {}
        for item in items:
            item_count[item] = item_count.get(item, 0) + 1

        total_price = 0
        for item, count in item_count.items():
            if item in self.discounts:
                discount_qty, discount_price = self.discounts[item]
                total_price += (count // discount_qty) * discount_price
                total_price += (count % discount_qty) * self.prices[item]
            else:
                total_price += count * self.prices[item]

        print("Total:", total_price)
