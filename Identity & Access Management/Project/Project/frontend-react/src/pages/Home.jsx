import React from 'react';
import Hero from '../components/Hero';
import ProductGrid from '../components/ProductGrid';
import { useAuth } from '../context/AuthContext';
import { Link } from 'react-router-dom';

const Home = () => {
    const { isAuthenticated, hasRole } = useAuth();

    return (
        <main className="main-grid">
            <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                <Hero />
                <ProductGrid />
            </div>

            <aside>
                <div className="glass-panel" style={{ padding: '20px' }}>
                    <h3>Quick Actions</h3>
                    {isAuthenticated ? (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                            <Link to="/admin" className="btn danger" style={{ justifyContent: 'center' }}>
                                Go to Admin Dashboard
                            </Link>
                            <p className="muted">
                                (Requires <code>admin</code> role)
                            </p>
                        </div>
                    ) : (
                        <p className="muted">Login to see available actions.</p>
                    )}
                </div>
            </aside>
        </main>
    );
};

export default Home;
