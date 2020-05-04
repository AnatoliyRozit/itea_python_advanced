class Shop:
    
    _total_sales = 0

    @classmethod
    def update_total_sales(cls, selling_qty):
        cls._total_sales += selling_qty

    @classmethod
    def get_total_sales(cls):

        return cls._total_sales

    def __init__(self, name, sold_qty):
        self._name = name
        self._sold_qty = sold_qty
        self.update_total_sales(self._sold_qty)

    def change_sold_qty(self, selling_qty):

        self._sold_qty += selling_qty
        self.update_total_sales(selling_qty)


if __name__ == '__main__':
    atb = Shop('ATB', 1)
    atb.change_sold_qty(2)
    silpo = Shop('SILPO', 5)
    silpo.change_sold_qty(3)
    print(atb.sold_qty)
    print(Shop.get_total_sales())
    print(silpo.sold_qty)
    print(Shop.get_total_sales())