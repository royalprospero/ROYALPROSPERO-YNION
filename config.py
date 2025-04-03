import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Wallet credentials
WALLET_MNEMONIC = os.getenv("WALLET_MNEMONIC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# Define supported networks and their token list URLs
NETWORKS = {
    "bbn-test-5": {
        "name": "Babylon Testnet",
        "tokens": ["USDT", "BBN", "UNO"],
        "token_list_url": "https://unionlabs.github.io/token-lists/babylon.babylon-testnet-1/tokenlist.json"
    },
    "elgafar-1": {
        "name": "Stargaze Testnet",
        "tokens": ["STARS", "UNO", "mkUSD"],
        "token_list_url": "https://unionlabs.github.io/token-lists/stargaze.elgafar-1/tokenlist.json"
    },
    "stride-internal-1": {
        "name": "Stride Testnet",
        "tokens": ["STRD"],
        "token_list_url": "https://unionlabs.github.io/token-lists/stride.stride-internal-1/legacy-tokenlist.json"
    },
    "union-testnet-9": {
        "name": "Union Testnet",
        "tokens": ["USDT", "mkUSD", "UNO"],
        "token_list_url": "https://unionlabs.github.io/token-lists/union.union-testnet-9/tokenlist.json"
    },
}

# Transfer URL
TRANSFER_URL = "https://app.union.build/transfer"
