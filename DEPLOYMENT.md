# Quick Deployment Guide

## 🚀 Choose Your Platform

### 1️⃣ Streamlit Cloud (Easiest - FREE)

**Best for**: Quick demos, personal projects, sharing with team

**Steps**:
1. Create a GitHub account (if you don't have one)
2. Create a new repository on GitHub
3. Upload all files from this folder to the repository
4. Go to [share.streamlit.io](https://share.streamlit.io)
5. Sign in with GitHub
6. Click "New app"
7. Select your repository
8. Set main file: `app.py`
9. Click "Deploy" ✅

**Time**: 5 minutes  
**Cost**: FREE  
**URL**: `https://yourapp.streamlit.app`

---

### 2️⃣ Heroku (Easy - FREE tier available)

**Best for**: Production apps, custom domains, scalability

**Prerequisites**: 
- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Create Heroku account

**Steps**:
```bash
# Login to Heroku
heroku login

# Create new app
heroku create walmart-esg-dashboard

# Deploy
git init
git add .
git commit -m "Initial deployment"
heroku git:remote -a walmart-esg-dashboard
git push heroku main

# Open app
heroku open
```

**Time**: 10 minutes  
**Cost**: FREE (with limitations)  
**URL**: `https://walmart-esg-dashboard.herokuapp.com`

---

### 3️⃣ Docker (Flexible)

**Best for**: Consistent environments, any cloud platform

**Prerequisites**: Install Docker Desktop

**Steps**:
```bash
# Build image
docker build -t walmart-esg-dashboard .

# Run locally
docker run -p 8501:8501 walmart-esg-dashboard

# Access at http://localhost:8501
```

**Deploy to cloud**:
- Google Cloud Run
- AWS ECS
- Azure Container Instances
- DigitalOcean App Platform

**Time**: 15 minutes  
**Cost**: Varies by platform

---

### 4️⃣ AWS EC2 (Full Control)

**Best for**: Enterprise deployments, high traffic

**Steps**:
```bash
# SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install Python & dependencies
sudo apt update
sudo apt install python3-pip -y

# Clone repo (or upload files)
git clone https://github.com/yourusername/walmart-esg-dashboard.git
cd walmart-esg-dashboard

# Install requirements
pip3 install -r requirements.txt

# Run app (background)
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &
```

**Security Group**: Allow inbound traffic on port 8501

**Time**: 20 minutes  
**Cost**: ~$5-10/month (t2.micro)  
**URL**: `http://your-ec2-ip:8501`

---

### 5️⃣ Local Development

**Best for**: Testing, development

**Steps**:
```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

**Access**: `http://localhost:8501`

---

## 🔐 Environment Variables (Optional)

If you need to secure your dashboard:

Create `.streamlit/secrets.toml`:
```toml
[passwords]
admin_password = "your-secure-password"
```

Add authentication in `app.py`:
```python
import streamlit as st

def check_password():
    """Returns True if user enters correct password"""
    if "password_correct" not in st.session_state:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    return st.session_state["password_correct"]

def password_entered():
    """Checks whether a password entered is correct"""
    if st.session_state["password"] == st.secrets["passwords"]["admin_password"]:
        st.session_state["password_correct"] = True
        del st.session_state["password"]
    else:
        st.session_state["password_correct"] = False

if not check_password():
    st.stop()
```

---

## 📊 Performance Tips

### For Production:
1. **Enable caching**: Already implemented with `@st.cache_data`
2. **Optimize data loading**: Load data once, cache results
3. **Use CDN**: For static assets (images, CSS)
4. **Monitor**: Set up uptime monitoring (UptimeRobot, Pingdom)

### Scaling:
- Streamlit Cloud: Auto-scales
- Heroku: Upgrade dyno type
- Docker: Use orchestration (Kubernetes, Docker Swarm)
- EC2: Use load balancer + auto-scaling group

---

## 🐛 Common Issues

### Port already in use
```bash
# Kill process on port 8501
# Mac/Linux:
lsof -ti:8501 | xargs kill -9
# Windows:
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

### ModuleNotFoundError
```bash
pip install -r requirements.txt --upgrade
```

### Streamlit not opening
```bash
# Try different port
streamlit run app.py --server.port 8502
```

### Memory issues on free tier
- Reduce data size
- Optimize visualizations
- Use data sampling

---

## 📞 Support Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Forums](https://discuss.streamlit.io)
- [Heroku Dev Center](https://devcenter.heroku.com)
- [Docker Documentation](https://docs.docker.com)

---

## ✅ Pre-Deployment Checklist

- [ ] Test locally (`streamlit run app.py`)
- [ ] All dependencies in `requirements.txt`
- [ ] Remove sensitive data from code
- [ ] Update README with your info
- [ ] Test on mobile (responsive design)
- [ ] Set up monitoring/alerts
- [ ] Configure custom domain (optional)
- [ ] Enable HTTPS (automatic on Streamlit Cloud/Heroku)

---

**Ready to deploy? Pick a platform above and follow the steps! 🚀**
