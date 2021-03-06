import os.path
from data.file import File
from pathlib import Path


class FileManager:
    """Class for creating a file manager for managing all
    external files in 1 place.
    
    Attributes
    ----------
    files : list(File objects)
        a list containing the path and name of each file
        
    Methods
    -------
    directory(new_directory)
        change the directory
    add_file
        Add an existing file to the manager
    get_file(file_path or nickname)
        Find and retrieve an existing file from the manager
    generate_list
        Generates a new file list from the files within the current dir
        TODO: add this function
    drop_file
        Removes a file from the manager
    print_files
        Prints out a list of all the files in the manager
    is_empty
        Returns true if there are no files in the manager
    validate_path
            make sure the path entered exists and is valid. If not, throw error
    """
    def __init__(self, dir_name='.'):
        # Check to make sure the directory exists
        self.available_files = []
        self.directory = dir_name
        self.files = []
        self.extensions = ['xlsx', 'xls', 'xlsm', 'csv', 'txt']
        
    @property
    def directory(self):
        return self._directory
    
    @directory.setter
    def directory(self, new_directory):
        """ Set the new directory.
            Parameters
            ----------
            new_directory: str
                name of the new directory. This is relative to the project path"""
        self._directory = self.validate_directory(new_directory)
        self.available_files = os.listdir(self._directory)
        
    def add_file(self, file_name):
        """ Adds an existing file to the list of files
            File must be existing. If not, throw error.
            TODO: prevent adding duplicates
        
            Parameters
            ----------
            file_name : str
                Must include the suffix of the file name
        """
        if file_name not in self.files:
            if self.validate_file(file_name):
                new_file = File(file_name).save()
                self.files.append(new_file)
                print('New file created.')
            else:
                raise('File type is not valid.')
        else:
            raise('File already in list.')
        
    def get_file(self, file_name):
        # first see if the file exists in the list
        if type(file_name) == str:
            for file in self.files:
                if file.name == file_name:
                    return self._directory + '\\' + file.name
            else:
                raise KeyError('Not in list!')
        elif type(file_name) == int:
            try:
                file = self.files[file_name]
                return self._directory + '\\' + file.name
            except IndexError:
                print('Not in list!')
    
    def create_file(self, file_name):
        """ Creates a new file and adds it to the files list.
        
            Parameters
            ----------
            file_name: str
                The name of the file, including file extension.
        """
        
        new_file = File(file_name).save()
        self.add_file(file_name)
        
        
    def drop_file(self, file):
        if file in self.files:
            self.files.remove(file)
            return True
        else:
            return False
        
    def is_empty(self):
        return self.files == []
        
    def print_files(self):
        for file in self.files:
            print(file)

    @staticmethod
    def validate_directory(new_directory):
        p = os.getcwd()
        if os.path.exists(new_directory):
            if new_directory == '.':
                return os.path.abspath(__file__ + "/../")
            elif new_directory == '..':
                return os.path.abspath(__file__ + "/../../")
            else:
                return new_directory
        else:
            raise Exception('The directory {} does not exist.'.format(new_directory))
            # return new_directory
    
    def validate_file(self, existing_file):
        if os.path.exists(self._directory + '\\' + existing_file):
            f = self._directory + '\\' + existing_file
            return True
        else:
            return False
