import sys
import os
#sys.path.append(os.path.abspath(".")) #worked
sys.path.insert(0, os.path.abspath("."))

from notebooks.customer_load import customer_count

def test_customer_count():
    customers = ["Ali", "Jhon", "Maria"]
    assert customer_count(customers) == 3