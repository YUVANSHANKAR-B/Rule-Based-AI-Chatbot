# Production Deployment Guide

This guide explains how to deploy the Rule-Based AI Chatbot to production.

## Prerequisites

- GitHub account
- Production deployment platform (Heroku, PythonAnywhere, AWS, etc.)
- Command-line tools installed

## Deployment Options

### Option 1: Heroku (Recommended for Beginners)

**Benefits:**
- Free tier available
- Easy deployment from GitHub
- Automatic scaling
- Built-in monitoring

**Steps:**

1. **Create Heroku Account**
   - Go to https://www.heroku.com
   - Sign up and verify email

2. **Install Heroku CLI**
   ```bash
   # Windows (via npm or download)
   npm install -g heroku
   
   # macOS (via Homebrew)
   brew tap heroku/brew && brew install heroku
   ```

3. **Login to Heroku**
   ```bash
   heroku login
   ```

4. **Create Heroku App**
   ```bash
   heroku create your-chatbot-name
   ```

5. **Deploy from GitHub**
   ```bash
   git push heroku main
   ```

6. **View Logs**
   ```bash
   heroku logs --tail
   ```

7. **Access Your App**
   ```
   https://your-chatbot-name.herokuapp.com
   ```

### Option 2: PythonAnywhere (Great for Python)

**Benefits:**
- Python-focused hosting
- Easy web-based setup
- Suitable for learning

**Steps:**

1. Go to https://www.pythonanywhere.com
2. Create account and verify
3. Use "Web" to create Flask app
4. Upload your files
5. Configure WSGI file
6. Reload app

### Option 3: AWS (For Enterprise Scale)

**Benefits:**
- Highly scalable
- Production-grade
- More complex setup

**Methods:**
- AWS Elastic Beanstalk
- AWS Lambda + API Gateway
- EC2 instances

### Option 4: Docker + Any Cloud

**Build Docker image:**
```bash
docker build -t rule-based-chatbot .
docker run -p 5000:5000 rule-based-chatbot
```

**Deploy to:**
- DigitalOcean
- Google Cloud Run
- AWS ECR

## Production Checklist

- [ ] **Security**
  - [ ] Set strong `SECRET_KEY` environment variable
  - [ ] Enable HTTPS only (`SESSION_COOKIE_SECURE=True`)
  - [ ] Use environment variables for secrets
  - [ ] Keep dependencies updated

- [ ] **Performance**
  - [ ] Use production WSGI server (gunicorn)
  - [ ] Enable caching headers
  - [ ] Implement rate limiting
  - [ ] Monitor response times

- [ ] **Monitoring**
  - [ ] Set up error tracking (Sentry)
  - [ ] Enable application logging
  - [ ] Configure alerting
  - [ ] Monitor uptime

- [ ] **Maintenance**
  - [ ] Automated backups
  - [ ] Regular dependency updates
  - [ ] Security patches
  - [ ] Performance optimization

## Environment Variables

Create `.env` file (do NOT commit to git):

```env
FLASK_ENV=production
SECRET_KEY=generate-a-strong-random-key-here
```

Or set via deployment platform:
- Heroku: `heroku config:set SECRET_KEY=your-key`
- PythonAnywhere: Web UI
- AWS: Systems Manager Parameter Store

## Monitoring & Logging

**Sentry Integration:**
```python
import sentry_sdk
sentry_sdk.init("your-sentry-dsn")
```

**Application Logging:**
```python
import logging
logging.basicConfig(level=logging.INFO)
```

## Scaling Strategies

1. **Database**: Add PostgreSQL for data persistence
2. **Caching**: Implement Redis for session caching
3. **Load Balancing**: Use multiple app instances
4. **CDN**: Cache static files with CloudFlare/Akamai

## Troubleshooting

**App won't start:**
```bash
heroku logs --tail
```

**Out of memory:**
- Upgrade dyno type
- Optimize code
- Clear cache

**Slow responses:**
- Check slow queries
- Enable caching
- Optimize database

## Cost Estimation

| Platform | Free | Paid |
|----------|------|------|
| Heroku | $0-50/month | $7-25+/month |
| PythonAnywhere | Limited | $5-35/month |
| AWS | Free tier | $10-100+/month |
| DigitalOcean | - | $5-12+/month |

## Next Steps

1. Choose deployment platform
2. Set up environment variables
3. Deploy and test
4. Monitor performance
5. Set up CI/CD pipeline
6. Configure monitoring & alerts

## Resources

- [Heroku Documentation](https://devcenter.heroku.com/)
- [Flask Deployment Guide](https://flask.palletsprojects.com/deployment/)
- [PythonAnywhere Docs](https://help.pythonanywhere.com/)
- [GitHub Actions](https://github.com/features/actions)

## Support

For deployment issues:
1. Check platform-specific documentation
2. Review application logs
3. Test locally first
4. Post on Stack Overflow or platform forums

---

**Remember:** Always test in staging before production deployment!
