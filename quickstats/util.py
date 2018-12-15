def bytes_to_human(bytes_val: int) -> str:
    """
    Convert a numerical bytes value to a human readble string
    e.g. 10240 -> "10 K"
    """

    if not isinstance(bytes_val, (int, float)):
        raise ValueError("Input must be an integer or float")

    if bytes_val < 0:
        raise ValueError("Negative not supported")

    units = ["", "K", "M", "G", "T", "P", "E"]

    for unit in units:
        if bytes_val < 1024:
            if unit == "":
                return "{:.2f}".format(bytes_val)
            else:
                return "{:.2f} {}".format(bytes_val, unit)
        bytes_val /= 1024
