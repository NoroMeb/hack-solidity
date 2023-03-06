// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;


contract EtherStore {


    mapping (address=>uint256) balance;

    constructor () payable {
        
    }

    function deposit( ) external payable {
        require(msg.value>= 0, "Can't deposit zero");
        balance[msg.sender] = balance[msg.sender] + msg.value;

    }

    function withdraw() external {
        uint256 bal = balance[msg.sender];
        require(bal > 0);

        (bool sent,) = msg.sender.call{value: bal}("");
        require(sent, "Failed to  send ether ");

        balance[msg.sender] = 0;
    }
}