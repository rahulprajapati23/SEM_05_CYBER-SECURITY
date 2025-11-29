// Keycloak Configuration
const keycloakConfig = {
    url: 'http://localhost:8080',
    realm: 'simple-iam',
    clientId: 'simple-web-client'
};

// Check if Keycloak is loaded
if (typeof Keycloak === 'undefined') {
    console.error('Keycloak library not loaded from CDN.');
    // Mock Keycloak to prevent crash
    window.Keycloak = function () {
        return {
            init: () => Promise.reject('Keycloak library missing'),
            login: () => console.log('Login clicked (Keycloak missing)'),
            logout: () => console.log('Logout clicked (Keycloak missing)'),
            realmAccess: { roles: [] },
            tokenParsed: {}
        };
    };
}

// Initialize Keycloak
const keycloak = new Keycloak(keycloakConfig);

// Mock Products
const products = [
    { id: 1, name: "Wireless Headphones", price: 99.99, image: "🎧" },
    { id: 2, name: "Smart Watch", price: 199.99, image: "⌚" },
    { id: 3, name: "Laptop Sleeve", price: 29.99, image: "💻" },
    { id: 4, name: "Mechanical Keyboard", price: 149.99, image: "⌨️" },
    { id: 5, name: "USB-C Hub", price: 49.99, image: "🔌" },
    { id: 6, name: "Noise Cancelling Earbuds", price: 129.99, image: "🎵" }
];

// Cart State
let cart = [];

// Determine current page
const isDashboard = window.location.pathname.endsWith('dashboard.html');

// Init Options
const initOptions = {
    onLoad: isDashboard ? 'login-required' : 'check-sso',
    checkLoginIframe: false,
    enableLogging: true
};

// Render products immediately
document.addEventListener('DOMContentLoaded', () => {
    if (!isDashboard) {
        try {
            renderProducts();
            setupCartUI();
        } catch (e) {
            console.error("Error rendering products:", e);
        }
    }
});

// Timeout wrapper for Keycloak init
const initPromise = keycloak.init(initOptions);
const timeoutPromise = new Promise((_, reject) =>
    setTimeout(() => reject(new Error('Keycloak init timed out')), 2000)
);

Promise.race([initPromise, timeoutPromise])
    .then(authenticated => {
        console.log(`User is ${authenticated ? 'authenticated' : 'not authenticated'}`);
        updateAuthUI(authenticated);

        if (isDashboard) {
            if (authenticated) {
                renderDashboard();
            } else {
                window.location.href = 'index.html';
            }
        }
    }).catch(err => {
        console.error('Failed to initialize Keycloak:', err);
        showAuthWarning();
    });

function showAuthWarning() {
    console.log("Showing auth warning...");
    const main = document.querySelector('main');
    const warning = document.createElement('div');
    warning.className = 'auth-warning';
    warning.style.display = 'block';
    warning.innerHTML = `
        <strong>⚠️ Authentication Server Unavailable</strong><br>
        Unable to connect to Keycloak at <code>${keycloakConfig.url}</code>.<br>
        Login functionality is currently disabled. You can still browse products.
    `;
    // Insert before the first child of main
    if (main) main.insertBefore(warning, main.firstChild);

    // Disable login buttons
    const navLogin = document.getElementById('navLogin');
    if (navLogin) {
        navLogin.textContent = 'Login Unavailable';
        navLogin.style.opacity = '0.5';
        navLogin.onclick = (e) => e.preventDefault();
    }

    const checkoutBtn = document.getElementById('checkoutBtn');
    if (checkoutBtn) {
        checkoutBtn.textContent = 'Checkout Unavailable';
        checkoutBtn.disabled = true;
        checkoutBtn.style.backgroundColor = '#9ca3af';
        checkoutBtn.style.cursor = 'not-allowed';
    }
}

