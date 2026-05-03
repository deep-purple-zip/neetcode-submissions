def divide_numbers(a: str, b: str) -> None:
    try:
        print(int(a) / int(b))
    except Exception as exc:
        print(f"An error occurred: {exc}")


# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
