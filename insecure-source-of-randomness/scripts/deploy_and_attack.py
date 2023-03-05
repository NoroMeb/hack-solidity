from brownie import GuessTheRandomNumber, Attack, accounts
from web3 import Web3

def main():
    deploy_guess_the_random_number()
    deploy_attack()
    check_balance()
    attack()
    check_balance()

def deploy_guess_the_random_number():
    guess_the_random_number = GuessTheRandomNumber.deploy({"from": accounts[0], "value": Web3.toWei(10, "ether")})


def deploy_attack():
    attack = Attack.deploy({"from": accounts[1]})

def attack():
    tx = Attack[-1].attack(GuessTheRandomNumber[-1], {"from": accounts[1]})

def check_balance():
    print("_________________________________")
    print(Attack[-1].balance())
    print("_________________________________")