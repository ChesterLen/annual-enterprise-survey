Annual Enterprise Survey - Data Analysis Project

📌 Project Overview

This project analyzes the Annual Enterprise Survey (2023 Financial Year - Provisional) dataset using Python and the pandas library. The dataset contains financial performance metrics across various industries and aggregation levels. The goal is to extract meaningful insights and trends through data cleaning, exploration, and visualization.

🔍 Data Description

    • The dataset includes the following key columns:

    • Year – The financial year of the data.

    • Industry_aggregation_NZSIOC – Industry aggregation level.

    • Industry_code_NZSIOC – Industry code.

    • Industry_name_NZSIOC – Industry name.

    • Units – Measurement unit (e.g., dollars in millions).

    • Variable_name – Type of financial variable (e.g., Total income, Total expenditure).

    • Value – The numerical value of the financial variable.

🎯 Project Tasks

✅ Data Cleaning & Exploration

    • Convert Value to a numeric data type.

    • Handle missing or incorrect values.

    • Explore unique values in categorical columns.

✅ Data Analysis

    1. Calculate total income per industry for a given year

      • Find total income by grouping data by industry.

    2. Find the industry with the highest total income in 2023

      • Identify the top industry based on total income.

    3. Compare total income and total expenditure across industries

      • Analyze which industries are profitable or operating at a loss.

    4. Analyze trends over years for a specific financial variable

      • Plot trends to observe income/expenditure growth over time.

    5. Group by industry aggregation levels and calculate summary statistics

      • Compute total, average, min, and max values for industries.

📊 Visualizations

    • Bar charts to compare total income across industries.

    • Line graphs to track financial trends over multiple years.

    • Pie charts to illustrate industry contributions to total income.

🛠 Technologies Used

    • Python (pandas, matplotlib)

    • Git & GitHub for version control

🚀 How to Use

    1. Clone the repository:
    git clone https://github.com/yourusername/annual-enterprise-survey-analysis.git

    2 Install dependencies:
    pip install -r requirements.txt