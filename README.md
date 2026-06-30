Phase 1 ✅ Project Setup
Phase 2 Spark Configuration
Phase 3 Raw → Bronze
Phase 4 Bronze → Silver
Phase 5 Silver → Gold
Phase 6 Databricks
Phase 7 SQL Warehouse
Phase 8 Power BI
Phase 9 Production Pipeline

VS Code
     │
     ▼
GitHub Repository
     │
     ▼
Databricks Repos
     │
     ▼
Databricks Spark Cluster
     │
     ▼
Bronze Layer (Delta)
     │
     ▼
Silver Layer (Delta)
     │
     ▼
Gold Layer (Delta)
     │
     ▼
Databricks SQL Warehouse
     │
     ▼
Power BI Dashboard

                    Airflow Scheduler
                           │
                           ▼
                ┌──────────────────────┐
                │   run_bronze.py      │
                └──────────────────────┘
                           │
                           ▼
                  Read New Raw Records
                           │
                           ▼
             Add Batch ID & Load Timestamp
                           │
                           ▼
                     Bronze (Delta)
                           │
                           ▼
                 Update Metadata Table
                           │
                           ▼
                ┌──────────────────────┐
                │   run_silver.py      │
                └──────────────────────┘
                           │
                           ▼
                  Read New Bronze Batch
                           │
                           ▼
                Cleaning + Features
                           │
                           ▼
                     Silver (Delta)
                           │
                           ▼
                 Update Metadata Table
                           │
                           ▼
                ┌──────────────────────┐
                │    run_gold.py       │
                └──────────────────────┘
                           │
                           ▼
                  Read New Silver Batch
                           │
                           ▼
                   Business Aggregations
                           │
                           ▼
                      Gold (Delta)
                           │
                           ▼
                 Update Metadata Table