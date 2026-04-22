# Mine Water Balance – Climate Data Processing

This repository contains tools, workflows, and documentation for extracting, validating, and processing gridded meteorological data for use as climate input to a mine site water balance model.

The primary objective of this repository is to generate **site-specific monthly climate statistics (means and variability)** from gridded observation datasets, suitable for input into an Excel-based mine water balance and associated uncertainty analysis.

---

## Project Objectives

- Extract daily precipitation and temperature data from gridded observation datasets at a specific mine site location
- Aggregate daily data to monthly totals, means, and variability statistics
- Validate gridded climate data against nearby meteorological station (airport) observations
- Generate clean, auditable Excel-ready climate inputs for mine water balance modeling
- Maintain traceability between raw data sources and final engineering inputs

---

## Repository Structure

```text
pcic-climate-extract/
│
├── README.md
├── environment.yml
├── .gitignore
│
├── config/
│   ├── site_config.yml
│   └── paths.yml
│
├── data/
│   ├── raw/
│   │   ├── pcic_blend/
│   │   └── station/
│   │
│   ├── interim/
│   └── processed/
│       └── excel_inputs/
│
├── notebooks/
│   ├── 00_data_inventory.ipynb
│   ├── 01_extract_site_climate.ipynb
│   ├── 02_monthly_aggregation.ipynb
│   ├── 03_station_validation.ipynb
│   └── 04_uncertainty_characterization.ipynb
│
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── spatial.py
│   ├── climate_stats.py
│   ├── validation.py
│   └── export.py
│
├── outputs/
│   ├── figures/
│   └── tables/
│
└── docs/
    └── methodology_notes.md
```

## Folder and File Descriptions

### `config/`
Configuration files used to parameterize the analysis without hard-coding values in notebooks or scripts.

- **`site_config.yml`**  
  Defines mine site metadata such as latitude, longitude, elevation, site name, and other site-specific parameters.

- **`paths.yml`**  
  Defines file system paths to raw datasets and key outputs. Centralizing paths allows restructuring without modifying code.

---

### `data/`
All project datasets, organized by processing stage.

- **`raw/`**  
  Raw, unmodified input datasets exactly as received. These files must remain read-only.
  - `pcic_blend/` — PCIC‑Blend gridded netCDF datasets  
  - `station/` — Station or airport observational data (e.g., CSV files)

- **`interim/`**  
  Intermediate datasets created during processing (e.g., extracted daily site time series). These data support quality control and validation but are not final engineering inputs.

- **`processed/`**  
  Final datasets used directly in engineering analysis.
  - `excel_inputs/` — Excel-ready climate inputs for the mine water balance model

---

### `notebooks/`
Jupyter notebooks used for exploratory analysis, diagnostics, and stepwise processing.

Notebooks are numbered to clearly indicate workflow order. Each notebook focuses on a single processing task and relies on shared functions defined in the `src/` directory.

---

### `src/`
Reusable Python modules containing core functionality used across notebooks.

- **`io.py`** — Dataset loading and configuration parsing  
- **`spatial.py`** — Site extraction and spatial helper functions  
- **`climate_stats.py`** — Temporal aggregation and statistical calculations  
- **`validation.py`** — Bias, correlation, and validation metrics  
- **`export.py`** — Export of processed data to CSV and Excel formats  

---

### `outputs/`
Generated figures and summary tables intended for reporting, quality assurance, or technical review.

---

### `docs/`
Technical documentation describing methodology, assumptions, and intended use of the dataset and processing workflow.

---

## Environment Setup

A Conda environment is recommended for reproducibility. Create the environment using:

```bash
conda env create -f environment.yml
conda activate pcic-climate
