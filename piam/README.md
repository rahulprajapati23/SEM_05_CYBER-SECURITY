# Keycloak SSO & TOTP 2FA Demo

This project demonstrates a full-stack application with Identity & Access Management (IAM) using Keycloak. It features OIDC authentication, Role-Based Access Control (RBAC), Single Sign-On (SSO), and enforced 2FA (TOTP).

## Tech Stack

- **Identity Provider**: Keycloak (Docker)
- **Database**: PostgreSQL (Docker)
- **Backend**: Node.js + Express + TypeScript
- **Frontend**: React + Vite + TypeScript
- **Infrastructure**: Docker Compose

## Prerequisites

- Docker and Docker Compose installed.
- Node.js (optional, for local development without Docker).

## Quick Start

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd piam
    ```

2.  **Start the infrastructure**:
    ```bash
    docker compose up --build
    ```
    This will start Keycloak, Postgres, Backend, and Frontend.
    - Keycloak: http://localhost:8080
    - Frontend: http://localhost:5173
    - Backend: http://localhost:4000

3.  **Wait for Keycloak**:
    Keycloak takes a minute to start. Watch the logs for `Keycloak 26.0.x started`.

## Usage & Testing

### 1. Login Flow
1.  Open the Frontend at [http://localhost:5173](http://localhost:5173).
2.  Click **Login**. You will be redirected to Keycloak.
3.  Login with the default user:
    - **Username**: `alice`
    - **Password**: `Alice@123`

### 2. TOTP Setup (2FA)
1.  On first login, you will be forced to configure TOTP (Google Authenticator).
2.  Scan the QR code with your authenticator app (e.g., Google Authenticator, Authy).
3.  Enter the code and submit.
4.  You will be redirected back to the Dashboard.

### 3. Protected Resources
1.  **Dashboard**: Accessible to all authenticated users. Shows user profile and token claims.
2.  **Admin Console**: Accessible only to users with the `admin` role.
    - Try accessing as `alice` (User): You will see an error or "Insufficient permissions".
    - Logout and login as `bob` (Admin):
        - **Username**: `bob`
        - **Password**: `Bob@123`
    - Access Admin Console: You should see the admin data.

### 4. Single Sign-On (SSO)
1.  Open a new tab or browser window (incognito if testing separation, but same browser for SSO).
2.  If you are logged in, you should be automatically authenticated or just need to click "Login" without re-entering credentials (depending on prompt settings).

### 5. Global Logout
1.  Click **Logout** in the Frontend.
2.  This triggers a global logout in Keycloak, invalidating the session.

## Project Structure

```
.
├── backend/            # Node.js + Express Backend
├── frontend/           # React + Vite Frontend
├── keycloak/           # Keycloak Configuration
│   └── realm.json      # Realm Export (Users, Roles, Clients)
├── docker-compose.yml  # Docker Compose Configuration
└── README.md           # This file
```

## Development

### Running Locally (without Docker for apps)

1.  **Start Keycloak & Postgres**:
    ```bash
    docker compose up keycloak postgres
    ```

2.  **Backend**:
    ```bash
    cd backend
    npm install
    npm run dev
    ```

3.  **Frontend**:
    ```bash
    cd frontend
    npm install
    npm run dev
    ```

## Security Considerations

- **HTTPS**: In a production environment, ensure Keycloak and the applications are served over HTTPS.
- **Secrets**: Do not commit `.env` files or secrets to version control. Use a secrets manager.
- **Token Storage**: This demo stores tokens in memory/localStorage for simplicity. For higher security, consider using HTTP-only cookies or a Backend-for-Frontend (BFF) pattern.

## License

MIT
