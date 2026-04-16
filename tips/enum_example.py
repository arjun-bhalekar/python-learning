from enum import Enum


# Define the Enum
class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4


# Accessing Enum
for status in OrderStatus:
    print(status)

current_status = OrderStatus.PENDING
if current_status == OrderStatus.SHIPPED:
    print("Your order is shipped")
else:
    print("Your order is not shipped")
