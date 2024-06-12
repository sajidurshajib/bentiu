# 🎓 Bentiu University Project

## ⚠️ Caution - for host in cpanel

-   **Pull from GitHub:** Ensure you have pulled the latest version of the project from the GitHub repository.

-   **GCC Permission:** Make sure you have `gcc` permission before installing all libraries.

-   **Install Pillow:** Install the specific version of Pillow library.

`pip install pillow==8.0.0`

-   **Copy Static Directory:** Copy the `static` directory to `public_html`.

-   **Setup Environment Variables:** Configure the following environment variables before running the project.

```
SECRET_KEY=
DEBUG=False
DB_HOST=
DB_NAME=
DB_USER=
DB_PASS=
DB_PORT=3306
```

## 🗄️ Database

1. **Configure Environment Variables:** Set up environment variables according to your database credentials.

2. **Create Database:** Create your database in MySQL.

3. **Migrate Database:** Navigate to the project directory and run migrations.
   `cd university && python3 manage migrate`.

## ⚙️ Backend

To run the backend of the project, follow these steps:

1. Navigate to the project directory - `cd university`
2. Start the server - `python manage runserver`

## 🎨 Frontend

Before starting frontend development, ensure to build the CSS continuously using TailwindCSS:

-   Run the following command to build 1style.min.css1 continuously:
    `npm run build:css`
