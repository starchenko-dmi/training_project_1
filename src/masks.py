def get_mask_card_number(card_number: int) -> str:
    """Возврашает маску номера карты"""
    if len(str(card_number)) == 16:
        return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    else:
        raise ValueError('Не верный номер карты')


def get_mask_account(account: int) -> str:
    """Возврашает маску номера счета"""
    if len(str(account)) == 20:
        return f"**{str(account)[-4:]}"
    else:
        raise ValueError('Не верный номер счета')
