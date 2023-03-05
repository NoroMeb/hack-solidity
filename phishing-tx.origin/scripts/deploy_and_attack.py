from brownie import Wallet, Attack, accounts
from web3 import Web3

def main():
    deploy_wallet()
    deploy_attack()
    print(accounts[1].balance())
    attack()
    print(accounts[1].balance())

def deploy_wallet():
    wallet = Wallet.deploy({"from": accounts[0], "value": Web3.toWei(10, "ether")})

def deploy_attack():
    attack = Attack.deploy(Wallet[-1], {"from": accounts[1]})

def attack():
    tx = Attack[-1].attack({"from": accounts[0]})