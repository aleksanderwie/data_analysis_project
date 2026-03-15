# Manufacturing Data Analysis
## Overview
This project has been created to analyze and visualize manufacturing process dataset. Data description do not specify more detailed infromations about the process 
The main goal of this project is to explore how diffrent process parameters influence the **Quality Rating**, which is the target variable. 
---
## Dataset description
This dataset obtains various manufacturing parameters such as:
* `Temperature(°C)`: process temperature in range 100 - 300°C.
* `Pressure (kPa)`: pressure in the system.
* `Material Fusion Metric`: Indicator of material fusion.
* `Material Transformation Metric`: Indicator of material transformation .
* **`Quality Rating`**:  **`Target variable`** - process quality result on a scale 0-100. 
  This is the main variable we aim to analyze and understand in correlation with other parameters.
---
## Functionality
The Python analysis script ('main.py') performs the following tasks:
* `Exploratory Data Analysis (EDA)`: Generates descriptive statistics and checks missing data
* `Outlier Detection`:  Generates Boxplots to locate outliers data in temperature.
* `Distribution Analysis`: Visualizes the spread of all numeric parameters using  histograms.
* `Correlation Mapping`: Includes a Heatmap and Spearman correlation to find hidden relationship between variables.
---
## Requirements
To run this project, you need following Python libraries installed:
* `matplotlib`
* `pandas`
* `seaborn`
You can install them using:

```bash
pip install pandas matplotlib seaborn

```
## How to Run
1. Clone this repository.
2. Ensure the `manufacturing.csv` file is in the `Data/` folder.
3. Run the script from the project root using:
   ```bash
   python src/main.py
---
## Visualization and insights
Below are the key findings from the manufacturing data analysis:

## 1. Correlation Heatmap
![Correlation Heatmap](plots/Correlation%20heatmap.png)

This heatmap shows how different process parameters relate to each other. It helps identify which factors most strongly influence the Quality Rating.

## 2. Temperature vs Quality Rating

A scatterplot showing the relationship between process temperature and the final quality score. Note how the quality changes as temperature increases.

![Scatterplot](plots/Scatterplot%20Temperature%20vs%20Quality%20Ratings.png)

## 3. Temperature Distribution (Outliers)
This boxplot helps us idetify if there are any unusual temperature spikes or drops during the process.

![Boxplot](plots/Boxplot%20for%20temperature.png)

## Additional Visualizations

The analysis generates more detailed plots and statistics. You can find all the generated charts, including distribution histograms and specific metric correlations, in the:
* **`plots/`** folder.
Feel free to explore them to get a deeper understanding of the process parameters.
---
## Conclusions
Based on the analysis of the manufacturing data, we can draw the following conclusions:

* **Critical Temperature:** Maintaining the process temperature below **275°C** is crucial. Above this threshold, the **Quality Rating** drops significantly, leading to defective products.
* **Key Correlations:** High correlation between **Material Fusion** and **Transformation Metrics** suggests these two parameters move together and both impact the final quality.
* **Optimization:** To maximize quality, the process should be stabilized in the **150°C - 250°C** range with consistent pressure.

## Contact

If you have any questions or suggestions regarding this project, feel free to reach out:

* **Name:** Aleksander Wiertel
* **Email:** aleksanderwie65@gmail.com
* **LinkedIn:** [linkedin.com/in/aleksander-wiertel](https://www.linkedin.com/in/aleksander-wiertel)
* **GitHub:** [github.com/aleksanderwie](https://github.com/aleksanderwie)















