import os


class DirectoryCleaner:
    @staticmethod
    def clean(directory):
        for item in os.listdir(directory):
            os.remove(directory + item)
