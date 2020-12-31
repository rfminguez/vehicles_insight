import pandas as pd
import numpy as np

def get_df_shape(df):
    return df.shape

def get_column_names(df):
    return list(df.columns)

def get_column_dtypes(df):
    return df.dtypes

def get_nan_values_count(df):
    return df.isna().sum()

def get_numeric_columns(df):
    return list(df.select_dtypes(include=[np.number]).columns)

def get_max_and_min_values_per_each_column(df):
    result = {}
    for column in get_numeric_columns(vehicles_df):
        result[column] = {"max": vehicles_df[column].max(), "min": vehicles_df[column].min()}
    return result


if __name__ == "__main__":
    vehicles_df = pd.read_csv("data/vehicles.csv")

    num_rows, num_columns = get_df_shape(vehicles_df)

    print(f"Numero de filas: {num_rows}\n")
    print(f"Numero de columnas: {num_columns}\n")
    print(f"Nombre de las columnas: {get_column_names(vehicles_df)}\n")
    print(f"Tipo de datos de las columnas:\n{get_column_dtypes(vehicles_df)}\n")
    print(f"Valores nulos por columnas:\n{get_nan_values_count(vehicles_df)}\n")
    print(f"Valores maximo y minimo por columna:\n{get_max_and_min_values_per_each_column(vehicles_df)}")

