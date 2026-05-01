def farewell(name: str, /) -> None:
    print(f"Goodbye, {name}")


farewell("Bob")
farewell("Charlie")

# don't modify below this line
farewell("NeetCode")
