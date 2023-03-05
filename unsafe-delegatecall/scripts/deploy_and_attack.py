from brownie import Lib, HackMe, Attacker, accounts

first_account = accounts[0]
second_account = accounts[1]

def main():
    lib = deploy_lib()
    hack_me = deploy_hack_me()
    attacker = deploy_attacker()
    hack_me_check_owner()
    attack()
    hack_me_check_owner()


def deploy_lib():
    lib = Lib.deploy({"from": first_account})
    return lib

def deploy_hack_me():
    hack_me = HackMe.deploy(Lib[-1], {"from": first_account})
    return hack_me

def deploy_attacker():
    attacker = Attacker.deploy(HackMe[-1], {"from": second_account})
    return attacker

def attack():
    attacker = Attacker[-1]
    tx = attacker.attack({"from": second_account})


def hack_me_check_owner():
    print("________________________________________")
    print(f" HackMe Owner :  {HackMe[-1].owner()}")
    print("________________________________________")