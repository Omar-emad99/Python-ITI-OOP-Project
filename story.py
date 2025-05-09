from classes import Person, Employee, Car, Office

def story_mode():
    print("=== Story Mode ===")
# 1) Create Samy's Car
    car = Car(name="Fiat 128", fuel_rate=100, velocity=80)  

# 2) Create Samy as a Person/Employee
    samy = Employee(
        name="Samy",
        money=1000,
        mood="neutral",
        health_rate=80,
        emp_id="ITI123",
        email="samy@iti.org",
        salary=5000,
        car=car,
        distance_to_work=20  
    )

# 3) Create ITI Office and hire Samy
    iti_office = Office("ITI Smart Village")
    iti_office.hire(samy)

    print(f"\nStory: {samy.name} is an Employee. He works at {iti_office.name} and has a {samy.car.name}.")
    print("He goes every day (except weekends) to the ITI Smart Village Office by his Fiat 128 car.\n")

    while True:
        print("\n--- Story Actions ---")
        print("1. Drive to work")
        print("2. Check if Samy is late")
        print("3. Refuel car")
        print("4. Samy eats")
        print("5. Samy sleeps")
        print("6. Show Samy's status")
        print("0. Exit Story Mode")

        choice = input("Choose an action: ")

        if choice == "1":
            samy.drive()
        elif choice == "2":
            move_hour = float(input("At what hour did Samy leave home? (e.g., 7.5): "))
            iti_office.check_lateness(samy.id, move_hour)
        elif choice == "3":
            amount = float(input("Enter fuel amount to refuel: "))
            samy.refuel(amount)
        elif choice == "4":
            meals = int(input("How many meals did Samy eat today? (1-3): "))
            samy.eat(meals)
        elif choice == "5":
            hours = int(input("How many hours did Samy sleep? "))
            samy.sleep(hours)
        elif choice == "6":
            print(f"\n--- {samy.name}'s Status ---")
            print(f"Money: {samy.money}")
            print(f"Salary: {samy.salary}")
            print(f"Mood: {samy.mood}")
            print(f"Health: {samy.health_rate}")
            print(f"Fuel: {samy.car.fuel_rate}")
            print(f"Car velocity: {samy.car.velocity}")
        elif choice == "0":
            print("Exiting Story Mode.")
            break
        else:
            print("Invalid option, please try again.")
            
story_mode()