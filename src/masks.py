def get_mask_card_number(card_number: int) -> str:
    """Возврашает маску номера карты"""
    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account: int) -> str:
    """Возврашает маску номера счета"""
    return f"**{str(account)[-4:]}"

