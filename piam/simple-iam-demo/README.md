# Simple IAM Demo

2.  Login with `admin` / `admin`.
32.  **Web Server**: Run a static server in the `simple-iam-demo` directory on port **5525**.
    - `cd simple-iam-demo`
    - `python -m http.server 5525` (or use VSCode Live Server)
3.  **Browser**: Open `http://localhost:5525`.e manually:
        - Realm Name: `simple-iam`
    - You will be prompted to setup Mobile Authenticator (TOTP).
-   **HTTPS**: Always use HTTPS for OIDC in production.
-   **Security**: Do not expose the Keycloak Admin Console publicly.
