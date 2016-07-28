//
// Solidity wrapper for multisig verify precompiled contract.
//
// (C) 2016 Alex Beregszaszi
// Uncopyright 2016 InitC3 Workshop Participants
//
// MIT License
//

contract Committee {
    
    event SubroutineFailed();
    event SignatureSucceeded(bool);

    // This copies call data (everything, except the method signature) to the precompiled contract.
    function thresholdVerify(string VK, string messageHash, string signature) returns (bool) {
        uint len;   
        
        assembly {
            len := calldatasize()
        }

        bytes memory req = new bytes(len - 4);
        bytes memory res = new bytes(1);
        

        uint status;
        assembly {
            let alen := len
            calldatacopy(req, 4, alen)
            call(sub(gas, 10000), 5, 0, req, alen, add(res, 1), 1)
            =: status
        }

        if (status != 1) {
          SubroutineFailed();
          return false;
        }

        SignatureSucceeded(res[0] == 1);
        return res[0] == 1;
     }

}
