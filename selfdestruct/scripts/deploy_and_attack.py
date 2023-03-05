from brownie import EtherGame, Attacker, accounts
from web3 import Web3 

def main():
    deploy_ether_game()
    deploy_attacker()
    get_balance()
    attack()
    get_balance()
    deposit()

def deploy_ether_game():
    ether_game = EtherGame.deploy({"from": accounts[0]})

def deploy_attacker():
    attacker = Attacker.deploy({"from": accounts[0]})

def deposit():
    ether_game = EtherGame[-1]
    tx = ether_game.deposit({"from": accounts[0], "value": Web3.toWei(1, "ether")})

def claim_reward():
    ether_game = EtherGame[-1]
    tx = ether_game.claimReward({"from": accounts[0]})

def attack():
    attacker = Attacker[-1]
    ether_game = EtherGame[-1]
    tx = attacker.attack(ether_game.address, {"from": accounts[0], "value": Web3.toWei(7, "ether")})

def get_balance():
    ether_game = EtherGame[-1]
    print("_____________________________________")
    print(ether_game.balance())
    print("_____________________________________")

    