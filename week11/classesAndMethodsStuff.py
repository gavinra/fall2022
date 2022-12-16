class Package:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def dropOff(self, driver):
        print(f"Delivered {self.name} weighing {self.weight} by {driver} of truck {truck.truckNumber}")

class AmazonTruck:
    packages = []
    driver = "nobody"

    def __init__(self, truckNumber):
        self.truckNumber = truckNumber
     
    def load(self, package):
        self.packages.append(package)   # add the package to the truck

    def deliver(self):
        for package in self.packages:
            package.dropOff(self.driver)
            
xbox = Package("xbox", "9 lbs")
tshirt = Package("tshirt", "0.5 lbs")
blades = Package("rollerblades", "6 lbs")


truck = AmazonTruck("589")
truck.driver = "Joe"
truck.load(xbox)
truck.load(tshirt)
truck.load(blades)
truck.deliver()
