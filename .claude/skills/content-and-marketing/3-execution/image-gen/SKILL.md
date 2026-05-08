# Skill: /image-gen (Marketing-OS Edition)

**Trigger:** "Generate marketing images using DALL-E, Midjourney, or Stable Diffusion"

**Purpose:** Create high-quality marketing visuals from text prompts. Supports product photography, ad creatives, UI mockups, illustrations, and brand assets using multiple image generation APIs.

---

## What It Does

1. Takes a text prompt describing the desired image
2. Routes to the appropriate API (DALL-E 3, Midjourney, Stable Diffusion, or Flux)
3. Generates image(s) with specified dimensions, style, and quality settings
4. Returns download URL(s) or base64 encoded images
5. Optionally upscales, edits (inpainting/outpainting), or creates variations

---

## Supported APIs & Models

| API | Model | Strengths | Best For | Cost |
|-----|-------|-----------|----------|------|
| **OpenAI** | DALL-E 3 | Photorealism, prompt understanding, safety | Product photos, ads, realistic scenes | $0.08 (1024×1024) |
| **Midjourney** | v6 | Artistic quality, unique aesthetics, fast | Illustrations, creative designs, posters | $0.06-0.12 per image |
| **Stable Diffusion** | SDXL 1.0 | Open source, customizable, cost-effective | Batch generation, fine-tuning | $0.02-0.04 per image |
| **Flux** | Dev / Pro | Cutting edge, superior quality | Premium campaigns, hero images | $0.10 per image |

---

## How to Use

### Setup (one-time)

```bash
# Add API keys to .env:
export OPENAI_API_KEY="sk-..."
export MIDJOURNEY_API_KEY="mj_..."
export STABILITY_API_KEY="sk-..."
export REPLICATE_API_KEY="..."  # For Stable Diffusion / Flux
```

### Quick Start

**Trigger:**
```
/image-gen

Prompt: "A minimalist product shot of a glass jar of ginger paste on a marble countertop, 
warm studio lighting, 9:16 aspect ratio, professional food photography"

API: DALL-E 3 (or Midjourney, Stable Diffusion)
```

**Output:**
- Image URL (or base64 data)
- Generation time
- Token usage / cost
- Metadata (dimensions, model, seed for reproducibility)

---

## Prompt Templates by Use Case

### 1. E-Commerce Product Photography

**Template:**
```
A professional product shot of [PRODUCT] on [SURFACE], [LIGHTING], [PROPS], 
[ANGLE], [STYLE], [RESOLUTION], [ASPECT_RATIO]
```

**Example (Sunny Homemade):**
```
A professional product shot of a glass jar of golden ginger paste on a white marble 
countertop with fresh ginger root beside it, warm studio lighting, 45-degree angle, 
minimal aesthetic, sharp focus, shallow depth of field, 1024x1280, 9:16 aspect ratio, 
food photography, professional, high resolution
```

**Best API:** DALL-E 3 or Midjourney (photorealism)

---

### 2. Ad Creative (Cold Audience)

**Template:**
```
[EMOTIONAL_HOOK] design showing [PRODUCT] solving [PROBLEM], 
[AUDIENCE], [COLOR_SCHEME], [STYLE], [RESOLUTION], 9:16 or 16:9
```

**Example:**
```
A vibrant, energetic design showing a woman in an office drinking warm ginger tea 
from a ceramic cup, looking relieved and focused, cold fluorescent office lighting 
in background, warm amber tea in foreground, wellness aesthetic, bright colors, 
modern minimalist design, 1080x1920, 9:16 aspect ratio, social media ad, 
professional illustration
```

**Best API:** Midjourney (creative aesthetic)

---

### 3. UI & Social Media Mockups

**Template:**
```
A clean [PLATFORM] screenshot mockup showing [CONTENT], [BRAND_COLORS], 
[TYPOGRAPHY], [LAYOUT], [STYLE], [RESOLUTION]
```

**Example:**
```
A clean Instagram feed mockup showing 3 posts for a homemade food brand:
- Post 1: Product shot of ginger paste jar
- Post 2: Before-after wellness transformation
- Post 3: Recipe video thumbnail

Brand colors: warm earth tones (amber, terracotta, cream), clean sans-serif typography,
minimalist layout with spacious padding, modern aesthetic, 1080x1350 per post,
professional product mockup, high resolution
```

**Best API:** Stable Diffusion or DALL-E 3 (consistency)

---

### 4. Hero Image / Poster Design

**Template:**
```
A professional hero image for [BRAND/CAMPAIGN] featuring [MAIN_ELEMENT], 
[SECONDARY_ELEMENTS], [COLOR_PALETTE], [MOOD], [COMPOSITION], [STYLE], 
[RESOLUTION], [ASPECT_RATIO]
```

**Example (Marketing-OS):**
```
A professional hero image for Marketing-OS system featuring a minimalist 
dashboard showing content calendars, analytics graphs, and team workflows in harmony.
Golden accents (#C9A96E) on dark background (#0A0A0A), secondary colors: indigo (#6366F1), 
confident and strategic mood, centered composition with floating UI elements, 
modern tech aesthetic, sleek and premium, 1920x1080, 16:9 aspect ratio, 
high resolution, professional product marketing image
```

**Best API:** Flux or Midjourney (quality and detail)

---

### 5. Illustration & Icon Design

