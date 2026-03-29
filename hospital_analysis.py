import pandas as pd

# ── STEP 1: Load both files ───────────────────────────────────────────────────
locations = pd.read_csv("hospital_locations.csv")
general   = pd.read_csv("Hospital_General_Information.csv")

print("hospital_locations shape   :", locations.shape)
print("Hospital_General_Information shape:", general.shape)

print("\nhospital_locations columns:\n",   locations.columns.tolist())
print("\nHospital_General_Information columns:\n", general.columns.tolist())


# ── STEP 2: Clean hospital_locations ─────────────────────────────────────────

# Keep only useful columns
locations = locations[[
    'NAME', 'CITY', 'STATE', 'TYPE', 'STATUS', 'POPULATION', 'COUNTY', 'COUNTRY'
]].copy()

# Rename for readability
locations.rename(columns={
    'NAME'       : 'Hospital_Name',
    'CITY'       : 'City',
    'STATE'      : 'State',
    'TYPE'       : 'Hospital_Type',
    'STATUS'     : 'Status',
    'POPULATION' : 'Population',
    'COUNTY'     : 'County',
    'COUNTRY'    : 'Country'
}, inplace=True)

# Keep only US hospitals
locations = locations[locations['Country'] == 'USA']

# Remove rows where Status is CLOSED
locations = locations[locations['Status'] == 'OPEN']

# Fix population — replace -999 (placeholder for unknown) with NaN
locations['Population'] = locations['Population'].replace(-999, pd.NA)

# Drop rows missing Hospital_Name or State
locations.dropna(subset=['Hospital_Name', 'State'], inplace=True)

print("\nCleaned locations shape:", locations.shape)
print("Missing values in locations:\n", locations.isnull().sum())


# ── STEP 3: Clean Hospital_General_Information ────────────────────────────────

# Keep only useful columns
general = general[[
    'Hospital Name', 'City', 'State', 'ZIP Code',
    'County Name', 'Hospital Type', 'Hospital Ownership',
    'Emergency Services', 'Meets criteria for meaningful use of EHRs',
    'Hospital overall rating'
]].copy()

# Rename for readability
general.rename(columns={
    'Hospital Name'                              : 'Hospital_Name',
    'City'                                       : 'City',
    'State'                                      : 'State',
    'ZIP Code'                                   : 'ZIP_Code',
    'County Name'                                : 'County',
    'Hospital Type'                              : 'Hospital_Type',
    'Hospital Ownership'                         : 'Ownership',
    'Emergency Services'                         : 'Emergency_Services',
    'Meets criteria for meaningful use of EHRs'  : 'Uses_EHR',
    'Hospital overall rating'                    : 'Overall_Rating'
}, inplace=True)

# Replace 'Not Available' strings with NaN across the dataframe
general.replace('Not Available', pd.NA, inplace=True)

# Convert Overall_Rating to numeric
general['Overall_Rating'] = pd.to_numeric(general['Overall_Rating'], errors='coerce')

# Drop rows missing Hospital_Name or State
general.dropna(subset=['Hospital_Name', 'State'], inplace=True)

print("\nCleaned general info shape:", general.shape)
print("Missing values in general:\n", general.isnull().sum())


# ── STEP 4: Analysis on General Information ───────────────────────────────────

# 1. Hospital count by State (top 15)
print("\n── Hospital Count by State (Top 15) ──")
state_counts = general['State'].value_counts().head(15).reset_index()
state_counts.columns = ['State', 'Hospital_Count']
print(state_counts)

# 2. Hospital count by Type
print("\n── Hospital Count by Type ──")
type_counts = general['Hospital_Type'].value_counts().reset_index()
type_counts.columns = ['Hospital_Type', 'Count']
print(type_counts)

# 3. Hospital count by Ownership
print("\n── Hospital Count by Ownership ──")
ownership_counts = general['Ownership'].value_counts().reset_index()
ownership_counts.columns = ['Ownership', 'Count']
print(ownership_counts)

# 4. Emergency Services availability
print("\n── Emergency Services Availability ──")
emergency = general['Emergency_Services'].value_counts().reset_index()
emergency.columns = ['Emergency_Services', 'Count']
print(emergency)

# 5. Average Overall Rating by Hospital Type
print("\n── Average Rating by Hospital Type ──")
rating_by_type = general.groupby('Hospital_Type')['Overall_Rating'].mean().round(2).reset_index()
rating_by_type.columns = ['Hospital_Type', 'Avg_Rating']
rating_by_type.sort_values('Avg_Rating', ascending=False, inplace=True)
print(rating_by_type)

# 6. Average Overall Rating by Ownership
print("\n── Average Rating by Ownership ──")
rating_by_ownership = general.groupby('Ownership')['Overall_Rating'].mean().round(2).reset_index()
rating_by_ownership.columns = ['Ownership', 'Avg_Rating']
rating_by_ownership.sort_values('Avg_Rating', ascending=False, inplace=True)
print(rating_by_ownership)

# 7. EHR adoption rate
print("\n── EHR Adoption ──")
ehr = general['Uses_EHR'].value_counts().reset_index()
ehr.columns = ['Uses_EHR', 'Count']
print(ehr)


# ── STEP 5: Analysis on Locations ─────────────────────────────────────────────

# 1. Hospital count by State
print("\n── Hospital Count by State from Locations (Top 15) ──")
loc_state = locations['State'].value_counts().head(15).reset_index()
loc_state.columns = ['State', 'Count']
print(loc_state)

# 2. Hospital count by Type
print("\n── Hospital Type Distribution (Locations) ──")
loc_type = locations['Hospital_Type'].value_counts().reset_index()
loc_type.columns = ['Hospital_Type', 'Count']
print(loc_type)

# 3. Population served — average by state (top 10)
print("\n── Avg Population Served by State (Top 10) ──")
pop_by_state = locations.groupby('State')['Population'].mean().round(0).reset_index()
pop_by_state.columns = ['State', 'Avg_Population']
pop_by_state.sort_values('Avg_Population', ascending=False, inplace=True)
print(pop_by_state.head(10))


# ── STEP 6: Export both cleaned files for Power BI ────────────────────────────
general.to_csv("general_info_cleaned.csv",   index=False)
locations.to_csv("locations_cleaned.csv",    index=False)

print("\n✅ Done! Two cleaned files saved:")
print("   → general_info_cleaned.csv")
print("   → locations_cleaned.csv")
print("   Load both into Power BI Desktop to build your dashboard!")