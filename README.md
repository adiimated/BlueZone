# The Blue Zone Project

## Background
The desire to live a long and healthy life is universal. This project draws inspiration from "blue zones," areas identified by Dan Buettner and National Geographic where people live significantly longer and healthier lives. These regions include Sardinia (Italy), Okinawa (Japan), Loma Linda (California), Ikaria (Greece), and Nicoya (Costa Rica). The concept of blue zones offers insights into factors that contribute to longevity and reduced chronic illness.

## Problem
Despite high healthcare spending—averaging $13,493 per person and totaling $4.5 trillion annually—the U.S. healthcare system underperforms in various health metrics compared to other developed nations. The life expectancy in the U.S. has recently fallen below that of China, highlighting flaws in the American healthcare system. Furthermore, although the U.S. leads in cancer screenings and has seen a significant reduction in cancer deaths, the healthcare system is plagued with inconsistencies and inefficiencies, particularly in how it manages chronic conditions.

## Goal
This project aims to:
- Identify American counties with the highest number of centenarians and investigate the contributing factors to such longevity.
- Examine the impact of healthcare variables, environmental conditions, lifestyle choices, socioeconomic status, and demography on life expectancy.
- Explore disparities between rural and urban areas in terms of healthcare and lifestyle factors.
- Evaluate variations in life expectancy among U.S. counties to provide a nuanced understanding of the local healthcare systems.

## Data Sources
This project will leverage various data sources including public health records, census data, environmental reports, and local government databases.

## Task 1 - Literature Review

**Objective:** Conduct a detailed literature review to identify the factors linked to longevity in the well-known global Blue Zones.

**Key Findings**:
The following table summarizes the key factors associated with the longevity observed in Blue Zones:

| Factor Category          | Description                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------------------|
| **Diet and Nutrition**   | Predominantly plant-based diets with minimal meat consumption, linked to reduced rates of chronic diseases.  |
| **Physical Activity**    | Daily life integrates moderate physical activities like walking and gardening instead of structured exercises.|
| **Social Engagement**    | Strong social connections and an active social life significantly impact mental health and longevity.         |
| **Psychological Health** | Traits include high life satisfaction, a sense of purpose, and effective stress management techniques.       |
| **Environmental Factors**| Supportive physical and social environments, including clean air and community-oriented living.               |
| **Healthcare Access**    | Easy access to healthcare and preventive services, coupled with economic stability, supports overall health.  |

All the articles used for the literature review can be found in the following GitHub folder:
[Research Articles Folder](https://github.com/adiimated/The-Blue-Zone-Project/tree/main/literature%20review/Research%20Articles)

## Task 2 - Data Collection

Sources: 
 * County Health Ranking and Roadmas: https://www.countyhealthrankings.org/
 * Surveillance, Epidemiology, and End Results (SEER) Program: https://seer.cancer.gov/popdata/
 * Census Data: https://data.census.gov/

## Task 3 - Data Preprocessing

#### Original Dataset

The original dataset contained multiple demographic attributes including `Year`, `State Abbreviation`, `State FIPS Code`, `County FIPS Code`, `Sex`, `Age`, `Race`, and `Population`. These attributes allowed for a detailed examination of population distributions across different demographics and geographical locations.

#### Creation of Specific Datasets
We initially divided the large dataset into three smaller datasets focused on the attributes of interest:
1. **Dataset by Sex:** Included attributes like `Sex` and `Population`.
2. **Dataset by Age:** Focused on `Age` and `Population`.
3. **Dataset by Age with Additional Details:** Included `Age`, `Race`, and `Population`.

Each of these datasets retained common attributes: `Year`, `State Abbreviation`, `State FIPS Code`, and `County FIPS Code`.

For detailed analysis and to reduce complexity, we performed aggregation based on:
- **Sex:** The population was aggregated by `Sex`, summing up individuals grouped by `Year`, `State Abbreviation`, `State FIPS Code`, `County FIPS Code`.
- **Age:** Population totals were aggregated by `Age`, following the same grouping strategy.
The aggregated data was then saved into new CSV files for each grouped attribute, making it easier for further analysis or reporting.

#### Files Generated
- **Aggregated by Sex:** `aggregated_dataset_by_sex.csv`
- **Aggregated by Age:** `aggregated_dataset_by_age.csv`
These files provide a concise view of the population distribution either by sex or age across various locations and time frames.

(here I am talking about the work I did)

