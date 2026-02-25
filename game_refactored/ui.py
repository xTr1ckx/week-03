def get_player_guess():
    """Pieprasa lietotāja ievadi"""
    guess_input = input("# Tavs minējums: ")

    try:
        guess = int(guess_input)
    except ValueError:
        print("# Minējumam ir jābūt veselam skaitlim no 1 līdz 100!")
        return None
    
    if not(1 <= guess <= 100):
        print("# Minējumam ir jābūt veselam skaitlim no 1 līdz 100!")
        return None

    return guess

    #def valid_guess(guess):
        #return 1 <= guess <= 100
    
    #previous_guesses = set()

    #while True:

        #guess_input = input("# Tavs minējums: ")
    
        #try:
        #    guess = int(guess_input)
        #except ValueError:
        #    print("# Minējumam ir jābūt veselam skaitlim no 1 līdz 100!")
        #    return None

        #if guess in previous_guesses:
        #    print("# Jūs jau iepriekš minējāt šo skaitli.")
        #    return None
        #else:
        #    previous_guesses.add(guess)

        #if not valid_guess(guess):
        #    print("# Minējumam ir jābūt veselam skaitlim no 1 līdz 100!")
        #    return None

def show_hint(result):
    """Parāda padomu (augstāk vai zemāk)"""
    if result == "too_low":
        print("# Par mazu.")
    elif result == "too_high":
        print("# Par lielu.")

def show_game_over(secret, attempts, won):
    """Parāda beigu ziņojumu"""
    if won:
        print(f"# Pareizi! Skaitlis bija {secret}.")
        print(f"# Atbilde sasniegta {attempts} mēģinājumos.")
    else:
        print(f"# Mēģinājumu limits sasniegts! Minējamais skaitlis bija {secret}.")

def ask_play_again():
    """Jautā spēlētājam vai spēlēt vēlreiz"""
    answer = input("# Vai vēlaties spēlēt vēlreiz? (j/n): ").lower()
    return answer == "j"

if __name__ == "__main__":
    print(get_player_guess())
    show_hint("too_low")
    show_game_over(42, 5, True)
    print(ask_play_again())

    #CTRL + C lai apstādinātu programmu terminālī