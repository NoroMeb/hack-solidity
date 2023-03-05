from brownie import Target, Hack, accounts


def main():
    deploy_target()
    deploy_hack()
    print(Hack[-1].isContract())
    print(Target[-1].pwned())

def deploy_target():
    target = Target.deploy({"from": accounts[0]})

def deploy_hack():
    hack = Hack.deploy(Target[-1], {"from": accounts[0]})