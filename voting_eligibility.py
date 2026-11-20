def check_eligibility(name, age, citizenship):
    if age >= 18 and citizenship == "y":
        print(f"{name} is eligible to vote.")
        return True
    else:
        print(f"{name} is not eligible to vote.")

        if age < 18:
            years_left = 18 - age
            print(f"Years left to become eligible: {years_left}")

        if citizenship != "y":
            print("Reason: Not an Indian citizen.")

        return False


eligible_count = 0
not_eligible_count = 0

while True:
    name = input("Name: ")

    while True:
        try:
            age = int(input("Age: "))

            if 0 <= age <= 120:
                break
            else:
                print("Invalid age. Age must be between 0 and 120.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    while True:
        citizenship = input("Indian citizen (y/n): ").lower()

        if citizenship in ["y", "n"]:
            break
        else:
            print("Please enter y or n.")

    result = check_eligibility(name, age, citizenship)

    if result:
        eligible_count += 1
    else:
        not_eligible_count += 1

    again = input("Check another voter? (y/n): ").lower()

    if again != "y":
        break

print("\nVoters checked:", eligible_count + not_eligible_count)
print("Eligible:", eligible_count)
print("Not eligible:", not_eligible_count)