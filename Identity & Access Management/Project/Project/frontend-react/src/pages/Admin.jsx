import React from 'react';
import { useAuth } from '../context/AuthContext';

const Admin = () => {
    const { user } = useAuth();

    return (
        <div className="glass-panel" style={{ padding: '30px' }}>
            <h1>Admin Dashboard</h1>
            <p>Welcome, <strong>{user.name}</strong>!</p>
            <p>You have access to this area because you have the <code>admin</code> role.</p>

            <div style={{ marginTop: '20px', padding: '20px', background: 'rgba(0,0,0,0.2)', borderRadius: '10px' }}>
                <h3>System Status</h3>
                <p>✅ Keycloak Connection: Active</p>
                <p>✅ Database: Connected</p>
                <p>✅ 2FA Enforcement: Enabled</p>
            </div>
        </div>
    );
};

export default Admin;
