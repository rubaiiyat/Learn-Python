class Cart:
    def __init__(self, name, total_amount=0) -> None:
        self.name = name
        self.total_amount = total_amount
        self.products = []
        

    def shopping(self, item_name, price):
        self.total_amount += price
        self.products.append({"name": item_name, "price": price})
        return price

    def vat(self):
        self.vat_amount = (self.total_amount * 5) / 100
        return self.vat_amount

    def total(self):

        self.current_amount = self.total_amount + self.vat_amount
        return self.current_amount

    def print_receipt(self):
        print(f"Customer: {self.name}")
        
        for item in self.products:
            print(f'Item: {item['name']} - Price: ${item['price']}')

        print(f'Without Vat Cost: ${self.total_amount}')
        print(f'Your total 5% vat: ${self.vat()}')
        print(f'Total Cost: ${self.total()}')

abir=Cart('Abir')
abir.shopping('Watch',20)
abir.shopping('Belt', 14)
abir.shopping('Keyboard',40)
abir.shopping('Mouse',25)
abir.shopping('Laptop',800)
abir.print_receipt()
