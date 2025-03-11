# Bot configuration
BOT_USERNAME = os.getenv("BOT_USERNAME", "GreenInfoBot")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "0.0.0.0")
WEBHOOK_PORT = int(os.getenv("PORT", 8000))
WEBHOOK_PORT = int(os.getenv("PORT", 5000))
# Logging configuration 
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
def run():
    try:
        logger.info("Starting Flask server on port 5000...")
        app.run(host='0.0.0.0', port=5000)  
        app.run(host='0.0.0.0', port=5000)  # ALWAYS serve on port 5000
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise  # Re-raise the exception to ensure we know if the server fails
        # Don't raise the exception to keep the thread alive
        return
def keep_alive():
    server = Thread(target=run)
    server.daemon = True
    server.daemon = True  # Make thread daemon so it stops when main program stops
    server.start()
    logger.info("Keep-alive server thread started")
# Load environment variables
load_dotenv()
# Get bot token from environment variable
try:
    TOKEN = os.environ["BOT_TOKEN"]
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable is empty")
    logger.info(f"Bot token loaded successfully (length: {len(TOKEN)})")
except KeyError:
    logger.error("BOT_TOKEN environment variable not found")
    raise
except ValueError as e:
    logger.error(str(e))
    raise
