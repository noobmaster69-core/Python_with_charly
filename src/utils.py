"""
Utilileria de limpieza y conversió
"""
def to_mx(value,rate = 18.58) -> float:
    """
    this fuction converts valor (dls)
    to mxn via tasa
    """
    return float(value)*float(rate)

def clean_string(name: str) -> str:
    """
    this fuctioni clean name
    """
    return"" .join(name.strip().title().split()) 

# name: " CarlOs       AnTonio  TOvar GarcIa   "
#strip -> # name: "CarlOs       AnTonio  TOvar GarcIa"
#title -> #name: "Carlos    Antonio  Tovar Garcia"
#split -> #name: ["Carlos", "Antonio",  "Tovar", "Garcia"]
