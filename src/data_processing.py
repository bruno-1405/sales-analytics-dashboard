import pandas as pd


def load_data(file_path):
    """Carrega o arquivo CSV e prepara os dados."""
    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"])

    df["revenue"] = df["quantity"] * df["unit_price"]

    return df


def get_total_revenue(df):
    """Retorna o faturamento total."""
    return df["revenue"].sum()


def get_total_quantity(df):
    """Retorna a quantidade total de produtos vendidos."""
    return df["quantity"].sum()


def get_average_ticket(df):
    """Retorna o ticket médio."""
    if len(df) == 0:
        return 0

    return df["revenue"].sum() / len(df)


def get_sales_by_category(df):
    """Retorna o faturamento agrupado por categoria."""
    return (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )


def get_sales_by_product(df):
    """Retorna o faturamento agrupado por produto."""
    return (
        df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )


def get_sales_over_time(df):
    """Retorna o faturamento agrupado por mês."""
    monthly_sales = (
        df.set_index("date")
        .resample("ME")["revenue"]
        .sum()
    )

    return monthly_sales