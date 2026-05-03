def remove_keys(my_dict: dict[str, int], keys: list[str]) -> dict[str, int]:
    return {
        key: value
        for key, value in my_dict.items()
        if key not in keys
        # else del my_dict[key]
    }


# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
