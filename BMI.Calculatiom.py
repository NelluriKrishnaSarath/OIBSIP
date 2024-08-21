def calculate_bmi(weight, height_cm):
    """
    Calculate BMI using the formula: BMI = weight(kg) / (height(m) ** 2)

    Parameters:
    weight (float): Weight in kilograms
    height_cm (float): Height in centimeters

    Returns:
    float: The calculated BMI
    str: The BMI category
    """

    # Convert height from centimeters to meters
    height_m = height_cm / 100

    bmi = weight / (height_m ** 2)

    # Determine the BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    return bmi, category


def main():
    # Input: Weight in kilograms and height in centimeters
    weight = float(input("Enter your weight in kilograms: "))
    height_cm = float(input("Enter your height in centimeters: "))

    # Calculate BMI and determine the category
    bmi, category = calculate_bmi(weight, height_cm)

    # Output: Display the BMI and its category
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")


if __name__ == "__main__":
    main()
