from brownie import Foo, Bar, Mal, accounts


def main():
    deploy_bar()
    deploy_mal()
    deploy_foo()
    call_bar()

def deploy_bar():
    bar = Bar.deploy({"from": accounts[0]})

def deploy_mal():
    mal = Mal.deploy({"from": accounts[0]})

def deploy_foo():
    foo = Foo.deploy(Mal[-1], {"from": accounts[0]})

def call_bar():
    tx = Foo[-1].callBar({"from": accounts[0]})
    print(tx.events)