**Template:**
```
A [STYLE] illustration of [SUBJECT], [COLOR_SCHEME], [MOOD], [COMPOSITION], 
[AESTHETIC], [RESOLUTION]
```

**Example:**
```
A flat design illustration of a ginger root with leaves, warm terracotta and cream 
color palette, wellness and natural mood, centered composition, vector illustration style,
playful yet professional, 512x512, high resolution, icon design, minimalist
```

**Best API:** Stable Diffusion or Midjourney (artistic control)

---

## Integration with Marketing-OS (SCEO Framework)

### Layer 3 (E: Execution) — Image Generation

**Composed with:**
- `/content-calendar-strategy` (defines what images needed)
- `/copy-gen` (writes ad copy to pair with visuals)
- `/social-scheduling` (posts generated images)
- `/infographic` (complements data visualization)
- `/video-gen` (creates thumbnails for videos)

### Typical SCEO Flow

1. **S (Strategic):** Market research identifies visual needs
2. **C (Creative):** Content calendar defines image specs and prompts
3. **E (Execution):** Image-gen creates assets, copy-gen writes captions, social-scheduling publishes
4. **O (Optimization):** Track which images drive highest engagement

### Sunny Homemade Example

**Weekly Content Calendar Usage:**
- Monday: Product shot (DALL-E 3)
- Wednesday: Ad creative (Midjourney)
- Friday: Social mockup (Stable Diffusion)

---

## Output Format

### Default: URL Response
```json
{
  "url": "https://cdn.openai.com/...",
  "model": "dall-e-3",
  "dimensions": "1024x1024",
  "generation_time": "8.2s",
  "cost": "$0.08",
  "revised_prompt": "..."  // For DALL-E safety refinements
}
```

### Alternative: Base64 Data
```json
{
  "image_data": "data:image/png;base64,iVBORw0KGgo...",
  "format": "png",
  "size_kb": 245
}
```

### Batch Mode (Multiple Images)
```json
{
  "images": [
    { "url": "...", "variation": "primary" },
    { "url": "...", "variation": "alternative" },
    { "url": "...", "variation": "square_crop" }
  ],
  "total_cost": "$0.24"
}
```

---

## Advanced Features

### Image Editing (Inpainting / Outpainting)

```
/image-gen
Prompt: "Extend the background to show a warm kitchen setting"
Mode: outpainting
Base image: [URL or file path]
Mask area: bottom 30% of image
```

### Variations & Upscaling

```
/image-gen
Mode: variations
Base image: [URL]
Count: 3 variations
Upscale: 2x (from 512x512 to 1024x1024)
```

### Style Transfer

```
/image-gen
Mode: style-transfer
Content image: product photo
Style reference: "warm, vintage food photography aesthetic"
Strength: 0.8 (0-1 scale)
```

---

## API Routing Logic

**Choose API based on:**

1. **Photorealism needed?** → DALL-E 3
2. **Artistic/unique aesthetic?** → Midjourney
3. **Budget-conscious, batch processing?** → Stable Diffusion
4. **Premium quality, cutting edge?** → Flux
5. **Fast turnaround?** → Midjourney (1-2 min)

---

## Pricing & Budget Management

For Sunny Homemade (example):
- 7 images/week × $0.08 (DALL-E) = $0.56/week = $2.24/month
- OR 7 images/week × $0.06 (Midjourney) = $0.42/week = $1.68/month
- OR 7 images/week × $0.03 (Stable Diffusion) = $0.21/week = $0.84/month

**Total API spend across all projects must stay under $5/month** (hard constraint).

See `projects/marketing-os/tasks/COST-ANALYSIS-AND-BUDGET-ENFORCEMENT.md` for details.

---

## When to Use This Skill

- Product photography (e-commerce, food, SaaS)
- Ad creatives (cold audience, retargeting, brand awareness)
- Social media content (Instagram, TikTok, LinkedIn)
- UI mockups and app screenshots
- Hero images for landing pages, README files, marketing materials
- Illustrations and icon designs
- Before-after comparison visuals

---

## Best Practices

**Do:**
- Be specific about dimensions and aspect ratio
- Use brand colors in prompt (hex codes)
- Reference professional photography terminology (lighting, composition, angle)
- Include style guide references ("minimal aesthetic", "luxury brand", "playful")
- Batch generate 3-4 variations and pick the best
- Store generated images in `projects/<name>/assets/generated/`
- Log cost and performance in `tasks/lessons.md`

**Don't:**
- Use ambiguous prompts ("make it look nice")
- Ask for copyrighted characters or brands (will be filtered/revised)
- Expect photorealism from abstract concepts (use Midjourney for creative instead)
- Exceed monthly API budget without approval
- Generate images larger than needed (1024x1024 good for web, upscale only if necessary)

---

## Generic Marketing Examples

**B2B SaaS:**
```
Professional mockup of a project management dashboard showing team collaboration 
features, modern dark theme with blue accents, modern tech aesthetic, 1920x1080
```

**E-Commerce:**
```
Professional product photography of [PRODUCT] lifestyle shot showing customer using item, 
natural outdoor lighting, aspirational mood, 1280x1600, 9:16
```

**Personal Brand / LinkedIn:**
```
Professional portrait of a confident professional in business casual setting, 
modern office background, warm lighting, approachable expression, 1080x1350
```

**Landing Page Hero:**
```
Abstract modern geometric design representing [CONCEPT], sophisticated color palette,
minimalist, premium tech aesthetic, 1920x1080, 16:9
```
