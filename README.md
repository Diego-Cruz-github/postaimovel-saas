# PostAImovel - Real Estate SaaS

SaaS platform for real estate listings, designed for realtors. Includes CRM, AI chat, client portal, and Hotmart subscription management.

## Stack

- **Backend:** Node.js, React
- **Database:** MySQL
- **AI:** Groq (chat assistant for realtors)
- **Payments:** Hotmart webhooks (subscription management)
- **Infra:** Nginx, PM2, DigitalOcean VPS, Docker
- **Admin:** Custom admin panel with dashboard, user management, CSV export

## Features

- AI-powered chat for property listing assistance
- CRM with client management and visit scheduling
- Hotmart webhook integration for automatic user activation/deactivation
- Admin panel: dashboard, financials, user management, email templates
- Property listing templates
- Client portal
- Isolated deployment (separate database, user, and .env per app)

## Scripts

- `scripts/health_check.py` - Service health monitoring
- `scripts/webhook_test.py` - Hotmart webhook validation

---

*Private repository - client project*
