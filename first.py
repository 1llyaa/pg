def sudy(cislo: int) -> bool:
    if cislo % 2 > 0: return False 
    else: return True

def main():
   print(sudy(6))
   print(sudy(7))


def test_sudy():
    assert sudy(6) == True
    assert sudy(7) == False
    assert sudy(1000000000) == True
    assert sudy(1234384766812) == True

if __name__ == "__main__":
    main()

