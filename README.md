# Calorie Burn Efficiency Prediction Dashboard (Track 4)

## 1. Problem & Target User
- [cite_start]**Analytical Problem**: Most fitness trackers focus on raw metrics like steps or calories but fail to explain the **Metabolic Efficiency** behind those numbers[cite: 3]. [cite_start]Users often hit "plateaus" because their bodies are in a "Low Efficiency" (saving) mode, yet they lack tools to diagnose this physiological state[cite: 3].
- **Intended User**: 
    - [cite_start]**Gym Owners & Personal Trainers**: To use as a professional assessment tool to identify clients' metabolic bottlenecks and justify personalized training interventions[cite: 3, 9].
    - [cite_start]**Fitness Enthusiasts**: Individuals seeking data-driven insights into why their current routine is or isn't working[cite: 3].

## 2. Data Source
- **Original Source**: [Close to Realistic Calorie Efficiency Dataset](https://www.kaggle.com/datasets/parasharmanu/close-to-realistic-calorie-efficiency-dataset) via Kaggle.
- **Access Date**: 2026-04-24.
- [cite_start]**Key Fields**: Biometric data (BMI, Resting Heart Rate, Body Fat %) and lifestyle logs (Daily Steps, Active Minutes, Sleep, Hydration)[cite: 3].
- [cite_start]**Data Access Instructions**: Due to the file size (approx. 76MB), the full dataset is not uploaded to this repository[cite: 8]. 
    1. Download the CSV from the Kaggle link above.
    2. Rename it to `calorie_efficiency_dataset.csv`.
    3. [cite_start]Place it in the root directory of this project before running the code[cite: 8].

## 3. Methods (Python Workflow)
[cite_start]This project follows a substantive Python analytical pipeline[cite: 3]:
- [cite_start]**Data Preprocessing**: Handling missing values and capping extreme outliers at the 1st and 99th percentiles to ensure model robustness[cite: 3].
- [cite_start]**Feature Engineering**: Creating custom physiological markers including `activity_intensity` (active mins/steps) and `recovery_score` (sleep x hydration)[cite: 3].
- [cite_start]**Handling Imbalance**: Implementing **SMOTE** (Synthetic Minority Over-sampling Technique) to address class imbalance, as "High Efficiency" users were underrepresented[cite: 3].
- [cite_start]**Modeling**: Training a **Random Forest Classifier** to accurately categorize metabolic tiers[cite: 3].
- [cite_start]**Deployment**: Building an interactive UI using **Streamlit** with fluid data capsules and global metabolic spectrums[cite: 9].

## 4. Key Findings
- [cite_start]**Dominant Predictors**: Feature importance analysis shows that **Daily Steps** and **Active Minutes** are the strongest predictors of overall calorie burn efficiency[cite: 3].
- [cite_start]**Metabolic Trap**: Users can be highly active during workouts but still fall into the "Low Efficiency" category if their baseline daily movement (steps) is insufficient[cite: 3].

## 5. How to Run
[cite_start]To launch the interactive tool locally, follow these steps[cite: 8]:
1. **Clone the repository** to your local machine.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   Run the application:

3. **Run the application**:
   ```bash
   streamlit run app
## 6. Project Links
- [cite_start]**Demo Video**:https://video.xjtlu.edu.cn/Mediasite/Play/275fdcf168fa4867b955381045773ef21d

- [cite_start]**GitHub Repository**:[Your GitHub Link Here]

## 7. Limitations & Next Steps
- [cite_start]**Data Sensitivity**: The current model uses synthetic data; future iterations should be validated with clinical metabolic data.

- [cite_start]**Automation:**:Integrating real-time data fetching from wearable APIs (e.g., Apple Health) to replace manual user inputs.

## 8. AI Disclosure: Generative AI was used to assist in debugging Streamlit environment configurations and structuring the Markdown documentation. Full details are provided in the submitted reflection report
