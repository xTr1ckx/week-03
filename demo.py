from utils import capitalize, truncate, count_words, clamp, is_prime, factorial, total, average
from validators import is_email, is_phone_number, is_valid_age, is_strong_password, is_valid_date

def demo_utils():
    print("# === Utils demonstrācija ===")

    print(f"# capitalize('hello') → '{capitalize('hello')}'")
    print(f"# clamp(15, 0, 10) → {clamp(15, 0, 10)}")
    print(f"# is_prime(17) → {is_prime(17)}")
    print(f"# average([10, 20, 30]) → {average([10, 20, 30])}")

    try:
        factorial(-1)
    except ValueError as e:
        print(f"# factorial(-1) → ValueError: {e}")

    print("#")

def demo_validators():
    print("# === Validators demonstrācija ===")

    print(f"# is_email('test@test.lv') → {is_email('test@test.lv')}")
    print(f"# is_email('test@') → {is_email('test@')}")
    print(f"# is_strong_password('abc') → {is_strong_password('abc')}")
    print(f"# is_strong_password('abc12345') → {is_strong_password('abc12345')}")
    print(f"# is_valid_date('2025-13-01') → {is_valid_date('2025-13-01')}")
    print(f"# is_valid_date('2025-12-01') → {is_valid_date('2025-12-01')}")


if __name__ == "__main__":
    demo_utils()
    demo_validators()