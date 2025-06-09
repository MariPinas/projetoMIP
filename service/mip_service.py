from model import Product, Pest, ProductThreshold, PestOccurrence, Region
from loader.json_loader import JSONLoader
from uuid import UUID
from datetime import datetime

class MIPService:
    def __init__(self, paths: dict):
        self.paths = paths
        self.pests = {}
        self.regions = {}
        self.products = []
        self.occurrences = []

    def load_data(self):
        data_pests = JSONLoader.load_json(self.paths["pests"])
        data_regions = JSONLoader.load_json(self.paths["regions"])
        data_products = JSONLoader.load_json(self.paths["products"])
        data_occurrences = JSONLoader.load_json(self.paths["occurrences"])

        self.pests = {str(p["id"]): Pest(UUID(p["id"]), p["name"]) for p in data_pests}

        for r in data_regions:
            parent = self.regions.get(str(r.get("parent_region_id"))) if r.get("parent_region_id") else None
            size = r.get("size", None)
            self.regions[str(r["id"])] = Region(UUID(r["id"]), r["name"], size, parent)

        for p in data_products:
            thresholds = []
            for t in p["thresholds"]:
                pest = self.pests[str(t["pest_id"])]
                thresholds.append(ProductThreshold(pest, t["minimum_occurrence"], t["dose_per_hectare"]))
            product = Product(UUID(p["id"]), p["name"], p["cost_per_dose"], thresholds)
            self.products.append(product)

        for o in data_occurrences:
            pest = self.pests[str(o["pest_id"])]
            region = self.regions[str(o["region_id"])]
            loc = o["location"]
            location = (loc["latitude"], loc["longitude"])
            created_at = datetime.fromisoformat(o["created_at"])
            occurrence = PestOccurrence(UUID(o["id"]), pest, created_at, location, region)
            self.occurrences.append(occurrence)

    def generate_recommendations(self):
        ocorrencias_por_regiao = {}
        for oc in self.occurrences:
            key = (oc.region.id, oc.pest.id)
            ocorrencias_por_regiao[key] = ocorrencias_por_regiao.get(key, 0) + 1

        print("\n *------ Recomendacoes de Aplicacao ------* \n")
        for (region_id, pest_id), count in ocorrencias_por_regiao.items():
            region = self.regions[str(region_id)]
            pest = self.pests[str(pest_id)]
            print(f"Regiao: {region.name} - Praga: {pest.name} - Ocorrencias: {count}")

            for product in self.products:
                if product.should_apply(pest, count):
                    dose = product.calculate_dose(pest, count, region.size or 0.0)
                    custo = product.calculate_cost(pest, count, region.size or 0.0)
                    print(f" - Produto: {product.name} | Dose: {dose} | Custo: R${custo:.2f}")
            print()