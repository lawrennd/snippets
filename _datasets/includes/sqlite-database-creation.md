\ifndef{sqliteDatabaseCreation}
\define{sqliteDatabaseCreation}

\editme

\subsection{Database Integration with SQLite}

\notes{Throughout data science projects you will work with various datasets and data formats. An SQL database is one of the most common ways to store large amounts of data. We'll use this example to build a small database of animal sightings based on our processed camera trap data.

Databases provide several advantages:
- Efficient storage and retrieval for large datasets
- Built-in indexing for fast queries
- Concurrent access by multiple users
- Data integrity constraints
- Standardized query language (SQL)}

\setupcode{import sqlite3
import pandas as pd
import numpy as np}

\code{# Create a local SQLite database
def create_sightings_database(sightings_df, camera_coords, db_name="wildlife_sightings.db"):
    """
    Create SQLite database with animal sighting and camera data
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create camera coordinates table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cameras (
            camera_id TEXT PRIMARY KEY,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
    ''')
    
    # Insert camera data
    for camera_id, (lat, lon) in camera_coords.items():
        cursor.execute(
            "INSERT OR REPLACE INTO cameras VALUES (?, ?, ?)",
            (camera_id, lat, lon)
        )
    
    # Create sightings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sightings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            camera_id TEXT NOT NULL,
            species TEXT NOT NULL,
            sighted INTEGER NOT NULL,
            FOREIGN KEY (camera_id) REFERENCES cameras (camera_id)
        )
    ''')
    
    # Convert wide format to long format for database storage
    sightings_long = []
    for date_idx in sightings_df.index:
        for (camera, species) in sightings_df.columns:
            sighting = sightings_df.loc[date_idx, (camera, species)]
            sightings_long.append((str(date_idx), camera, species, int(sighting)))
    
    # Insert sighting data
    cursor.executemany(
        "INSERT INTO sightings (date, camera_id, species, sighted) VALUES (?, ?, ?, ?)",
        sightings_long
    )
    
    # Create indices for efficient queries
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_date ON sightings(date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_camera_species ON sightings(camera_id, species)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_location ON cameras(latitude, longitude)")
    
    conn.commit()
    print(f"Created database '{db_name}' with {len(camera_coords)} cameras and {len(sightings_long)} sighting records")
    
    return conn

# Create the database
if len(binary_sightings.columns) > 0:
    conn = create_sightings_database(binary_sightings, camera_coords)}

\code{# Demonstrate database queries
def demonstrate_sql_queries(conn):
    """Show various SQL query examples"""
    
    print("=== SQL Query Demonstrations ===\n")
    
    # Query 1: Count total sightings by species
    print("1. Total sightings by species:")
    query1 = """
        SELECT species, SUM(sighted) as total_sightings 
        FROM sightings 
        GROUP BY species 
        ORDER BY total_sightings DESC
    """
    result1 = pd.read_sql_query(query1, conn)
    print(result1.head())
    print()
    
    # Query 2: Camera activity levels
    print("2. Camera activity (total sighting days):")
    query2 = """
        SELECT s.camera_id, c.latitude, c.longitude, 
               COUNT(*) as active_days,
               SUM(s.sighted) as total_sightings
        FROM sightings s
        JOIN cameras c ON s.camera_id = c.camera_id
        WHERE s.sighted = 1
        GROUP BY s.camera_id
        ORDER BY total_sightings DESC
    """
    result2 = pd.read_sql_query(query2, conn)
    print(result2)
    print()
    
    # Query 3: Species sightings within geographic area (example)
    print("3. Example geographic query (sightings near center of study area):")
    # Find center coordinates
    center_query = "SELECT AVG(latitude) as center_lat, AVG(longitude) as center_lon FROM cameras"
    center = pd.read_sql_query(center_query, conn)
    center_lat, center_lon = center.iloc[0]['center_lat'], center.iloc[0]['center_lon']
    
    # Simple rectangular bounding box (in practice, you'd use proper geographic distance)
    bbox_size = 0.001  # Very small area for demonstration
    query3 = f"""
        SELECT s.species, COUNT(*) as sightings_in_area
        FROM sightings s
        JOIN cameras c ON s.camera_id = c.camera_id
        WHERE s.sighted = 1
        AND c.latitude BETWEEN {center_lat - bbox_size} AND {center_lat + bbox_size}
        AND c.longitude BETWEEN {center_lon - bbox_size} AND {center_lon + bbox_size}
        GROUP BY s.species
        ORDER BY sightings_in_area DESC
    """
    result3 = pd.read_sql_query(query3, conn)
    print(f"Area around ({center_lat:.4f}, {center_lon:.4f}):")
    print(result3)

# Run demonstrations
if 'conn' in locals():
    demonstrate_sql_queries(conn)
    conn.close()}

\notes{SQL databases provide powerful tools for data analysis, especially when dealing with large datasets that don't fit in memory. The indexing system allows for fast queries even on millions of records, and the relational structure helps maintain data integrity and enables complex joins between different data sources.}

\endif


