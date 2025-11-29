# Create main project folder
New-Item -ItemType Directory -Path "college-erp"

# Create subdirectories
New-Item -ItemType Directory -Path "college-erp/styles"
New-Item -ItemType Directory -Path "college-erp/js"
New-Item -ItemType Directory -Path "college-erp/assets"
New-Item -ItemType Directory -Path "college-erp/keycloak"

# Create files
New-Item -ItemType File -Path "college-erp/index.html"
New-Item -ItemType File -Path "college-erp/styles/styles.css"
New-Item -ItemType File -Path "college-erp/js/app.js"
New-Item -ItemType File -Path "college-erp/keycloak/keycloak.json"
New-Item -ItemType File -Path "college-erp/keycloak/keycloak.js"

# Create placeholder images in assets folder
New-Item -ItemType File -Path "college-erp/assets/dashboard.jpg"
New-Item -ItemType File -Path "college-erp/assets/students.jpg"
New-Item -ItemType File -Path "college-erp/assets/faculty.jpg"
New-Item -ItemType File -Path "college-erp/assets/courses.jpg"
New-Item -ItemType File -Path "college-erp/assets/settings.jpg"

Write-Host "College ERP project structure created successfully!"
