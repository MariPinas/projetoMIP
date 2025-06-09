from service.mip_service import MIPService

def main():
    paths = {
        "pests": "data/pests.json",
        "products": "data/products.json",
        "occurrences": "data/pest_occurrences.json",
        "regions": "data/regions.json"
    }

    service = MIPService(paths)
    service.load_data()
    service.generate_recommendations()

if __name__ == "__main__":
    main()