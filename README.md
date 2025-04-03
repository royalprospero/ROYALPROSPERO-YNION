# ROYALPROSPERO-YNION

**README.md**

# Union Swap Bot

A bot to automate testnet token swaps on Cosmos-based networks using Union Testnet.

### 1. Clone the repository
   Open your terminal and run the following command to clone the repository:
   ```sh
   git clone https://github.com/KingTheAnalyst/UnionBOT.git
   cd union-swap-bot
 ```

### 2. Install dependencies
   Ensure you have Python installed, then install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### 3. Set up environment variables
   Copy the example environment file and update it with your private details:
   ```sh
   cp .env.example .env
   ```
   Open `.env` and fill in your **WALLET_MNEMONIC** and **PRIVATE_KEY**:
   ```plaintext
   WALLET_MNEMONIC=your_mnemonic_here
   PRIVATE_KEY=your_private_key_here
   ```

### 4. Fetch token list
   Before running swaps, fetch the token list:
   ```sh
   python token_list.py
   ```
   This will retrieve available tokens from the Union testnet.

### 5. Run the bot
   Finally, execute the bot to start swapping tokens:
   ```sh
   python swap_bot.py
   ```
   The bot will execute multiple transactions with randomized parameters.

### 6. Monitor logs
   Check the console output to monitor transaction success or failure.

## Troubleshooting
- If the bot fails to fetch tokens, check the **TOKEN_LIST_URL** in `config.py`.
- If transactions fail, ensure your **WALLET_MNEMONIC** and **PRIVATE_KEY** are correct.
- Verify that your Python installation includes all dependencies by running:
   ```sh
   pip freeze
   ```
