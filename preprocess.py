def fill_missing(df, column_name, ,groupby, stat):
    """
    Fill in missing values for one column. 
    Inputs: dataframe
            column_name - string
            stat - string in [mean, median, mode]
    """
    mean = df[column_name].mean()
    median = df[column_name].median()
    mode = df[column_name].mode()
    
    if stat == 'mean':
        #mean = credit_data.groupby('zipcode')['MonthlyIncome'].mean().loc[60601]
        df[[column_name]] = df[[column_name]].fillna(value=mean)
        
    if stat == 'median':
        df[[column_name]] = df[[column_name]].fillna(value=median)
        
    if stat == 'mode':
        df[[column_name]] = df[[column_name]].fillna(value=mode)   
import pandas as pd

def discretize(df, col_name, new_col_name, quartiles, labels):
    '''
    Transform a continuous variable into discrete variable.
    
    Inputs: dataframe
            colum_name - string
            new_col_name - string
            quartiles - integer (ex: 2 creates bins above & below 50% percentile)
            labels - list of length blah; if None, retains range of values
            
    Return: dataframe with discrete variable column added
    '''
    df[new_col_name] = pd.qcut(df[col_name], quartiles, labels = labels)
    return df
    
def make_binary(df, column_names):
    '''
    Transform categorical variable into dummy variable and add columns to dataframe. 
    
    Inputs: dataframe
            column_names - list of strings
    Return: dataframe with dummy columns added
    '''
    return pd.get_dummies(df, columns = column_names)