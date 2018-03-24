import rps
import pytest
import subprocess
import sys

#Testy kontoluji, jestli jsou vstupy spravne (kamen, nuzky, papir)
def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True

def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True

def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True

#Testovani toho, co validni neni
def test_lizard_is_not_valid_play():
    assert rps.is_valid_play("lizard") is False

def test_spock_is_not_valid_play():
    assert rps.is_valid_play("spock") is False

#Testuju, jestli je validni to, co vraci pocitac (zase jen kamen, nuzky, papir)
def test_random_play_is_valid():
    for _ in range(100):
        play = rps.random_play()
        assert rps.is_valid_play(play)

def test_random_play_is_fairish():
    #test nemusi vzdy projit
    plays = [rps.random_play() for _ in range(1000)]    #1000x hraje pocitac
    #testuji, jestli z 1000 pokusu je aspon 100x rock, paper or scissors
    assert plays.count("rock") > 100
    assert plays.count("paper") > 100
    assert plays.count("scissors") > 100

def test_paper_beats_rock():
    assert rps.determine_game_result('paper', 'rock') == 'human'
    assert rps.determine_game_result('paper', 'scissors') == 'computer'
    assert rps.determine_game_result('rock', 'paper') == 'computer'
    assert rps.determine_game_result('rock', 'scissors') == 'human'
    assert rps.determine_game_result('scissors', 'rock') == 'computer'
    assert rps.determine_game_result('scissors', 'paper') == 'human'
    assert rps.determine_game_result('paper', 'paper') == 'tie'
    assert rps.determine_game_result('rock', 'rock') == 'tie'
    assert rps.determine_game_result('scissors', 'scissors') == 'tie'

#funkce, ktera bude vracet vsechnz fejky
def input_fake(fake):
    #falesna funkce input
    def input_fake_(prompt):
        print(prompt)
        return fake
    return input_fake_

#dekorator
@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors'])

#test na celou hru / fixtures
def test_whole_game(capsys, play):
    rps.main(input=input_fake(play)) #dependency injection
    out, err = capsys.readouterr()
    assert 'rock, paper or scissors?' in out
    assert ('computer wins' in out) or ('human wins' in out) or ('it is a tie!' in out)

def run_app(input):
    cp = subprocess.run([sys.executable, 'rps.py'], #sys.executable je python, ktery zrovna pouzivam
                        input=input,
                        encoding='utf-8',
                        stdout=subprocess.PIPE) #precteni
    return cp.stdout

def test_game_asks_again_if_wrong_input():
    assert run_app('adsf\nrock').count('rock, paper or scissors?') == 2 #byl to a6 treti pokus, nez se uzivatel strefil
    assert run_app('nic\njjj\nbla\npaper').count('rock, paper or scissors?') == 4
