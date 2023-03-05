// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;


contract TimeLock {
    mapping (address=>uint) public lockTime;
    mapping (address=>uint) public balance;

    function deposit() external payable {
        balance[msg.sender] += msg.value;
        lockTime[msg.sender] = block.timestamp + 1 weeks;
    }

    function increaseLockTime(uint _secondsToIncrease) external {
        lockTime[msg.sender] += _secondsToIncrease;
    }

    function withdraw() external  {
        require(balance[msg.sender] > 0, "Nothing to withdraw");
        require(block.timestamp > lockTime[msg.sender], "Not yet");

        uint amount = balance[msg.sender];
        balance[msg.sender] = 0;
        (bool sent, ) = msg.sender.call{value: amount}("");

        require(sent, "Failed to send Ether");
    }


}
