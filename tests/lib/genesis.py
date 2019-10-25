from dataclasses import dataclass
from dacite import from_dict


@dataclass
class Cbft:
    initialNodes: list
    epoch: int
    amount: int
    validatorMode: str
    period: int


@dataclass
class Config:
    chainId: int
    eip155Block: int
    cbft: Cbft


@dataclass
class Common:
    ExpectedMinutes: int
    ValidatorCount: int
    AdditionalCycleTime: int


@dataclass
class Staking:
    StakeThreshold: int
    MinimumThreshold: int
    EpochValidatorNum: int
    HesitateRatio: int
    EffectiveRatio: int
    UnStakeFreezeRatio: int
    PassiveUnDelegateFreezeRatio: int
    ActiveUnDelegateFreezeRatio: int


@dataclass
class Slashing:
    PackAmountAbnormal: int
    DuplicateSignHighSlashing: int
    NumberOfBlockRewardForSlashing: int
    EvidenceValidEpoch: int


@dataclass
class Gov:
    VersionProposalVote_DurationSeconds: int
    VersionProposalActive_ConsensusRounds: int
    VersionProposal_SupportRate: float
    TextProposalVote_DurationSeconds: int
    TextProposal_VoteRate: float
    TextProposal_SupportRate: float
    CancelProposal_VoteRate: float
    CancelProposal_SupportRate: float


@dataclass
class Reward:
    NewBlockRate: int
    PlatONFoundationYear: int


@dataclass
class InnerAcc:
    PlatONFundAccount: str
    PlatONFundBalance: int
    CDFAccount: str
    CDFBalance: int


@dataclass
class EconomicModel:
    Common: Common
    Staking: Staking
    Slashing: Slashing
    Gov: Gov
    Reward: Reward
    InnerAcc: InnerAcc


@dataclass
class Genesis:
    config: Config
    EconomicModel: EconomicModel
    nonce: str
    timestamp: str
    extraData: str
    gasLimit: str
    alloc: dict
    number: str
    gasUsed: str
    parentHash: str

    def to_dict(self):
        from copy import copy
        data = copy(self.__dict__)
        data["config"] = copy(self.config.__dict__)
        data["config"]["cbft"] = copy(self.config.cbft.__dict__)
        data["EconomicModel"] = copy(self.EconomicModel.__dict__)
        data["EconomicModel"]["Common"] = copy(self.EconomicModel.Common.__dict__)
        data["EconomicModel"]["Staking"] = copy(self.EconomicModel.Staking.__dict__)
        data["EconomicModel"]["Slashing"] = copy(self.EconomicModel.Slashing.__dict__)
        data["EconomicModel"]["Gov"] = copy(self.EconomicModel.Gov.__dict__)
        data["EconomicModel"]["Reward"] = copy(self.EconomicModel.Reward.__dict__)
        data["EconomicModel"]["InnerAcc"] = copy(self.EconomicModel.InnerAcc.__dict__)
        return data

    def to_file(self, file):
        data = self.to_dict()
        with open(file, "w") as f:
            f.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    from common.load_file import LoadFile
    from conf.settings import GENESIS_FILE
    import json
    genesis_data = LoadFile(GENESIS_FILE).get_data()
    genesis = from_dict(data_class=Genesis, data=genesis_data)
    genesis.config.chainId = 1
    # print(genesis_to_dict(genesis))
    print(genesis.to_dict())
