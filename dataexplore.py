import pandas as pd
import os.path
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew



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


def get_col_means(df, column_names, return_value=True):
    '''
    Get the mean value of specified column
    Input:
    Return: Mean value(float) or print statement
    '''
    for i in range(len(column_names)):
        assert type(df[column_names[i]].iloc[0]) is not str, "Cannot take the mean of strings! Trying selecting another column." 
    
    mean_list = []
    for col in column_names:
        mean_list.append(df[col].mean())
        
    if return_value:
            return mean_list
    else:
        for i,val in enumerate(column_names):
            print("The mean of" + " " + val + " " "is" + " " + str(mean_list[i]))



def get_statistics(df):
    '''Get general descriptive statistics for a data frame.'''
    return df.describe()


def get_frequency_chart(df, column_name, chart_type):
    '''
    Display counts of a column's unique values (non-continuous).
    
    Inputs: dataframe
            column_name - string
            chart_type - string in ['pie', 'bar', 'barh']
    '''
    plot = df[column_name].value_counts().plot(chart_type)
    plt.title('Distribution of' + ' ' + column_name)
    
    if chart_type == "bar":
        plot.set_xlabel(column_name)
        plot.set_ylabel('frequency')
        
    if chart_type == "barh":
        plot.set_xlabel('frequency')
        plot.set_ylabel(column_name)
        
    plt.show(plot)


def graph_crosstab(df, col1, col2):
    '''
    Graph crosstab of two discrete variables
    
    Inputs: Dataframe, column names (strings)
    '''
    
    pd.crosstab(df[col1], df[col2]).plot(kind='bar')
    plt.title(col2 + " " + "distribution by" + " " + col1)
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()

def stats_by_var(df, col_name, stat):
    '''
    Get descriptive statistics of all variables in dataframe, by selected column. The values 
    in the column should not be continous. 
    '''
    
    if stat == 'mean':
        return df.groupby(col_name).mean()  
        
    if stat == 'median':
        return df.groupby(col_name).median()        
    
    if stat == 'mode':
        return df.groupby(col_name).mode()  


def correlation(df):
    sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap="YlGnBu")
    plt.title('Correlation of columns')
    plt.show()


def histogram(df, column_name, num_bins):
    if skew(df[column_name]) > 10:
        q = df[column_name].quantile(0.99)
        no_outliers = df[df[column_name] < q]
        sns.distplot(no_outliers[column_name], bins=num_bins, norm_hist = False)
    else: 
        sns.distplot(df[col], bins=num_bins, norm_hist = True)
    plt.title('Histogram of' + ' ' + column_name)
    plt.ylabel('Count')
    plt.show()


def histogram_all(df, num_bins):
    for col in df.columns.tolist():
        if skew(df[col]) > 10:
            q = df[col].quantile(0.99)
            no_outliers = df[df[col] < q]
            sns.distplot(no_outliers[col], bins=num_bins, norm_hist = True)
        else: 
            sns.distplot(df[col], bins=num_bins, norm_hist = True)
        plt.show()
        

#credit_data['MonthlyIncome'].plot.hist(bins=100)
#plt.show()

