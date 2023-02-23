import sys 
sys.path.append('/Users/otavi/Bitcoin')

from blockchain.backend.core.block import Block
from blockchain.backend.core.blockheader import BlockHeader
from blockchain.backend.util.util import hash256
from blockchain.backend.core.database.database_ import BlockchainDB
import time


ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain_:
    def __init__(self):
        self.GenesisBlock()


    def write_on_disk(self, block):
        blockchainDB=BlockchainDB()
        blockchainDB.write(block)


    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()


    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    
    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Codies Alert sent {BlockHeight} Bitcoins to joe"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        self.write_on_disk([Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__])
        
    
    def main(self):
        while True:
            lastBlock = self.fetch_last_block()
            BlockHeight = lastBlock["Height"] + 1
            prevBlockHash = lastBlock["BlockHeader"]['blockHash']
            self.addBlock(BlockHeight, prevBlockHash)


if __name__== "__main__":
    blockchain = Blockchain_()
    blockchain.main()