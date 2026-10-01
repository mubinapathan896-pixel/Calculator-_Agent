TEMPERATURES = [80.0, 100.0, 101.0, 120.0]


def debug_agent(temperatures: list[float]) -> list[str]:
    log: list[str] = []
    index = 0

    while index < len(temperatures):
        temperature = temperatures[index]
        action = "cool" if temperature > 100 else "idle"
        log.append(
            f"Step {index + 1}: temperature={temperature:g}, action={action}"
        )
        index += 1

    return log


def main() -> None:
    for entry in debug_agent(TEMPERATURES):
        print(entry)


if __name__ == "__main__":
    main()