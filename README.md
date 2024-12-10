# 🚀 TrackVia Data Scraper and SharePoint Uploader
This project automates the process of connecting to TrackVia using Selenium, scraping data from tables, saving the data as CSV files, and uploading the CSV files to a SharePoint folder for easy synchronization with Power BI.

## 📋 Table of Contents
1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Configuration](#configuration)
5. [License](#license) 

## ✨ Features
Automated Login to TrackVia using Selenium.
Scrape Table Data from TrackVia views.
Save Data as CSV Files with dynamically generated filenames based on the table name.
Upload CSV Files to SharePoint for easy integration with Power BI.
Handles Multi-Page Tables for comprehensive data scraping.

## ✅ **Prerequisites**

- **Python 3.8+**  
- **Google Chrome** (latest version) and **ChromeDriver**  
- **TrackVia Account** with access to the tables you want to scrape  
- **SharePoint Account** with permission to upload files  
- **Azure App Registration** for OAuth authentication 

```bash
pip install selenium bs4 pandas msal Office365-REST-Python-Client

```

## ⚙️ Configuration
1. TrackVia Credentials
Update your TrackVia and SharePoint credentials in the script file: secrets.py located in the configs folder after removing the _example:

```python
USERNAME = "your_trackvia_email@example.com"
PASSWORD = "your_trackvia_password"
LOGIN_URL = "https://go.trackvia.com/login"
GRID_URL = "https://go.trackvia.com/app/your-app-id/your-view-id"

```

## 2. SharePoint Settings
Update your SharePoint and Azure App details:

```python
Copy code
SHAREPOINT_URL = "https://yourcompany.sharepoint.com/sites/yoursite"
SHAREPOINT_FOLDER = "/Shared Documents/PowerBI Data"
CLIENT_ID = "your_client_id"
TENANT_ID = "your_tenant_id"

```

## 3. Azure App Registration
Ensure you have an Azure App Registration with the following:

```bash
API Permissions: Sites.ReadWrite.All
```
Admin Consent granted.


The script will prompt you to visit https://microsoft.com/devicelogin and enter a code.
Complete the authentication, including any Multi-Factor Authentication (MFA) required.

Check Output:
The scraped data will be saved as a CSV file in the project directory.
The CSV file will be uploaded to the specified SharePoint folder.


## 📜 License
This project is licensed under the MIT License.

## 💬 Feedback and Support
For feedback, questions, or issues, please open an issue in the repository or contact me at [wisnercelucus@gmail.com].