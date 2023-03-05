from brownie import EtherStore, Attacker, accounts, config
from web3 import Web3

account = accounts.add(config["wallets"]["from_key"])

def main():
    # deploy_ether_store()
    # deploy_attacker()

    attack()


def deploy_ether_store():
    ether_store = EtherStore.deploy({"from": account, "value": Web3.toWei(1, "ether")})



def deploy_attacker():
    ether_store_address = EtherStore[-1].address
    attacker = Attacker.deploy(ether_store_address, {"from": account})


def attack():
    attacker = Attacker[-1]
    attack.tx = attacker.attack({"from": account, "value": Web3.toWei(0.1, "ether"), "priority_fee": "2 gwei"})