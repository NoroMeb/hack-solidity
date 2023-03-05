from brownie import Vault, accounts, config, web3


def main():
    # print(Vault[-1].storage(0))
    print(web3.eth.getStorageAt(Vault[-1].address, 1))
    

def deploy_vault():
    account = accounts.add(config["wallets"]["from_key"])
    password = "MerciAuClientsFideles"
    vault = Vault.deploy(bytes(password.encode("utf-8")), {"from": account, "priority_fee": "2 gwei"})