function updateAuthUI(authenticated) {
    const navLogin = document.getElementById('navLogin');
    const navAccount = document.getElementById('navAccount');
    const checkoutBtn = document.getElementById('checkoutBtn');

    if (authenticated) {
        if (navLogin) navLogin.style.display = 'none';
        if (navAccount) navAccount.style.display = 'inline';
        if (checkoutBtn) {
            checkoutBtn.textContent = 'Checkout';
            checkoutBtn.onclick = () => alert('Checkout successful! (Mock)');
        }
    } else {
        if (navLogin) {
            navLogin.style.display = 'inline';
            navLogin.onclick = () => keycloak.login({ redirectUri: window.location.origin + '/dashboard.html' });
        }
        if (navAccount) navAccount.style.display = 'none';
        if (checkoutBtn) {
            checkoutBtn.textContent = 'Login to Checkout';
            checkoutBtn.onclick = () => keycloak.login({ redirectUri: window.location.origin + '/index.html' });
        }
    }
}

function renderProducts() {
    const grid = document.getElementById('productGrid');
    if (!grid) return;

    grid.innerHTML = products.map(product => `
        <div class="product-card">
            <div class="product-image">${product.image}</div>
            <div class="product-info">
                <div class="product-title">${product.name}</div>
                <div class="product-price">$${product.price}</div>
                <button class="btn primary" onclick="addToCart(${product.id})">Add to Cart</button>
            </div>
        </div>
    `).join('');
}

// Global scope for onclick
window.addToCart = function (productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        cart.push(product);
        updateCartCount();
        updateCartModal();
        // Simple feedback
        const btn = event.target;
        const originalText = btn.textContent;
        btn.textContent = "Added!";
        setTimeout(() => btn.textContent = originalText, 1000);
    }
};

window.removeFromCart = function (index) {
    cart.splice(index, 1);
    updateCartCount();
    updateCartModal();
};

function updateCartCount() {
    const count = document.getElementById('cartCount');
    if (count) count.textContent = cart.length;
}

function updateCartModal() {
    const cartItems = document.getElementById('cartItems');
    const cartTotal = document.getElementById('cartTotal');
    if (!cartItems || !cartTotal) return;

    if (cart.length === 0) {
        cartItems.innerHTML = '<p>Your cart is empty.</p>';
        cartTotal.textContent = '0.00';
    } else {
        let total = 0;
        cartItems.innerHTML = cart.map((item, index) => {
            total += item.price;
            return `
                <div class="cart-item">
                    <span>${item.name}</span>
                    <span>
                        $${item.price} 
                        <button class="btn secondary" style="padding: 0.2rem 0.5rem; margin-left: 0.5rem;" onclick="removeFromCart(${index})">&times;</button>
                    </span>
                </div>
            `;
        }).join('');
        cartTotal.textContent = total.toFixed(2);
    }
}

function setupCartUI() {
    const modal = document.getElementById('cartModal');
    const btn = document.getElementById('navCart');
    const span = document.getElementsByClassName("close")[0];

    if (btn && modal) {
        btn.onclick = (e) => {
            e.preventDefault();
            modal.style.display = "block";
        }
    }

    if (span && modal) {
        span.onclick = () => modal.style.display = "none";
    }

    window.onclick = (event) => {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

function renderDashboard() {
    // Populate User Info
    document.getElementById('headerUsername').textContent = keycloak.tokenParsed.preferred_username;
    document.getElementById('username').textContent = keycloak.tokenParsed.preferred_username;
    document.getElementById('email').textContent = keycloak.tokenParsed.email || 'N/A';
    document.getElementById('fullName').textContent = keycloak.tokenParsed.name || 'N/A';

    // Roles
    const roles = keycloak.realmAccess ? keycloak.realmAccess.roles : [];
    document.getElementById('roles').textContent = roles.join(', ') || 'None';

    // Logout
    document.getElementById('logoutBtn').onclick = () => keycloak.logout({ redirectUri: window.location.origin + '/index.html' });
}
