# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import mysql.connector
# import os
# from dotenv import load_dotenv

# # Load env variables
# load_dotenv()

# # Page config
# st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

# # DB Connection
# conn = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_NAME")
# )

# # Load data
# @st.cache_data
# def load_data():
#     return pd.read_sql("SELECT * FROM airbnb_cleaned", conn)

# df = load_data()

# # Title
# st.title("🏠 Airbnb Market Insights Dashboard")
# st.markdown("### Real-Time Analytics using MySQL")

# # Sidebar
# st.sidebar.title("🔍 Filters")

# room_type = st.sidebar.multiselect(
#     "Room Type",
#     options=df['room_type'].unique(),
#     default=df['room_type'].unique()
# )

# price_category = st.sidebar.multiselect(
#     "Price Category",
#     options=df['price_category'].dropna().unique(),
#     default=df['price_category'].dropna().unique()
# )

# filtered_df = df[
#     (df['room_type'].isin(room_type)) &
#     (df['price_category'].isin(price_category))
# ]

# # KPIs
# col1, col2, col3, col4 = st.columns(4)
# col1.metric("Total Listings", len(filtered_df))
# col2.metric("Avg Price", round(filtered_df['price'].mean(), 2))
# col3.metric("Max Price", filtered_df['price'].max())
# col4.metric("Min Price", filtered_df['price'].min())

# st.markdown("---")

# # Tabs
# tab1, tab2, tab3 = st.tabs(["📊 Overview", "🌍 Geo Analysis", "📈 Insights"])

# # Overview
# with tab1:
#     fig1 = px.bar(filtered_df, x='room_type', y='price',
#                   color='room_type', title="Room Type vs Price")
#     st.plotly_chart(fig1, use_container_width=True)

#     fig2 = px.pie(filtered_df, names='price_category',
#                   title="Price Distribution")
#     st.plotly_chart(fig2, use_container_width=True)

# # Geo
# with tab2:
#     fig_map = px.scatter_mapbox(
#         filtered_df,
#         lat="latitude",
#         lon="longitude",
#         color="price",
#         size="price",
#         hover_name="neighbourhood",
#         mapbox_style="carto-positron",
#         zoom=10,
#         title="Geo Price Distribution"
#     )
#     st.plotly_chart(fig_map, use_container_width=True)

# # Insights
# with tab3:
#     fig_scatter = px.scatter(
#         filtered_df,
#         x="availability_365",
#         y="price",
#         color="room_type",
#         title="Price vs Availability"
#     )
#     st.plotly_chart(fig_scatter, use_container_width=True)

# st.markdown("---")
# st.markdown("Built by Jyothi 🚀")





# import warnings
# warnings.filterwarnings("ignore")

# import logging

# logging.getLogger("tornado").setLevel(logging.ERROR)
# logging.getLogger("streamlit").setLevel(logging.ERROR)

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import mysql.connector
# import os
# from dotenv import load_dotenv

# # ----------------------
# # LOAD ENV
# # ----------------------
# load_dotenv()

# # ----------------------
# # PAGE CONFIG
# # ----------------------
# st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

# st.title("🏠 Airbnb Market Insights Dashboard")
# st.markdown("### Real-Time Analytics using MySQL")

# # ----------------------
# # DB CONNECTION
# # ----------------------
# conn = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_NAME")
# )

# # ----------------------
# # LOAD DATA WITH SPINNER
# # ----------------------
# with st.spinner("Loading data from MySQL..."):
#     df = pd.read_sql("SELECT * FROM airbnb_cleaned", conn)

# # ----------------------
# # ERROR HANDLING
# # ----------------------
# if df.empty:
#     st.error("❌ No data found in database")
#     st.stop()

# # ----------------------
# # SQL AGGREGATIONS
# # ----------------------
# room_summary = pd.read_sql("""
# SELECT 
#     room_type,
#     AVG(price) AS avg_price,
#     COUNT(*) AS total_listings
# FROM airbnb_cleaned
# GROUP BY room_type
# """, conn)

# location_summary = pd.read_sql("""
# SELECT 
#     neighbourhood_group,
#     AVG(price) AS avg_price,
#     COUNT(*) AS total_listings
# FROM airbnb_cleaned
# GROUP BY neighbourhood_group
# """, conn)

# # ----------------------
# # SIDEBAR
# # ----------------------
# st.sidebar.markdown("## 🎛️ Dashboard Controls")
# st.sidebar.markdown("---")

