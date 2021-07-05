import os
import glob

class FileHydra:
    """This hydra lives in your folder structure and works with your files"""
    def __init__(self,location):
        self.location=location
        self.target=location  
    
    def move_file(self,prefix,suffix,olddir,newdir,index):
        """processes only files without spaces in name"""
        files=self.get_files_in_directory(olddir,suffix)
        list1=self.name_contains(prefix,files)
        if len(list1)>0:
            filename=list1[index]
        	 #print(list1, olddir,newdir)
            filename=filename.split(olddir+'\\')[1]
            path="move "+olddir+"\\"+filename+" "+newdir#+"\\"+filename
            print(path)
            os.system(path)
            
        else:
            print("No files found")
        
    def get_files_in_directory(self,dir,suffix):
        """Returns list of .txt files in given directory"""
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))    
        DIRECTORY = os.path.join(SITE_ROOT, dir)
        files = glob.glob(DIRECTORY + '/*'+suffix, recursive=True)
        return(files)        
    
    def name_contains(self,s,files):
        """Returns list of files containing given string s in their name"""
        filtered_files=[file for file in files if s in file]
        return(filtered_files) 
    
    def rename_file(self,oldfile,newfile):
        pass
    
    def copy_file(self,oldfile,newfile):
        pass




    def create_folder(self,name):
        os.mkdir(name)

 
        
fh=FileHydra(".")
fh.generate_file_queue("HELLO")