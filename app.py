from pathlib import Path

import plotly.express as px
import streamlit as st

from src.data_processing import (
    get_average_ticket,
    get_sales_by_category,
    get_sales_by_product,
    get_sales_over_time,
    get_total_quantity,
    get_total_revenue,
    load_data,
)


# --------------------------------------------------
# Configuração
# --------------------------------------------------

st.set_page_config(
    page_title="Sales Analytics",
    page_icon="📊",
    layout="wide",
)


DATA_PATH = Path("data/sales.csv")


# --------------------------------------------------
# Carregamento dos dados
# --------------------------------------------------

df = load_data(DATA_PATH)


# --------------------------------------------------
# Título
# --------------------------------------------------

st.title("📊 Sales Analytics Dashboard")

st.markdown(
    """
    Dashboard interativo para análise de vendas,
    faturamento e desempenho dos produtos.
    """
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("Filtros")

categories = sorted(df["category"].unique())

selected_categories = st.sidebar.multiselect(
    "Categoria",
    categories,
    default=categories,
)

min_date = df["date"].min().date()
max_date = df["date"].max().date()

selected_dates = st.sidebar.date_input(
    "Período",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)


# --------------------------------------------------
# Aplicação dos filtros
# --------------------------------------------------

filtered_df = df[
    (df["category"].isin(selected_categories))
    & (df["date"].dt.date >= selected_dates[0])
    & (df["date"].dt.date <= selected_dates[1])
]


# --------------------------------------------------
# Indicadores
# --------------------------------------------------

total_revenue = get_total_revenue(filtered_df)
total_quantity = get_total_quantity(filtered_df)
average_ticket = get_average_ticket(filtered_df)

col1, col2, col3 = st.columns(3)

col1.metric(
    "💰 Faturamento",
    f"R$ {total_revenue:,.2f}",
)

col2.metric(
    "📦 Produtos vendidos",
    f"{total_quantity:,}",
)

col3.metric(
    "🧾 Ticket médio",
    f"R$ {average_ticket:,.2f}",
)


st.divider()


# --------------------------------------------------
# Faturamento ao longo do tempo
# --------------------------------------------------

st.subheader("📈 Faturamento ao longo do tempo")

sales_over_time = get_sales_over_time(filtered_df)

fig_time = px.line(
    sales_over_time,
    x=sales_over_time.index,
    y=sales_over_time.values,
    markers=True,
    labels={
        "x": "Data",
        "y": "Faturamento",
    },
)

fig_time.update_layout(
    xaxis_title="Data",
    yaxis_title="Faturamento (R$)",
)

st.plotly_chart(
    fig_time,
    use_container_width=True,
)


# --------------------------------------------------
# Gráficos lado a lado
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("🏷️ Vendas por categoria")

    sales_category = get_sales_by_category(filtered_df)

    fig_category = px.bar(
        x=sales_category.index,
        y=sales_category.values,
        labels={
            "x": "Categoria",
            "y": "Faturamento",
        },
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True,
    )


with col2:

    st.subheader("🏆 Produtos por faturamento")

    sales_product = get_sales_by_product(filtered_df)

    fig_product = px.bar(
        x=sales_product.values,
        y=sales_product.index,
        orientation="h",
        labels={
            "x": "Faturamento",
            "y": "Produto",
        },
    )

    st.plotly_chart(
        fig_product,
        use_container_width=True,
    )


# --------------------------------------------------
# Dados
# --------------------------------------------------

st.divider()

st.subheader("🔎 Dados das vendas")

display_df = filtered_df.copy()

display_df["date"] = display_df["date"].dt.strftime("%d/%m/%Y")

display_df["unit_price"] = display_df["unit_price"].map(
    lambda value: f"R$ {value:,.2f}"
)

display_df["revenue"] = display_df["revenue"].map(
    lambda value: f"R$ {value:,.2f}"
)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
)