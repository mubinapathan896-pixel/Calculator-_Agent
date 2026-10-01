SAFETY_LIMIT = 100.0


def main() -> None:
	print("Termination agent started. Enter q to stop manually.")

	while True:
		entry = input("Enter current temperature: ").strip()
		if entry.lower() in {"q", "quit"}:
			print("Agent stopped manually.")
			break

		try:
			temperature = float(entry)
		except ValueError:
			print("Please enter a valid number, or q to quit.")
			continue

		if temperature > SAFETY_LIMIT:
			print(f"Temperature: {temperature:g} | Agent action: cool")
			continue

		print(f"Temperature: {temperature:g} | Agent action: idle")
		print("Safety limit reached. Terminating agent.")
		break


if __name__ == "__main__":
	main()
