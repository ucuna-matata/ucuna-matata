# Ucuna Matata - Team Portfolio

![Ucuna Matata Team](https://img.shields.io/badge/Team-Ucuna%20Matata-blueviolet?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 🚀 About Our Team

**Ucuna Matata** — a team of ambitious developers and creative designers who strive to create innovative web solutions. Our philosophy: "No worries — only solutions".

We combine modern technologies with creative thinking to achieve the best results. Our goal is to create intuitive and powerful web applications that solve real user problems.

## 👥 Team Members

### Nazar Mykhailyshchuk - Full Stack Developer
Our own full stack developer who creates end-to-end solutions with passion and expertise.

**Skills:** Python, JavaScript, Docker

**GitHub:** [@partum55](https://github.com/partum55)

### Anna Bondarenko - Frontend Developer
Specializes in creating interactive interfaces with React and Vue.js. Has an eye for details and UX design.

**Skills:** React, JavaScript, CSS, HTML5

### Dmytro Koval - Backend Developer
Expert in Python and Node.js. Creates reliable and scalable server solutions with clean code.

**Skills:** Python, Node.js, API, Databases

### Olena Melnyk - UI/UX Designer
Creates modern and aesthetic designs that combine beauty with functionality and user convenience.

**Skills:** Figma, Adobe XD, UI/UX Design, Prototyping

## ✨ Project Features

- 🎨 **Modern Design** - Minimalistic and attractive interface
- 🌈 **Animations** - Smooth transitions and interactive elements
- 📱 **Responsive Design** - Looks great on all devices
- ⚡ **Performance** - Optimized code without unnecessary dependencies
- 🎭 **Interactivity** - Dynamic effects when interacting with user
- 🔥 **Backend Integration** - Flask API for contact form and statistics
- 📊 **Animated Stats** - Counter animations for team statistics
- 📧 **Contact Form** - Fully functional contact form with backend
- 🔐 **Admin Panel** - Secure admin dashboard to manage messages
- 🔗 **Clickable Team Cards** - Each team member card links to their GitHub profile

## 🛠️ Technologies

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styles, gradients, animations
- **JavaScript (Vanilla)** - Interactivity without frameworks
- **Google Fonts** - Inter font for modern look

### Backend
- **Python 3** - Backend logic
- **Flask** - Web framework for API
- **Flask-CORS** - Cross-origin resource sharing
- **Session Management** - Secure admin authentication

## 🌐 Demo

🔗 **Live Version:** [https://ucuna-matata.onrender.com](https://ucuna-matata.onrender.com)

🔐 **Admin Panel:** [https://ucuna-matata.onrender.com/admin](https://ucuna-matata.onrender.com/admin)

## 📦 Installation and Setup

### Option 1: Static Site (GitHub Pages)

1. Clone the repository:
```bash
git clone https://github.com/partum55/ucuna-matata.git
cd ucuna-matata
```

2. Open `index.html` in your browser:
```bash
# On Linux/Mac
open index.html

# On Windows
start index.html

# Or use a local server
python -m http.server 8000
```

3. Open browser and go to `http://localhost:8000`

### Option 2: With Flask Backend (Full Features)

1. Clone the repository (if not already done)

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask application:
```bash
python app.py
```

5. Open browser and go to `http://localhost:5000`

The Flask backend provides:
- Contact form submission handling
- Message storage in JSON file
- Statistics API endpoint
- Admin panel for message management
- Session-based authentication
- CORS support for development

## 🔐 Admin Panel

The admin panel allows you to view and manage contact form submissions.

### Access Admin Panel

**URL:** `/admin` (e.g., `http://localhost:5000/admin`)

### Default Credentials

**Username:** `admin`  
**Password:** `hackathon2025`

⚠️ **IMPORTANT:** Change these credentials before deploying to production!

### Admin Features

- 📊 **Dashboard Statistics** - View total messages, today's messages, and weekly messages
- 📬 **Message Management** - View all contact form submissions
- 🗑️ **Delete Messages** - Remove individual messages
- 🔒 **Secure Authentication** - Session-based login system
- ⏰ **Timestamp Display** - See when messages were received with relative time

### Changing Admin Credentials

Set environment variables:

```bash
export ADMIN_USERNAME="your_username"
export ADMIN_PASSWORD="your_secure_password"
export SECRET_KEY="your_secret_key_here"
```

Or in your deployment platform (Render, Heroku, etc.), add these as environment variables.

## 📁 Project Structure

```
ucuna-matata/
├── index.html          # Main HTML page
├── admin.html          # Admin dashboard page
├── styles.css          # Styles and animations
├── script.js           # JavaScript for interactivity
├── app.py              # Flask backend application
├── requirements.txt    # Python dependencies
├── messages.json       # Contact form submissions (auto-generated)
├── Dockerfile          # Docker image configuration
├── docker-compose.yml  # Docker Compose configuration
├── .dockerignore       # Docker ignore file
├── render.yaml         # Render deployment configuration
├── README.md           # Project documentation
├── LICENSE             # License
└── .gitignore          # Git ignore file
```

## 🎯 Hackathon Requirements Checklist

✅ **Team Name** - Ucuna Matata  
✅ **Team Description** - Presented on the main page  
✅ **Team Member Information** - Cards with name, role, and description  
✅ **Online Availability** - Ready for GitHub Pages deployment  
✅ **GitHub Repository** - Public repository  
✅ **README.md** - Complete documentation  
✅ **Extra Features** - Flask backend with contact form, stats, and admin panel

## 🚀 Deploy to GitHub Pages

### Static Site Only (Recommended for Hackathon)

1. Push code to your GitHub repository:
```bash
git add .
git commit -m "Add team portfolio with Flask backend and admin panel"
git push origin main
```

2. Go to Settings → Pages in your repository
3. Select branch `main` and folder `/ (root)`
4. Click Save
5. Your site will be available in a few minutes!

**Note:** GitHub Pages only supports static files. The contact form and admin panel need a backend server.

## 🐳 Deploy with Docker

### Build and Run Locally with Docker

1. Build the Docker image:
```bash
docker build -t ucuna-matata .
```

2. Run the container:
```bash
docker run -p 5000:5000 \
  -e ADMIN_USERNAME=admin \
  -e ADMIN_PASSWORD=your_password \
  -e SECRET_KEY=your_secret_key \
  ucuna-matata
```

3. Open browser and go to `http://localhost:5000`

### Using Docker Compose

```bash
# Start the application
docker-compose up

# Start in detached mode
docker-compose up -d

# Stop the application
docker-compose down
```

## 🚀 Deploy to Render (Recommended)

Render provides free hosting for web applications with Docker support!

### Method 1: Using render.yaml (Automatic)

1. Push your code to GitHub

2. Go to [Render Dashboard](https://dashboard.render.com/)

3. Click "New" → "Blueprint"

4. Connect your GitHub repository

5. Render will automatically detect `render.yaml` and deploy your app!

6. **Set Environment Variables** in Render Dashboard:
   - `ADMIN_USERNAME` - Your admin username
   - `ADMIN_PASSWORD` - Your admin password (use a strong password!)
   - `SECRET_KEY` - Random secret key for sessions

### Method 2: Manual Deployment

1. Go to [Render Dashboard](https://dashboard.render.com/)

2. Click "New" → "Web Service"

3. Connect your GitHub repository

4. Configure:
   - **Name:** ucuna-matata
   - **Environment:** Docker
   - **Plan:** Free
   - **Branch:** main

5. Add Environment Variables:
   - `ADMIN_USERNAME` = your_username
   - `ADMIN_PASSWORD` = your_secure_password
   - `SECRET_KEY` = generate_random_string_here

6. Click "Create Web Service"

7. Your app will be live at: `https://ucuna-matata.onrender.com`

### Important Notes for Render:

- The free tier may spin down after inactivity (takes ~30 seconds to wake up)
- `messages.json` will reset on each deployment (consider using a database for production)
- Environment variables can be set in Render dashboard
- **Always change default admin credentials for production!**

### Deploy Backend to Other Platforms

For full backend functionality, you can also deploy to:
- **Railway:** https://railway.app (supports Docker)
- **PythonAnywhere:** https://www.pythonanywhere.com
- **Heroku:** https://heroku.com (supports Docker)
- **DigitalOcean App Platform:** https://www.digitalocean.com/products/app-platform

## 🔧 Environment Variables

For production deployment, set these environment variables:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `PORT` | Port number | 5000 | No (auto-set by Render) |
| `ADMIN_USERNAME` | Admin login username | admin | Yes (change in production!) |
| `ADMIN_PASSWORD` | Admin login password | hackathon2025 | Yes (change in production!) |
| `SECRET_KEY` | Flask session secret key | auto-generated | Yes (change in production!) |
| `FLASK_ENV` | Flask environment | production | No |

### Generating a Secure Secret Key

```python
python -c "import secrets; print(secrets.token_hex(32))"
```

## 🎨 Customization

You can easily customize the page for your team:

1. **Change team information** in `index.html`:
   - Team name and tagline
   - Team description
   - Member information (name, role, description, GitHub links)
   - Update member initials in avatar placeholders

2. **Customize colors** in `styles.css`:
   - Change CSS variables in `:root`
   - Adjust gradients and color schemes

3. **Add team photos**:
   - Replace `.image-placeholder` with `<img>` tags
   - Add photos to the project folder

4. **Update statistics** in `app.py`:
   - Modify the `/api/stats` endpoint
   - Change values in the stats dictionary

5. **Configure Docker**:
   - Modify `Dockerfile` for custom Python version or dependencies
   - Update `docker-compose.yml` for development settings

6. **Update admin credentials**:
   - Set `ADMIN_USERNAME` and `ADMIN_PASSWORD` environment variables
   - Never commit credentials to Git!

## 🔌 API Endpoints

### Public Endpoints

#### POST `/api/contact`
Submit a contact form message
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello team!"
}
```

#### GET `/api/stats`
Get team statistics
```json
{
  "projects_completed": 15,
  "coding_hours": 48,
  "team_members": 4,
  "coffee_cups": 100
}
```

### Admin Endpoints (Authentication Required)

#### POST `/api/login`
Admin login
```json
{
  "username": "admin",
  "password": "password"
}
```

#### POST `/api/logout`
Admin logout

#### GET `/api/check-auth`
Check if user is authenticated

#### GET `/api/messages`
Get all submitted messages (admin only)

#### DELETE `/api/messages/<message_id>`
Delete a specific message (admin only)

## 🔒 Security Notes

- Admin panel uses session-based authentication
- **Change default credentials before deploying to production**
- Use environment variables for sensitive data
- HTTPS is recommended for production (Render provides this for free)
- Consider adding rate limiting for the contact form
- For production, use a real database instead of JSON file
- Add CSRF protection for production use

## 🤝 Contributing

This project was created for a hackathon. If you want to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Team Ucuna Matata**

- GitHub: [@partum55/ucuna-matata](https://github.com/partum55/ucuna-matata)
- Project Link: [https://ucuna-matata.onrender.com](https://ucuna-matata.onrender.com)

**Project created with ❤️ for Hackathon 2025**

---

⭐ Star this project if you like it!

## 🎉 Quick Start Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/partum55/ucuna-matata.git
   cd ucuna-matata
   ```

2. **Run locally**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python app.py
   ```

3. **Access the application**
   - Main site: http://localhost:5000
   - Admin panel: http://localhost:5000/admin
   - Login: admin / hackathon2025

4. **Deploy to Render**
   - Push to GitHub
   - Connect to Render
   - Set environment variables
   - Deploy!

That's it! You're ready to go! 🚀