# room_type = st.sidebar.multiselect(
#     "Room Type",
#     options=df['room_type'].dropna().unique(),
#     default=df['room_type'].dropna().unique()
# )

# price_category = st.sidebar.multiselect(
#     "Price Category",
#     options=df['price_category'].dropna().unique(),
#     default=df['price_category'].dropna().unique()
# )

# # ----------------------
# # FILTER DATA
# # ----------------------
# filtered_df = df[
#     (df['room_type'].isin(room_type)) &
#     (df['price_category'].isin(price_category))
# ]

# # ----------------------
# # KPIs
# # ----------------------
# st.markdown("## 📊 Key Performance Indicators")

# col1, col2, col3, col4 = st.columns(4)

# col1.metric("Total Listings", len(filtered_df))
# col2.metric("Avg Price", round(filtered_df['price'].mean(), 2))
# col3.metric("Max Price", filtered_df['price'].max())
# col4.metric("Min Price", filtered_df['price'].min())

# # ----------------------
# # DOWNLOAD BUTTON
# # ----------------------
# st.download_button(
#     label="📥 Download Cleaned Data",
#     data=filtered_df.to_csv(index=False),
#     file_name="airbnb_cleaned.csv",
#     mime="text/csv"
# )

# st.markdown("---")

# # ----------------------
# # TABS
# # ----------------------
# tab1, tab2, tab3, tab4 = st.tabs(
#     ["📊 Overview", "🌍 Geo Analysis", "📈 Insights", "📑 SQL Analysis"]
# )

# # ----------------------
# # OVERVIEW TAB
# # ----------------------
# with tab1:
#     st.subheader("Room Type vs Price")

#     fig1 = px.bar(
#         filtered_df,
#         x='room_type',
#         y='price',
#         color='room_type'
#     )
#     st.plotly_chart(fig1, use_container_width=True)

#     st.subheader("Price Distribution")

#     fig2 = px.pie(
#         filtered_df,
#         names='price_category'
#     )
#     st.plotly_chart(fig2, use_container_width=True)

# # ----------------------
# # GEO TAB
# # ----------------------
# with tab2:
#     st.subheader("Geo Price Distribution")

#     fig_map = px.scatter_mapbox(
#         filtered_df,
#         lat="latitude",
#         lon="longitude",
#         color="price",
#         size="price",
#         hover_name="neighbourhood",
#         mapbox_style="carto-positron",
#         zoom=10
#     )
#     st.plotly_chart(fig_map, use_container_width=True)

# # ----------------------
# # INSIGHTS TAB
# # ----------------------
# with tab3:
#     st.subheader("Price vs Availability")

#     fig_scatter = px.scatter(
#         filtered_df,
#         x="availability_365",
#         y="price",
#         color="room_type"
#     )
#     st.plotly_chart(fig_scatter, use_container_width=True)

# # ----------------------
# # SQL ANALYSIS TAB (NEW 🔥)
# # ----------------------
# with tab4:
#     st.subheader("📊 Room Type Summary")
#     st.dataframe(room_summary)

#     st.subheader("🌍 Location Summary")
#     st.dataframe(location_summary)

# # ----------------------
# # FOOTER
# # ----------------------
# st.markdown("---")
# st.markdown("Built by Jyothi 🚀 | Production-Level Project")





# import streamlit as st
# import pandas as pd
# from sqlalchemy import create_engine
# import plotly.express as px
# from urllib.parse import quote_plus
# import os
# from dotenv import load_dotenv

# # ---------------- DB ----------------
# load_dotenv()

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# engine = create_engine(
#     f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

# # ---------------- UI ----------------
# st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

# st.markdown("<h1 style='text-align:center;'>🏠 Airbnb Analytics Dashboard</h1>", unsafe_allow_html=True)

# # ---------------- LOAD DATA ----------------
# @st.cache_data
# def load_data():
#     return pd.read_sql("SELECT * FROM listings", engine)

# df = load_data()

# # ---------------- SIDEBAR ----------------
# st.sidebar.title("Filters")

# neighbourhood = st.sidebar.multiselect("Neighbourhood", df["neighbourhood"].unique())
# room_type = st.sidebar.multiselect("Room Type", df["room_type"].unique())

# filtered_df = df.copy()

# if neighbourhood:
#     filtered_df = filtered_df[filtered_df["neighbourhood"].isin(neighbourhood)]

# if room_type:
#     filtered_df = filtered_df[filtered_df["room_type"].isin(room_type)]

