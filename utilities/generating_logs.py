import logging


def generate_logs():
    logging.basicConfig(
        filename="SwagLabs.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )

    # Return the logger so it can be used
    return logging.getLogger()