# Student Score Scraper (Ministry of Education)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]() 
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Python Version](https://img.shields.io/badge/python-3.x-yellow)]()

An automated Python tool designed to retrieve student examination results from the Ministry of Education's official portal.

> **Note:** This project is currently **archived**. Because the Ministry of Education website is updated annually, this codebase serves as a technical demonstration of web automation and may require updates to function with current web structures.

## Overview

This project was developed to automate the retrieval of student scores for data analysis and convenience. Since the target website employs measures to block standard URL requests (APIs), this tool utilizes browser simulation to replicate human interaction with the site.

## Features

- **Full Automation:** Replicates human browsing behavior to navigate search forms.
- **Dynamic Scraper:** Uses **Selenium** for browser automation and **BeautifulSoup** for precise HTML parsing.
- **Robustness:** Handles dynamic content that standard HTTP libraries cannot reach.

## Technical Stack

- **Language:** Python
- **Automation:** Selenium WebDriver
- **Parsing:** BeautifulSoup4
- **Driver Management:** webdriver_manager

## Getting Started

Follow these instructions to set up a local copy of the project for development or code review.

### Prerequisites

Ensure you have Python installed, then install the required dependencies:
```bash
pip install selenium beautifulsoup4 webdriver-manager
```

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Run the script:**
   ```bash
   python score.py
   ```

## Disclaimer
This project was created for educational purposes and personal use. Please ensure you comply with the Ministry of Education's Terms of Service and data privacy laws when using web scrapers.