# # ---------------- KPIs ----------------
# st.markdown("## 📊 Key Metrics")

# c1, c2, c3, c4 = st.columns(4)

# c1.metric("Total Listings", len(filtered_df))
# c2.metric("Avg Price", f"${filtered_df['price'].mean():.2f}")
# c3.metric("Max Price", f"${filtered_df['price'].max():.2f}")
# c4.metric("Min Price", f"${filtered_df['price'].min():.2f}")

# st.markdown("---")

# # ---------------- TABS ----------------
# tab1, tab2, tab3, tab4 = st.tabs(
#     ["📊 Overview", "🌍 Geo Analysis", "📈 Insights", "📑 SQL Analysis"]
# )

# # ---------------- TAB 1 ----------------
# with tab1:
#     st.subheader("Room Type Distribution")

#     fig1 = px.bar(
#         filtered_df,
#         x="room_type",
#         y="price",
#         color="room_type"
#     )
#     st.plotly_chart(fig1, use_container_width=True)

#     st.subheader("Price Distribution")

#     fig2 = px.pie(filtered_df, names="room_type")
#     st.plotly_chart(fig2, use_container_width=True)

# # ---------------- TAB 2 (MAP) ----------------
# # ---------------- TAB 2 (MAP) ----------------
# with tab2:
#     st.subheader("🌍 Geo Analysis Dashboard")

#     st.write("📌 Exploring spatial price distribution of Airbnb listings")

#     # ---------------- SAFETY CHECK ----------------
#     if "latitude" in filtered_df.columns and "longitude" in filtered_df.columns:

#         geo_df = filtered_df.dropna(subset=["latitude", "longitude"]).copy()

#         # ================= MAIN MAP =================
#         st.markdown("### 📍 Price Distribution Map")

#         fig_map = px.scatter_mapbox(
#             geo_df,
#             lat="latitude",
#             lon="longitude",
#             color="price",
#             size="price",
#             hover_name="neighbourhood",
#             hover_data=["room_type", "price"],
#             zoom=10,
#             mapbox_style="carto-positron"
#         )

#         st.plotly_chart(fig_map, use_container_width=True)

#         # ================= HEATMAP =================
#         st.markdown("### 🔥 Price Heatmap (Hot Zones)")

#         fig_heat = px.density_mapbox(
#             geo_df,
#             lat="latitude",
#             lon="longitude",
#             z="price",
#             radius=12,
#             center=dict(
#                 lat=geo_df["latitude"].mean(),
#                 lon=geo_df["longitude"].mean()
#             ),
#             zoom=10,
#             mapbox_style="carto-positron"
#         )

#         st.plotly_chart(fig_heat, use_container_width=True)

#         # ================= CLUSTER VIEW =================
#         st.markdown("### 🔵 Clustered Listings View")

#         fig_cluster = px.scatter_mapbox(
#             geo_df,
#             lat="latitude",
#             lon="longitude",
#             color="neighbourhood",
#             hover_data=["price", "room_type"],
#             zoom=10,
#             mapbox_style="carto-positron"
#         )

#         st.plotly_chart(fig_cluster, use_container_width=True)

#         # ================= QUICK GEO INSIGHTS =================
#         st.markdown("### 🧠 Geo Insights")

#         col1, col2, col3 = st.columns(3)

#         col1.metric("Total Geo Listings", len(geo_df))
#         col2.metric("Avg Price (Geo)", round(geo_df["price"].mean(), 2))
#         col3.metric("Max Price (Geo)", geo_df["price"].max())

#     else:
#         st.error("❌ Latitude/Longitude columns not found in dataset")

# # ---------------- TAB 3 ----------------
# with tab3:
#     st.subheader("Price vs Availability")

#     if "availability_365" in df.columns:
#         fig3 = px.scatter(
#             filtered_df,
#             x="availability_365",
#             y="price",
#             color="room_type"
#         )
#         st.plotly_chart(fig3, use_container_width=True)

# # ---------------- TAB 4 (SQL INSIGHTS) ----------------
# with tab4:
#     st.subheader("SQL Aggregation")

#     room_summary = filtered_df.groupby("room_type")["price"].mean().reset_index()

#     st.dataframe(room_summary)

# # ---------------- INSIGHTS ----------------
# st.subheader("🧠 Insights")

# top_area = filtered_df.groupby("neighbourhood")["price"].mean().idxmax()

# st.info(f"""
# - 💰 Avg Price: ${filtered_df['price'].mean():.2f}
# - 📍 Most expensive area: {top_area}
# - 🏠 Listings: {len(filtered_df)}
# """)

