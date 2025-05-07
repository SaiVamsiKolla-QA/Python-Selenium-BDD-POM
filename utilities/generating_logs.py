import logging
import os
import sys


def generate_logs():
    # Get the current working directory
    current_dir = os.getcwd()

    # Create Test-artifacts directory if it doesn't exist
    test_artifacts_dir = os.path.join(current_dir, "Test-artifacts")
    os.makedirs(test_artifacts_dir, exist_ok=True)

    # Create logs directory under Test-artifacts
    logs_dir = os.path.join(test_artifacts_dir, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Define log file path
    log_file_path = os.path.join(logs_dir, "Swag.log")  # change the file name if need

    # Print log location for reference
    print(f"\nLog file location: {log_file_path}\n")

    # Clear any existing handlers
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Configure logging with both file and console handlers
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s-%(levelname)s-%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p',
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Get and return the logger
    logger = logging.getLogger()
    logger.info("Logging initialized")

    return logger
