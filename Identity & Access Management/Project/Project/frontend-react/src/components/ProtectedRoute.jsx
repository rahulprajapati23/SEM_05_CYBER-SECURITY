import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const ProtectedRoute = ({ children, role }) => {
    const { isAuthenticated, hasRole } = useAuth();

    if (!isAuthenticated) {
        return <div>Please login to view this page.</div>;
    }

    if (role && !hasRole(role)) {
        return (
            <div className="glass-panel" style={{ padding: '20px', textAlign: 'center' }}>
                <h2>Access Denied</h2>
                <p>You do not have the required role: <code>{role}</code></p>
                <p>Current roles: {useAuth().user.roles.join(', ')}</p>
            </div>
        );
    }

    return children;
};

export default ProtectedRoute;
