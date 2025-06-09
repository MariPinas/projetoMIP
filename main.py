from model import Pest, Product, ProductThreshold

def main():
    p1 = Pest(1, 'oi')
    p2 = Pest(2, 'oi2')
    print(p1)
    
    protresh1 = ProductThreshold(p1, 10, 10)
    protresh2 = ProductThreshold(p2, 2, 2)
    prod1 = Product(1, 'produto', 10, [protresh1, protresh2])
    
    resultado = prod1.get_threshold_for_pest(p1)
    print(resultado)
    
    print(prod1.should_apply(p1, 10))
    print(prod1.calculate_dose(p1, 10, 10))
    print(prod1.calculate_cost(p1, 10, 10))
    
if __name__ == '__main__':
    main()