import random

def generate_secret(low=1, high=100):
    """Ģenerē nejaušu skaitli"""
    return random.randint(low, high)

def check_guess(guess, secret):
    """Pārbauda minējumu un atgriež atbildi, balstoties uz minējumu"""
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "too_low"
    else:
        return "too_high"
    
def is_game_over(attempts, max_attempts=10):
    """Pārbauda vai spēle ir beigusies"""
    return attempts >= max_attempts

if __name__ == "__main__":
    secret = generate_secret()
    print("Secret:", secret)
    print(check_guess(50, secret))
    print(is_game_over(10))