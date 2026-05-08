---
name: cost-tracker
description: Use when someone asks to estimate API costs, track budget, design rate limiting, estimate token usage, calculate cost per generation, or optimize a portfolio project for the $5/month budget.
disable-model-invocation: true
argument-hint: [project-path]
---

# Cost Tracker Skill

## Purpose

Analyze a portfolio project's API usage patterns and design a rate limiting strategy to protect your $5/month budget. Produces cost estimates, rate limit configs, and real-time monitoring code.

---

## Inputs

- **Target project:** Directory path (e.g., `projects/sprint-machine/codebase`)
- **Files to scan:** Source code, API calls, LLM operations, package.json (for models), environment config
- **User input:** Expected usage patterns (# of users, frequency, peak usage)

---

## Step-by-Step Process

### Step 1: Analyze Codebase for API Usage

Read source code and identify all API/LLM operations:

**What to find:**
- API calls to Claude (chat, completion, batch)
- Model selection (Haiku 4.5, Sonnet 4.6, Opus 4.7)
- Input/output patterns (approximate token counts)
- Retry logic or loops that amplify calls
- Batch operations or bulk processing
- External service calls (storage, compute, webhooks)

**Output:** Inventory of all costly operations with estimated token range.

Example:
```
Operation: Generate Marketing Copy
- Model: Claude Haiku 4.5
- Input: User prompt (avg 150 tokens)
- Output: Generated copy (avg 200 tokens)
- Total per call: ~350 tokens
- Frequency: Once per user session
- Risk factors: None

Operation: PDF Processing
- Model: Claude Sonnet 4.6
- Input: Document chunks (avg 2000 tokens per chunk)
- Output: Summary (avg 300 tokens)
- Total per document: ~5000-8000 tokens (variable)
- Frequency: On demand
- Risk factors: Unbounded - large documents = large tokens
```

### Step 2: Ask About Usage Patterns

Ask the user these clarifying questions:

1. **Expected user base:** How many users per month?
2. **Usage frequency:** How often does the average user run generation?
3. **Peak usage:** What's your busiest day/week? (e.g., 10x normal traffic)
4. **User tiers (if applicable):** Free vs paid, different limits?
5. **Historical data:** Any existing usage data to calibrate?

Example response format:
```
Based on analysis:
- Primary operation: Generation (Haiku 4.5, ~350 tokens)
- Secondary operations: None detected

If 100 users run generation 2x/week:
- Monthly calls: 100 × 2 × 4.3 weeks = 860 calls
- Token cost: 860 × 350 = 301,000 tokens
- USD cost: $0.15/month (well within budget)

But if you have 1000 users or 20 calls/week/user, costs spike.

What's your actual target user count and usage frequency?
```

### Step 3: Calculate Token Costs

Using Haiku 4.5 as baseline (default for budget projects):

**Haiku 4.5 Pricing (as of 2024):**
- Input: $0.80 per 1M tokens
- Output: $4.00 per 1M tokens
- Average cost per 1000-token call: ~$0.0024

For each operation found:
1. Estimate avg input tokens
2. Estimate avg output tokens
3. Calculate cost per call: `(input_tokens × 0.80 + output_tokens × 4.00) / 1,000,000`
4. Multiply by expected calls/month
5. Calculate total monthly cost

**If Sonnet 4.6 is used for some operations:**
- Input: $3 per 1M tokens
- Output: $15 per 1M tokens
- Average cost per 1000-token call: ~$0.018

Clearly mark which operations use which model.

### Step 4: Calculate Budget Runway

Given $5/month budget:

```
Total monthly tokens available: $5 / $0.0024 per 1K tokens = ~2.08M tokens

With current operation mix (assuming Haiku):
- If average cost per call = $0.0024
- Budget supports: ~2080 calls/month

If users average 2 calls/week:
- 100 users × 2 calls/week × 4.3 weeks = 860 calls/month ✓ SAFE
- 1000 users × 2 calls/week = 8600 calls/month ✗ OVER BUDGET (4x)

Rate limit recommendation:
- Free users: 10 calls/week (580 calls/month for 1000 users = $1.39)
- Free users: 5 calls/week (290 calls/month for 1000 users = $0.69)
```

**Document:**
- Tokens consumed per operation
- Cost per call
- Cost per user (if tiered)
- Monthly burn rate at current projected usage
- How many calls fit in $5
- Recommended rate limits to stay within budget

### Step 5: Design Rate Limiting Strategy

Based on budget and usage analysis, design rate limits:

**Factors to consider:**
- Free vs paid users (if applicable)
- Peak traffic (don't design for average, design for peak)
- Competitive positioning (what are similar services doing?)
- User experience (limits should feel generous, not restrictive)
- Cost protection (hard limit before hitting $5)

**Example strategy for Sprint Machine:**
```
FREE TIER:
- Unauthenticated users: 3 generations/day
- After limit: Show popup "Upgrade to run unlimited, or git clone for free local use"

PAID TIER (if future):
- Authenticated free account: 20 generations/day
- Paid $5/month: Unlimited

PROTECTIONS:
- Rate limit per IP: 30 requests/minute (prevents bot abuse)
- Rate limit per authenticated user: 1 request/5 seconds (prevents rapid-fire)
- Concurrent request limit: 2 (prevents queue explosion)
```

### Step 6: Generate Outputs

Create three files in `projects/<name>/tasks/`:

#### File 1: `COST-ESTIMATE.md`

```markdown
# Cost Estimate - [Project Name]

**Budget:** $5/month
**Model:** Claude Haiku 4.5 (default) + [other models if used]
**Analysis Date:** [today]

---

## Operations Breakdown

### [Operation Name]
- **Model:** Haiku 4.5
- **Avg Input:** 150 tokens
- **Avg Output:** 200 tokens
- **Cost per call:** $0.00092
- **Frequency:** 1x per user session

### [Operation Name 2]
- **Model:** Sonnet 4.6
- **Avg Input:** 2000 tokens
- **Avg Output:** 300 tokens
- **Cost per call:** $0.0096
- **Frequency:** On demand (optional feature)

---

## Scenario Analysis

### Scenario A: Conservative (100 active users, 2 calls/week)
- Monthly calls: 860
- Haiku tokens: 301,000
- Cost: $0.15
- **Status: ✓ SAFE**

### Scenario B: Moderate (500 active users, 2 calls/week)
- Monthly calls: 4,300
- Haiku tokens: 1.5M
- Cost: $0.77
- **Status: ✓ SAFE**

### Scenario C: Growth (1000 active users, 3 calls/week)
- Monthly calls: 12,900
- Haiku tokens: 4.5M
- Cost: $2.31
- **Status: ⚠ APPROACHING LIMIT**

### Scenario D: Viral (5000 active users, 5 calls/week)
- Monthly calls: 108,500
- Haiku tokens: 38M
- Cost: $19.50
- **Status: ✗ WAY OVER BUDGET - Rate limiting required**

---

## Budget Math

**Available budget:** $5/month
**Cost per 1000 tokens:** $0.0024 (Haiku avg)
**Total tokens available:** ~2.08M tokens/month

At current usage: X calls = $Y cost
Remaining budget: $Z

---

## Rate Limit Recommendations

See RATE_LIMITS.env for implementation.

---

## Cost Explosion Risks

**Flagged risks (run `/security-audit` for full analysis):**
- [Risk 1]: Unbounded PDF processing (any file size accepted)
- [Risk 2]: Retry loop on API failure (could 2x-5x costs)
- [Risk 3]: No rate limiting on generation endpoint

---

## Monitoring

Use `cost-monitor.js` to track real costs vs estimates.
```

#### File 2: `RATE_LIMITS.env`

```env
# Rate Limiting Configuration
# Generated by cost-tracker skill
# Deploy these limits to protect $5/month budget

# Per-endpoint limits
GENERATION_ENDPOINT_LIMIT=3/day/ip
GENERATION_ENDPOINT_LIMIT_AUTH=10/day/user
GENERATION_CONCURRENT_MAX=2

# Burst protection (per-minute)
REQUESTS_PER_MINUTE=30

# Authenticated user limits (free tier)
FREE_TIER_DAILY_LIMIT=20
FREE_TIER_MONTHLY_LIMIT=400

# If offering paid tier
PAID_TIER_DAILY_LIMIT=unlimited
PAID_TIER_MONTHLY_LIMIT=unlimited

# Cost limits (hard stop)
MONTHLY_COST_LIMIT_CENTS=500

# Cleanup & monitoring
RESET_COUNTERS_DAILY=true
ALERT_AT_PERCENT_BUDGET=80
LOG_COST_EVENTS=true
```

#### File 3: `cost-monitor.js`

```javascript
/**
 * Cost Monitor - Track API usage and costs
 * Generated by cost-tracker skill
 * 
 * Usage:
 *   const monitor = require('./cost-monitor');
 *   monitor.trackCall('generation', { inputTokens: 150, outputTokens: 200 });
 *   console.log(monitor.getBudgetStatus());
 */

class CostMonitor {
  constructor() {
    this.calls = [];
    this.budgetCents = 500; // $5.00
    this.models = {
      'haiku': { inputCost: 0.80 / 1e6, outputCost: 4.00 / 1e6 },
      'sonnet': { inputCost: 3 / 1e6, outputCost: 15 / 1e6 },
      'opus': { inputCost: 15 / 1e6, outputCost: 60 / 1e6 }
    };
  }

  trackCall(operationName, { model = 'haiku', inputTokens, outputTokens, success = true }) {
    if (!success) return; // Don't charge for failed calls

    const costUsd = (inputTokens * this.models[model].inputCost) 
                  + (outputTokens * this.models[model].outputCost);

    this.calls.push({
      timestamp: new Date(),
      operation: operationName,
      model,
      inputTokens,
      outputTokens,
      costUsd,
      costCents: Math.round(costUsd * 100)
    });
  }

  getTotalCost() {
    return this.calls.reduce((sum, call) => sum + call.costCents, 0);
  }

  getBudgetStatus() {
    const spent = this.getTotalCost();
    const remaining = this.budgetCents - spent;
    const percentUsed = (spent / this.budgetCents) * 100;

    return {
      budgetCents: this.budgetCents,
      spentCents: spent,
      remainingCents: remaining,
      percentUsed: percentUsed.toFixed(1),
      status: remaining > 0 ? '✓ SAFE' : '✗ OVER BUDGET'
    };
  }

  getCallsSummary() {
    const byOperation = {};
    this.calls.forEach(call => {
      if (!byOperation[call.operation]) {
        byOperation[call.operation] = { count: 0, totalCost: 0 };
      }
      byOperation[call.operation].count++;
      byOperation[call.operation].totalCost += call.costCents;
    });
    return byOperation;
  }

  logStatus() {
    const status = this.getBudgetStatus();
    const summary = this.getCallsSummary();

    console.log('\n--- Cost Monitor Status ---');
    console.log(`Budget: $${(status.budgetCents / 100).toFixed(2)} | Spent: $${(status.spentCents / 100).toFixed(2)} | Remaining: $${(status.remainingCents / 100).toFixed(2)}`);
    console.log(`Usage: ${status.percentUsed}% [${status.status}]\n`);

    console.log('Operations:');
    Object.entries(summary).forEach(([op, data]) => {
      console.log(`  ${op}: ${data.count} calls, $${(data.totalCost / 100).toFixed(4)}`);
    });
  }
}

module.exports = new CostMonitor();
```

### Step 7: Flag Cost-Explosion Risks

Scan code for patterns that could spike costs:

- **Unbounded loops:** Automatic retry with exponential backoff
- **Large file uploads:** No max file size limits
- **Batch/bulk operations:** No request size limits
- **External integrations:** Webhook or event-driven calls that aren't throttled

Flag these as **COST SECURITY RISKS** and recommend running `/security-audit` for full analysis.

---

## Output

All files saved to: `projects/<project-name>/tasks/`
- `COST-ESTIMATE.md` - cost breakdown and budget scenarios
- `RATE_LIMITS.env` - rate limit configuration
- `cost-monitor.js` - monitoring code to track real usage

---

## Notes & Guardrails

- **Always assume worst case.** Budget for 2x-3x normal usage (peak, viral moments, bot attacks).
- **Rate limiting is a security feature.** Treat it like authentication/authorization.
- **Monitor early.** Add cost-monitor.js to your critical API endpoints on day 1, not when you hit $100 spend.
- **Haiku 4.5 is your baseline.** If you use Sonnet/Opus, costs multiply by ~7-10x.
- **Account for failures.** Retries, error handling, and edge cases consume tokens too.
- **User education.** When users hit rate limits, show them the value: "You've generated 10 pieces of content this week. Upgrade or run locally for unlimited access."

---

## Cost-Explosion Scenarios This Protects Against

✓ User accidentally calls API in a loop (rate limit stops it)
✓ Bot/attacker brute forces endpoint (IP rate limiting blocks it)
✓ Large batch file upload triggers expensive processing (file size limits + rate limits)
✓ Webhook retry storm from third-party (rate limiting prevents amplification)
✓ Concurrent request bomb (concurrent limit protects)
✓ Silent cost drift (cost-monitor.js logs every call)
