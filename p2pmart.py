#!/usr/bin/env python3
"""
P2PMART - Unified Entry Point
Runs both the Telegram Bot and UserBot concurrently
"""

import asyncio
import threading
import logging
import sys

# Configure logging
logging.basicConfig(
    format='%(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Suppress verbose library logging
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger('telegram').setLevel(logging.WARNING)
logging.getLogger('telegram.ext').setLevel(logging.WARNING)
logging.getLogger('telethon').setLevel(logging.WARNING)


def run_userbot():
    """Run the UserBot in a separate thread"""
    try:
        from userbot import main as userbot_main
        asyncio.run(userbot_main())
    except KeyboardInterrupt:
        logger.info("🛑 UserBot stopped")
    except Exception as e:
        logger.error(f"❌ UserBot error: {e}")


async def run_bot():
    """Run the Telegram Bot asynchronously (stub - actual run happens in main thread)"""
    pass


def main():
    """Start both bot and userbot concurrently"""
    logger.info("🚀 P2PMART Starting...")
    
    # Start userbot in a separate thread
    userbot_thread = threading.Thread(target=run_userbot, daemon=False)
    userbot_thread.start()
    
    # Run bot in the main thread (required for signal handling and polling)
    try:
        from bot import main as bot_main
        bot_main()
    except KeyboardInterrupt:
        logger.info("🛑 P2PMART stopped")
        sys.exit(0)


if __name__ == '__main__':
    main()
