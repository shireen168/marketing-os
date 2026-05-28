# Phase 4: Build (Day 5-7)

**Goal:** Code + security. Build the product with architectural discipline.

**Skills:** 5  
**Outcome:** Implementation complete, security audit passed, code reviewed  
**Start:** `/context-restore` (Day 6 morning)

---

## Skill 22: `/context-restore`
**Resume from Day 5 checkpoint (design + architecture locked).**

**Next:** Skill 23 (`/cso`)

---

## Skill 23: `/cso`

**Chief Strategist thinking. Data privacy strategy (HIPAA/GDPR).**
- Question: How do we handle sleep data legally + ethically?
- Considerations: Encryption, user consent, data deletion, third-party sharing
- Non-negotiable: Health data = liability
- Output: Privacy strategy + compliance checklist

**Next:** Skill 24 (`/guard`)

---

## Skill 24: `/guard`

**Security + compliance audit.**
- Check: HIPAA readiness, GDPR compliance, data encryption, API security
- Verify: Authentication, rate limiting, data access logs
- Test: Can users delete their data? Is it actually deleted?
- Output: Security audit report + remediation checklist

**Next:** Skill 25 (`/setup-deploy`)

---

## Skill 25: `/setup-deploy`

**Configure CI/CD pipeline. GitHub Actions automation.**
- Pipeline: Push to main → run tests → deploy to staging → manual approve → deploy to prod
- Automation: Every deploy is consistent, humans don't manually deploy
- Monitoring: Alert on deploy failures
- Output: Automated deployment pipeline ready

**Next:** Skill 26 (`/scrape`)

---

## Skill 26: `/scrape`

**Gather competitive feature data.**
- Target: Oura app screenshots, Apple Health interface, Whoop insights
- Question: What data is shown first? What's secondary? What's hidden?
- Use: Competitive intelligence for feature prioritization
- Output: Competitive feature inventory + UX patterns

**Next:** Skill 27 (`/review`)

---

## Skill 27: `/review`

**Code review on implementation.**
- Review: Sleep tracking algorithm correctness
- Check: Edge cases (DST changes, timezone changes), test coverage
- Goal: Catch bugs before they ship
- Output: Code approved or remediation needed

**Next:** Phase 5 (Testing)

---

## What You Have Now

✓ Privacy strategy defined (legally sound)  
✓ Security audit passed (health data protected)  
✓ CI/CD automated (consistent deploys)  
✓ Competitive analysis done (know your UX patterns)  
✓ Code reviewed (no obvious bugs)  
✓ Ready for testing

---

## Next Phase

→ [**Phase 5: Test (Day 7-8)**](./phase-5-test.md)

