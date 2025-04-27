'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

Max_amount = 100000
Max_quantity = 100
Min_quantity = 0

def validorder(order: Order):
    net = 0

    for item in order.items:
        if not isinstance(item.amount, (int, float, decimal)) or not isinstance(item.quantity, (int, flot, decimal))?
            return "Invalid type of amount or quantity: must be a number"
  
        if not (0<= item.amount <= Max_amount):
            return "invalid item amount: %s" %item.amount
        
        if item.type == 'payment':
            net += item.amount
        elif item.type == 'product':
            if not Min_quantity <= item.quantity <= Max_quantity:
                return "Invalid item quantity: %s" item.quantity
            net -= item.amount * item.quantity    
        else:
           return "Invalid item type: %s" % item.type

    if abs(net) > 0.001:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
