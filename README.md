# DATA471-Individual-Project

By Jia Wei Leong (300560651)

## Instructions

Unzip the spiral dataset (`SpiralData.zip`) and move the two folders: `Controles30jun14` and `Protocolo temblor` to the `data/raw` directory. Then execute `python src/data.py` to parse the spiral dataset and create a new csv titled `data_cleaned.csv` in `data/processed`. This csv can then be parsed in the EDA and modelling notebooks.

These Python packages were used for this project: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `shap`, `scikit-learn` and `imblearn`, which can all be installed using the `pip install` command.

Please check the EDA and modelling notebooks for reproducing of my findings from my report. Both notebooks will load the `data_cleaned.csv` file from the `data/processed` directory, so run `data.py` first before running any cells in both notes.

## Acknowledgements

The clean dataset and data loading scripts were originally written by Marco Vieto for the EDA project and was used in this project with his permission.
