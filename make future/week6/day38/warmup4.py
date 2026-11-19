def is_valid_row(row, required_fields):
    """Return (True, None) if row is good.
       Return (False, reason_string) if row is bad."""
    for field in required_fields:
        if field not in row or row[field] is None:
            return (False, f"missing field: {field}")
    for field in required_fields:
        if not row[field].strip():
            return (False, f"empty field: {field}")
    if None in row:  # extra columns under key None
        return (False, "extra columns")
    return (True, None)

row = {"name": None, "phone":"123"}
print(is_valid_row(row,["name", "phone"]))
