# Initializing our blockchain
MINING_REWARD = 10

genesis_block = {
        "previous_hash": "",
        "index": 0,
        "transaction": []
    } 
blockchain = [genesis_block]
open_transactions = []
owner = "Sabelo"
participants = {"Sabelo "}


def hash_block(block):
    return "-".join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block["transaction"] if tx["sender"] == participant] for block in blockchain ]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
             amount_sent += tx[0]  
    tx_recipient = [[tx["amount"] for tx in block["transaction"] if tx["recipient"] == participant] for block in blockchain ]         
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
             amount_received += tx[0] 
    return  amount_received - amount_sent

def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner,   amount=1.0):
    transaction = {"sender": sender,
                    "recipient": recipient,
                      "amount":amount }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)
   

def mine_block():
    last_block = blockchain[-1]
    hashed_block  = hash_block(last_block)
    reward_transaction = {
        "sender": "MINING",
        "recipient": owner,
        "amount": MINING_REWARD
    }
    open_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transaction": open_transactions

    } 
    blockchain.append(block) 
    return True


def get_transaction_value():
    #Get the user the input, transform it from a string to float and store it
    tx_recipient = input("Enter the recipient of transaction: ")
    tx_amount = float(input("Your Transaction amount please: "))
    return tx_recipient, tx_amount


def get_user_choose():
    user_input = input("Your Choice: ")
    return user_input

def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain: 
        print("Outputting block")
        print(block)
    else:
        print("-" * 20)    


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index -1]):
            return False
    return True

    
waiting_for_input = True

while waiting_for_input:
    print("Please Choose")
    print("1: add a new transaction value")
    print("2: Mine a block")
    print("3: Output blockchain block")
    print("4: Output participants")
    print("h: Manipulate the chain")
    print("q: Exit the blockchain")
    user_choice = get_user_choose()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == "2":
         if mine_block():
            open_transactions = []    
    elif user_choice == "3":
         print_blockchain_elements()  
    elif user_choice == "4":
         print(participants)    
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transaction": [{"sender": "christ", "recipient": "max", "amount": 1100.0}]
            }       
    elif user_choice == "q":
         waiting_for_input = False    
    else:
        print("Input was invalid, pick correct one")
    if not verify_chain():
        print("invalid blockchain")
        break
    print(get_balance("Sabelo"))


print("Done!")