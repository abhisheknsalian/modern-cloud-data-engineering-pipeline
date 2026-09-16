import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Retail Data Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GOLD_PATH = PROJECT_ROOT / "data" / "gold"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 1rem;
        opacity: 0.65;
        margin-bottom: 1.5rem;
    }

    .section-title {
        font-size: 1.4rem;
        font-weight: 650;
        margin-top: 1rem;
    }

    div[data-testid="stMetric"] {
        border: 1px solid rgba(128, 128, 128, 0.25);
        padding: 16px;
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():

    monthly_sales = pd.read_parquet(
        GOLD_PATH / "monthly_sales.parquet"
    )

    country_sales = pd.read_parquet(
        GOLD_PATH / "country_sales.parquet"
    )

    customer_summary = pd.read_parquet(
        GOLD_PATH / "customer_summary.parquet"
    )

    top_products = pd.read_parquet(
        GOLD_PATH / "top_products.parquet"
    )

    return (
        monthly_sales,
        country_sales,
        customer_summary,
        top_products,
    )


# ============================================================
# LOAD DATA SAFELY
# ============================================================

try:

    (
        monthly_sales,
        country_sales,
        customer_summary,
        top_products,
    ) = load_data()

except Exception as e:

    st.error("Unable to load Gold layer datasets.")

    st.code(str(e))

    st.stop()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📊 Retail Data Platform</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Modern Cloud Data Engineering Pipeline • Online Retail II Analytics"
    "</div>",
    unsafe_allow_html=True,
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a page",
    [
        "Overview",
        "Sales Analytics",
        "Customer Analytics",
        "Product Analytics",
        "Data Quality",
        "Pipeline Status",
    ],
)

st.sidebar.divider()

st.sidebar.caption("Data Platform")

st.sidebar.write("Python ETL")
st.sidebar.write("S3 Data Lake")
st.sidebar.write("Snowflake")
st.sidebar.write("dbt")
st.sidebar.write("Terraform")
st.sidebar.write("GitHub Actions")


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def find_column(df, possible_names):

    """
    Find a column using case-insensitive matching.
    """

    lookup = {
        str(column).lower(): column
        for column in df.columns
    }

    for name in possible_names:

        if name.lower() in lookup:
            return lookup[name.lower()]

    return None


def format_currency(value):

    return f"€{value:,.2f}"


# ============================================================
# OVERVIEW
# ============================================================

if page == "Overview":

    st.header("Overview")

    # --------------------------------------------------------
    # Identify columns
    # --------------------------------------------------------

    revenue_column = find_column(
        monthly_sales,
        ["Revenue", "Sales", "Total Revenue"],
    )

    customer_column = find_column(
        customer_summary,
        ["Customer ID", "CustomerID", "customer_id"],
    )

    country_column = find_column(
        country_sales,
        ["Country"],
    )

    product_column = find_column(
        top_products,
        ["Description", "Product", "Product Description"],
    )

    # --------------------------------------------------------
    # Metrics
    # --------------------------------------------------------

    total_revenue = 0

    if revenue_column:

        total_revenue = monthly_sales[
            revenue_column
        ].sum()

    total_customers = (
        customer_summary[customer_column].nunique()
        if customer_column
        else len(customer_summary)
    )

    total_countries = (
        country_sales[country_column].nunique()
        if country_column
        else len(country_sales)
    )

    total_products = (
        top_products[product_column].nunique()
        if product_column
        else len(top_products)
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Revenue",
            format_currency(total_revenue),
        )

    with col2:

        st.metric(
            "Customers",
            f"{total_customers:,}",
        )

    with col3:

        st.metric(
            "Countries",
            f"{total_countries:,}",
        )

    with col4:

        st.metric(
            "Products",
            f"{total_products:,}",
        )

    st.divider()

    # --------------------------------------------------------
    # Revenue Trend
    # --------------------------------------------------------

    st.subheader("📈 Revenue Trend")

    if revenue_column:

        chart_df = monthly_sales.copy()

        year_column = find_column(
            chart_df,
            ["Year"],
        )

        month_column = find_column(
            chart_df,
            ["Month"],
        )

        if year_column and month_column:

            chart_df["Date"] = pd.to_datetime(
                chart_df[year_column].astype(str)
                + "-"
                + chart_df[month_column].astype(str)
                + "-01"
            )

            chart_df = chart_df.sort_values("Date")

            chart_df = chart_df.set_index("Date")

            st.line_chart(
                chart_df[revenue_column]
            )

        else:

            st.line_chart(
                chart_df[revenue_column]
            )

    else:

        st.info(
            "Revenue column was not found in monthly sales data."
        )

    st.divider()

    # --------------------------------------------------------
    # Architecture
    # --------------------------------------------------------

    st.subheader("🏗️ Data Platform Architecture")

    st.code(
        """
                    Online Retail II
                           │
                           ▼
                    Python ETL Pipeline
                           │
                           ▼
                 ┌─────────────────────┐
                 │   Bronze Layer      │
                 │   Raw Data          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Silver Layer      │
                 │   Cleaned Data      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Gold Layer        │
                 │   Analytics Data    │
                 └──────────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
             Snowflake                dbt
                 │                     │
                 └──────────┬──────────┘
                            ▼
                    Streamlit Dashboard
        """,
        language="text",
    )


