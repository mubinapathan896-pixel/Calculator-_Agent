SAFETY_LIMIT = 100.0
SAMPLE_TEMPERATURES = (80.0, 120.0)


def predict_two_step_agent() -> list[str]:
    predictions: list[str] = []

    for step, temperature in enumerate(SAMPLE_TEMPERATURES, start=1):
        action = "cool" if temperature > SAFETY_LIMIT else "idle"
        predictions.append(
            f"Step {step}: temperature={temperature:g}, predicted action={action}"
        )

    return predictions


def main() -> None:
    for prediction in predict_two_step_agent():
        print(prediction)


if __name__ == "__main__":
    main()