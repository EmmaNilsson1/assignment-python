

from cv2 import split
import klassCovid as kc
import pandas as pd



def main():
   covs = kc.Covid('vaccin_covid.csv', 'vaccin_covid.db', 'vaccinet')
   covs.split_column('vaccines', ',')
   covs.join()
   covs.no_na_value('Missing')
   covs.df_path.head()
   covs.df_path.tail()
   covs.df_path.describe()

   covs.create_db()



if __name__ == '__main__':
   main()
