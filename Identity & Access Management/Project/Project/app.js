const keycloak = new Keycloak({
  url: "http://localhost:8080/",
  realm: "demo-ecommerce",
  clientId: "ecommerce-frontend"
});

// Initialize Keycloak when the app loads
keycloak
  .init({ onLoad: "check-sso" })
  .then((authenticated) => {
    console.log("Authenticated:", authenticated);
    // You can update UI based on auth state here if needed
  })
  .catch((err) => {
    console.error("Keycloak init error", err);
  });

// Called when user clicks "Login with SSO"
function loginWithSSO() {
  keycloak.login({
    redirectUri: "http://localhost:3000/frontend/pages/admin.html"
  });
}

// Optional logout function if you add a logout button later
function logoutSSO() {
  keycloak.logout({
    redirectUri: "http://localhost:3000/index.html"
  });
}
