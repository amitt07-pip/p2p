# Telegram UserBot Setup Guide

## Step 1: Get Your API Credentials

1. Go to https://my.telegram.org/apps
2. Log in with your Telegram account
3. Create a new app or use existing one
4. Copy:
   - **API ID**
   - **API Hash**

## Step 2: Set Environment Variables

Add these to your `.env` file:

```
TELEGRAM_API_ID=your_api_id_here
TELEGRAM_API_HASH=your_api_hash_here
TELEGRAM_PHONE=+1234567890
```

Replace with:
- Your actual API ID (number)
- Your actual API Hash (string)
- Your phone number with country code (e.g., +1 for US)

## Step 3: Run the UserBot

```bash
python userbot.py
```

On first run:
1. Bot will send a code to your Telegram account
2. Enter the code when prompted
3. If you have 2FA enabled, enter your password
4. Bot will authenticate and start listening

## Step 4: Use the UserBot

Once authenticated, you can use commands:

- `/deal @username` - Create a deal room

## Important Notes

- The userbot logs in as your personal account
- Keep your API credentials secret
- Session file (`p2pmart_userbot.session`) stores your authentication
- Don't commit session files to git

## Troubleshooting

**"TELEGRAM_API_ID or TELEGRAM_API_HASH not set"**
- Make sure you added them to `.env` file
- Restart the bot after adding

**"Error: 401 UNAUTHORIZED"**
- Your API credentials are incorrect
- Check them at https://my.telegram.org/apps

**"Phone number not registered"**
- Make sure your phone number format includes country code (+1, +44, etc)
- Check you're using the same number registered with your Telegram account
