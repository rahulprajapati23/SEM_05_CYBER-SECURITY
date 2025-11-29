import React from 'react';
import { useAuth } from '../context/AuthContext';
import { Link } from 'react-router-dom';

const Navbar = () => {
    const { user, isAuthenticated, login, logout } = useAuth();

    return (
        <header className="navbar glass-panel">
            <div className="navbar-left">
                <div className="logo-circle">IAM</div>
                <div className="logo-text">
                    <span className="brand-name">IAM Demo Shop</span>
                    <span className="brand-subtitle">Keycloak SSO • 2FA • RBAC</span>
                </div>
            </div>

            <div className="navbar-right">
                {isAuthenticated ? (
                    <>
                        <div className="user-pill">
                            <span id="user-name">{user.name}</span>
                            <span className="user-roles">{user.roles.join(', ')}</span>
                        </div>
                        <button className="btn subtle" onClick={logout}>Logout</button>
                    </>
                ) : (
                    <button className="btn primary" onClick={login}>Login with SSO</button>
                )}
            </div>
        </header>
    );
};

export default Navbar;
