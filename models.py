from sqlalchemy import Column, Integer, String, Float
from database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    neighbourhood = Column(String)
    room_type = Column(String)

    price = Column(Float)
    minimum_nights = Column(Integer)

    # ✅ GEO FIELDS (REQUIRED FOR MAPS)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)