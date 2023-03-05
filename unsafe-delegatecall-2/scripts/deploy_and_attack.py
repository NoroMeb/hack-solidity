from brownie import HackMe, Lib, Attack, accounts



def main():
    deploy_lib()
    deploy_hack_me()
    deploy_attack()
    check_hack_me_owner()
    attack()
    check_hack_me_owner()


def deploy_lib():
    lib = Lib.deploy({"from": accounts[0]})

def deploy_hack_me():
    hack_me = HackMe.deploy(Lib[-1], {"from": accounts[0]})

def deploy_attack():
    attack = Attack.deploy(HackMe[-1], {"from": accounts[1]})

def attack():
    tx = Attack[-1].attack({"from": accounts[-1]})

def check_hack_me_owner():
    print("______________________________________")
    print(HackMe[-1].owner())
    print("______________________________________")