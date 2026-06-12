# PostAImovel - Real Estate SaaS
> **English** | [Português (BR)](README.pt-BR.md)

SaaS for realtors: listing posts, CRM, client portal and AI assistance.

> **Case overview** - the production code is private (client engagement). This page
> documents the problem, the architecture and the engineering decisions.

## The problem

Realtors spent hours writing listing posts and managing clients across
WhatsApp, notes and spreadsheets - with no subscription model to support the
product as a business.

## The solution

- **AI-assisted listing posts**: chat assistant (Groq) helps realtors produce
  publication-ready property posts and templates.
- **CRM with client management** and visit scheduling.
- **Client portal** for each realtor's customers.
- **Subscription management via Hotmart webhooks**: payment events activate,
  suspend or cancel accounts automatically - zero manual billing operations.
- **Admin panel** with dashboard, user management and CSV export.

## Architecture

```
Realtor browser --> [ React frontend ] --> [ Node.js API ] --> MySQL
                                               |
                  Hotmart --- webhooks ------->+<------- Groq (AI chat)
                                               |
                                        [ Admin panel ]
```

Runs on a DigitalOcean VPS behind Nginx with PM2.

## Stack

| Layer | Technology |
|---|---|
| Frontend | React |
| Backend | Node.js |
| Database | MySQL |
| AI | Groq |
| Billing | Hotmart webhooks |
| Infra | DigitalOcean, Nginx, PM2, Docker |

## Engineering notes

- **Billing as automation**: subscription lifecycle is fully event-driven from
  the payment provider - the system never depends on a human checking payments.
- **Multi-tenant from day one**: each realtor's clients and data are isolated
  at the application layer.

## Status

Delivered and in production. Sole engineer: full stack and infrastructure.