# # ---------------- BUTTONS UNDER INSIGHTS ----------------
# col1, col2 = st.columns(2)

# with col1:
#     view_data = st.button("👁️ View Data")

# with col2:
#     st.download_button(
#         "⬇️ Download CSV",
#         filtered_df.to_csv(index=False),
#         file_name="airbnb_data.csv",
#         mime="text/csv"
#     )

# # ---------------- EXPANDABLE DATA VIEW ----------------
# if view_data:
#     st.markdown("## 📋 Dataset Preview")
#     st.dataframe(filtered_df, use_container_width=True)
# st.markdown("---")
# st.markdown("<h3 style='text-align:right;'>📥 Export Data</h3>", unsafe_allow_html=True)












# import streamlit as st
# import pandas as pd
# from sqlalchemy import create_engine
# import plotly.express as px
# from urllib.parse import quote_plus
# import os
# from dotenv import load_dotenv

# # ---------------- DB ----------------
# load_dotenv()

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# engine = create_engine(
#     f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

# # ---------------- UI ----------------
# st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

# st.markdown(
#     "<h1 style='text-align:center;'>🏠 Airbnb Analytics Dashboard</h1>",
#     unsafe_allow_html=True
# )

# # ---------------- LOAD DATA ----------------
# @st.cache_data
# def load_data():
#     return pd.read_sql("SELECT * FROM listings", engine)

# df = load_data()

# # ---------------- SIDEBAR FILTERS ----------------
# st.sidebar.title("Filters")

# neighbourhood = st.sidebar.multiselect(
#     "Neighbourhood", df["neighbourhood"].dropna().unique()
# )

# room_type = st.sidebar.multiselect(
#     "Room Type", df["room_type"].dropna().unique()
# )

# filtered_df = df.copy()

# if neighbourhood:
#     filtered_df = filtered_df[filtered_df["neighbourhood"].isin(neighbourhood)]

# if room_type:
#     filtered_df = filtered_df[filtered_df["room_type"].isin(room_type)]

# # ---------------- SAFE KPI CALCULATION ----------------
# def safe_mean(x):
#     return x.mean() if len(x) else 0

# def safe_max(x):
#     return x.max() if len(x) else 0

# def safe_min(x):
#     return x.min() if len(x) else 0

# # ---------------- KPIs ----------------
# st.markdown("## 📊 Key Metrics")

# c1, c2, c3, c4 = st.columns(4)

# c1.metric("Total Listings", len(filtered_df))
# c2.metric("Avg Price", f"${safe_mean(filtered_df['price']):.2f}")
# c3.metric("Max Price", f"${safe_max(filtered_df['price']):.2f}")
# c4.metric("Min Price", f"${safe_min(filtered_df['price']):.2f}")

# st.markdown("---")

# # ---------------- TABS ----------------
# tab1, tab2, tab3, tab4 = st.tabs(
#     ["📊 Overview", "🌍 Geo Analysis", "📈 Insights", "📑 SQL Analysis"]
# )

# # ---------------- TAB 1 ----------------
# with tab1:
#     st.subheader("Room Type Distribution")

#     fig1 = px.bar(
#         filtered_df,
#         x="room_type",
#         y="price",
#         color="room_type"
#     )
#     st.plotly_chart(fig1, use_container_width=True)

#     st.subheader("Price Distribution")

#     fig2 = px.pie(
#         filtered_df,
#         names="room_type"
#     )
#     st.plotly_chart(fig2, use_container_width=True)

# # ---------------- TAB 2 (MAP FIXED) ----------------
# with tab2:
#     st.subheader("🌍 Geo Analysis Dashboard")

#     if {"latitude", "longitude"}.issubset(filtered_df.columns):

#         geo_df = filtered_df.dropna(subset=["latitude", "longitude"]).copy()

#         st.markdown("### 📍 Price Distribution Map")

#         fig_map = px.scatter_map(
#             geo_df,
#             lat="latitude",
#             lon="longitude",
#             color="price",
#             size="price",
#             hover_name="neighbourhood",
#             hover_data=["room_type", "price"],
#             zoom=10
#         )
#         fig_map.update_layout(map_style="open-street-map")
#         st.plotly_chart(fig_map, use_container_width=True)

#         st.markdown("### 🔥 Price Heatmap")