# ============================================================
# SALES ANALYTICS
# ============================================================

elif page == "Sales Analytics":

    st.header("📈 Sales Analytics")

    # --------------------------------------------------------
    # Monthly Sales
    # --------------------------------------------------------

    st.subheader("Monthly Sales")

    st.dataframe(
        monthly_sales,
        use_container_width=True,
        hide_index=True,
    )

    revenue_column = find_column(
        monthly_sales,
        ["Revenue", "Sales", "Total Revenue"],
    )

    year_column = find_column(
        monthly_sales,
        ["Year"],
    )

    month_column = find_column(
        monthly_sales,
        ["Month"],
    )

    if revenue_column:

        st.subheader("Revenue Trend")

        chart_df = monthly_sales.copy()

        if year_column and month_column:

            chart_df["Date"] = pd.to_datetime(
                chart_df[year_column].astype(str)
                + "-"
                + chart_df[month_column].astype(str)
                + "-01"
            )

            chart_df = (
                chart_df
                .sort_values("Date")
                .set_index("Date")
            )

            st.line_chart(
                chart_df[revenue_column]
            )

        else:

            st.line_chart(
                chart_df[revenue_column]
            )

    st.divider()

    # --------------------------------------------------------
    # Country Sales
    # --------------------------------------------------------

    st.subheader("🌍 Sales by Country")

    st.dataframe(
        country_sales,
        use_container_width=True,
        hide_index=True,
    )

    country_column = find_column(
        country_sales,
        ["Country"],
    )

    country_revenue_column = find_column(
        country_sales,
        ["Revenue", "Sales", "Total Revenue"],
    )

    if country_column and country_revenue_column:

        country_chart = (
            country_sales
            .sort_values(
                country_revenue_column,
                ascending=False,
            )
            .head(15)
        )

        st.subheader("Top Countries by Revenue")

        st.bar_chart(
            country_chart.set_index(
                country_column
            )[country_revenue_column]
        )


# ============================================================
# CUSTOMER ANALYTICS
# ============================================================

elif page == "Customer Analytics":

    st.header("👥 Customer Analytics")

    customer_id_column = find_column(
        customer_summary,
        ["Customer ID", "CustomerID", "customer_id"],
    )

    customer_revenue_column = find_column(
        customer_summary,
        ["Revenue", "Sales", "Total Revenue"],
    )

    # --------------------------------------------------------
    # Customer metrics
    # --------------------------------------------------------

    total_customers = (
        customer_summary[customer_id_column].nunique()
        if customer_id_column
        else len(customer_summary)
    )

    total_customer_revenue = (
        customer_summary[customer_revenue_column].sum()
        if customer_revenue_column
        else 0
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Customers",
            f"{total_customers:,}",
        )

    with col2:

        st.metric(
            "Customer Revenue",
            format_currency(total_customer_revenue),
        )

    st.divider()

    # --------------------------------------------------------
    # Customer table
    # --------------------------------------------------------

    st.subheader("Customer Summary")

    st.dataframe(
        customer_summary,
        use_container_width=True,
        hide_index=True,
    )

    # --------------------------------------------------------
    # Top Customers
    # --------------------------------------------------------

    if customer_id_column and customer_revenue_column:

        st.subheader("Top Customers by Revenue")

        top_customers = (
            customer_summary
            .sort_values(
                customer_revenue_column,
                ascending=False,
            )
            .head(20)
        )

        chart_data = (
            top_customers
            .set_index(customer_id_column)[
                customer_revenue_column
            ]
        )

        st.bar_chart(chart_data)


# ============================================================
# PRODUCT ANALYTICS
# ============================================================

