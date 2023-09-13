import pandas as pd
import sqlite3

def commit_query(database, xlsx_path, sheet_name=None):
    dfs = pd.read_excel(xlsx_path, sheet_name=sheet_name)

    for table, df in dfs.items():
        df.to_sql(table, database, index=False)
    database.commit()

    return


def main():
    db = sqlite3.connect("flat-table-3.sqlite")
    commit_query(db, './make_db/복리후생.xlsx')
    db.close()

if __name__ == "__main__":
    main()