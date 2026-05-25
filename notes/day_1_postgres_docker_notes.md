# Day 1 Notes: PostgreSQL with Docker

Today I created a PostgreSQL database using Docker instead of installing PostgreSQL directly on my machine.

Docker allows the same database setup to run on both Windows and Mac.

The PostgreSQL container is named sales_postgres.
The database is named salesdb.
The database user is rashid.
The database runs on port 5432.

I tested:
- Python environment setup
- PostgreSQL container startup
- Python connection to PostgreSQL
- SQL table creation
- SQL insert and query operations

foundation for Data Engineering project: Sales Analytics ETL Pipeline.

Rule: when switch laptop - OS

cd ~/projects/de-mlops-portfolio
git pull
conda activate de-mlops
cd project_1_sales_etl
docker compose up -d

Daily otherwise:
Start as:

cd ~/projects/de-mlops-portfolio
git pull
conda activate de-mlops

Ends as:

git status
git add .
git commit -m "update ?"
git push


important Concepts: 
| Item               | Shared between Mac and Windows? | How?                |
| ------------------ | ------------------------------- | ------------------- |
| Code               | Yes                             | GitHub              |
| SQL files          | Yes                             | GitHub              |
| Python scripts     | Yes                             | GitHub              |
| Docker config      | Yes                             | GitHub              |
| Docker container   | No                              | Local machine       |
| Database data      | No                              | Local Docker volume |
| Conda environment  | No                              | Create separately   |
| Installed packages | No                              | Install separately  |

Check for container of interest:
docker ps

if exists but stopped (no green spot with it):
docker start sales_postgres
or
docker compose up -d

added line to basic_queries.sql:
ON CONFLICT (order_id) DO NOTHING;
to make it idempotent

created start_project.sh exe file to make part of start:
code start_project.sh
chmod +x start_project.sh

Start Changed:
cd ~/projects/de-mlops-portfolio
git pull
conda activate de-mlops
cd project_1_sales_etl
./start_project.sh

Ends with:
cd ~/projects/de-mlops-portfolio
git status
git add .
git commit -m "update project 1 database setup automation"
git push

