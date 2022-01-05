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

# connect to Account
acct = w3.eth.account.privateKeyToAccount(
    'eaba28f33a0493e52d3e9331cf43be2baa14a7850cc304bdaf64e2ae793a4db9')

# check account balance
balance = w3.eth.get_balance('0x0619B368c99A53eA45d4a3D127D58D5fff25A7dB')
print(f"Account balance is : {balance}")

# transaction to deploy contract
construct_txn = contract_.constructor().buildTransaction({
    'from': acct.address,
    'nonce': w3.eth.getTransactionCount(acct.address),
    'gas': 1728712,
    'gasPrice': w3.toWei('21', 'gwei')})

signed = acct.signTransaction(construct_txn)

final = w3.eth.sendRawTransaction(signed.rawTransaction)

# print smart contract address
flag = 0
while flag == 0:

    try:
        flag = 1
        print(w3.eth.getTransactionReceipt(final.hex())["contractAddress"])
    except:
        flag = 0
