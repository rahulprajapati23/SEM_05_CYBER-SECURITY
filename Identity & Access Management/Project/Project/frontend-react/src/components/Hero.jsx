import React from 'react';
import { useAuth } from '../context/AuthContext';

const Hero = () => {
    const { isAuthenticated, login } = useAuth();

    return (
        <section className="hero glass-panel">
            <h1>Secure E-Commerce with <span className="accent">Keycloak</span></h1>
            <p className="hero-text">
                This demo shows how an e-commerce website uses
                <strong> Keycloak</strong> for
                <strong> Single Sign-On (SSO)</strong>,
                <strong> Two-Factor Authentication (TOTP)</strong>, and
                <strong> role-based access control (RBAC)</strong>.
            </p>

            <ul className="hero-list">
                <li>🔐 Centralized identity in Keycloak (no passwords in app).</li>
                <li>📲 2FA enforced via TOTP (Google Authenticator, etc.).</li>
                <li>🛂 Roles like <code>customer</code> and <code>admin</code> control access.</li>
            </ul>

            <div className="hero-actions">
                {!isAuthenticated && (
                    <button className="btn primary" onClick={login}>
                        Login &amp; Experience SSO
                    </button>
                )}
                <button className="btn ghost">
                    View ID Token in Console
                </button>
            </div>

            <div className="info-chip-row">
                <div className="info-chip">
                    <span className="chip-label">Status</span>
                    <span className={`chip-value ${isAuthenticated ? 'online' : 'offline'}`}>
                        {isAuthenticated ? 'Authenticated' : 'Not authenticated'}
                    </span>
                </div>
                <div className="info-chip">
                    <span className="chip-label">2FA</span>
                    <span className="chip-value">TOTP via Keycloak</span>
                </div>
            </div>
        </section>
    );
};

export default Hero;