#         fig_heat = px.density_map(
#             geo_df,
#             lat="latitude",
#             lon="longitude",
#             z="price",
#             radius=12,
#             center=dict(
#                 lat=geo_df["latitude"].mean(),
#                 lon=geo_df["longitude"].mean()
#             ),
#             zoom=10
#         )
#         fig_heat.update_layout(map_style="open-street-map")
#         st.plotly_chart(fig_heat, use_container_width=True)

#         st.markdown("### 🔵 Cluster View")

#         fig_cluster = px.scatter_map(
#             geo_df,
#             lat="latitude",
#             lon="longitude",
#             color="neighbourhood",
#             hover_data=["price", "room_type"],
#             zoom=10
#         )
#         fig_cluster.update_layout(map_style="open-street-map")
#         st.plotly_chart(fig_cluster, use_container_width=True)

#         st.markdown("### 🧠 Geo Insights")

#         col1, col2, col3 = st.columns(3)

#         col1.metric("Total Geo Listings", len(geo_df))
#         col2.metric("Avg Price (Geo)", round(safe_mean(geo_df["price"]), 2))
#         col3.metric("Max Price (Geo)", safe_max(geo_df["price"]))

#     else:
#         st.error("❌ Latitude/Longitude columns not found in dataset")

# # ---------------- TAB 3 ----------------
# with tab3:
#     st.subheader("Price vs Availability")

#     if "availability_365" in df.columns:
#         fig3 = px.scatter(
#             filtered_df,
#             x="availability_365",
#             y="price",
#             color="room_type"
#         )
#         st.plotly_chart(fig3, use_container_width=True)

# # ---------------- TAB 4 ----------------
# with tab4:
#     st.subheader("SQL Aggregation")

#     room_summary = filtered_df.groupby("room_type")["price"].mean().reset_index()
#     st.dataframe(room_summary)

# # ---------------- INSIGHTS ----------------
# st.subheader("🧠 Insights")

# if len(filtered_df):
#     top_area = (
#         filtered_df.groupby("neighbourhood")["price"]
#         .mean()
#         .idxmax()
#     )
# else:
#     top_area = "N/A"

# st.info(f"""
# - 💰 Avg Price: ${safe_mean(filtered_df['price']):.2f}
# - 📍 Most expensive area: {top_area}
# - 🏠 Listings: {len(filtered_df)}
# """)

# # ---------------- BUTTONS ----------------
# col1, col2 = st.columns(2)

# with col1:
#     view_data = st.button("👁️ View Data")

# with col2:
#     st.download_button(
#         "⬇️ Download CSV",
#         filtered_df.to_csv(index=False),
#         file_name="airbnb_data.csv",
#         mime="text/csv"
#     )

# # ---------------- DATA VIEW ----------------
# if view_data:
#     st.markdown("## 📋 Dataset Preview")
#     st.dataframe(filtered_df, use_container_width=True)

# st.markdown("---")
# st.markdown(
#     "<h3 style='text-align:right;'>📥 Export Data</h3>",
#     unsafe_allow_html=True
# )







# import os
# import warnings
# import logging

# # =======================
# # 🔇 SUPPRESS WARNINGS & TORCH LOGS
# # =======================
# warnings.filterwarnings("ignore")

# logging.getLogger("tornado").setLevel(logging.ERROR)
# logging.getLogger("streamlit").setLevel(logging.ERROR)
# logging.getLogger("asyncio").setLevel(logging.ERROR)

# os.environ["PYTHONWARNINGS"] = "ignore"

# # =======================
# # IMPORTS
# # =======================
# import streamlit as st
# import pandas as pd
# from sqlalchemy import create_engine
# import plotly.express as px
# from urllib.parse import quote_plus
# from dotenv import load_dotenv

# # ---------------- DB ----------------
# load_dotenv()

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# engine = create_engine(
#     f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

# # ---------------- UI ----------------
# st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

# st.markdown(
#     "<h1 style='text-align:center;'>🏠 Airbnb Analytics Dashboard</h1>",
#     unsafe_allow_html=True
# )

# # ---------------- DATA ----------------
# @st.cache_data
# def load_data():
#     return pd.read_sql("SELECT * FROM listings", engine)

# df = load_data()

# # ---------------- FILTERS ----------------
# st.sidebar.title("Filters")

# neighbourhood = st.sidebar.multiselect(
#     "Neighbourhood", df["neighbourhood"].dropna().unique()
# )

# room_type = st.sidebar.multiselect(
#     "Room Type", df["room_type"].dropna().unique()
# )

# filtered_df = df.copy()

