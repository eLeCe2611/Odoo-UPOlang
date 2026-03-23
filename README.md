# Odoo-UPOlang: University Language Center Management 🌍🏫

**Odoo-UPOlang** is a comprehensive ERP module developed for **Odoo** designed to manage the daily operations of a University Language Center. This module streamlines the entire academic and administrative workflow, from student enrollment and academic tracking to billing and human resources.

## 🌟 Key Features

The module implements a robust data model to handle several business areas:

* **Academic Management**: Manage subjects (`asignatura`), classrooms (`aula`), and different types of courses.
* **Student Lifecycle**: Full tracking of students (`alumno`), including enrollments (`matricula`), progress tracking (`progreso`), evaluations, and final certifications.
* **Faculty & Staff**: Management of teachers (`profesor`), their contracts, and evaluations.
* **Financial Suite**: Integrated billing system with support for invoices (`factura`), payments, and various payment methods.
* **Corporate Relations**: Tools for managing company-related contracts (`empresa` and `contrato`).
* **Quality Control**: Feedback and rating systems (`valoracion`) to monitor service quality.

## 📁 Repository Structure

The module follows the standard Odoo directory architecture:

* **`models/`**: Defines the business logic and database schema using the Odoo ORM (Python).
* **`views/`**: XML files defining the User Interface (List, Form, Search views) and the main menu structure.
* **`security/`**: Configuration of Access Control Lists (ACLs) and security groups to ensure data privacy.
* **`demo/`**: Sample datasets (CSV and XML) for testing the module's functionality in a sandbox environment.
* **`controllers/`**: Web controllers for handling potential frontend or external requests.

## 🛠️ Technical Stack
* **Framework**: [Odoo](https://www.odoo.com/) (Version 14.0+ recommended).
* **Backend**: Python.
* **Frontend**: Odoo XML (QWeb).
* **Database**: PostgreSQL.

## ⚙️ Installation

1.  Clone this repository into your Odoo `addons` folder:
    ```bash
    git clone [https://github.com/eLeCe2611/Odoo-UPOlang.git](https://github.com/eLeCe2611/Odoo-UPOlang.git)
    ```
2.  Update your Odoo configuration file to include the new path.
3.  Restart your Odoo server.
4.  Activate the "Developer Mode" in the Odoo settings.
5.  Go to the **Apps** menu, click "Update Apps List," and search for **UPOlang**.
6.  Click **Install**.

## 👤 Author
* **Luis Carmona** - [eLeCe2611](https://github.com/eLeCe2611)

---
*Developed for academic purposes to demonstrate proficiency in Odoo ERP development and business process automation.*
