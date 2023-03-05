// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;


contract Wallet {
    address public owner;
    constructor () payable  {
        owner = msg.sender;
    }

    function transfer(address _to, uint256 _amount) public {
        require(tx.origin == owner, "Only owner can call this function");

        (bool sent, ) = _to.call{value: _amount}("");
        require(sent, "Failed to sent ether");
    }


}