# if neighbourhood:
#     filtered_df = filtered_df[filtered_df["neighbourhood"].isin(neighbourhood)]

# if room_type:
#     filtered_df = filtered_df[filtered_df["room_type"].isin(room_type)]

# # ---------------- SAFE FUNCTIONS ----------------
# def safe_mean(x):
#     return x.mean() if len(x) else 0

# def safe_max(x):
#     return x.max() if len(x) else 0

# def safe_min(x):
#     return x.min() if len(x) else 0

# # ---------------- KPI ----------------
# st.markdown("## 📊 Key Metrics")

# c1, c2, c3, c4 = st.columns(4)

# c1.metric("Total Listings", len(filtered_df))
# c2.metric("Avg Price", f"${safe_mean(filtered_df['price']):.2f}")
# c3.metric("Max Price", f"${safe_max(filtered_df['price']):.2f}")
# c4.metric("Min Price", f"${safe_min(filtered_df['price']):.2f}")

# st.markdown("---")

# # ---------------- TABS ----------------
# tab1, tab2, tab3, tab4 = st.tabs(
#     ["📊 Overview", "🌍 Geo Analysis", "📈 Insights", "📑 SQL Analysis"]
# )

# # ---------------- TAB 1 ----------------
# with tab1:
#     st.subheader("Room Type Distribution")

#     fig1 = px.bar(
#         filtered_df,
#         x="room_type",
#         y="price",
#         color="room_type"
#     )
#     st.plotly_chart(fig1, use_container_width=True)

#     st.subheader("Price Distribution")

#     fig2 = px.pie(filtered_df, names="room_type")
#     st.plotly_chart(fig2, use_container_width=True)

# # ---------------- TAB 2 (MAP CLEAN) ----------------
# with tab2:
#     st.subheader("🌍 Geo Analysis Dashboard")

#     if {"latitude", "longitude"}.issubset(filtered_df.columns):

#         geo_df = filtered_df.dropna(subset=["latitude", "longitude"])

#         st.markdown("### 📍 Map View")

#         fig_map = px.scatter_map(
#             geo_df,
#             lat="latitude",
#             lon="longitude",
#             color="price",
#             size="price",
#             hover_name="neighbourhood",
#             hover_data=["room_type", "price"],
#             zoom=10
#         )
#         fig_map.update_layout(map_style="open-street-map")
#         st.plotly_chart(fig_map, use_container_width=True)

#         st.markdown("### 🔥 Heatmap")

#         fig_heat = px.density_map(
#             geo_df,
#             lat="latitude",
#             lon="longitude",
#             z="price",
#             radius=12,
#             center=dict(
#                 lat=geo_df["latitude"].mean(),
#                 lon=geo_df["longitude"].mean()
#             ),
#             zoom=10
#         )
#         fig_heat.update_layout(map_style="open-street-map")
#         st.plotly_chart(fig_heat, use_container_width=True)

#     else:
#         st.error("Latitude / Longitude missing")

# # ---------------- TAB 3 ----------------
# with tab3:
#     st.subheader("Price vs Availability")

#     if "availability_365" in df.columns:
#         fig3 = px.scatter(
#             filtered_df,
#             x="availability_365",
#             y="price",
#             color="room_type"
#         )
#         st.plotly_chart(fig3, use_container_width=True)

# # ---------------- TAB 4 ----------------
# with tab4:
#     st.subheader("SQL Aggregation")

#     room_summary = filtered_df.groupby("room_type")["price"].mean().reset_index()
#     st.dataframe(room_summary)

# # ---------------- INSIGHTS ----------------
# st.subheader("🧠 Insights")

# if len(filtered_df):
#     top_area = filtered_df.groupby("neighbourhood")["price"].mean().idxmax()
# else:
#     top_area = "N/A"

# st.info(f"""
# - 💰 Avg Price: ${safe_mean(filtered_df['price']):.2f}
# - 📍 Most expensive area: {top_area}
# - 🏠 Listings: {len(filtered_df)}
# """)

# # ---------------- DATA VIEW ----------------
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("👁️ View Data"):
#         st.dataframe(filtered_df, use_container_width=True)

# with col2:
#     st.download_button(
#         "⬇️ Download CSV",
#         filtered_df.to_csv(index=False),
#         file_name="airbnb_data.csv",
#         mime="text/csv"
#     )








# import streamlit as st
# import pandas as pd
# from sqlalchemy import create_engine
# import plotly.express as px
# import os
# from dotenv import load_dotenv
# from urllib.parse import quote_plus

