# Virkņu funkcijas

def capitalize(text):
    """
    Description
    -----------
    Nomaina teksta pirmā vārda pirmo burtu uz lielo burtu.

    Args
    ----
    text (str): Lietotāja teksts
    
    Returns
    -------
    str: Teksts ar pirmo lielo burtu
    
    Example
    -------
    >>> capitilize("hello")
    Hello
    
    """
    if not isinstance(text, str):
        raise TypeError("Tekstam ir jābūt string!")
    if text == "":
        return text
    return text[0].upper() + text[1:]

def truncate(text, max_len=20):
    """
    Description
    -----------
    Apgriež tekstu un pievieno "..." galā, ja teksts ir garāks par max_len.

    Args
    ----
    text (str): Lietotāja teksts
    max_len (int): Maksimālais teksta garums (20 pēc noklusējuma)
    
    Returns
    -------
    str: Apgriezts teksts
    
    Example
    -------
    >>> truncate("Hello world", 5)
    Hello...
    """
    if not isinstance(text, str):
        raise TypeError("Tekstam ir jābūt string!")
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."

def count_words(text):
    """
    Description
    -----------
    Saskaita vārdus tekstā.

    Args
    ----
    text (str): Lietotāja teksts
    
    Returns
    -------
    int: Vārdu daudzums tekstā
    
    Example
    -------
    >>> count_words("Hello world")
    2
    """
    if not isinstance(text, str):
        raise TypeError("Tekstam ir jābūt string!")
    return len(text.split())

# Skaitļu funkcijas

def clamp(num, low, high):
    """
    Description
    -----------
    Ierobežo skaitli norādītajā diapazonā.

    Args
    ----
    num (int vai float): Skaitlis, ko ierobežot
    low (int vai float): Minimālā robeža
    high (int vai float): Maksimālā robeža
    
    Returns
    -------
    int vai float: Ierobežotā vērtība
    
    Example
    -------
    >>> clamp(15, 0, 10)
    10
    """
    return max(low, min(num, high))

def is_prime(num):
    """
    Description
    -----------
    Nosaka vai ievadītais skaitlis ir pirmskaitlis.

    Args
    ----
    num (int): Skaitlis, ko pārbaudīt
    
    Returns
    -------
    bool: True, ja ir pirmskaitlis, False, ja nav
    
    Example
    -------
    >>> is_prime(3)
    True
    """
    if not isinstance(num, int):
        raise TypeError("Skaitlim ir jābūt integer!")
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(n):
    """
    Description
    -----------
    Aprēķina faktoriālu ar validāciju n >= 0.

    Args
    ----
    n (int): Pozitīvs skaitlis
    
    Returns
    -------
    int: n!
    
    Example
    -------
    >>> factorial(4)
    24
    """
    if not isinstance(n, int):
        raise TypeError("Skaitlim ir jābūt veselam integer!")
    if n < 0:
        raise ValueError("Skaitlim ir jābūt lielākam vai vienādam ar 0!")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sarakstu funkcijas

def total(numbers):
    """
    Description
    -----------
    Sasummē visus saraksta skaitļus manuāli.

    Args
    ----
    numbers (list): Skaitļu saraksts
    
    Returns
    -------
    int vai float: Skaitļu summa
    
    Example
    -------
    >>> total(3, 6, 1)
    10
    """
    #if not isinstance(numbers, int, float):
        #raise TypeError("Visiem skaitļiem ir jābūt integer vai float!")
    s = 0
    for n in numbers:
        s += n
    return s

def average(numbers):
    """
    Description
    -----------
    Aprēķina vidējo aritmētisko

    Args
    ----
    numbers (list): Skaitļu saraksts
    
    Returns
    -------
    float: Vidējā skaitļu vērtība
    
    Example
    -------
    >>> average(2, 3, 7)
    4
    """
    #if not isinstance(numbers | int | float):
        #raise TypeError("Visiem skaitļiem ir jābūt integer vai float!")
    if len(numbers) == 0:
        raise ValueError("Saraksts nevar būt tukšs!")
    return total(numbers) / len(numbers)

# Demonstrācija

if __name__ == "__main__":
    print(capitalize("hello"))
    print(truncate("This is a very long text", 12))
    print(count_words("Hello Python world!"))

    print(clamp(15, 0, 10))
    print(is_prime(17))
    print(factorial(5))

    numbers = [1, 2, 3, 4, 6]
    print(total(numbers))
    print(average(numbers))