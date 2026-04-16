# Environment Variables

Environment variables should be used for configuration and secrets.

---

## Environment Files

Next.js commonly uses:

.env  
.env.local  
.env.production

Sensitive values should never be hard-coded.

---

## Client vs Server Variables

Variables prefixed with `NEXT_PUBLIC_` are exposed to the browser.

Example:

NEXT_PUBLIC_API_URL

Do not expose secrets with this prefix.

---

## Security Rule

Never expose sensitive data such as:

- database credentials
- API keys
- service tokens
- JWT signing secrets

to client-side code.
