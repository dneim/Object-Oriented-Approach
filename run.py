"""Running the Xetra ETL application"""
import logging
import logging.config

import yaml

def main():
    """
      entry point to run the xetra ETL job
    """
    # Parsing YAML file
    config_path = r'C:\Users\Dan\Desktop\Data Analysis Projects\ETL Pipeline\Object-Oriented Approach\Object-Oriented-Approach\configs\xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    # Configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")

if __name__ == '__main__':
    main()