# # ---------------- CONFIG ----------------
# load_dotenv()

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# # ---------------- CACHE ENGINE ----------------
# @st.cache_resource
# def get_engine():
#     return create_engine(DB_URL)


# engine = get_engine()


# # ---------------- LOAD DATA ----------------
# @st.cache_data(ttl=3600)
# def load_data():
#     query = "SELECT * FROM listings"
#     df = pd.read_sql(query, engine)
#     return df


# df = load_data()

# # ---------------- SIDEBAR ----------------
# st.sidebar.title("Filters")

# neighbourhoods = df["neighbourhood"].dropna().unique()
# selected_area = st.sidebar.selectbox("Select Area", neighbourhoods)

# filtered_df = df[df["neighbourhood"] == selected_area]

# # ---------------- MAIN UI ----------------
# st.title("🏠 Airbnb Dashboard")

# st.subheader("Insights")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("Total Listings", len(filtered_df))

# with col2:
#     st.metric("Avg Price", round(filtered_df["price"].mean(), 2))

# with col3:
#     st.metric("Max Price", filtered_df["price"].max())

# # ---------------- CHART ----------------
# fig = px.histogram(filtered_df, x="price")
# st.plotly_chart(fig, use_container_width=True)

# # ---------------- TABLE ----------------
# with st.expander("View Data"):
#     st.dataframe(filtered_df)

#     csv = filtered_df.to_csv(index=False).encode("utf-8")
#     st.download_button("Download CSV", csv, "airbnb_data.csv", "text/csv")







# import streamlit as st
# import pandas as pd
# from sqlalchemy import create_engine
# from urllib.parse import quote_plus
# import os
# from dotenv import load_dotenv
# import plotly.express as px

# # ---------------- CONFIG ----------------
# st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

# load_dotenv()

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# # ---------------- CACHE ENGINE ----------------
# @st.cache_resource
# def get_engine():
#     return create_engine(DB_URL)

# engine = get_engine()


# # ---------------- LOAD DATA ----------------
# @st.cache_data(ttl=3600)
# def load_data():
#     query = "SELECT * FROM listings"
#     return pd.read_sql(query, engine)

# df = load_data()


# # ---------------- SIDEBAR FILTERS ----------------
# st.sidebar.title("Filters")

# neighbourhoods = df["neighbourhood"].dropna().unique()
# selected_area = st.sidebar.selectbox("Select Neighbourhood", neighbourhoods)

# filtered_df = df[df["neighbourhood"] == selected_area]


# # ---------------- TABS UI ----------------
# tab1, tab2, tab3, tab4 = st.tabs([
#     "🏠 Overview",
#     "📊 Insights",
#     "📍 Price Analysis",
#     "📂 Data View"
# ])


# # ================= TAB 1 =================
# with tab1:
#     st.title("🏠 Airbnb Dashboard Overview")

#     st.metric("Total Listings", len(filtered_df))
#     st.metric("Avg Price", round(filtered_df["price"].mean(), 2))
#     st.metric("Max Price", filtered_df["price"].max())


# # ================= TAB 2 =================
# with tab2:
#     st.subheader("🧠 Insights")

#     if len(filtered_df) > 0:
#         top_area = filtered_df.groupby("neighbourhood")["price"].mean().idxmax()

#         col1, col2 = st.columns(2)

#         with col1:
#             st.info(f"""
#             💰 Avg Price: ${filtered_df['price'].mean():.2f}
#             📍 Most expensive area: {top_area}
#             🏠 Listings: {len(filtered_df)}
#             """)

#         with col2:
#             st.bar_chart(filtered_df["price"].value_counts().head(10))


# # ================= TAB 3 =================
# with tab3:
#     st.subheader("📊 Price Distribution")

#     fig = px.histogram(filtered_df, x="price", nbins=50)
#     st.plotly_chart(fig, use_container_width=True)

#     fig2 = px.box(filtered_df, y="price")
#     st.plotly_chart(fig2, use_container_width=True)


# # ================= TAB 4 =================
# with tab4:
#     st.subheader("📂 Data Table")

#     st.dataframe(filtered_df)

#     csv = filtered_df.to_csv(index=False).encode("utf-8")

#     st.download_button(
#         "⬇ Download CSV",
#         csv,
#         "airbnb_data.csv",
#         "text/csv"
#     )









import os
import warnings
import logging

