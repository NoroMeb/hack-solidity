// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./Logger.sol";

contract Bank {

    Logger logger;
    mapping (address=>uint256) balances;

    constructor (address _loggerAddress) {
        logger = Logger(_loggerAddress);
    }

    function deposit() public payable {
        balances[msg.sender] += msg.value;
        logger.log(msg.sender, msg.value, "Deposit");
    }

    function withdraw(uint256 _amount) public {
        require(_amount <= balances[msg.sender], "Insufficient funds");

        (bool sent, ) = msg.sender.call{value: _amount}("");
        require(sent, "Failed to send Ether");

        balances[msg.sender] -= _amount;

        logger.log(msg.sender, _amount, "Withdraw");
    }
    }
