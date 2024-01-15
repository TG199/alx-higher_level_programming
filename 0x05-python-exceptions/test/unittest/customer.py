class Customer:
    """A sample customer class"""
    discount = 0.95
    

    def __init__(self, firstname, lastname, purchase):
        self.firstname = firstname
        self.lastname = lastname
        self.purchase = purchase

        @property
        def customer_mail(self):
            return f'{self.firstname}.{self.lastname}@email.com'

        @property
        def customer_fullname(self):
            return f'{self.firstname}.{self.lastname}'

        def apply_discount(self):
            self.purchase = int(self.purchase self.discount)

