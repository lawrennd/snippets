\ifndef{sightingProbabilityAnalysis}
\define{sightingProbabilityAnalysis}

\editme

\subsection{Statistical Analysis of Sighting Patterns}

\notes{Now let's create a simple prediction system for whether a specific `camera` captured a `species` on a given `date`. Before we jump into addressing the question, let's further assess the data. 

We'll calculate and plot average probabilities for dates, species, and cameras. This exploratory analysis helps us understand the underlying patterns in the data.}

\notes{First, let's address some remaining data quality issues:
- "Impala, Monkey" should be split into two species
- "Can't Tell" should be removed
- Large counts likely represent burst photography - convert to binary presence/absence}

\code{# Clean the data further
def clean_species_data(daily_counts):
    """Clean species data and convert to binary sighting indicators"""
    binary_df = daily_counts.copy()
    
    # Convert to binary (presence/absence) to handle burst photography
    binary_df = (binary_df > 0).astype(int)
    
    # Handle multi-species entries (this is dataset-specific logic)
    # Remove "Can't Tell" columns if they exist
    cols_to_drop = []
    for col in binary_df.columns:
        if len(col) == 2:  # (camera, species) tuple
            camera, species = col
            if "Can't Tell" in str(species) or "can't tell" in str(species).lower():
                cols_to_drop.append(col)
    
    binary_df = binary_df.drop(columns=cols_to_drop, errors='ignore')
    
    return binary_df

binary_sightings = clean_species_data(daily_counts)
print(f"Binary sightings shape: {binary_sightings.shape}")
binary_sightings.head()}

\setupcode{import matplotlib.pyplot as plt
import seaborn as sns}

\code{# Calculate overall sighting probabilities by species
if len(binary_sightings.columns) > 0:
    # Extract species names from MultiIndex columns
    species_probs = {}
    for camera, species in binary_sightings.columns:
        if species not in species_probs:
            species_probs[species] = []
        species_probs[species].extend(binary_sightings[(camera, species)].values)
    
    # Calculate mean probability for each species
    species_means = {species: np.mean(sightings) 
                    for species, sightings in species_probs.items()}
    
    # Plot species probabilities
    plt.figure(figsize=(12, 6))
    species_names = list(species_means.keys())
    probabilities = list(species_means.values())
    
    plt.subplot(1, 2, 1)
    plt.bar(range(len(species_names)), probabilities)
    plt.xlabel('Species')
    plt.ylabel('Sighting Probability')
    plt.title('Average Sighting Probability by Species')
    plt.xticks(range(len(species_names)), species_names, rotation=45, ha='right')
    
    # Calculate temporal patterns
    daily_totals = binary_sightings.sum(axis=1)
    plt.subplot(1, 2, 2)
    plt.plot(daily_totals.index, daily_totals.values)
    plt.xlabel('Date')
    plt.ylabel('Total Daily Sightings')
    plt.title('Total Daily Sightings Over Time')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    print("Species sighting probabilities:")
    for species, prob in sorted(species_means.items(), key=lambda x: x[1], reverse=True):
        print(f"  {species}: {prob:.3f}")}

\notes{This analysis reveals important ecological patterns - which species are more commonly observed, seasonal trends, and site-specific preferences. Understanding these patterns is crucial for building accurate predictive models.}

\endif
