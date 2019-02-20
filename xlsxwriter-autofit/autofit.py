import pandas as pd

def get_df(fn:str):
    # print("Hellow World!")
    df = pd.read_excel(fn)
    return df

def make_xlsx(fn:str, df:pd.DataFrame, idx_bool:bool=True):
    def autofit(writer):
        """
        This is the function that will make all sheets be autofitted to data.

        """

        workbook = writer.book
        worksheet_list = workbook.worksheets()
        for ws in worksheet_list:
            pass
        
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(fn, engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Testing1', index=idx_bool)
    df.to_excel(writer, sheet_name='Testing2', index=idx_bool)

    autofit(writer)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

if __name__ == "__main__":
    # execute only if run as a script
    filename = 'TestBook.xlsx'
    df = get_df(filename)
    print(df.head())
    make_xlsx('NewBook.xlsx', df, False)