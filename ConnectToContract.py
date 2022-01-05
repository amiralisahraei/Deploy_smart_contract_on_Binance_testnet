from web3 import Web3
from solcx import compile_source
from solidity_code import *

compiled_sol = compile_source(
    solidity_code, output_values=["abi", "bin"])

contract_id, contract_interface = compiled_sol.popitem()

# Access to abi and bytecode
bytecode = contract_interface['bin']
abi = contract_interface['abi']

# connect to Binance smart chain
w3 = Web3(Web3.HTTPProvider(
    "https://data-seed-prebsc-1-s1.binance.org:8545"))
contract_ = w3.eth.contract(abi=abi, bytecode=bytecode)

# Connect to contract
greeter = w3.eth.contract(
     address="0x54f5A7e4E0138d6409fD01684c2f9F01C1bA3486",
     abi=abi
)

acct = w3.eth.account.privateKeyToAccount(
    'eaba28f33a0493e52d3e9331cf43be2baa14a7850cc304bdaf64e2ae793a4db9')

# tranaction to call one function in onctract
# construct_txn1 = greeter.functions.setGreeting('Nihao').buildTransaction({
#     'from': acct.address,
#     'nonce': w3.eth.getTransactionCount(acct.address),
#     'gas': 1728712,
#     'gasPrice': w3.toWei('21', 'gwei')})  

# signed1 = acct.signTransaction(construct_txn1)

# final1 = w3.eth.sendRawTransaction(signed1.rawTransaction)


# call function that does not need transaction /////
print(greeter.functions.greet().call())

