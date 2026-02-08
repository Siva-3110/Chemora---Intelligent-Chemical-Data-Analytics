# Chemora – Chemical Equipment Parameter Visualizer
A Hybrid Application for Industrial Data Analytics (Web + Desktop)

Chemora is a full-stack hybrid application designed to visualize and analyze chemical equipment parameters (Flowrate, Pressure, Temperature). It features a synchronized React Web Dashboard and a PyQt5 Desktop Application, both powered by a unified Django REST API.

Users can upload CSV datasets to generate instant analytics, interactive charts, and downloadable reports (PDF).

## 🛠 Tech Stack
| Component | Technologies Used |
|-----------|------------------|
| Backend | Django 4.2, Django REST Framework, SQLite, Pandas, ReportLab |
| Web App | React.js, Chart.js, Axios, Modern CSS |
| Desktop App | Python, PyQt5, Matplotlib (embedded visualization) |
| Deployment | Netlify(Frontend), Render(Backend API) |

## 📸 Screenshots
| Web Dashboard | Desktop Application |
|---------------|-------------------|
| ![Web Dashboard](screenshots/webapp.png) | ![Desktop App](screenshots/desktopapp.png) |

## 🚀 Live Demos
- **Web App (Netlify)**: https://chemora.netlify.app/
- **Backend API (Render)**: https://chemora.onrender.com
- **Desktop App**: Download `main.exe` from [GitHub Releases](https://github.com/Siva-3110/Chemora/tree/master/desktop/dist) 


## 🔐 Demo Credentials
To test the live system, you can use these guest credentials or create a new account:

- **Username**: admin
- **Password**: admin

## 📂 Project Structure
```
Chemora/
├── backend/                      # Django REST API Backend
│   ├── api/                      # REST API Application
│   │   ├── migrations/           # Database migrations
│   │   ├── admin.py              # Django admin configuration
│   │   ├── models.py             # Database models (Dataset, Equipment)
│   │   ├── serializers.py        # DRF serializers
│   │   ├── urls.py               # API URL routing
│   │   └── views.py              # API endpoints & PDF generation
│   ├── equipment_api/            # Django project settings
│   │   ├── settings.py           # Configuration (CORS, Auth, Database)
│   │   ├── urls.py               # Main URL routing
│   │   └── wsgi.py               # WSGI application
│   ├── build.sh                  # Render build script (auto-creates admin)
│   ├── db.sqlite3                # SQLite database
│   ├── manage.py                 # Django management script
│   ├── Procfile                  # Render deployment config
│   ├── render.yaml               # Render service configuration
│   ├── requirements.txt          # Python dependencies
│   └── start.sh                  # Local startup script
│
├── frontend/                     # React Web Application
│   ├── public/
│   │   ├── chemora image.jpg     # Logo
│   │   └── index.html            # HTML template
│   ├── src/
│   │   ├── components/
│   │   │   ├── Analytics.js      # Data visualization & charts
│   │   │   ├── Charts.js         # Chart components
│   │   │   ├── Dashboard.js      # Main dashboard layout
│   │   │   ├── DataManagement.js # Data management features
│   │   │   ├── DataTable.js      # Equipment data table
│   │   │   ├── DataUpload.js     # CSV upload component
│   │   │   ├── FileUpload.js     # File upload handler
│   │   │   ├── History.js        # Dataset history & reports
│   │   │   ├── HomePage.js       # Landing page
│   │   │   ├── Login.js          # Login page
│   │   │   ├── Overview.js       # Overview component
│   │   │   ├── Reports.js        # Report generation
│   │   │   ├── Signup.js         # User registration
│   │   │   └── TestChart.js      # Chart testing
│   │   ├── App.js                # Main app component (Basic Auth)
│   │   ├── App_fixed.css         # Updated styles
│   │   ├── App.css               # Original styles
│   │   ├── Dashboard.css         # Dashboard styles
│   │   └── index.js              # React entry point
│   ├── .env                      # Environment variables (API URL)
│   ├── package.json              # Node dependencies
│   └── package-lock.json         # Locked dependencies
│
├── desktop/                      # PyQt5 Desktop Application
│   ├── main.py                   # Desktop app (Fixed Basic Auth)
│   ├── main.spec                 # PyInstaller configuration
│   ├── requirements.txt          # Python dependencies
│   └── equipment_report_4.pdf    # Sample generated report
│
├── screenshots/                  # Application screenshots
│   ├── desktopapp.png
│   └── webapp.png
│
├── documentation/                # Project documentation
│   ├── AUTHENTICATION_COMPARISON.md  # Auth fix comparison
│   ├── DESKTOP_LOGIN_FIX.md          # Desktop login fix details
│   ├── FIX_SUMMARY.md                # Quick fix summary
│   ├── TESTING_INSTRUCTIONS.md       # Testing guide
│   └── DEMO.md                       # Demo information
│
├── sample_data.csv               # Sample dataset for testing
├── sample_equipment_data.csv     # Additional sample data
├── equipment_report_16.pdf       # Sample PDF report
│
├── scripts/                      # Utility scripts
│   ├── start_backend.bat         # Start Django backend
│   ├── start_frontend.bat        # Start React frontend
│   ├── start_desktop.bat         # Start desktop app
│   ├── test_desktop_auth.py      # Auth testing script
│   ├── clear_accounts.html       # Account management
│   ├── debug.html                # Debug utilities
│   └── test_connection.html      # Connection testing
│
├── .gitignore                    # Git ignore rules
└── README.md                     # Project documentation
```

## ✨ Features
- **Unified Backend**: A single Django API serves both Web and Desktop clients.
- **Data Visualization**: Interactive Bar, Line, Pie, and Scatter charts using Chart.js (Web) and Matplotlib (Desktop).
- **Detailed Analytics**:
  - Summary Cards: Total count, Averages (Pressure, Temperature, Flowrate).
  - Distribution: Breakdown of equipment types (Reactors, Pumps, Vessels, HeatExchangers, Compressors).
  - Data Preview: Full-width, scrollable raw data table.
- **History Tracking**: Sidebar retains uploaded datasets for quick switching.
- **Reporting**: One-click export to PDF reports with embedded charts and statistics.
- **Clean UI**: Borderless charts and modern interface design without emoji clutter.
- **Cross-Platform**: Web browser access + Windows desktop application.

## 🚀 Local Setup Guide

### Prerequisites
- Python 3.10+
- Node.js 16+
- Git

### 1. Backend Setup (Django)
Open your terminal in the project root:

```bash
# Clone repository
git clone https://github.com/Siva-3110/Chemora.git
cd chemical_equipment_visualizer

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\Activate

# Install dependencies
pip install -r backend/requirements.txt

# Run Migrations & Create User
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create your local login

# Start Server
python manage.py runserver
```
*API will run at: http://127.0.0.1:8000/*

### 2. Web App Setup (React)
Open a new terminal:

```bash
cd frontend

# Install dependencies
npm install

# Start Client
npm start
```
*App will open at: http://localhost:3000/*

### 3. Desktop App Setup (PyQt5)
Open a new terminal (ensure venv is active):

```bash
# Navigate to desktop folder
cd desktop

# Install desktop-specific requirements
pip install -r requirements.txt

# Run App
python main.py
```

### 4. Quick Start (Alternative)
Use the provided batch files for Windows:

```bash
# Start backend
start_backend.bat

# Start frontend (new terminal)
start_frontend.bat

# Start desktop app (new terminal)
start_desktop.bat
```

## 🔗 API Endpoints Overview
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/datasets/` | Get list of uploaded datasets |
| POST | `/api/upload/` | Upload CSV File (Multipart) |
| GET | `/api/equipment/{id}/` | Get equipment data for dataset |
| GET | `/api/summary/{id}/` | Get dataset statistics & analytics |
| GET | `/api/report/{id}/` | Download Analytics Report (PDF) |

## 📱 Usage Instructions

### Web Application
1. Visit the deployed web app or run locally
2. Login with demo credentials (admin/admin)
3. Upload CSV file with equipment data (columns: name, type, flowrate, pressure, temperature)
4. View interactive charts and analytics in the "Charts & Analysis" tab
5. Generate and download PDF reports

### Desktop Application
1. Download `main.exe` from GitHub releases or run locally with Python
2. Double-click to run (no installation needed for .exe)
3. Login with same credentials
4. Upload and analyze data with professional desktop interface
5. Offline capability after initial setup

## 🎯 Key Achievements
- **Hybrid Architecture**: Single Django backend serving both web and desktop clients
- **Real-time Analytics**: Instant chart generation from CSV uploads with multiple visualization types
- **Cross-platform Support**: Web browser + Windows desktop executable
- **Professional Reports**: PDF generation with embedded charts and comprehensive statistics
- **Clean Design**: Modern UI with borderless charts, removed emoji icons for professional appearance
- **Data Processing**: Handles multiple equipment types with statistical analysis
- **Deployment Ready**: Configured for Render (backend) and Netlify (frontend) deployment

## 🏗️ Deployment

### Frontend (Netlify)
- **Platform**: Netlify
- **Build Command**: `npm run build`
- **Publish Directory**: `frontend/build`
- **Base Directory**: `frontend`
- **Environment Variables**:
  - `REACT_APP_API_URL`: Your Render backend URL (e.g., `https://chemora-backend.onrender.com/api`)
  - `CI`: `false` (to disable treating warnings as errors)
- **Auto Deploy**: Connected to GitHub repository for automatic deployments on push

### Backend (Render)
- **Platform**: Render Web Service
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn equipment_api.wsgi:application`
- **Configuration**: `Procfile` and `render.yaml`
- **Auto Deploy**: Connected to GitHub repository
- **Features**:
  - Automatic admin user creation on deployment
  - SQLite database persistence
  - CORS enabled for Netlify frontend

### Desktop Distribution
- **Packaging**: PyInstaller
- **Output**: Single executable file (`main.exe`)
- **Distribution**: GitHub Releases
- **No Installation Required**: Standalone Windows executable

## 📊 Sample Data Format
CSV file should contain columns:
```csv
name,type,flowrate,pressure,temperature
Reactor-1,Reactor,105.23,112.60,179.73
Pump-2,Pump,98.45,108.30,165.20
...
```

## 📝 Submission Details
- **Repository**: [GitHub - Chemora](https://github.com/Siva-3110/Chemora---Intelligent-Chemical-Data-Analytics)
- **Demo Video**: [Demo Video](https://drive.google.com/file/d/1fSfkYz-fNBJme21PgT5aso7gzwQ8E_KE/view?usp=sharing)
