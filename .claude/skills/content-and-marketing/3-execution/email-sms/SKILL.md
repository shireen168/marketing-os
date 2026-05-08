---
name: marketing-os-email-sms-workflow
description: Design and automate email/SMS nurture sequences for lead conversion and customer retention
type: marketing
---

# Marketing-OS: Email/SMS Workflow Skill

Build automation sequences that move leads from cold to warm to convert. Turns customer segments into drip campaigns with timing, messaging, and conversion hooks.

## Use When

- Launching new product (launch sequence)
- Have cold email list (prospecting sequence)
- Need cart abandonment recovery (urgency sequence)
- Building customer re-engagement (win-back sequence)
- Nurturing existing customers (retention/upsell sequence)

## How to Use

**Input:** Segment (cold leads, cart abandoners, existing customers), goal (convert, retain, expand), product/offer

**Output:** Email + SMS sequence template with copy, timing, hooks, and CTA

## Templates

### Template 1: Product Launch Sequence (Email + SMS)

```
PROMPT:
I'm launching [PRODUCT/OFFER] to [SEGMENT] and need an email + SMS sequence.

Product: [what you're selling]
Target segment: [cold audience / warm list / existing customers]
Launch date: [DATE]
Conversion goal: [immediate purchase / sign-up / trial / consultation]
Price point: [cost to customer]
Main benefit: [what problem does this solve?]
Social proof: [testimonials / case studies / metrics available?]

Generate a 5-email + 3-SMS sequence:

Timing:
- Email 1: Day 0 (launch announcement)
- SMS 1: Day 1 (reminder, urgency)
- Email 2: Day 2 (social proof)
- Email 3: Day 4 (fear of missing out)
- SMS 2: Day 5 (last chance)
- Email 4: Day 6 (objection handling)
- Email 5: Day 7 (final push)
- SMS 3: Day 7 (hard close)

For each message, provide:
1. Subject line / SMS preview
2. Hook (why they should read/open)
3. Body copy (problem > solution > product)
4. Social proof (if available)
5. CTA (clear action)
6. Signature

Return as JSON with email_1, sms_1, email_2, etc.
```

### Template 2: Cart Abandonment Recovery (Email + SMS)

```
PROMPT:
Customer abandoned cart with [ITEMS] worth $[AMOUNT]. I need to recover this sale.

Items in cart: [product names]
Cart value: $[amount]
Discount available: [yes/no, amount if yes]
Urgency: [stock limited? sale ending soon?]
Shipping policy: [free? standard cost?]

Generate a 3-email + 1-SMS recovery sequence (24-48 hours):

Timing:
- Email 1: 1 hour after abandonment (soft reminder)
- Email 2: 24 hours (add urgency)
- SMS: 36 hours (last chance)
- Email 3: 48 hours (final offer)

Each should:
1. Acknowledge what's in cart (show product image/details)
2. Remove friction (address shipping cost / payment concerns)
3. Add incentive (discount / free shipping / bonus if provided)
4. Create urgency (limited stock / sale ending)
5. One clear CTA

Return as JSON.
```

### Template 3: Win-Back Sequence (Re-engagement)

```
PROMPT:
I have [NUMBER] inactive customers (haven't purchased in [TIME PERIOD]). I want to win them back.

Customer segment: [who they are, what they bought before]
Time since last purchase: [30/60/90 days]
Product/offer to re-engage: [new product / discount / content]
Why they left: [I have data or I'm guessing? what reason?]

Generate a 4-email sequence over 14 days:

Message 1 (Day 1): "We miss you" emotional hook
Message 2 (Day 5): Show what's new (product updates / new features / new inventory)
Message 3 (Day 10): Social proof (other customers doing X)
Message 4 (Day 14): Final offer (special discount or exclusive access)

Each email should:
1. Acknowledge their past purchase (build relationship)
2. Show what's changed (new value)
3. Remove friction (why they left? address it)
4. Offer incentive (reason to come back)

Return as JSON.
```

## Real Examples

### Sunny Homemade Example: Product Launch Sequence

**Product:** Bak Zang (new product launch)
**Segment:** Existing collagen customer list (warm audience)
**Goal:** Get 20% of list to try bak zang in first week

**Sequence Output:**

