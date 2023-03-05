from brownie import Bank, Logger, HoneyPot, Attack, accounts
from web3 import Web3

def main():
    deploy_honey_pot()
    deploy_bank()
    deploy_attack()
    attack()

def deploy_honey_pot():
    honey_pot = HoneyPot.deploy({"from": accounts[0]})


def deploy_bank():
    bank = Bank.deploy(HoneyPot[-1], {"from": accounts[0]})


def deploy_attack():
    attack = Attack.deploy(Bank[-1], {"from": accounts[1]})

def attack():
    tx = Attack[-1].attack({"from": accounts[0], "value": Web3.toWei(1, "ether")})