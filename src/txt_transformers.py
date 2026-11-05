from utils import to_mx, clean_string
#Nesting - lista de diccioanrios 
raw = [
    {"name": "         AnA    ", "activate": True, "cash": "120.50"},
    {"name": "        LuIs   ", "activate": True, "cash": "0"},
    {"name": "         mara    ", "activate": True, "cash": "99.99"},
]


def clean(row: dict) -> dict:
    """
    this fuction return a 
    formatted dictioanary
    """
    return {
        "name": clean_string(row["name"]),
        "activate": bool(row["activate"]),
        "cash_mnx":  to_mx(row["cash"]),
    }


# dale caña 
# List comprehension

clean_data = [clean(r) for r in raw]

print("\n\nlista original: \n", raw)
print("\n\nlista formateada: \n", clean_data)