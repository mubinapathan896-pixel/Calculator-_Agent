VALID_ACTIONS = {"COOL", "IDLE"}


def handle_action(action: object) -> dict[str, str]:
    if not isinstance(action, str):
        return {
            "error": "invalid_action",
            "message": "Action must be a string.",
            "received": repr(action),
        }

    normalized_action = action.strip().upper()
    if normalized_action not in VALID_ACTIONS:
        return {
            "error": "invalid_action",
            "message": "Action must be COOL or IDLE.",
            "received": action,
        }

    return {"status": "ok", "action": normalized_action}


def main() -> None:
    print("Action validator started. Enter q to quit.")

    while True:
        action = input("Enter action (COOL or IDLE): ").strip()
        if action.lower() in {"q", "quit"}:
            print("Action validator stopped.")
            break

        print(handle_action(action))


if __name__ == "__main__":
    main()