```json
{
  "sequence_name": "Sunny Homemade - Bak Zang Launch",
  "segment": "Existing collagen customers",
  "duration": "7 days",
  "goal": "20% trial purchase",
  "messages": [
    {
      "day": 0,
      "type": "email",
      "subject": "One ingredient. A thousand uses. (New from Sunny Homemade)",
      "preview": "The morning staple your Ah Ma knew. Now, in a jar.",
      "hook": "Nostalgia + curiosity + tradition",
      "body": "You trusted us with your collagen. Now we want to show you something we've been perfecting for months. Bak zang. A single ingredient that transforms breakfast, lunch, dinner... and even snacks. 11 ways to use one jar. And it pairs beautifully with your collagen. Click below to see what Ah Ma knew.",
      "cta": "Discover Bak Zang",
      "cta_link": "[product-page-url]"
    },
    {
      "day": 1,
      "type": "sms",
      "preview": "Bak zang + collagen = morning power combo. Limited first batch. Shop now > [link]",
      "hook": "Urgency + pairing benefit"
    },
    {
      "day": 2,
      "type": "email",
      "subject": "11 ways to use bak zang (+ 1 surprising pairing)",
      "body": "Breakfast: Nasi lemak, toast, oatmeal. Lunch: Tteokbokki, dipping sauce, sandwich. Dinner: Stir-fry seasoning, rice mix, soup base. Snack: Cracker dip, egg dip, butter bread. Each one takes 30 seconds to prep. Here's the surprising pairing: Mix bak zang + collagen into a morning smoothie. Two years of customer feedback in one recipe.",
      "social_proof": "Testimonial: 'I've tried 5 brands. This tastes like home.' — Patricia, KL",
      "cta": "See the 11 recipes"
    },
    {
      "day": 4,
      "type": "email",
      "subject": "Running low on first batch. Last chance this week.",
      "body": "We make bak zang in small batches. This first run (100 jars) is almost gone. After this, the next batch won't be ready until June 15. If you want to try it while collagen is still fresh in your mind, this is the window.",
      "cta": "Secure your jar now",
      "urgency_note": "Limited stock, next batch 4 weeks away"
    },
    {
      "day": 5,
      "type": "sms",
      "preview": "Final 24 hours. Bak zang first batch closing orders tomorrow. [link]",
      "urgency": "Hard close"
    },
    {
      "day": 6,
      "type": "email",
      "subject": "Objection: 'Is bak zang worth it if I already have [other brand]?'",
      "body": "Fair question. Here's what's different: We only use 1 ingredient (no fillers). We grind it fresh (you taste the difference). We pair it with collagen because we know your routine. Other brands? They're designed for generic cooking. This is designed for the morning ritual you already trust us with.",
      "cta": "Compare (full specs)"
    },
    {
      "day": 7,
      "type": "email",
      "subject": "Final 12 hours. Closing at midnight.",
      "body": "First batch closes tonight. Next available: June 15. This is the hard deadline.",
      "cta": "Get bak zang"
    },
    {
      "day": 7,
      "type": "sms",
      "preview": "Final 2 hours. Bak zang closes tonight. Last chance. [link]",
      "urgency": "Hard close, time-specific"
    }
  ],
  "conversion_tracking": [
    "Email clicks",
    "SMS clicks",
    "Add-to-cart events",
    "Completed orders",
    "Pairing rate (collagen + bak zang in same order)"
  ],
  "follow_up_sequence": "If converted: thank you email + request review. If not: win-back sequence (14 days later)"
}
```

### Generic Example: SaaS Free-to-Paid Conversion

**Product:** Project management tool
**Segment:** Free trial users (day 14, didn't upgrade)
**Goal:** Convert 15% to paid plan

**Email Sequence:**

```json
{
  "email_1": {
    "timing": "Day 14 (trial ending tomorrow)",
    "subject": "Your trial ends tomorrow. Here's what you'd lose.",
    "body": "[Name], you've created [X] projects, [Y] tasks. Your team has saved [Z] hours using [Product]. Tomorrow, your trial ends. If you don't upgrade, you'll lose access to: unlimited team members, integrations with Slack/GitHub, priority support. The projects you created will be read-only.",
    "cta": "Upgrade to Pro now"
  },
  "email_2": {
    "timing": "Day 15 (trial ended, account now limited)",
    "subject": "Your account is now limited. Upgrade to restore access.",
    "body": "Your trial ended. [Product] is now in read-only mode. Your data is safe, but you can't add new tasks or projects. Upgrade to Pro to restore full access. Pro users report 6+ hours saved per week.",
    "cta": "Restore full access"
  },
  "email_3": {
    "timing": "Day 18 (3 days later, social proof)",
    "subject": "See what 2,000+ teams are doing with [Product] Pro",
    "body": "Context: [Testimonial] 'Switched from [competitor]. Best $30/month we spend.' — Marcus, [Company]. [Testimonial] 'Freed up 10 hours/week.' — Priya, [Company]. Your team can be next.",
    "cta": "See pricing"
  }
}
```

## Workflow Integration

**Timeline:**
1. **Define segment:** Who are you reaching (cold, warm, customer)?
2. **Define goal:** What action do you want (purchase, sign-up, retention)?
3. **Run this skill:** Generate sequence template
4. **Copy adaptation:** Customize for your brand voice
5. **Set up automation:** Connect to email provider (Mailchimp, ConvertKit, etc.) + SMS (Twilio, etc.)
6. **Schedule sends:** Set timing in automation tool
7. **Monitor metrics:** Track open rate, click rate, conversion rate
8. **Iterate:** Update copy based on performance

## Pro Tips

**Sequence design:**
- Cold audience: longer sequence (5-7 emails over 2-3 weeks, build trust)
- Warm audience: medium sequence (3-5 emails over 1-2 weeks, quick conversion)
- Existing customers: shorter sequence (2-3 emails over 1 week, loyal audience)

**Email + SMS mix:**
- Email: detailed copy, narrative, social proof
- SMS: urgency, time-sensitive, call-to-action reinforcement
- Timing: Email before SMS (email educates, SMS pushes)

**Sunny Homemade specific:**
- Bilingual subject lines (Mandarin + English)
- Emotional narrative (tradition, health, family)
- Product pairing (collagen + bak zang together)
- Urgency hook (limited batches, seasonal availability)

**Conversion optimization:**
- Subject line: [Curiosity + benefit] (avoid all-caps, spammy language)
- Hook: First 50 words matter most (mobile preview)
- CTA: Use color contrast, 1-2 per email max
- Objection handling: Address why they don't want it
- Final push: Time + scarcity (this week, limited stock)

## Output Format

Handoff to email/SMS provider should include:
- Email template (HTML or plain text)
- SMS text (160 characters max, shortened link)
- Timing schedule (day by day)
- Segmentation rules (who gets this sequence)
- Conversion tracking pixel/event name
- A/B testing variants (subject line, CTA copy)
- Metrics dashboard setup (what to measure)
