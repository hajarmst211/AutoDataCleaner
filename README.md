
# General Information about the Project:
1. Name of the project: Data Plumbing
2. My Personal intensions from the project: Learning new skills and finding a solution to a widely existing problem.
3. Global End of the Project: Automate general cleaning of newly added or modified `.csv` files and sending an alert email at the end of the task<br>

# Project Overview:
This project is a data cleaning and processing pipeline designed to automate the ingestion, cleaning, and storage of CSV or generated data. It also supports real-time monitoring of an input directory to detect new files, clean them, and archive the results. Additionally, it contains components for generating synthetic data, storing it in a database, and sending notifications via email.<br>

# Detailed Information about the Project:
This project implements a fully automated ETL (Extract, Transform, Load) pipeline for CSV or generated data. The pipeline consists of the following stages:

1. **Extract**
<br>
Data is extracted either from:<br>

- Incoming CSV files placed in a designated input folder.

- Generated synthetic data stored as Parquet files.(this was implemented for testing)

2. **Transform**<br>

Data is cleaned and processed automatically:

- Duplicate rows are removed.

- Column names are standardized.

- Date columns are converted to proper datetime types when valid.

- Columns with excessive null values are removed.

- Missing values are handled based on type (numeric or categorical).

3. **Load**<br>

Cleaned data is saved in an archive folder as CSV files.

Optionally, Parquet data can be loaded into a SQLite database for structured storage and further analysis.

4. **Automation**<br>
<p>
1. A folder watcher continuously monitors the input directory.
<p>
2. New files are detected, cleaned, and archived automatically without manual intervention.
<p>
3. Deleted files are also removed from the archive folder.

<p>This ETL pipeline ensures reliable, repeatable, and real-time processing of incoming datasets, making it suitable for automated data workflows and downstream analytics.</p>

# Improvements and fixes:
- The mail sending code is not functional. I still need to look for a more adapted and optimal way to send an email without lowering the security measures of the sender's gmail account.  
- Make a json or yaml file from whom the cleaner script take  information about the cleaning: implementation method, .... and then the cleaner script does the cleaning based on that.
- Make the project cover all types of structured data file (json, xsl, ...)
