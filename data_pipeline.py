# import warnings
# warnings.filterwarnings("ignore")


# import pandas as pd
# import numpy as np
# import mysql.connector
# import os
# from dotenv import load_dotenv

# # ----------------------
# # LOAD ENV VARIABLES
# # ----------------------
# load_dotenv()

# # ----------------------
# # LOAD DATASET
# # ----------------------
# df = pd.read_csv("Airbnb_Open_Data.csv", low_memory=False)

# # ----------------------
# # FIX COLUMN NAMES
# # ----------------------
# df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# print("Columns in dataset:\n", df.columns)

# # ----------------------
# # CLEANING
# # ----------------------

# # PRICE
# df['price'] = df['price'].replace('[\$,]', '', regex=True)
# df['price'] = pd.to_numeric(df['price'], errors='coerce')
# df['price'] = df['price'].fillna(df['price'].median())

# # MINIMUM NIGHTS
# if 'minimum_nights' in df.columns:
#     df['minimum_nights'] = pd.to_numeric(df['minimum_nights'], errors='coerce')
#     df['minimum_nights'] = df['minimum_nights'].fillna(df['minimum_nights'].median())

# # AVAILABILITY
# if 'availability_365' in df.columns:
#     df['availability_365'] = pd.to_numeric(df['availability_365'], errors='coerce')
#     df['availability_365'] = df['availability_365'].fillna(0)

# # CATEGORICAL
# for col in ['room_type', 'neighbourhood_group', 'neighbourhood']:
#     if col in df.columns:
#         df[col] = df[col].fillna('Unknown')

# # RENAME LAT/LONG
# if 'lat' in df.columns:
#     df.rename(columns={'lat': 'latitude'}, inplace=True)

# if 'long' in df.columns:
#     df.rename(columns={'long': 'longitude'}, inplace=True)

# # REMOVE DUPLICATES
# df = df.drop_duplicates()

# # ----------------------
# # FEATURE ENGINEERING
# # ----------------------
# df['price_category'] = pd.cut(
#     df['price'],
#     bins=[0, 100, 300, 1000, 10000],
#     labels=['Low', 'Medium', 'High', 'Luxury']
# )

# df['availability_status'] = np.where(
#     df.get('availability_365', 0) > 0,
#     'Available',
#     'Not Available'
# )

# print("Final Shape:", df.shape)

# # ----------------------
# # CONNECT TO MYSQL
# # ----------------------
# conn = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_NAME")
# )

# cursor = conn.cursor()