elif page == "Product Analytics":

    st.header("🛍️ Product Analytics")

    product_column = find_column(
        top_products,
        [
            "Description",
            "Product",
            "Product Description",
        ],
    )

    product_revenue_column = find_column(
        top_products,
        [
            "Revenue",
            "Sales",
            "Total Revenue",
        ],
    )

    quantity_column = find_column(
        top_products,
        [
            "Quantity",
            "Units Sold",
            "Total Quantity",
        ],
    )

    # --------------------------------------------------------
    # Product metrics
    # --------------------------------------------------------

    total_products = (
        top_products[product_column].nunique()
        if product_column
        else len(top_products)
    )

    total_units = (
        top_products[quantity_column].sum()
        if quantity_column
        else 0
    )

    total_revenue = (
        top_products[product_revenue_column].sum()
        if product_revenue_column
        else 0
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Products",
            f"{total_products:,}",
        )

    with col2:

        st.metric(
            "Units Sold",
            f"{total_units:,.0f}",
        )

    with col3:

        st.metric(
            "Revenue",
            format_currency(total_revenue),
        )

    st.divider()

    # --------------------------------------------------------
    # Product table
    # --------------------------------------------------------

    st.subheader("Top Products")

    st.dataframe(
        top_products,
        use_container_width=True,
        hide_index=True,
    )

    # --------------------------------------------------------
    # Product chart
    # --------------------------------------------------------

    if product_column and product_revenue_column:

        st.subheader("Top Products by Revenue")

        product_chart = (
            top_products
            .sort_values(
                product_revenue_column,
                ascending=False,
            )
            .head(15)
        )

        st.bar_chart(
            product_chart.set_index(
                product_column
            )[product_revenue_column]
        )


# ============================================================
# DATA QUALITY
# ============================================================

elif page == "Data Quality":

    st.header("🔍 Data Quality")

    st.info(
        "These metrics represent the data-quality checks "
        "performed during the Python validation stage."
    )

    # --------------------------------------------------------
    # Known validation metrics
    # --------------------------------------------------------

    quality_metrics = {
        "Duplicate Rows": 12133,
        "Missing Customer ID": 243007,
        "Missing Description": 4382,
        "Negative Price": 5,
        "Negative Quantity": 229,
    }

    col1, col2, col3, col4, col5 = st.columns(5)

    metrics = list(quality_metrics.items())

    for column, (metric, value) in zip(
        [col1, col2, col3, col4, col5],
        metrics,
    ):

        with column:

            st.metric(
                metric,
                f"{value:,}",
            )

    st.divider()

    # --------------------------------------------------------
    # Data Layers
    # --------------------------------------------------------

    st.subheader("Data Layer Status")

    layers = pd.DataFrame(
        {
            "Layer": [
                "Bronze",
                "Silver",
                "Gold",
            ],
            "Purpose": [
                "Raw extracted data",
                "Cleaned and transformed data",
                "Analytics-ready datasets",
            ],
            "Status": [
                "Available",
                "Available",
                "Available",
            ],
        }
    )

    st.dataframe(
        layers,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    # --------------------------------------------------------
    # Gold datasets
    # --------------------------------------------------------

    st.subheader("Gold Layer Datasets")

    gold_files = [
        "monthly_sales.parquet",
        "country_sales.parquet",
        "customer_summary.parquet",
        "top_products.parquet",
    ]

    for file_name in gold_files:

        file_path = GOLD_PATH / file_name

        if file_path.exists():

            st.success(
                f"✓ {file_name}"
            )

        else:

            st.error(
                f"✗ {file_name}"
            )


# ============================================================
# PIPELINE STATUS
# ============================================================

elif page == "Pipeline Status":

    st.header("⚙️ Pipeline Status")

    st.subheader("ETL Pipeline")

    pipeline_steps = pd.DataFrame(
        {
            "Stage": [
                "Extract",
                "Validate",
                "Transform",
                "Bronze",
                "Silver",
                "Gold",
            ],
            "Technology": [
                "Python / Pandas",
                "Python Validation",
                "Python / Pandas",
                "Parquet",
                "Parquet",
                "Parquet",
            ],
            "Status": [
                "Completed",
                "Completed",
                "Completed",
                "Completed",
                "Completed",
                "Completed",
            ],
        }
    )

    st.dataframe(
        pipeline_steps,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader("Cloud & Analytics Components")

    platform_components = pd.DataFrame(
        {
            "Component": [
                "Amazon S3",
                "Snowflake",
                "dbt",
                "Terraform",
                "GitHub Actions",
                "Streamlit",
            ],
            "Purpose": [
                "Cloud data lake",
                "Cloud data warehouse",
                "SQL transformation",
                "Infrastructure as Code",
                "Continuous Integration",
                "Analytics interface",
            ],
            "Status": [
                "Configured",
                "Configured",
                "Configured",
                "Validated",
                "Passing",
                "Running",
            ],
        }
    )

    st.dataframe(
        platform_components,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader("Pipeline Flow")

    st.code(
        """
Extract
  ↓
Validate
  ↓
Transform
  ↓
Bronze
  ↓
Silver
  ↓
Gold
  ↓
Snowflake
  ↓
dbt
  ↓
Streamlit Dashboard
        """,
        language="text",
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Modern Cloud Data Engineering Pipeline | "
    "Python • S3 • Snowflake • dbt • Terraform • GitHub Actions • Streamlit"
)