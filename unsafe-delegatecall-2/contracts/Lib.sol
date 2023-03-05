// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;


contract Lib {
    uint256 public someNumber;
    function doSomething(uint256 _num) public {
        someNumber = _num;
    }
}