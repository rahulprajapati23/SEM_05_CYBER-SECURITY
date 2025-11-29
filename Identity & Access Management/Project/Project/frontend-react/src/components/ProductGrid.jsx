import React from 'react';

const products = [
    {
        id: 1,
        title: "Intro to Cyber Security",
        description: "Understand basic threats, passwords, phishing, and safe browsing.",
        price: "₹999",
        pill: "Beginner",
        accent: false
    },
    {
        id: 2,
        title: "Identity & Access Management Deep Dive",
        description: "OAuth2, OIDC, SAML, SSO, federation and governance in one course.",
        price: "₹1,499",
        pill: "IAM & SSO",
        accent: true
    },
    {
        id: 3,
        title: "Red Team Lab",
        description: "Practice attacking and defending modern web applications.",
        price: "₹1,999",
        pill: "Advanced",
        accent: false
    }
];

const ProductGrid = () => {
    return (
        <section className="products glass-panel">
            <div className="section-header">
                <h2>Featured Security Courses</h2>
                <p>Fake products – real IAM demo 😄</p>
            </div>

            <div className="product-grid">
                {products.map(product => (
                    <article key={product.id} className="product-card">
                        <div className={`product-pill ${product.accent ? 'accent-pill' : ''}`}>
                            {product.pill}
                        </div>
                        <h3>{product.title}</h3>
                        <p>{product.description}</p>
                        <div className="product-footer">
                            <span className="price-tag">{product.price}</span>
                            <button className="btn small">Add to Cart</button>
                        </div>
                    </article>
                ))}
            </div>
        </section>
    );
};

export default ProductGrid;
