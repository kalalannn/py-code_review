import array
from product import Product
from address import Address
from product_repository import ProductRepository
from cache_repository import CacheRepository

class ProductQualifier:
    availableProducts: array.array[Product] = []
    address: Address

    def __init__(self, address:Address):
        self.address = address

    def getAvailableProducts(self) -> array.array[Product]:
        primarySource: ProductRepository = ProductRepository()
        primaryProducts = primarySource.getProducts(self.address)

        for element in primaryProducts:
            add: bool = True
            for availableProduct in self.availableProducts:
                if availableProduct.id == element.id:
                    add = False

            if (add):
                self.availableProducts.append(element)
            else:
                print('Product already exists.')

        cacheSource: CacheRepository = CacheRepository()
        cachedProducts = cacheSource.getKey(self.address.fullAddressName)

        for element in cachedProducts:
            add: bool = True
            for availableProduct in self.availableProducts:
                if availableProduct.id == element.id:
                    add = False

            if (add):
                self.availableProducts.append(element)
            else:
                print('Product already exists.')

        cacheEfficiency = cachedProducts.length / (cachedProducts.length + primaryProducts.length)
        print('Cache efficiency: {efficiency}'.format(efficieny=cacheEfficiency))

        return self.availableProducts

    def getAddressCategory(self) -> str:
        if (len(self.availableProducts) > 2):
            return 'A'
        elif (len(self.availableProducts) > 4):
            return 'B'
        else:
            return 'C'