# computer-infrastructure-assessment README

Welcome to this repository!  
This project downloads, processes, visualizes, and automates data for the five FAANG stocks — **META, AAPL, AMZN, NFLX, GOOG**.  
The steps below outline how the workflow in this repo operates and what each component does.

---

## **Problem 1 – Downloading Data**

This first step sets up the data collection:

- Uses `yfinance` to download **hourly data from the last 5 days** for all FAANG stocks.
- Saves the output into a **data** folder (creating it if it does not exist).
- Names each file using a timestamp format: `YYYYMMDD-HHmmss.csv`.

This ensures the repository consistently stores clean, time-stamped datasets.

---

## **Problem 2 – Plotting Data**

This step processes and visualizes the most recent dataset:

- Loads the **latest CSV** found in the `data` folder.
- Plots the **Close prices** for all five FAANG stocks on a single chart.
- Includes proper axis labels, a legend, and a timestamped title.
- Saves the resulting image into a `plots` folder using:  
  `YYYYMMDD-HHmmss.png`.

This produces easy-to-read visual summaries for each dataset collected.

---

## **Problem 3 – The faang.py Script**

The script ties everything together:

- Contains the functions that **downloads** the data and **plots** the results.
- Runs both steps when executed as:  
  `./faang.py`
- Includes a shebang line and is set as executable.
- The notebook explains how the script is constructed and configured.

This allows the entire workflow to run from a single command.

---

## **Problem 4 – Automation with GitHub Actions**

The final step automates the process:

- Adds a workflow in `.github/workflows/faang.yml`.
- Runs the script **every Saturday morning**.
- Installs dependencies and then **executes** `./faang.py`.
- The notebook provides a line-by-line explanation of the workflow.

This ensures the project maintains up-to-date data and plots without manual intervention.

---

## **Project Structure**

├── faang.py
├── README.md
├── data/
├── plots/
└── .github/
└── workflows/
└── faang.yml

---

## **Summary**

This repository:

1. **Downloads** recent FAANG stock data  
2. **Saves** it using a consistent timestamp format  
3. **Loads** the latest dataset  
4. **Plots** the closing prices clearly and cleanly  
5. **Automates** the entire workflow weekly  

Follow these steps to understand, run, and extend the project. Contributions and improvements are always welcome!
