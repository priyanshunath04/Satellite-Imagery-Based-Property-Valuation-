# Satellite-Driven Property Price Prediction

## Project Summary

This project implements a multimodal regression framework for estimating residential property prices by combining:

* Structured tabular data (property attributes such as size, quality, and location)
* Satellite imagery embeddings extracted using the Mapbox Static Images API

The central goal is to examine whether visual context from overhead imagery**—including land use patterns, greenery, road networks, and neighborhood layout—adds meaningful predictive value beyond traditional housing features.

---

## 📂 Repository Setup

### Clone the Repository

Start by cloning the repository to your local system:

```bash
git clone https://github.com/<your-username>/<your-repository-name>.git
```

Move into the project directory:

```bash
cd <your-repository-name>
```

---

## 🧪 Environment Setup

All experiments are designed to run inside a **Python virtual environment to ensure dependency isolation.

### Create a Virtual Environment

#### Windows (PowerShell)

python -m venv venv

#### macOS / Linux

python3 -m venv venv

---

### Activate the Environment

#### Windows

venv\Scripts\activate

#### macOS / Linux

source venv/bin/activate

You should now see (venv) in your terminal prompt.

---

## 📦 Install Dependencies

Upgrade pip and install all required packages:

pip install --upgrade pip
pip install -r requirements.txt

---

## 🔐 Mapbox API Configuration
This project does not use `dotenv` or `.env` files.
Instead, the Mapbox API key is supplied directly as an environment variable via PowerShell.

### Set API Key (Windows PowerShell)

$env:MAPBOX_API_KEY="your_mapbox_access_token_here"

> ⚠️ This variable is session-scoped.
> You must re-run the command if you open a new terminal.

The Python scripts automatically read the key using os.environ.

---

## 🛰 Satellite Image Collection

Satellite images are fetched using the Mapbox Static Images API based on latitude and longitude coordinates provided in the dataset.

To download imagery, run:

python data_fetcher.py

### What this script does:

* Loads property coordinates from train.csv
* Queries satellite imagery at predefined zoom levels
* Saves images locally for later feature extraction

These images are later processed into embeddings during model training.

---

## 📓 preprocessing.ipynb

This notebook focuses on data understanding and preparation and acts as the analytical backbone of the project.

### Contents:

* Exploratory Data Analysis (EDA)
  Examines distributions, correlations, and influential variables affecting property prices.
* Data preprocessing
  Includes categorical encoding, numerical scaling, missing-value handling, and log transformation of the target variable.
* Initial tabular benchmarks
  Traditional regression models are evaluated to establish strong non-visual baselines.
* Dataset readiness checks
  Ensures consistency between tabular records and available satellite imagery.

This notebook prepares all inputs required for downstream modeling and experimentation.

---

## 📓 model_training.ipynb

This notebook contains the complete modeling and interpretability workflow, including both multimodal learning and visual explanations.

### Key components:

* Image embedding extraction
  Pretrained convolutional networks are used to convert satellite images into fixed-length feature vectors.
* Multimodal regression models
  Tabular features and image embeddings are combined using multiple fusion strategies.
* Comparison experiments
  Performance is evaluated across:

  * Tabular-only models
  * Image-only models
  * Combined multimodal models
* Grad-CAM analysis
  Gradient-based class activation maps are applied to satellite imagery to visualize which spatial regions most influence predictions.
* Final model selection
  The best-performing approach is chosen based on validation metrics and robustness.

This notebook represents the core experimental stage of the project and supports all conclusions reported.

---

## 📤 Outputs & Deliverables

* `23119029_final.csv`
  Final prediction file containing estimated property prices for the test dataset.

* `23119029_report.pdf`
  Comprehensive project report covering:

  * Problem motivation
  * EDA findings
  * Visual and financial insights
  * Model architectures
  * Experimental results and conclusions

---

## 👤 Author Information

Priyanshu Nath. 
23119029
Production and Industrial Engineering. 
IIT ROORKEE 



