# IAM Demo Shop - React Version

This is a port of the IAM Demo Shop to React + Vite.

## Prerequisites
- Node.js installed.
- Keycloak running on `http://localhost:8080`.

## Installation

1.  Open a terminal in this directory.
2.  Install dependencies:
    ```bash
    npm install
    ```

## Running the App

### Standard Method
```bash
npm run dev
```

### Windows Workaround (If path contains '&' or spaces)
If you see errors like `'Access' is not recognized`, use the provided batch file:
```bash
.\run_dev.bat
```

## Building for Production

### Standard Method
```bash
npm run build
```

### Windows Workaround
```bash
.\build_app.bat
```

> **Note:** If you encounter errors related to "Access" or "Module not found", it might be due to the `&` character in the parent directory path ("Identity & Access Management"). Try moving the project to a path without special characters if the build fails.

## Project Structure

- `src/context/AuthContext.jsx`: Handles Keycloak integration.
- `src/components`: Reusable UI components (Navbar, Hero, etc.).
- `src/pages`: Page layouts (Home, Admin).
- `src/App.jsx`: Main router configuration.