# # ----------------------
# # CREATE TABLE
# # ----------------------
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS airbnb_cleaned (
#     price FLOAT,
#     minimum_nights FLOAT,
#     room_type VARCHAR(50),
#     neighbourhood_group VARCHAR(50),
#     availability_365 INT,
#     price_category VARCHAR(20),
#     availability_status VARCHAR(20),
#     latitude FLOAT,
#     longitude FLOAT,
#     neighbourhood VARCHAR(100)
# )
# """)

# # ----------------------
# # CLEAR OLD DATA
# # ----------------------
# cursor.execute("DELETE FROM airbnb_cleaned")

# # ----------------------
# # INSERT DATA (FIXED)
# # ----------------------
# for _, row in df.iterrows():
#     row_values = [
#         row.get('price'),
#         row.get('minimum_nights'),
#         row.get('room_type'),
#         row.get('neighbourhood_group'),
#         row.get('availability_365'),
#         str(row.get('price_category')) if pd.notna(row.get('price_category')) else None,
#         row.get('availability_status'),
#         row.get('latitude'),
#         row.get('longitude'),
#         row.get('neighbourhood')
#     ]

#     # 🔥 Convert NaN → None (IMPORTANT FIX)
#     row_values = [None if pd.isna(x) else x for x in row_values]

#     cursor.execute("""
#     INSERT INTO airbnb_cleaned 
#     (price, minimum_nights, room_type, neighbourhood_group,
#      availability_365, price_category, availability_status,
#      latitude, longitude, neighbourhood)
#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#     """, tuple(row_values))

# conn.commit()
# conn.close()

# print("✅ Data inserted into MySQL successfully")





# import warnings
# warnings.filterwarnings("ignore")

# import pandas as pd
# import numpy as np
# import mysql.connector
# import os
# from dotenv import load_dotenv

# # ----------------------
# # LOAD ENV VARIABLES
# # ----------------------
# load_dotenv()

# # ----------------------
# # LOAD DATASET
# # ----------------------
# df = pd.read_csv("Airbnb_Open_Data.csv", low_memory=False)

# # ----------------------
# # FIX COLUMN NAMES
# # ----------------------
# df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# print("Columns in dataset:\n", df.columns)

# # ----------------------
# # CLEANING
# # ----------------------

# # PRICE
# df['price'] = df['price'].replace('[\$,]', '', regex=True)
# df['price'] = pd.to_numeric(df['price'], errors='coerce')
# df['price'] = df['price'].fillna(df['price'].median())

# # MINIMUM NIGHTS
# if 'minimum_nights' in df.columns:
#     df['minimum_nights'] = pd.to_numeric(df['minimum_nights'], errors='coerce')
#     df['minimum_nights'] = df['minimum_nights'].fillna(df['minimum_nights'].median())

# # AVAILABILITY
# if 'availability_365' in df.columns:
#     df['availability_365'] = pd.to_numeric(df['availability_365'], errors='coerce')
#     df['availability_365'] = df['availability_365'].fillna(0)

# # CATEGORICAL
# for col in ['room_type', 'neighbourhood_group', 'neighbourhood']:
#     if col in df.columns:
#         df[col] = df[col].fillna('Unknown')

# # RENAME LAT/LONG
# if 'lat' in df.columns:
#     df.rename(columns={'lat': 'latitude'}, inplace=True)

# if 'long' in df.columns:
#     df.rename(columns={'long': 'longitude'}, inplace=True)

# # REMOVE DUPLICATES
# df = df.drop_duplicates()

# # ----------------------
# # FEATURE ENGINEERING
# # ----------------------
# df['price_category'] = pd.cut(
#     df['price'],
#     bins=[0, 100, 300, 1000, 10000],
#     labels=['Low', 'Medium', 'High', 'Luxury']
# )

# df['availability_status'] = np.where(
#     df.get('availability_365', 0) > 0,
#     'Available',
#     'Not Available'
# )

# print("Final Shape:", df.shape)

# # ----------------------
# # CONNECT TO MYSQL
# # ----------------------
# conn = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_NAME")
# )

# cursor = conn.cursor()

# # ----------------------
# # CREATE TABLE
# # ----------------------
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS airbnb_cleaned (
#     price FLOAT,
#     minimum_nights FLOAT,
#     room_type VARCHAR(50),
#     neighbourhood_group VARCHAR(50),
#     availability_365 INT,
#     price_category VARCHAR(20),
#     availability_status VARCHAR(20),
#     latitude FLOAT,
#     longitude FLOAT,
#     neighbourhood VARCHAR(100)
# )
# """)

# # ----------------------
# # CLEAR OLD DATA
# # ----------------------
# cursor.execute("DELETE FROM airbnb_cleaned")

# # ----------------------
# # PREPARE DATA FOR BULK INSERT
# # ----------------------
# data_to_insert = []

# for _, row in df.iterrows():
#     row_values = [
#         row.get('price'),
#         row.get('minimum_nights'),
#         row.get('room_type'),
#         row.get('neighbourhood_group'),
#         row.get('availability_365'),
#         str(row.get('price_category')) if pd.notna(row.get('price_category')) else None,
#         row.get('availability_status'),
#         row.get('latitude'),
#         row.get('longitude'),
#         row.get('neighbourhood')
#     ]

#     # Convert NaN → None
#     clean_row = tuple(None if pd.isna(x) else x for x in row_values)

#     data_to_insert.append(clean_row)

# # ----------------------
# # BULK INSERT (FAST)
# # ----------------------
# cursor.executemany("""
# INSERT INTO airbnb_cleaned 
# (price, minimum_nights, room_type, neighbourhood_group,
#  availability_365, price_category, availability_status,
#  latitude, longitude, neighbourhood)
# VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
# """, data_to_insert)

# conn.commit()
# conn.close()

# print("✅ Data inserted into MySQL successfully")









import pandas as pd
import warnings
from sqlalchemy.orm import Session

from database import SessionLocal, Base
from models import Listing

warnings.filterwarnings("ignore")

def load_data(csv_path):

    df = pd.read_csv(csv_path, low_memory=False)

    # normalize columns
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    print("Columns:", df.columns)

    df = df.drop_duplicates()

    # price cleaning
    df["price"] = (
        df["price"].astype(str)
        .str.replace(r"[^\d.]", "", regex=True)
    )
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # 🔥 FIX GEO COLUMN NAMES (IMPORTANT)
    if "lat" in df.columns:
        df["lat"] = pd.to_numeric(df["lat"], errors="coerce")

    if "long" in df.columns:
        df["long"] = pd.to_numeric(df["long"], errors="coerce")

    df = df.dropna(subset=["name", "price"])

    df["neighbourhood"] = df.get("neighbourhood", "Unknown").fillna("Unknown")
    df["room_type"] = df.get("room_type", "Unknown").fillna("Unknown")
    df["minimum_nights"] = pd.to_numeric(df.get("minimum_nights", 0), errors="coerce").fillna(0)

    db = SessionLocal()
    inserted = 0

    for _, row in df.iterrows():
        try:
            record = Listing(
                name=row["name"],
                neighbourhood=row["neighbourhood"],
                room_type=row["room_type"],
                price=float(row["price"]),
                minimum_nights=int(row["minimum_nights"]),
                latitude=row["lat"] if "lat" in df.columns else None,
                longitude=row["long"] if "long" in df.columns else None
            )

            db.add(record)
            inserted += 1

        except Exception:
            continue

    db.commit()
    db.close()

    print(f"✅ Inserted rows: {inserted}")

    return df   # 🔥 CRITICAL FIX (was missing)
