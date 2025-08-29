\ifndef{burstDetectionAnalysis}
\define{burstDetectionAnalysis}

\editme

\subsection{Extended Analysis: Burst Detection}

\notes{We didn't use all of the available data when we just classified days as "sighting" or "no sighting". Camera traps often capture "burst" sequences - multiple photos taken in rapid succession when motion is detected. Understanding and properly handling these bursts can provide richer information about animal behavior.

This extended analysis is quite challenging due to the complexity of burst detection and multi-species deduplication.}

\setupcode{import pandas as pd
import numpy as np
from datetime import datetime, timedelta}

\code{# Define what constitutes a "burst"
def detect_bursts(df, time_threshold_minutes=5, min_photos=2):
    """
    Detect photo bursts in camera trap data
    
    Parameters:
        df: DataFrame with timestamp and camera_id columns
        time_threshold_minutes: Photos within this time are considered same burst
        min_photos: Minimum photos to constitute a burst
    
    Returns:
        DataFrame with burst information
    """
    bursts = []
    
    # Group by camera and species
    for (camera, species), group in df.groupby(['camera_id', 'Species']):
        # Sort by timestamp
        group_sorted = group.dropna(subset=['timestamp']).sort_values('timestamp')
        
        if len(group_sorted) < min_photos:
            continue
            
        # Identify bursts using time gaps
        time_diffs = group_sorted['timestamp'].diff()
        burst_breaks = time_diffs > pd.Timedelta(minutes=time_threshold_minutes)
        burst_ids = burst_breaks.cumsum()
        
        # Process each burst
        for burst_id, burst_group in group_sorted.groupby(burst_ids):
            if len(burst_group) >= min_photos:
                burst_info = {
                    'camera_id': camera,
                    'species': species,
                    'burst_start': burst_group['timestamp'].min(),
                    'burst_end': burst_group['timestamp'].max(),
                    'duration_seconds': (burst_group['timestamp'].max() - 
                                       burst_group['timestamp'].min()).total_seconds(),
                    'num_photos': len(burst_group),
                    'date': burst_group['timestamp'].min().date()
                }
                bursts.append(burst_info)
    
    return pd.DataFrame(bursts)

# Apply burst detection to our data (if we have timestamp data)
if 'df' in locals() and 'timestamp' in df.columns:
    burst_data = detect_bursts(df)
    
    print(f"Detected {len(burst_data)} bursts")
    if len(burst_data) > 0:
        print("\nBurst statistics:")
        print(f"  Average photos per burst: {burst_data['num_photos'].mean():.1f}")
        print(f"  Average burst duration: {burst_data['duration_seconds'].mean():.1f} seconds")
        print(f"  Longest burst: {burst_data['num_photos'].max()} photos")
        
        # Show burst distribution by species
        burst_by_species = burst_data.groupby('species').agg({
            'num_photos': ['count', 'mean'],
            'duration_seconds': 'mean'
        }).round(2)
        burst_by_species.columns = ['Total_Bursts', 'Avg_Photos_per_Burst', 'Avg_Duration_Seconds']
        print("\nBurst patterns by species:")
        print(burst_by_species)
else:
    print("Timestamp data not available for burst analysis")}

\code{# Advanced analysis: Multi-species burst handling
def analyze_multispecies_interactions(burst_data, time_window_minutes=10):
    """
    Analyze cases where multiple species appear in close temporal/spatial proximity
    """
    if len(burst_data) == 0:
        return pd.DataFrame()
    
    interactions = []
    
    # Group bursts by camera and date
    for (camera, date), day_bursts in burst_data.groupby(['camera_id', 'date']):
        day_bursts_sorted = day_bursts.sort_values('burst_start')
        
        # Look for overlapping or closely timed bursts of different species
        for i in range(len(day_bursts_sorted)):
            burst1 = day_bursts_sorted.iloc[i]
            
            for j in range(i+1, len(day_bursts_sorted)):
                burst2 = day_bursts_sorted.iloc[j]
                
                # Check if bursts are close in time
                time_gap = (burst2['burst_start'] - burst1['burst_end']).total_seconds()
                
                if time_gap <= time_window_minutes * 60 and burst1['species'] != burst2['species']:
                    interaction = {
                        'camera_id': camera,
                        'date': date,
                        'species_1': burst1['species'],
                        'species_2': burst2['species'],
                        'time_gap_seconds': time_gap,
                        'interaction_type': 'sequential' if time_gap > 0 else 'overlapping'
                    }
                    interactions.append(interaction)
    
    return pd.DataFrame(interactions)

# Analyze species interactions
if 'burst_data' in locals() and len(burst_data) > 0:
    interactions = analyze_multispecies_interactions(burst_data)
    
    if len(interactions) > 0:
        print(f"\nFound {len(interactions)} potential species interactions")
        
        # Most common species pairs
        species_pairs = interactions.groupby(['species_1', 'species_2']).size().sort_values(ascending=False)
        print("\nMost frequent species interactions:")
        print(species_pairs.head())
        
        # Temporal patterns
        avg_gap = interactions['time_gap_seconds'].mean()
        print(f"\nAverage time gap between species: {avg_gap:.1f} seconds")
    else:
        print("\nNo close species interactions detected")
else:
    print("Burst data not available for interaction analysis")}

\notes{This extended analysis demonstrates how camera trap data can be mined for complex ecological insights. Burst patterns can reveal:

- **Feeding behavior**: Long bursts might indicate feeding sites
- **Group dynamics**: Multiple animals in quick succession
- **Species interactions**: Temporal associations between different species
- **Individual identification**: Consistent burst patterns might help identify individuals

The challenge lies in balancing detail with computational complexity, and in handling the inherent uncertainty in automated image analysis.}

\endif
