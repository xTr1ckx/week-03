def is_email(text):
    """
    Description
    -----------
    Pārbauda vai e-pasts ir pareizi strukturēts (e-pastam ir @, pirms un pēc @ ir teksts, e-pastam ir . un pēc . ir vismaz divi burti)

    Args
    ----
    text (str): Lietotāja e-pasts
    
    Returns
    -------
    bool: True, ja e-pasts atbilst prasībām, False, ja neatbilst
    
    Example
    -------
    >>> is_email("edgars@gmail")
    is_email("edgars@gmail") → False
    
    """
    if not isinstance(text, str):
        return False
    
    if text.count("@") != 1:
        return False
    
    local, domain = text.split("@")

    if local == "" or domain == "":
        return False
    
    if "." not in domain:
        return False
    
    parts = domain.rsplit(".", 1)
    if len(parts) != 2:
        return False
    
    domain_name, domain_ext = parts

    if domain_name == "" or len(domain_ext) < 2:
        return False
    
    return True

def is_phone_number(text):
    """
    Description
    -----------
    Pārbauda Latvijas telefona numuru formātu: +371 XXXXXXXX

    Args
    ----
    text (str): Telefona numurs

    Returns
    -------
    bool: True, ja numurs atbilst Latvijas standartam, False, ja neatbilst

    Example
    -------
    >>> is_phone_number("27555191")
    is_phone_number("27555191") → False
    """
    if not isinstance(text, str):
        return False

    if not text.startswith("+371 "):
        return False

    digits = text[5:]
    return digits.isdigit() and len(digits) == 8

def is_valid_age(age):
    """
    Description
    -----------
    Pārbauda cilvēka vecumu (no 0-150)

    Args
    ----
        age (int): Vecums

    Returns
    -------
        bool: True, ja vecums ir ticams, False, ja nav

    Example
    -------
    >>> is_valid_age(18)
    is_valid_age(18) → True
    """
    if not isinstance(age, int):
        return False
    return 0 <= age <= 150

def is_strong_password(text):
    """
    Description
    -----------
    Pārbauda vai parole ir derīga (vismaz 8 simboli, satur burtus un ciparus)

    Args
    ----
    text (str): Parole

    Returns
    -------
    bool: True, ja derīga, False, ja nederīga

    Example
    -------
    >>> is_strong_password("banans")
    is_strong_password("banans") → False
    """
    if not isinstance(text, str):
        return False

    if len(text) < 8:
        return False

    has_letter = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)

    return has_letter and has_digit

def is_valid_date(text):
    """
    Description
    -----------
    Pārbauda datuma formātu (YYYY-MM-DD)

    Args
    ----
    text (str): Ievadītais datums

    Returns
    -------
    bool: True, ja atbilst formatēšanas nosacījumam, False, ja nē

    Example
    -------
    >>> is_valid_date("2026-02-24")
    is_valid_date("2026-02-24") → True
    """
    if not isinstance(text, str):
        return False

    parts = text.split("-")
    if len(parts) != 3:
        return False

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    return 1 <= month <= 12 and 1 <= day <= 31

if __name__ == "__main__":
    emails = ["edgars@inbox.lv", "edgars.slipais@domain.com", "edgars@", "@inbox.lv", "edgars@domain"]
    for e in emails:
        print(f"# is_email('{e}') → {is_email(e)}")

    phone_numbers = ["+371 21234567", "26123456", "+371 123"]
    for n in phone_numbers:
        print(f"# is_phone_number('{n}') → {is_phone_number(n)}")

    valid_age = [24, -12, 175]
    for a in valid_age:
        print(f"# is_valid_age('{a}') → {is_valid_age(a)}")

    valid_password = ["abc12345", "abc123", "password", "12345678"]
    for p in valid_password:
        print(f"# is_strong_password('{p}') → {is_strong_password(p)}")

    valid_date = ["2026-02-24", "2026-13-01", "24-02-2026"]
    for d in valid_date:
        print(f"# is_valid_date('{d}') → {is_valid_date(d)}")