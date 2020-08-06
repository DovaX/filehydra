import os
import glob

class FileHydra:
    """This hydra lives in your folder structure and works with your files"""
    def __init__(self,location):
        self.location=location
        self.target=location  
    
