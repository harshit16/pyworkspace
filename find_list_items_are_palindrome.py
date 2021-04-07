# Check items in list palindrome or not: 

candidates = [
    # Valid
    "racecar", 
    "Kayak",
    "never odd or even",
    "rats live on no evil star",
    "A Toyota! Race fast... safe car: a Toyota",
    "Some men interpret nine memos",
    # Invalid
    "wombat",
    "No lemons, one melon", # lemons, one->lemon, no
    "Too bad – I hid a book", # book->boot
    "No trace; not one cartoon", # cartoon->carton
    "Ma'am, I'm Adam", # Ma'am->Madam
    "Del was a sled", # was->saw
    "Flee to Em, remote elf", # Em->me
    "Ma? Ha! A sham!" # Ha! A sham->Has a ham
]

def is_palindrome(candidate: str) -> bool:
    candidate = candidate.replace(" ", "")
    candidate = candidate.casefold()
    new_string = ''.join(e for e in candidate if e.isalnum())
    rev_string = ''.join(reversed(new_string))
    if new_string == rev_string:
        return True
    else:
        return  False
        
    #return flag

for candidate in candidates:
    print(f'{candidate}: {is_palindrome(candidate)}')
