import React, { createContext, useState, useEffect, useContext } from 'react';
import Keycloak from 'keycloak-js';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

const keycloak = new Keycloak({
    url: "http://localhost:8080/",
    realm: "demo-ecommerce",
    clientId: "ecommerce-frontend"
});

export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        keycloak.init({ onLoad: 'check-sso' }).then(authenticated => {
            setIsAuthenticated(authenticated);
            if (authenticated) {
                setUser({
                    name: keycloak.tokenParsed.preferred_username,
                    email: keycloak.tokenParsed.email,
                    roles: keycloak.tokenParsed.realm_access?.roles || []
                });
            }
            setLoading(false);
        }).catch(err => {
            console.error("Keycloak init failed", err);
            setLoading(false);
        });
    }, []);

    const login = () => keycloak.login();
    const logout = () => keycloak.logout();
    const hasRole = (role) => user?.roles?.includes(role);

    if (loading) {
        return <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>Loading...</div>;
    }

    return (
        <AuthContext.Provider value={{ isAuthenticated, user, login, logout, hasRole }}>
            {children}
        </AuthContext.Provider>
    );
};
