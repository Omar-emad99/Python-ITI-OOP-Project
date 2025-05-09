class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    @property
    def health_rate(self):
        return self._health_rate

    @health_rate.setter
    def health_rate(self, health):
        if health < 0:
            self._health_rate = 0
        elif health > 100:
            self._health_rate = 100
        else:
            self._health_rate = health

    def sleep(self, hours):
        if hours < 7:
            self.mood = "tired"
        elif hours == 7:
            self.mood = "happy"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate += self.health_rate * 1
        elif meals == 2:
            self.health_rate += self.health_rate * 0.75
        elif meals == 1:
            self.health_rate += self.health_rate * 0.5
        else:
            print("Not a normal meals number")
            
    def buy(self, items):
        if self.money < 10:
            print("not enough money")
            return
        if items == 0:
            print("no items bought")
        for i in range(items):
            if self.money < 0:
                print("not enough money")
                break
            else:
                self.money -=10
        print(f"Bought items {i+1}")
#------------------------------------------------------------------------------------------------------------
class Employee(Person):
    def __init__(self, name, money, mood, health_rate, emp_id, email, salary, car, distance_to_work=20):
        super().__init__(name, money, mood, health_rate)
        self.id = emp_id
        self.email = email
        self.salary = max(300, salary)
        self.car = car
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours > 8:
            self.mood = "tired"
        elif hours == 8:
            self.mood = "happy"
        else:
            self.mood = "lazy"

    def drive(self):
        self.car.run(self.car.velocity, self.distance_to_work)

    def refuel(self, gasAmount=100):
        self.car.fuel_rate = min(100, self.car.fuel_rate + gasAmount)
        print(f"Refueled to {self.car.fuel_rate} L.")
        if self.car.remaining_distance > 0:
            print("Attempting to continue remaining journey...")
            self.car.run(self.car.velocity, self.car.remaining_distance)
#------------------------------------------------------------------------------------------------------------
class Car:
    refueled = 0
    remaining_dist = 0
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = fuel_rate
        self.velocity = velocity  
        self.remaining_distance = 0

    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, fuel):
        if fuel < 0:
            self._fuel_rate = 0
        elif fuel > 100:
            self._fuel_rate = 100
        else:
            self._fuel_rate = fuel

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, vel):
        if vel < 0:
            self._velocity = 0
        elif vel > 200:
            self._velocity = 200
        else:
            self._velocity = vel

    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_per_meter = 0.001  
        total_meters = distance * 1000
        meters_traveled = 0

        while meters_traveled < total_meters:
            if self.fuel_rate <= 0:
                self.fuel_rate = 0
                remaining_km = (total_meters - meters_traveled) / 1000
                self.remaining_distance = remaining_km
                self.stop(remaining_km)
                return
            self.fuel_rate -= fuel_per_meter
            meters_traveled += 1

        self.remaining_distance = 0
        self.stop(0)

    def stop(self, remain_distance):
        if remain_distance > 0:
            print(f"Stopped before destination. Remaining distance: {remain_distance:.2f} km")
        else:
            print("Arrived at destination!")
#------------------------------------------------------------------------------------------------------------
class Office:
    employees_num = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        if not self.employees:
            print("No employees found.")
            return None
        else:
            print("\nEmployees in the office:")
            for emp in self.employees:
                print(f"ID: {emp.id}, Name: {emp.name}, Email: {emp.email} \n")
        
    def get_employee(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                return employee
            else:
                print("Not an Employee ! \n")     
                return None

    def hire(self, employee):
        for emp in self.employees:
            if emp.id == employee.id:
                print(f"Employee with ID {employee.id} is already hired.")
                return
        self.employees.append(employee)
        Office.employees_num += 1
        print(f"Employee {employee.name} has been hired successfully.")

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            Office.employees_num -= 1

    def deduct(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= amount

    def reward(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += amount

    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if emp:
            is_late = Office.calculate_lateness(9, move_hour, emp.distance_to_work, emp.car.velocity)
            if is_late:
                print(f"Employee {emp.name} is late.")
                self.deduct(emp_id, 10)
            else:
                print(f"Employee {emp.name} is on time.")
                self.reward(emp_id, 10)

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        travel_time = distance / velocity
        arrival_time = move_hour + travel_time
        if arrival_time <= target_hour:
            return False
        else:
            return True

    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num
        