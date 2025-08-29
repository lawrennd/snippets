\ifndef{correlationAnalysisImprovements}
\define{correlationAnalysisImprovements}

\editme

\subsection{Advanced Analysis and Model Improvement}

\notes{Let's analyze the data again to find the strongest relationships which can be used to improve predictions. We'll create correlation matrices and other helpful visualizations to understand the patterns better.

Reading through the [DSAIL-Porini paper](https://www.sciencedirect.com/science/article/pii/S2352340922010666) can provide inspiration about other probability analyses that can be done with this type of ecological data.}

\setupcode{import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats}

\code{# Calculate correlation matrices for different aspects of the data
def analyze_correlations(df):
    """Analyze correlations in sighting data"""
    
    # Species co-occurrence correlation
    # Create a matrix of species sightings across all cameras and dates
    species_data = {}
    for camera, species in df.columns:
        if species not in species_data:
            species_data[species] = []
        species_data[species].extend(df[(camera, species)].values)
    
    species_df = pd.DataFrame(species_data)
    
    # Calculate species correlation matrix
    species_corr = species_df.corr()
    
    # Plot correlation matrix
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    sns.heatmap(species_corr, annot=True, cmap='RdBu_r', center=0,
                square=True, fmt='.2f')
    plt.title('Species Co-occurrence Correlations')
    
    # Temporal correlations
    daily_totals = df.sum(axis=1)
    daily_totals_df = pd.DataFrame({
        'total_sightings': daily_totals,
        'day_of_week': [d.weekday() for d in daily_totals.index],
        'day_of_year': [d.timetuple().tm_yday for d in daily_totals.index]
    })
    
    plt.subplot(1, 2, 2)
    # Group by day of week
    weekly_pattern = daily_totals_df.groupby('day_of_week')['total_sightings'].mean()
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    plt.bar(range(7), weekly_pattern.values)
    plt.xlabel('Day of Week')
    plt.ylabel('Average Sightings')
    plt.title('Weekly Pattern in Sightings')
    plt.xticks(range(7), days)
    
    plt.tight_layout()
    plt.show()
    
    return species_corr, weekly_pattern

if len(binary_sightings.columns) > 0:
    species_correlations, weekly_patterns = analyze_correlations(binary_sightings)
    
    print("Strongest positive species correlations:")
    # Find strongest correlations (excluding diagonal)
    mask = np.triu(np.ones_like(species_correlations, dtype=bool))
    species_correlations_masked = species_correlations.mask(mask)
    
    for i in range(min(5, len(species_correlations))):
        max_idx = np.unravel_index(np.nanargmax(species_correlations_masked.values), 
                                  species_correlations_masked.shape)
        if not np.isnan(species_correlations_masked.iloc[max_idx]):
            species1 = species_correlations_masked.index[max_idx[0]]
            species2 = species_correlations_masked.columns[max_idx[1]]
            corr_val = species_correlations_masked.iloc[max_idx]
            print(f"  {species1} - {species2}: {corr_val:.3f}")
            species_correlations_masked.iloc[max_idx] = np.nan
        else:
            break}

\notes{These correlation analyses reveal important ecological relationships that can improve our predictions. Species that frequently occur together, temporal patterns, and location preferences all provide valuable signal for more sophisticated models.}

\code{def improved_sighting_probability(df, camera, species, date) -> float:
    """
    Improved prediction that incorporates correlation patterns
    """
    if isinstance(date, str) or isinstance(date, pd.Timestamp):
        date = pd.to_datetime(date).date()
        
    if (camera, species) not in df.columns:
        return 0.0
    
    # Remove target observation
    df_blind = df.copy()
    df_blind.loc[date, (camera, species)] = np.nan
    
    # Base probability from historical data
    base_prob = df_blind[(camera, species)].mean()
    if pd.isna(base_prob):
        base_prob = 0.1  # Default low probability
    
    # Temporal adjustment (day of week effect)
    day_of_week = date.weekday()
    
    # Get day-of-week effect for this species at this camera
    camera_species_data = df_blind[(camera, species)]
    weekly_data = pd.DataFrame({
        'sighting': camera_species_data,
        'dow': [d.weekday() for d in camera_species_data.index]
    }).dropna()
    
    if len(weekly_data) > 0:
        dow_effect = weekly_data.groupby('dow')['sighting'].mean()
        if day_of_week in dow_effect.index:
            temporal_multiplier = dow_effect[day_of_week] / dow_effect.mean()
        else:
            temporal_multiplier = 1.0
    else:
        temporal_multiplier = 1.0
    
    # Spatial context (other cameras nearby)
    # This is simplified - in practice you'd use actual distances
    other_camera_sightings = []
    for other_camera in set(col[0] for col in df.columns):
        if other_camera != camera and (other_camera, species) in df.columns:
            other_sighting = df_blind.loc[date, (other_camera, species)]
            if not pd.isna(other_sighting):
                other_camera_sightings.append(other_sighting)
    
    if other_camera_sightings:
        spatial_effect = np.mean(other_camera_sightings) * 0.3  # Moderate influence
    else:
        spatial_effect = 0
    
    # Combine factors
    improved_prob = base_prob * temporal_multiplier + spatial_effect
    
    return max(0.0, min(1.0, improved_prob))

# Test improved model
if len(binary_sightings.columns) > 0:
    test_camera, test_species = binary_sightings.columns[0]
    test_date = binary_sightings.index[15]
    
    basic_prob = naive_sighting_probability(binary_sightings, test_camera, test_species, test_date)
    improved_prob = improved_sighting_probability(binary_sightings, test_camera, test_species, test_date)
    actual = binary_sightings.loc[test_date, (test_camera, test_species)]
    
    print(f"\nModel comparison:")
    print(f"  Basic model: {basic_prob:.3f}")
    print(f"  Improved model: {improved_prob:.3f}")
    print(f"  Actual: {actual}")}

\notes{The improved model incorporates temporal patterns and spatial context, which often provide significant predictive power in ecological systems. Real-world improvements would also consider weather data, moon phases, seasonal migration patterns, and other environmental factors.}

\endif
