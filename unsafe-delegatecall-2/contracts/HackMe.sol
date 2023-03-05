// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;


contract HackMe {
    address public lib;
    address public owner;
    address public someNumber;

    constructor (address _lib) {
        lib = _lib;
        owner = msg.sender;
    }

    function doSomething(uint256 _num) public {
        lib.delegatecall(abi.encodeWithSignature("doSomething(uint256)", _num));
    }
}