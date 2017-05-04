def read_data(file_name):
    """
    Read file into python. 
    Inputs: file_name(string)
    Return: Pandas datafame
    """
    assert os.path.exists(file_name), "That file does not exist!"
    if file_name[-3:] == "csv":
        df = pd.read_csv(file_name)
        return df
    
    if file_name[-3:] == "xls":
        df = pd.read_excel(file_name)
        return df