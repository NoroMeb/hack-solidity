from brownie import TimeLock, Attacker, accounts, config
from web3 import Web3
account = accounts.add(config["wallets"]["from_key"])

def main():
    # deploy_time_lock()
    deploy_attacker()
    # deposit()
    # withdraw()
    attack()
    # check_balance()

def deploy_time_lock():
    time_lock = TimeLock.deploy({"from": account, "priority_fee": "2 gwei"})

def deploy_attacker():
    time_lock = TimeLock[-1]
    attacker = Attacker.deploy(time_lock, {"from": account, "priority_fee": "2 gwei"})


def deposit():
    time_lock = TimeLock[-1]
    tx = time_lock.deposit({"from": account, "value": Web3.toWei(0.2, "ether"), "priority_fee": "2 gwei"})

def withdraw():
    time_lock = TimeLock[-1]
    tx = time_lock.withdraw({"from": account, "priority_fee": "2 gwei"})


def attack():
    attacker = Attacker[-1]
    tx = attacker.attack({"from": account, "value": Web3.toWei(0.2, "ether"), "priority_fee": "2 gwei"})

def check_balance():
    print(TimeLock[-1].balance(Attacker[-1]))