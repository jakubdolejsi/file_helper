from src.destination.destination_type import DestinationType


class SourceType:

    def validate(self):
        pass

    def convert(self, dest_type: DestinationType):
        pass

    def merge(self):
        pass
