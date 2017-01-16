from decimal import *
import math
print(0.70*1.05)
print(Decimal(0.70)*Decimal(1.05))

print(Decimal(0.1))

print(math.pi)
print(3.14159265358979323846264338327950288419716939937510)
print(Decimal(math.pi))
print(Decimal(3.14159265358979323846264338327950288419716939937510))

print(len(str(Decimal(math.pi))))
print(len(str(Decimal(3.14159265358979323846264338327950288419716939937510))))