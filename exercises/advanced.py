'''Avancerade övningar.'''

def factorial(x):
    '''Faktorisera ett tal.

    Returnera en lista med alla faktorer för talet `x`.
    '''
#for x in range(0, x):
#    if x%2.isdigit
#        return prime
#    else:
    primes = []
    test = 2
    if x==1:
        return[1]
    else:
        while x > 1:
            if x % test == 0:
                x = x / test
                primes.append(test)
            else:
                test += 1
        return primes



def yahtzee_score(dice, round):
    '''Räkna ut den högsta godkända poäng för den aktuella rundan.

    Argumentet `dice` är en lista med fem heltal med värden 1 till och med 6.
    Argumentet `round` är en sträng med något av värdena i tabellen nedan.

    Runda       Värde
    -----------------
    Ettor       'aces'
    Tvåor       'twos'
    Treor       'threes'
    Fyror       'fours'
    Femmor      'fives'
    Sexor       'sixes'

    Triss       'three_of_a_kind'
    Fyrtal      'four_of_a_kind'
    Kåk         'full house'
    Liten stege 'small_straight'
    Stor stege  'large_straight'
    Yatzy       'yahtzee'
    Chans       'chance'
    '''
    ettor = 0
    tvåor = 0
    treor = 0
    fyror = 0
    femmor = 0
    sexor = 0
    for nummer in dice:
        if nummer == 1:
            ettor +=1
        if nummer == 2:
            tvåor +=1
        if nummer == 3:
            treor += 1
        if nummer == 4:
            fyror +=1
        if nummer == 5:
            femmor +=1
        if nummer == 6:
            sexor +=1



    if round == 'yahtzee':
        if ettor or tvåor or treor or fyror or femmor or sexor == 5:
            return 50
    elif round == 'large_straight':
        if 6 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
            return 20
    elif round == 'small_straight':
        if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
            return 15
    elif round == 'triss':
        if sexor == 3:
            return 3 * 6
        if femmor == 3:
            return 3 * 5
        if fyror == 3:
            return 3 * 4
        if treor == 3:
            return 3 * 3
        if tvåor == 3:
            return 3 * 2
        if ettor == 3:
            return 3 * 1

    elif round == 'aces':
            return sum(ettor)
    elif round == 'twos':
            return sum(tvåor)
    elif round == 'threes':
            return sum(treor)
    elif round == 'fours':
            return sum(fyror)
    elif round == 'fives':
            return sum(femmor)
    elif round == 'sixes':
            return sum(sexor)

def blackjack_score(cards):
    '''Räkna ut poängen för en korthand i blackjack.

    Argumentet cards anges som lista med strängar där varje sträng representerar
    ett kort. En sådan sträng består av en färg, ett bindestreck och en valör.

    Färg    Sträng          Valör   Sträng
    --------------          --------------
    Hjärter H               Ess     E
    Ruter   R               2-10    2-10
    Klöver  K               Knekt   Kn
    Spader  S               Dam     D
                            Kung    K

    Till exempel representeras klöver fem som 'K-5' och spader ess som 'S-E'.

    Om en hand innehåller ess ska den räknas på det sätt som är mest
    fördelaktigt för spelaren.
    '''
    pass
