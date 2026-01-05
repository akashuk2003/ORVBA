On-Road Vehicle Breakdown Assistance System (ORVBA)
A robust web-based platform designed to connect stranded vehicle owners with nearby mechanics during roadside emergencies. This system leverages Geolocation to automatically detect the user's position and OpenStreetMap to guide mechanics to the breakdown site.

🚀 Features
🚗 Vehicle Owner (User)
One-Click SOS: Automatically detects current GPS location (Latitude/Longitude).

Reverse Geocoding: Converts GPS coordinates into a readable street address automatically.

Service Selection: Choose between Towing, Mechanic, or Fuel delivery.

Status Tracking: Track request status (Pending → Accepted → Completed).

🔧 Service Provider (Mechanic)
Partner Registration: Register with workshop details and upload ID proof.

Approval System: Account remains inactive until approved by Admin.

Live Job Board: View nearby pending requests.

Interactive Map: View customer location on OpenStreetMap (Leaflet.js) with a dynamic pin.

Navigation: "Open in Google Maps" button for driving directions.

👮 Administrator (Custom Dashboard)
Secure Portal: Separate login for system administration.

User Management: Monitor total users and mechanics.

Verification: Review and approve/reject mechanic ID proofs.

Request Monitoring: Oversee all active and completed service requests.

🛠️ Tech Stack
Backend: Python (Django 5.0+)

Frontend: HTML5, CSS3, Bootstrap 5

Scripting: Vanilla JavaScript (ES6)

Database: SQLite (Default)

Maps & Location:

HTML5 Geolocation API: For capturing GPS coordinates.

Leaflet.js & OpenStreetMap: For rendering maps (No API Key required).

Nominatim API: For address lookup (Reverse Geocoding).

⚙️ Installation & Setup
Follow these steps to run the project locally.

1. Prerequisites
Python 3.10 or higher installed.

Git installed.

2. Clone the Repository
Bash

cd orvba-project
3. Create Virtual Environment
Bash

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
Bash

pip install django pillow
(Note: Pillow is required for ImageFields used in Mechanic ID uploads).

5. Database Setup
Bash

python manage.py makemigrations accounts
python manage.py makemigrations services
python manage.py migrate
6. Create Superuser (Admin)
Bash

python manage.py createsuperuser
# Follow prompts to set username (e.g., 'admin') and password.
7. Run the Server
Bash

python manage.py runserver
Access the project at: http://127.0.0.1:8000/

📖 Usage Guide (Demo Flow)
To demonstrate the full capability of the system during a presentation, follow this sequence:

Admin Setup:

Log in to /custom-admin/login/.

Observe the Dashboard (0 Mechanics, 0 Requests).

Mechanic Registration:

Open an Incognito window.

Register a new Mechanic at /accounts/register/mechanic/.

Notice: You cannot login immediately (Status: Pending).

Approve Mechanic:

Go back to Admin Dashboard.

Click "Manage Mechanics" and Approve the new user.

User Request:

Register a new User at /accounts/register/customer/.

Click Request Assistance.

Allow Location Access when prompted.

Wait for the address to auto-fill, then submit.

Mechanic Action:

Login as the Mechanic.

See the new request in "Available Jobs".

Click View Details to see the Map and Address.

Accept and then Complete the job.

📂 Project Structure
Plaintext

ORVBA/
├── accounts/           # User & Mechanic Authentication logic
├── custom_admin/       # Custom Admin Dashboard logic
├── services/           # Core business logic (Requests, Maps)
├── static/             # CSS, JS, Images
├── templates/          # HTML files (organized by role)
├── media/              # Uploaded ID proofs
├── manage.py           # Django entry point
└── db.sqlite3          # Database file
