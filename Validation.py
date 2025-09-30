# validation.py
def validate_age_marks(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid entry")

def validate_data(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Invalid entry")
