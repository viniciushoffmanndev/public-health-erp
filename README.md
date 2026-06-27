# Public Health ERP 🏥

A robust, Django-based Enterprise Resource Planning (ERP) system designed to manage and modernize complex public health databases. 

## 📖 About The Project

Handling public health administration requires managing an enormous amount of interconnected data. This project serves as a modern web interface connected to a massive legacy PostgreSQL database (hosted on Neon DB) containing exactly **1,499 tables**. 

The goal of this ERP is to transform raw, extensive healthcare data into an accessible, secure, and user-friendly administrative panel. It centralizes operations that are typically fragmented in municipal health management.

**Core Modules Covered:**
* **Patient Management:** Medical records, demographics, and SUS/e-SUS integration.
* **Scheduling & Operations:** Medical appointments, triage, exams, and AIH (Autorização de Internação Hospitalar).
* **Pharmacy & Inventory:** Medication dispensing, stock control, and procurement.
* **Human Resources:** Staff scheduling, CBOs (Brazilian Classification of Occupations), and medical teams.
* **Public Health Surveillance:** Epidemiological tracking, dengue monitoring, and sanitary inspections.

## 🚀 Built With

This project relies on a modern Python stack to handle the massive database schema through reverse engineering and ORM mapping.

* **Backend:** [Python 3](https://www.python.org/) & [Django](https://www.djangoproject.com/)
* **Database:** [PostgreSQL](https://www.postgresql.org/) (Hosted on [Neon](https://neon.tech/))
* **UI/Admin:** Django Admin (customized with modern UI themes)

## ⚠️ Security Notice

Due to the sensitive nature of healthcare data, this repository contains **only the application code and structural models**. 
* No real patient data (PHI) or database credentials are included in this repository. 
* Environment variables (`.env`) are strictly ignored via `.gitignore` to ensure database connections remain secure.
