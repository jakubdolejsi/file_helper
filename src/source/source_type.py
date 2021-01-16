from src.config.configuration import Configuration
from src.destination.destination_type import DestinationType

class SourceType:

    def __init__(self, config: Configuration):
        self.config = config

    def _validate_paths(self):
        pass

    def convert(self, dest_type: DestinationType):
        pass

    def merge(self):
        pass
