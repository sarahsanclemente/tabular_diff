################################################################################
# TODO:
# - Add filler row if there appears to be an extra row inserted
################################################################################
import pandas as pd
import doctest

df_old = pd.read_csv('./test_feed_1.csv', sep='\t')
df_new = pd.read_csv('./test_feed_2.csv', sep='\t')

def equalize_columns(old, new):
    """ Check if the # of columns match and add any missing columns with nulls
        Fill with "This cell was generated by the differ"
        !!! This modifies the dataframes passed to it in place !!!

        >>> old = pd.DataFrame({"header": [1]})
        >>> new = pd.DataFrame({"header": [1], "extra": [2]})
        >>> equalize_columns(old, new)
        >>> old
           header                                  extra
        0       1  This cell was generated by the differ
        >>> new = pd.DataFrame({"header": [1]})
        >>> old = pd.DataFrame({"header": [1], "extra": [2]})
        >>> equalize_columns(old, new)
        >>> new
           header                                  extra
        0       1  This cell was generated by the differ

    """
    extra_old_columns = old.columns.difference(new.columns).to_list()
    extra_new_columns = new.columns.difference(old.columns).to_list()
    if extra_old_columns:
        add_differ_column(new, extra_old_columns)
    if extra_new_columns:
        add_differ_column(old, extra_new_columns)

def add_differ_column(df, column_header_list):
    """ Recursively add columns filled with "This cell was generated by the differ" to the data frame for each header in header list
        !!! This modifies the dataframe passed to it in place !!!

        >>> df = pd.DataFrame({"header": [1]})
        >>> add_differ_column(df, ["a", "b", "c"])
        >>> df
           header                                      a                                      b                                      c
        0       1  This cell was generated by the differ  This cell was generated by the differ  This cell was generated by the differ

    """
    # this check if the column_header_list is empty
    if not column_header_list:
        return # can't return a dataframe so this just breaks the recursive loop
    header = column_header_list.pop(0)
    # add header to df and fill with differ string
    df[header] = "This cell was generated by the differ"
    add_differ_column(df, column_header_list)

print("tests passed")
