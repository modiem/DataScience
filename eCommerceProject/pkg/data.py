import os
import pandas as pd 

class Data:
    def get_data(self):
        """ 
        This function returns a dict.
        The key should be the name of dataset.
        The value should be pandas.df loaded from csv files.
        """

        root_dir = os.getcwd()
        csv_path = os.path.join(root_dir, "data", "csv")

        file_names = [f for f in os.listdir(csv_path) if f.endswith(".csv")]
        key_names = [
            name.replace("olist_", "")
            .replace(".csv", "")
            .replace("_dataset", "")
            for name in file_names
            ]
        
        #create the dictionary
        values = [
            pd.read_csv(path)
            for path in [
                os.path.join(csv_path, file_name) 
                for file_name in file_names]
            ]
        
        data = {key:value for (key,value) in zip(key_names, values)}
        return data