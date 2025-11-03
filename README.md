# 307401 — Big Data 

Repository supporting the *Big Data* course.
This repository includes lectures, notebooks, assignments, datasets, and demo code on big data technologies, tools, methodologies, and use in analytics scenarios.

---

## Table of Contents

* [Course overview](#course-overview)
* [Repository structure](#repository-structure)
* [Prerequisites](#prerequisites)
* [Setup Instructions](#setup-instructions)
* [Running notebooks, scripts, and big data tools](#running-notebooks-scripts-and-big-data-tools)
* [Datasets & data ingestion](#datasets--data-ingestion)
* [Assignments & evaluations](#assignments--evaluations)
* [Examples & demos](#examples--demos)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)
* [Instructor / contact info](#instructor--contact-info)

---

## Course overview

In this course, students explore the principles, architectures, and tools associated with handling and analyzing **big data**. Core topics include:

* Distributed data storage and processing (e.g. Hadoop, Spark)
* Big Data ecosystems and architectures (e.g. HDFS, YARN, Kafka)
* Data ingestion, ETL/ELT pipelines
* Streaming vs batch processing
* Data partitioning, indexing, and formats (Parquet, Avro, ORC)
* Data cleaning, transformation, aggregation at scale
* Scalable analytics and machine learning on big data
* System performance, fault tolerance, and optimization
* Use-cases in business: recommendation systems, large-scale reporting, real-time analytics

This repository provides notebooks, scripts, and example implementations so students can reproduce labs and build big data mini-projects.

---

## Repository structure

Here’s a suggested layout; update to match your actual structure:

```
/
├── notebooks/               # Jupyter / PySpark / other notebooks
├── scripts/                 # Standalone scripts (e.g. Spark jobs)
├── data/                    # Sample datasets (small scale) or ingestion scripts
├── assignments/              # Assignment instructions and templates
├── demos/                   # Demo projects or mini apps
├── configs/                 # Configuration files, e.g. for Hadoop, Spark
├── requirements.txt         # Python / library dependencies
├── environment.yml          # Optional: conda environment spec
└── README.md                 # This file
```

If there are extra directories (e.g. `docker/`, `resources/`, `logs/`), include them accordingly.

---

## Prerequisites

To work with this repository, you will need:

* **Python 3.8+** (with PySpark / relevant big data libraries)
* Java (e.g. OpenJDK 11 or compatible version)
* Apache Spark installation or environment (local or cluster)
* Hadoop / HDFS (if used in labs)
* Basic familiarity with distributed systems, cluster architecture
* Jupyter Notebook / JupyterLab
* (Optional) Docker, if environment is containerized

---

## Setup Instructions

### Using local / single-node setup

1. Clone the repository:

   ```bash
   git clone https://github.com/msfasha/307401-Big-Data.git
   ```

2. Create environment:

   * If `environment.yml` is provided:

     ```bash
     conda env create -f environment.yml
     conda activate bigdata
     ```
   * Or using `requirements.txt`:

     ```bash
     python -m venv .venv
     source .venv/bin/activate   # Windows: .venv\Scripts\activate
     pip install -r requirements.txt
     ```

3. Ensure you have Spark installed (or use pyspark package). For example:

   ```bash
   pip install pyspark
   ```

4. If labs use Hadoop / HDFS locally, ensure Hadoop is installed and configured, or use pseudo-distributed mode.

5. Start Jupyter:

   ```bash
   jupyter lab
   ```

6. Ensure environment variables or configuration files (e.g. for Spark master URL, HDFS paths) are set. Use a template file (e.g. `configs/config_template.yml`) and copy it to `configs/config.yml`.

---

## Running notebooks, scripts & big data jobs

* Use JupyterLab to open notebooks in `notebooks/`. Many notebooks will include configuration cells to set Spark context, HDFS paths, etc.
* For scripts in `scripts/`, run via command line, e.g.:

  ```bash
  spark-submit scripts/some_spark_job.py --input path/to/data --output path/to/result
  ```
* If demos in `demos/` include mini web apps or dashboards, check their README for how to launch (e.g. `streamlit`, `flask`, `dash`).
* If using a cluster, ensure your Spark/Hadoop configuration files point to the correct cluster endpoints.

---

## Datasets & data ingestion

* Sample datasets (smaller scale) are stored in `data/`.
* For large/real-world datasets, ingestion scripts or pointers (download scripts, links to cloud storage) are provided instead of storing full data.
* Include metadata or schema files so students know column names, types, and units.
* For streaming data scenarios, sample simulated streams may be provided (e.g. via Kafka or file-based generators).

---

## Assignments & evaluations

* Assignment folders in `assignments/` typically include:

  * `README.md` (task description, constraints, deliverables)
  * Starter notebooks or scripts
  * Sample data or links to data
  * Submission templates and grading rubric

* Students should submit via the designated method (GitHub Classroom, LMS, etc.).

* Ensure evaluation criteria (correctness, performance, scalability, clarity, code style) are clearly stated.

---

## Examples & demos

In `demos/`, you may find:

* Mini projects showcasing Spark streaming, batch analytics, or ETL pipelines
* Dashboard or reporting apps based on processed big data
* Utility modules (e.g. wrappers for reading/writing Parquet, data partitioning)
* Performance benchmarking scripts
* Each demo should include a README with instructions, dependencies, and expected outputs

---

## Troubleshooting

Common issues and tips:

1. **Spark configuration errors** — ensure `SPARK_HOME`, `JAVA_HOME`, and cluster settings are correct.
2. **Path or data not found** — confirm that data files exist in expected directories and that config files point correctly.
3. **Package version conflicts** — verify consistent versions of Spark, Hadoop, PySpark, etc.
4. **Memory / resource errors** — reduce partition sizes, increase executor memory, adjust parallelism.
5. **Notebook kernel / state issues** — restart kernel and re-run all cells after changes.
6. **Cluster connectivity issues** — check network, firewall, cluster endpoints.

If unresolved, consult instructor or raise an issue in the repository if enabled.

---

## Contributing

Contributions welcome (bug fixes, improved notebooks, extra demos). If contributing:

1. Fork the repository
2. Create a feature branch
3. Add or update code / docs / examples
4. Test locally in your environment
5. Submit a pull request with explanation of changes

Follow existing code style, document your changes, and avoid breaking existing labs.

---

## License

Refer to the `LICENSE` file in the repository root for the licensing terms (e.g. MIT, Apache, or a Creative Commons license). Adhere to those terms when reusing or modifying the course materials.

---

## Instructor / contact info

For questions, clarifications, or help with assignments, please contact the course instructor or TA as specified by the course. Optionally, open an issue (if enabled) with relevant details (course, assignment name, error message) to help with debugging.