# =======================
# 🔇 SUPPRESS WARNINGS
# =======================
warnings.filterwarnings("ignore")
logging.getLogger("tornado").setLevel(logging.ERROR)
logging.getLogger("streamlit").setLevel(logging.ERROR)

# =======================
# IMPORTS
# =======================
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
from urllib.parse import quote_plus
from dotenv import load_dotenv

# ---------------- DB ----------------
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ---------------- UI ----------------
st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

st.markdown(
    "<h1 style='text-align:center;'>🏠 Airbnb Analytics Dashboard</h1>",
    unsafe_allow_html=True
)

# ---------------- DATA ----------------
@st.cache_data
def load_data():
    return pd.read_sql("SELECT * FROM listings", engine)

df = load_data()

# ---------------- FILTERS ----------------
st.sidebar.title("Filters")

neighbourhood = st.sidebar.multiselect(
    "Neighbourhood", df["neighbourhood"].dropna().unique()
)

room_type = st.sidebar.multiselect(
    "Room Type", df["room_type"].dropna().unique()
)

filtered_df = df.copy()

if neighbourhood:
    filtered_df = filtered_df[filtered_df["neighbourhood"].isin(neighbourhood)]

if room_type:
    filtered_df = filtered_df[filtered_df["room_type"].isin(room_type)]

# ---------------- SAFE FUNCTIONS ----------------
def safe_mean(x):
    return x.mean() if len(x) else 0

def safe_max(x):
    return x.max() if len(x) else 0

def safe_min(x):
    return x.min() if len(x) else 0

# ---------------- KPI ----------------
st.markdown("## 📊 Key Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Listings", len(filtered_df))
c2.metric("Avg Price", f"${safe_mean(filtered_df['price']):.2f}")
c3.metric("Max Price", f"${safe_max(filtered_df['price']):.2f}")
c4.metric("Min Price", f"${safe_min(filtered_df['price']):.2f}")

st.markdown("---")

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 Overview", "🌍 Geo Analysis", "📈 Insights", "📑 SQL Analysis"]
)

# ---------------- TAB 1 ----------------
with tab1:
    st.subheader("Room Type Distribution")

    fig1 = px.bar(
        filtered_df,
        x="room_type",
        y="price",
        color="room_type"
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Room Type Share")

    fig2 = px.pie(filtered_df, names="room_type")
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- TAB 2 ----------------
with tab2:
    st.subheader("🌍 Geo Analysis Dashboard")

    if {"latitude", "longitude"}.issubset(filtered_df.columns):

        geo_df = filtered_df.dropna(subset=["latitude", "longitude"])

        st.markdown("### 📍 Map View")

        fig_map = px.scatter_mapbox(
            geo_df,
            lat="latitude",
            lon="longitude",
            color="price",
            size="price",
            hover_name="neighbourhood",
            zoom=10
        )
        fig_map.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig_map, use_container_width=True)

        st.markdown("### 🔥 Heatmap")

        fig_heat = px.density_mapbox(
            geo_df,
            lat="latitude",
            lon="longitude",
            z="price",
            radius=10,
            zoom=10
        )
        fig_heat.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig_heat, use_container_width=True)

    else:
        st.error("Latitude / Longitude missing")

# ---------------- TAB 3 ----------------
with tab3:
    st.subheader("Price vs Availability")

    if "availability_365" in df.columns:
        fig3 = px.scatter(
            filtered_df,
            x="availability_365",
            y="price",
            color="room_type"
        )
        st.plotly_chart(fig3, use_container_width=True)

# ---------------- TAB 4 ----------------
with tab4:
    st.subheader("SQL Aggregation")

    room_summary = filtered_df.groupby("room_type")["price"].mean().reset_index()
    st.dataframe(room_summary)

# ---------------- INSIGHTS ----------------
st.subheader("🧠 Insights")

if len(filtered_df):
    top_area = filtered_df.groupby("neighbourhood")["price"].mean().idxmax()
else:
    top_area = "N/A"

col1, col2 = st.columns([3, 1])

with col1:
    st.info(f"""
    - 💰 Avg Price: ${safe_mean(filtered_df['price']):.2f}
    - 📍 Most expensive area: {top_area}
    - 🏠 Listings: {len(filtered_df)}
    """)

with col2:
    st.download_button(
        "⬇️ Download CSV",
        filtered_df.to_csv(index=False),
        file_name="airbnb_data.csv",
        mime="text/csv"
    )

# 👁️ View data button (right aligned feel)
if st.button("👁️ View Data"):
    st.dataframe(filtered_df, use_container_width=True)