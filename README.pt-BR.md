# PostAImovel - SaaS Imobiliário

> [English](README.md) | **Português (BR)**

SaaS para corretores: posts de imóveis, CRM, portal do cliente e assistência com IA.

> **Visão geral do case** - o código de produção é privado (projeto de cliente). Esta página
> documenta o problema, a arquitetura e as decisões de engenharia.

## O problema

Corretores gastavam horas escrevendo posts de imóveis e gerenciando clientes entre
WhatsApp, anotações e planilhas - sem um modelo de assinatura que sustentasse o
produto como negócio.

## A solução

- **Posts assistidos por IA**: assistente de chat (Groq) ajuda o corretor a produzir
  posts e templates prontos pra publicação.
- **CRM com gestão de clientes** e agendamento de visitas.
- **Portal do cliente** para os clientes de cada corretor.
- **Gestão de assinaturas via webhooks do Hotmart**: eventos de pagamento ativam,
  suspendem ou cancelam contas automaticamente - zero operação manual de cobrança.
- **Painel admin** com dashboard, gestão de usuários e exportação CSV.

## Arquitetura

```
Navegador do corretor --> [ Frontend React ] --> [ API Node.js ] --> MySQL
                                                      |
                       Hotmart --- webhooks --------->+<------- Groq (chat IA)
                                                      |
                                               [ Painel admin ]
```

Roda em VPS DigitalOcean atrás de Nginx com PM2.

## Stack

| Camada | Tecnologia |
|---|---|
| Frontend | React |
| Backend | Node.js |
| Banco | MySQL |
| IA | Groq |
| Cobrança | Webhooks Hotmart |
| Infra | DigitalOcean, Nginx, PM2, Docker |

## Notas de engenharia

- **Cobrança como automação**: o ciclo de vida da assinatura é 100% orientado a
  eventos do provedor de pagamento - o sistema nunca depende de humano conferindo
  pagamento.
- **Multi-tenant desde o início**: clientes e dados de cada corretor são isolados
  na camada de aplicação.

## Status

Entregue e em produção. Engenheiro único: full stack e infraestrutura.
