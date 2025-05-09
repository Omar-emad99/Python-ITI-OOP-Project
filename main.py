from classes import Person, Employee, Car, Office

def run():
# Create Person
    print("=== Create Person ===")
    name = input("Enter name: ")
    money = float(input("Enter money: "))
    mood = input("Enter mood: ")
    health_rate = float(input("Enter health rate (0-100): "))
    person = Person(name, money, mood, health_rate)

    employee = None
    office = None

    while True:
        print("\n--- Person Menu ---")
        print("1. Eat")
        print("2. Sleep")
        print("3. Buy items")
        print("4. Show status")
        print("5. Hire as employee")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            meals = int(input("How many meals did you eat today? (1-3): "))
            person.eat(meals)
            print(f"Health rate now: {person.health_rate}")
        elif choice == "2":
            hours = int(input("How many hours did you sleep? "))
            person.sleep(hours)
            print(f"Mood after sleeping: {person.mood}")
        elif choice == "3":
            items = int(input("How many items do you want to buy? "))
            person.buy(items)
            print(f"Remaining money: {person.money}")
        elif choice == "4":
            print(f"\n--- {person.name}'s Status ---")
            print(f"Money: {person.money}")
            print(f"Mood: {person.mood}")
            print(f"Health: {person.health_rate}")
        elif choice == "5":
# Promote to Employee
            print("\n=== Enter Car Info ===")
            car_name = input("Enter car name: ")
            fuel_rate = float(input("Enter initial fuel rate (0-100): "))
            velocity = float(input("Enter car velocity (km/h): "))
            car = Car(car_name, fuel_rate, velocity)

            print("\n=== Enter Employee Info ===")
            emp_id = input("Enter employee ID: ")
            email = input("Enter employee email: ")
            salary = float(input("Enter salary: "))
            distance = float(input("Enter distance to work (km): "))

            employee = Employee(person.name, person.money, person.mood,
                                person.health_rate, emp_id, email, salary, car, distance)

            print("\n=== Create Office ===")
            office_name = input("Enter office name: ")
            office = Office(office_name)
            office.hire(employee)

            print(f"{employee.name} has been hired at {office.name}!")
            break
        elif choice == "0":
            print("Exiting system.")
            return
        else:
            print("Invalid choice. Try again.")

# After hiring — now show the full employee menu
    while True:
        print("\n--- Employee Menu ---")
        print("1. Drive to work")
        print("2. Refuel car")
        print("3. Check lateness")
        print("4. Work (change mood)")
        print("5. Sleep")
        print("6. Eat")
        print("7. Buy items")
        print("8. Show employee status")
        print("9. Fire employee")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee.drive()
        elif choice == "2":
            amount = float(input("Enter amount of gas to refuel: "))
            employee.refuel(amount)
        elif choice == "3":
            move_hour = float(input("Enter move hour (e.g., 7.5 for 7:30 AM): "))
            office.check_lateness(employee.id, move_hour)
        elif choice == "4":
            hours = int(input("Enter number of hours worked: "))
            employee.work(hours)
        elif choice == "5":
            hours = int(input("How many hours did you sleep? "))
            employee.sleep(hours)
            print(f"Mood after sleeping: {employee.mood}")
        elif choice == "6":
            meals = int(input("How many meals did you eat today? (1-3): "))
            employee.eat(meals)
            print(f"Health rate now: {employee.health_rate}")
        elif choice == "7":
            items = int(input("How many items do you want to buy? "))
            employee.buy(items)
            print(f"Remaining money: {employee.money}")
        elif choice == "8":
            print(f"\n--- {employee.name}'s Status ---")
            print(f"Money: {employee.money}")
            print(f"Salary: {employee.salary}")
            print(f"Mood: {employee.mood}")
            print(f"Health: {employee.health_rate}")
            print(f"Fuel: {employee.car.fuel_rate}")
            print(f"Car velocity: {employee.car.velocity}")
        elif choice == "9":
            office.fire(employee.id)
            print("Employee has been fired.")
        elif choice == "0":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Try again.")

run()