from models import customer_models


def concatenate_strings(string_1: str, string_2: str) -> str:
        return  (string_1.strip() + ' ' + string_2.strip()).strip()
# написати функцію яка зєднуватиме дві стрічки через пробіл (лишні прибирає) і повертає нову стрічку

def clean_name(name:str) -> str:
        return name.strip().title()