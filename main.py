def temperature_status(temp: float) -> str:
    return "cool" if temp > 100 else "idle"


def main() -> None:
    try:
        temp = float(input("Enter temperature: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    print(temperature_status(temp))


if __name__ == "__main__":
    main()
