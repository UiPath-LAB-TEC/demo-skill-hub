---
name: customer-stack-research
description: "Research a customer's enterprise technology stack from public and user-provided evidence. Use when Codex needs to infer likely cloud providers, workflow tools, automation tools, process orchestration tools, API integration or iPaaS platforms, code bases, frameworks, open-source technologies, or engineering practices from websites, browser/network clues, public searches, job postings, docs, blogs, forums, package evidence, or customer-provided artifacts."
metadata:
  author: "James Dickson"
  version: "1.0.0"
  ownerEmail: "james.dickson@uipath.com"
  changeSummary: "Initial customer technology stack research workflow."
  isBreaking: false
  category: "Sales Engineering"
  tags:
    - customer-research
    - technology-stack
    - sales-engineering
    - discovery
  platforms:
    - OpenAI
  businessUseCases:
    - "Prepare evidence-based customer technology stack summaries"
    - "Support demo discovery and account research"
---

# Customer Stack Research

Research the customer's likely enterprise technology stack from defensible evidence. Produce a useful account-research brief without overstating what public signals prove.

## Boundaries

- Use only public sources and user-provided evidence. Do not use credentialed systems, private tenant data, leaked material, paywall bypasses, or content the user is not allowed to share.
- Treat normal website browsing and browser DevTools inspection as allowed when the user asks for site inspection. Do not run vulnerability scans, directory brute force, credential tests, or high-volume scraping.
- Separate observed facts from inference. Never convert "a job posting mentions Azure" into "the company runs on Azure" without corroboration.
- Cite public sources with links. Label user-provided files, screenshots, notes, or HAR captures as user-provided evidence rather than public facts.
- Prefer current first-party evidence. Mark older, third-party, or single-signal evidence as lower confidence.

## Research Workflow

1. Define scope.
   - Identify the customer name, domain, relevant subsidiary or region, and whether the output is for sales discovery, demo tailoring, competitive research, or implementation planning.
   - If the user did not specify scope, use the main corporate site and current public evidence, then state that assumption.

2. Collect first-party public signals.
   - Inspect the corporate site, product pages, developer/docs portals, trust/security pages, privacy/subprocessor lists, status pages, customer support docs, careers pages, press releases, and engineering blogs.
   - Use Chrome DevTools or a HAR from normal page loads when website implementation clues matter. Look for API hostnames, CDN providers, analytics tags, auth endpoints, SDK names, GraphQL/REST clues, static bundle names, public environment labels, and third-party service domains.
   - Keep website clues scoped: they often describe the public web property, not the customer's internal enterprise stack.

3. Search public external sources.
   - Use targeted searches across vendor case studies, engineering blogs, documentation, public forums, conference talks, job postings, job titles, GitHub organizations, package registries, Docker images, Terraform modules, Helm charts, npm/PyPI/Maven packages, and public issue trackers.
   - Favor searches that combine the customer name or domain with specific technology families: cloud, RPA, workflow, BPMN, orchestration, iPaaS, API gateway, ERP, CRM, data platform, observability, CI/CD, and major frameworks.

4. Inspect job and people signals carefully.
   - Use official job postings, public job boards, and public profile titles to identify technologies the customer hires for.
   - Record role, location, business unit, posting date, and whether the technology is required, preferred, or merely adjacent.
   - Treat hiring signals as "likely used or being adopted by that team," not enterprise-wide proof.

5. Inspect code and package evidence.
   - For customer-owned public repos, examine manifests and infrastructure files such as `package.json`, lockfiles, `requirements.txt`, `pyproject.toml`, `pom.xml`, `Dockerfile`, `docker-compose.yml`, Terraform providers, GitHub Actions, Helm charts, and README badges.
   - Check ownership, repo activity, dates, archived status, and whether the code is sample/demo/open-source rather than production.

6. Build the stack map.
   - Cover likely cloud providers, hosting/CDN, identity/auth, data/AI platforms, workflow tools, automation/RPA tools, process orchestration tools, API integration/iPaaS tools, code bases, languages, backend/frontend frameworks, databases, messaging, DevOps/CI/CD, observability, security, CRM/ERP, and notable open-source technologies.
   - Include "not established" for categories with no defensible evidence instead of guessing.

## Evidence Quality

Use these confidence labels:

- `Observed`: directly visible in first-party public sources, customer-owned public code, user-provided artifacts, or normal browser/network evidence.
- `Likely`: supported by multiple independent signals, or by one strong first-party signal with a clear current date and relevant scope.
- `Possible`: supported by one weak, old, indirect, or team-specific signal.
- `Not established`: no reliable evidence found, or evidence conflicts too much to infer.

Rank evidence roughly as:

- Strong: official customer docs/blogs/job postings, customer-owned repos, user-provided artifacts, HAR/network evidence from the customer's own site, dated vendor case studies naming the customer.
- Medium: repeated current job-board copies, employee-authored public talks or posts, public package metadata tied to an owned org, reputable third-party technical writeups.
- Weak: anonymous forums, generic technology-profile sites, old postings, single unmaintained repos, analytics tags, CDN-only clues, or technologies mentioned without clear customer ownership.

When evidence conflicts, prefer current first-party sources and explain the conflict. Do not force a single answer.

## Output Format

Return a concise research brief:

1. Scope and assumptions.
2. Key findings by technology category, with each item labeled `Observed`, `Likely`, `Possible`, or `Not established`.
3. Evidence table with source, date or recency when available, observed signal, stack category, and confidence.
4. Inferences and rationale, explicitly separated from facts.
5. Unknowns and customer validation questions, especially for low-confidence categories that matter to the demo or sales motion.

Avoid unsupported claims, absolute language, and vendor recommendations that are not grounded in the evidence.
