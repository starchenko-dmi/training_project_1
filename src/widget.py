from masks import get_mask_account, get_mask_card_number


def mask_account_card(account: str) -> str:
    """извлекает и строкового значения номер карты или счета и возвращает маску"""
    words = account.split()
    name: list[str] = []
    for word in words:
        if word.isdigit() and len(word) == 16:
            return f"{" ".join(name)} {get_mask_card_number(int(word))}"
        elif word.isdigit() and len(word) == 20:
            return f"{" ".join(name)} {get_mask_account(int(word))}"
        else:
            name.append(word)


def get_date(date: str) -> str:
    """Декодирует дату и возврашает её в вормате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
