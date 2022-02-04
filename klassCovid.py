

from cv2 import minEnclosingCircle
import pandas as pd
import sqlite3


#Skapa en class som innehåller en dataframe, database och namnet på dessa
class Covid:
    
    def __init__(self, df_path, db_path, name):
        self.df_path = pd.read_csv(df_path)
        self.db_path = db_path
        self.name = name

#Skapa en databas som är kopplad till dataframen med dess värden
    def create_db(self):
            self.db_path = sqlite3.connect(self.db_path)
            self.df_path.to_sql(self.name, self.db_path)
           

#Skapa 'split'-funktion som spearerar värden i en kolumn, för att städa datan
    def split_column(self, column_in_df_file, split):
       self.new_df = self.df_path[column_in_df_file].str.split(split, expand = True)
       

#Skapa en metod som byter ut nan-värden i databasen till annat önskat värde
    def no_na_value(self, value):
        self.df_path = self.df_path.fillna(value)


#Skapa en metod som binder ihop nya och gamla kolumnner
    def join(self):
        self.df_path = self.df_path.join(self.new_df)
        




    















