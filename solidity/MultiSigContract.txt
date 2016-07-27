contract Multisig {

    Proposal[] proposals;
    address[] signers;
    uint8 threshold = 3;
    
    struct Proposal {
        address withdrawAddress;
        uint withdrawAmount;
        bool completed;
        address[] signers;
    }
    
    event SignedSuccessfully(
        uint indexed proposalID,
        address recipient,
        uint amount,
        address signer,
        uint numSignatures
    );
    
    event WithdrawComplete(
        uint indexed proposalID
    );
    
    event ProposalAdded(
        uint indexed proposalID,
        address sender,
        uint totalProposalCount
    );

    function() {
        
    }
    
    function Multisig()
    {
        address signer1 = 0x92F063DC4a2f9F4DB658092794C7CdFdFA169B41;
        address signer2 = 0x822F660e40F04abD0868Fa532F67F257E8ff3519;
        address signer3 = 0xA7dAa0a623A9e919D4a8C1E71A93a5E3204265Ed;
        address signer4 = 0xdAFB2B9b9661F3a2F25ae7eA3ae845A61a18b608;
        address signer5 = 0x92C41b1C21ECAb11658D51360Dcaf57a961391b5;
        
        signers.push(signer1);
        signers.push(signer2);
        signers.push(signer3);
        signers.push(signer4);
        signers.push(signer5);
    }

    function proposeWithdraw(address _withdrawAddress, uint _withdrawAmount) returns(uint)
    {
        address[] memory _signers;
        proposals.push(Proposal({
            withdrawAddress: _withdrawAddress,
            withdrawAmount: _withdrawAmount,
            completed: false,
            signers: _signers
        }));
        
        ProposalAdded(proposals.length - 1, msg.sender, proposals.length);
        
        return proposals.length - 1;
    }
    
    function sign(uint _proposalId) {
        if(proposals.length <= _proposalId)
            throw;
            
        bool canSign = false;
        for(uint i=0; i<signers.length; i++)
        {
            if(signers[i] == msg.sender)
            canSign = true;
        }
    
        if(!canSign) 
            throw;
            
        Proposal thisProposal = proposals[_proposalId];
    
        for(uint j=0; j<thisProposal.signers.length; j++)
        {
            if(thisProposal.signers[j] == msg.sender)
                throw;
        }
        
        thisProposal.signers.push(msg.sender);
        SignedSuccessfully(_proposalId, thisProposal.withdrawAddress, thisProposal.withdrawAmount,
            msg.sender, thisProposal.signers.length);
    
        if (msg.value > this.balance)
            throw;
    
        if(thisProposal.signers.length >= threshold && !thisProposal.completed)
        {
            thisProposal.completed = true;
            bool result = thisProposal.withdrawAddress.send(thisProposal.withdrawAmount);
            WithdrawComplete(_proposalId);
        }
    }
}