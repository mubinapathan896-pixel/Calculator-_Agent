SAFETY_LIMIT = 100.0


def temperature_command(temperature: float) -> str:
    return "COOL" if temperature > SAFETY_LIMIT else "IDLE"


def main() -> None:
    print("Command agent started. Enter q to quit.")

    while True:
        entry = input("Enter temperature: ").strip()
        if entry.lower() in {"q", "quit"}:
            print("Command agent stopped.")
            break

        try:
            temperature = float(entry)
        except ValueError:
            print("Please enter a valid number, or q to quit.")
            continue

        command = temperature_command(temperature)
        print(f"Temperature: {temperature:g} | Command: {command}")


if __name__ == "__main__":
    main()