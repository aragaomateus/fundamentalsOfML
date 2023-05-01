class Car:
    def __init__(self, model, total_cars):
        self.model = model
        self.total_cars = total_cars
        self.cars_rented = 0

    def __str__(self):
        return f"{self.model} ({self.total_cars - self.cars_rented} available out of {self.total_cars})"


class Customer:
    def __init__(self, customer_number, name):
        self.customer_number = customer_number
        self.name = name

    def __str__(self):
        return f"Customer {self.customer_number}: {self.name}"


class Rental:
    def __init__(self, customer, car):
        self.customer = customer
        self.car = car
        car.cars_rented += 1

    def __str__(self):
        return f"Rental: {self.customer} rented {self.car}"


def rent(customer, car, rental_list):
    if car.cars_rented < car.total_cars:
        rental = Rental(customer, car)
        rental_list.append(rental)
    else:
        print(f"Sorry, all {car.model}s are rented out.")
    return rental_list


def car_return(customer, car, rental_list):
    for rental in rental_list:
        if rental.customer == customer and rental.car == car:
            car.cars_rented -= 1
            rental_list.remove(rental)
            break
    else:
        print("No matching rental found.")
    return rental_list
def print_rentals(rental_list):
    if not rental_list:
        print("No cars rented.")
        return

    print("Current rentals:")
    for rental in rental_list:
        print(rental)


Corolla=Car("Toyota Corolla",2) # add object representing two Toyota Corollas 
JohnMiller=Customer(1,"John Miller") # create customer object for John Miller 
SusanChen=Customer(2,"Susan Chen") # create customer object for Susan Chen 
DonMikulski=Customer(3,"Don Mikulski") # create customer object for Don Mikulski 
print(Corolla) # print Corolla object
print(DonMikulski) # print Don Mikulski object
rented=[] # set list of rental objects to empty 
rented=rent(DonMikulski,Corolla,rented) # try to have Don Mikulski rent a Corolla
rented=rent(JohnMiller,Corolla,rented) # try to have John Miller rent a Corolla 
rented=rent(SusanChen,Corolla,rented) # try to have Susan Chen rent a Corolla 
print_rentals(rented) # print current rentals 
rented=car_return(JohnMiller,Corolla,rented) # try to have John Miller return a Corolla 
rented=car_return(SusanChen,Corolla,rented) # try to have Susan Chen return a Corolla 
print(Corolla) # print Corolla object
print_rentals(rented) # print current rentals
