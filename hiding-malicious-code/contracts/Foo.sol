// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./Bar.sol";

contract Foo {
    Bar bar;
    constructor (address _barAddress) {
        bar = Bar(_barAddress);
    }

    function callBar( ) public {
        bar.log();
    }
}