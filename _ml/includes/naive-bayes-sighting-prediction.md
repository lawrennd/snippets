\ifndef{naiveBayesSightingPrediction}
\define{naiveBayesSightingPrediction}

\editme

\subsection{Address: Naive Bayesian Prediction Model}

\notes{Using the data we collected in the Access stage and understood in Assess, we can now Address our question: create a naive Bayesian classification model for predicting the probability of a camera sighting a species on a given day.

The naive Bayes approach assumes independence between different factors, which simplifies our model:

$$P(\text{sighting} | \text{camera, species, date}) \propto P(\text{sighting} | \text{camera}) \times P(\text{sighting} | \text{species}) \times P(\text{sighting} | \text{date})$$}

\setupcode{from typing import Union
from datetime import date as DateType}

\code{def naive_sighting_probability(df, camera, species, date) -> float:
    """
    Estimates the probability of sighting a given species at a given camera 
    on a specific date using naive Bayes approach.
    
    Parameters:
        df (pd.DataFrame): DataFrame with MultiIndex columns (camera, species) 
                          and datetime.date index
        camera (str): Camera ID (e.g. 'C001')
        species (str): Species name (e.g. 'IMPALA')  
        date (str/date/Timestamp): Date of the observation
        
    Returns:
        float: Estimated sighting probability
    """
    if isinstance(date, str) or isinstance(date, pd.Timestamp):
        date = pd.to_datetime(date).date()
    
    # Check if the specific (camera, species) combination exists
    if (camera, species) not in df.columns:
        return 0.0
    
    # Remove the target observation to avoid data leakage
    df_blind = df.copy()
    df_blind.loc[date, (camera, species)] = np.nan
    
    # Calculate component probabilities
    # P(sighting | camera, species) - base rate for this camera-species combo
    camera_species_prob = df_blind[(camera, species)].mean()
    
    # P(sighting | camera) - how active is this camera
    camera_cols = [col for col in df_blind.columns if col[0] == camera]
    camera_prob = df_blind[camera_cols].mean().mean() if camera_cols else 0
    
    # P(sighting | species) - how common is this species
    species_cols = [col for col in df_blind.columns if col[1] == species]
    species_prob = df_blind[species_cols].mean().mean() if species_cols else 0
    
    # Simple combination (could be improved with proper Bayesian inference)
    if pd.isna(camera_species_prob):
        # Fallback to marginal probabilities
        combined_prob = camera_prob * species_prob
    else:
        # Weight the specific combination more heavily
        combined_prob = 0.7 * camera_species_prob + 0.3 * (camera_prob * species_prob)
    
    return max(0.0, min(1.0, combined_prob))  # Ensure valid probability

# Test the function
if len(binary_sightings.columns) > 0:
    # Get first available camera and species
    test_camera, test_species = binary_sightings.columns[0]
    test_date = binary_sightings.index[10]  # Use 10th date
    
    prob = naive_sighting_probability(binary_sightings, test_camera, test_species, test_date)
    actual = binary_sightings.loc[test_date, (test_camera, test_species)]
    
    print(f"Test prediction:")
    print(f"  Camera: {test_camera}")
    print(f"  Species: {test_species}")
    print(f"  Date: {test_date}")
    print(f"  Predicted probability: {prob:.3f}")
    print(f"  Actual sighting: {actual}")}

\notes{This simple model provides a baseline for prediction. The naive Bayes assumption of independence is often violated in ecological data (e.g., some species move together), but it provides a interpretable starting point that can be improved with more sophisticated techniques.}

\endif
