# 🚀 Render Deployment Guide - Ucuna Matata

This guide will walk you through deploying your Ucuna Matata team portfolio to Render.

## 📋 Prerequisites

- [x] GitHub account
- [x] Render account (free) - Sign up at https://render.com
- [x] Your code pushed to GitHub

## 🔧 Step 1: Prepare Your Repository

### 1.1 Commit All Changes

```bash
# Add all files
git add .

# Commit with a message
git commit -m "Add Flask backend with admin panel for Render deployment"

# Push to GitHub
git push origin main
```

### 1.2 Verify Files Are Present

Make sure these files exist in your repository:
- ✅ `Dockerfile` - Docker configuration
- ✅ `requirements.txt` - Python dependencies
- ✅ `app.py` - Flask application
- ✅ `render.yaml` - Render configuration (optional but recommended)
- ✅ `index.html` - Main page
- ✅ `admin.html` - Admin panel
- ✅ `styles.css` - Styles
- ✅ `script.js` - JavaScript

## 🚀 Step 2: Deploy to Render

### Method A: Automatic Deployment (Recommended - Uses render.yaml)

1. **Go to Render Dashboard**
   - Visit: https://dashboard.render.com/

2. **Click "New +" button** (top right)
   - Select **"Blueprint"**

3. **Connect GitHub Repository**
   - Click "Connect GitHub" if not already connected
   - Authorize Render to access your GitHub
   - Find and select your `ucuna-matata` repository

4. **Render Auto-Detects render.yaml**
   - Render will automatically find your `render.yaml` file
   - Review the configuration
   - Click **"Apply"**

5. **Set Environment Variables** (IMPORTANT!)
   - In the Blueprint setup, add these environment variables:
   
   ```
   ADMIN_USERNAME = your_chosen_username
   ADMIN_PASSWORD = your_secure_password_here
   SECRET_KEY = (generate with command below)
   ```
   
   Generate SECRET_KEY:
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

6. **Deploy!**
   - Click **"Create Resources"**
   - Render will build your Docker image and deploy
   - Wait 3-5 minutes for deployment

### Method B: Manual Deployment

1. **Go to Render Dashboard**
   - Visit: https://dashboard.render.com/

2. **Create New Web Service**
   - Click **"New +"** → **"Web Service"**

3. **Connect Repository**
   - Click "Connect GitHub"
   - Find and select `ucuna-matata`

4. **Configure Service**
   
   | Setting | Value |
   |---------|-------|
   | **Name** | `ucuna-matata` (or your choice) |
   | **Region** | Choose closest to you |
   | **Branch** | `main` |
   | **Root Directory** | Leave blank |
   | **Environment** | **Docker** |
   | **Plan** | **Free** |

5. **Add Environment Variables**
   - Click **"Advanced"** → **"Add Environment Variable"**
   - Add these three variables:
   
   ```
   Key: ADMIN_USERNAME
   Value: admin (or your choice)
   
   Key: ADMIN_PASSWORD
   Value: your_secure_password
   
   Key: SECRET_KEY
   Value: (paste generated key)
   ```

6. **Create Web Service**
   - Click **"Create Web Service"**
   - Render will start building

## ⏱️ Step 3: Wait for Deployment

### What Happens:
1. **Building** - Render builds your Docker image (2-3 minutes)
2. **Deploying** - Starts your container (30 seconds)
3. **Live!** - Your site is live!

### Monitor Progress:
- Watch the **Logs** tab in Render dashboard
- You'll see build progress in real-time
- Look for: `"Your service is live 🎉"`

## 🎉 Step 4: Access Your Site

Once deployed, you'll get a URL like:
```
https://ucuna-matata.onrender.com
```

Or with your custom name:
```
https://your-name.onrender.com
```

### Test Your Site:
1. **Main Page**: `https://your-app.onrender.com/`
2. **Admin Panel**: `https://your-app.onrender.com/admin`
3. **Login** with your credentials from environment variables

## 🔄 Step 5: Auto-Deploy on Git Push (Optional)

Render automatically redeploys when you push to GitHub!

```bash
# Make changes to your code
# Then:
git add .
git commit -m "Update feature"
git push origin main

# Render will automatically redeploy! 🚀
```

## ⚠️ Important Notes

### Free Tier Limitations:
- ✅ **Free hosting** - No credit card required
- ⚠️ **Spins down after 15 minutes** of inactivity
- ⏱️ **Takes ~30 seconds** to wake up on first request
- 💾 **Files reset** on each deploy (messages.json will be lost)

### Security:
- ⚠️ **NEVER use default passwords in production!**
- ✅ **Always set environment variables** for credentials
- ✅ **Use strong passwords** (16+ characters)
- ✅ **Keep SECRET_KEY secret** - never commit to Git

### Data Persistence:
- 📝 Messages are stored in `messages.json`
- ⚠️ **Data is lost** when container restarts
- 💡 **For production**: Use a database (PostgreSQL, MongoDB)

## 🐛 Troubleshooting

### Build Fails:
```bash
# Check these:
- Is Dockerfile present?
- Are all files committed and pushed?
- Check build logs in Render dashboard
```

### Site Won't Load:
```bash
# Check:
- Is deployment status "Live"?
- Check application logs
- Try the URL in incognito mode
- Wait 30 seconds (free tier spin-up time)
```

### Admin Login Fails:
```bash
# Verify:
- Environment variables are set correctly
- ADMIN_USERNAME and ADMIN_PASSWORD match
- SECRET_KEY is set
- Clear browser cookies and try again
```

### Port Issues:
```bash
# Render automatically sets PORT environment variable
# Our Dockerfile uses: CMD gunicorn --bind 0.0.0.0:${PORT:-5000}
# This works automatically!
```

## 🎯 Quick Commands Summary

```bash
# 1. Commit and push
git add .
git commit -m "Deploy to Render"
git push origin main

# 2. Generate secret key
python -c "import secrets; print(secrets.token_hex(32))"

# 3. Check deployment
curl https://ucuna-matata.onrender.com/

# 4. Check API
curl https://ucuna-matata.onrender.com/api/stats
```

## 🔗 Useful Links

- **Render Dashboard**: https://dashboard.render.com/
- **Render Docs**: https://render.com/docs
- **Docker Docs**: https://docs.docker.com/
- **Flask Docs**: https://flask.palletsprojects.com/

## 📞 Need Help?

If you encounter issues:
1. Check Render logs in dashboard
2. Review this guide again
3. Check Render documentation
4. Look at build/deploy logs for errors

## 🎊 Success Checklist

- [ ] Code committed and pushed to GitHub
- [ ] Render account created
- [ ] Repository connected to Render
- [ ] Environment variables set
- [ ] Service deployed successfully
- [ ] Main page loads at your URL
- [ ] Admin panel accessible at /admin
- [ ] Can login with your credentials
- [ ] Contact form works
- [ ] Messages appear in admin panel

## 🚀 You're Done!

Your Ucuna Matata portfolio is now live on Render!

Share your link:
- With your team
- On your GitHub README
- For your hackathon submission

**Good luck with your hackathon! 🎉**

