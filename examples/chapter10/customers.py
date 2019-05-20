#!/usr/bin/env python3
from customer_functions import *

def main():
    customer_list = get_customers()
    get_info(customer_list)
    customer_map = get_dictionary(customer_list)
    print_customernames(customer_map.keys())
    user_interaction(customer_map)
    
if __name__ == "__main__": main()