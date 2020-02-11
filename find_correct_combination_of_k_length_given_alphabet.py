global_mon = ""
global_bool = False

def is_valid(secret, guess):
    return secret == guess

def gen_guesses(set, guess, guess_len, alpha_len, secret_len, secret):
    global global_mon
    global global_bool

    if is_valid(secret, guess):
        global_mon = guess
        global_bool = True
    else:
        for i in range(alpha_len):
            if not global_bool and guess_len <= secret_len:
                new_guess = guess + set[i]
                gen_guesses(set, new_guess, guess_len + 1, alpha_len, secret_len, secret)
            else:
                break
    return

gen_guesses(["a", "b", "c"], "", 0, 3, 2, "ab")
print(global_mon)

global_mon = ""
global_bool = False

gen_guesses(["a", "b", "c", "f", "4"], "", 0, 3, 3, "ccb")
print(global_mon)
