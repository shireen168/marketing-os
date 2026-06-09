# Smart Sleep Device: Phase 4 Build & Development

## Implementation Strategy for Hardware Firmware, Cloud Infrastructure, and Product Launch

**Prepared by:** Engineering & Product Development Division

**Report Date:** 2026

**Phase Focus:** Development Roadmap, Technical Execution, Resource Allocation, Risk Mitigation

**Status:** Customer-Facing Build & Development Framework

---

## Table of Contents

<details>

<summary><strong>1. Executive Summary</strong></summary>

- [1.1 Build & Development Thesis](#11-build--development-thesis)
- [1.2 Development Timeline & Milestones](#12-development-timeline--milestones)
- [1.3 Resource Requirements](#13-resource-requirements)
- [1.4 Budget Overview](#14-budget-overview)
- [1.5 Success Criteria](#15-success-criteria)

</details>

<details>

<summary><strong>2. Development Team Structure</strong></summary>

- [2.1 Organizational Chart](#21-organizational-chart)
- [2.2 Core Engineering Teams](#22-core-engineering-teams)
- [2.3 Cross-Functional Dependencies](#23-cross-functional-dependencies)
- [2.4 External Partners & Vendors](#24-external-partners--vendors)

</details>

<details>

<summary><strong>3. Hardware Firmware Development</strong></summary>

- [3.1 Microcontroller Architecture](#31-microcontroller-architecture)
- [3.2 Sensor Integration & Signal Processing](#32-sensor-integration--signal-processing)
- [3.3 Wireless Connectivity (WiFi & Bluetooth)](#33-wireless-connectivity-wifi--bluetooth)
- [3.4 Power Management & Battery Optimization](#34-power-management--battery-optimization)
- [3.5 Firmware Development Roadmap](#35-firmware-development-roadmap)
- [3.6 Testing & Validation](#36-testing--validation)

</details>

<details>

<summary><strong>4. Cloud Backend Development</strong></summary>

- [4.1 AWS Infrastructure Setup](#41-aws-infrastructure-setup)
- [4.2 Data Pipeline Architecture](#42-data-pipeline-architecture)
- [4.3 ML Pipeline & Sleep Stage Classification](#43-ml-pipeline--sleep-stage-classification)
- [4.4 API Development & Documentation](#44-api-development--documentation)
- [4.5 Database Schema & Migration Strategy](#45-database-schema--migration-strategy)
- [4.6 Security & Compliance Infrastructure](#46-security--compliance-infrastructure)
- [4.7 Backend Development Roadmap](#47-backend-development-roadmap)

</details>

<details>

<summary><strong>5. Mobile & Web Application Development</strong></summary>

- [5.1 iOS App Development (Swift)](#51-ios-app-development-swift)
- [5.2 Android App Development (Kotlin)](#52-android-app-development-kotlin)
- [5.3 Web Portal Development (React)](#53-web-portal-development-react)
- [5.4 Healthcare Provider Portal](#54-healthcare-provider-portal)
- [5.5 Corporate Admin Dashboard](#55-corporate-admin-dashboard)
- [5.6 Cross-Platform Development Roadmap](#56-cross-platform-development-roadmap)

</details>

<details>

<summary><strong>6. Sprint Planning & Development Cadence</strong></summary>

- [6.1 Sprint Structure (2-week cycles)](#61-sprint-structure-2-week-cycles)
- [6.2 Week-by-Week Development Plan (Months 0-3 MVP)](#62-week-by-week-development-plan-months-0-3-mvp)
- [6.3 Post-MVP Development (Months 3-6)](#63-post-mvp-development-months-3-6)
- [6.4 Scaling Phase (Months 6-9)](#64-scaling-phase-months-6-9)
- [6.5 Definition of Done & QA Gates](#65-definition-of-done--qa-gates)

</details>

<details>

<summary><strong>7. Manufacturing & Supply Chain</strong></summary>

- [7.1 Hardware Manufacturing Partner Selection](#71-hardware-manufacturing-partner-selection)
- [7.2 Component Procurement & BOM](#72-component-procurement--bom)
- [7.3 Manufacturing Timeline & Scaling](#73-manufacturing-timeline--scaling)
- [7.4 Quality Assurance & Defect Management](#74-quality-assurance--defect-management)

</details>

<details>

<summary><strong>8. Risk Mitigation & Contingency Planning</strong></summary>

- [8.1 Technical Risk Register](#81-technical-risk-register)
- [8.2 Dependency & Critical Path Risks](#82-dependency--critical-path-risks)
- [8.3 Contingency Plans](#83-contingency-plans)

</details>

<details>

<summary><strong>9. Launch Readiness Checklist</strong></summary>

- [9.1 Pre-Launch Validation](#91-pre-launch-validation)
- [9.2 Customer Support & Documentation](#92-customer-support--documentation)
- [9.3 Launch Rollout Strategy](#93-launch-rollout-strategy)

</details>

<details>

<summary><strong>10. Sources & References</strong></summary>

Jump to [Section 10](#10-sources--references) for citations.

</details>

---

# 1. Executive Summary

## 1.1 Build & Development Thesis

Phase 3 established the design, technical architecture, and go-to-market strategy. Phase 4 translates that blueprint into working code, firmware, manufacturing, and product delivery. The critical success factor is **execution discipline**: maintaining the technical roadmap while adapting to inevitable hardware integration challenges, ML model performance variability, and mobile ecosystem fragmentation.

The build phase spans 9 months (Months 0-9):

1. **MVP Phase (Months 0-3):** Deliver a functional hardware device (500-unit production run), cloud backend APIs, and a working iOS/Android consumer app capable of end-to-end sleep tracking and basic reporting. This phase prioritizes getting a closed loop working (device → cloud → app) over feature completeness.

2. **Post-MVP Phase 1 (Months 3-6):** Scale manufacturing to 5,000-10,000 units/month, add healthcare integrations (EHR connectors, clinical dashboards), implement AI coaching, and prepare regulatory submission materials.

3. **Scaling Phase (Months 6-9):** Transition to sustained production operations, complete FDA 510(k) submission, launch healthcare and corporate wellness channels, and optimize for cost of goods (COGS) reduction from USD 180 to USD 120.

This report outlines the team structure, sprint-by-sprint execution plan, technical dependencies, resource requirements (USD 3.2M for 9-month build + manufacturing), and contingency plans for the most likely failure modes.

## 1.2 Development Timeline & Milestones

| Phase | Duration | Key Milestones | Go/No-Go Gate |
|-------|----------|-----------------|--------------|
| **MVP (Firmware)** | Weeks 0-4 | Sensor accuracy validated (92%+ vs. PSG); firmware stable on STM32 | Week 4 accuracy gate |
| **MVP (Backend)** | Weeks 2-6 | Core APIs functional; DynamoDB tables live; Lambda functions tested | Week 6 API gate |
| **MVP (Mobile)** | Weeks 4-10 | iOS & Android apps downloadable; onboarding → dashboard → first sleep report | Week 10 app UX gate |
| **Manufacturing** | Weeks 4-12 | Design finalized; injection molds completed; first 500 units produced | Week 12 quality gate |
| **Clinical Study** | Weeks 0-12 | IRB approval; 150+ patients enrolled; PSG + device data collected | Week 12 enrollment gate |
| **Post-MVP Phase 1** | Weeks 12-24 | EHR integrations live; healthcare dashboard functional; AI coaching deployed | Month 6 revenue gate |
| **Regulatory** | Weeks 12-30 | FDA 510(k) submitted (Week 16); clearance expected Month 6-8 | Clearance gate |
| **Scaling** | Weeks 24-36 | 10K+ units/month capacity; corporate wellness pilots signed; published research | Month 9 traction gate |

**Total build duration: 36 weeks (9 months)**

## 1.3 Resource Requirements

**Engineering Headcount (Full-Time Equivalent, FTE):**

| Team | Count | Ramp Timeline | Key Roles |
|------|-------|---------------|-----------|
| Firmware | 2 | Week 0; 1 additional Week 12 | Lead embedded engineer, sensor integration specialist |
| Backend | 3 | Week 0; 1 QA engineer Week 4 | Principal backend architect, ML engineer, DevOps/infrastructure |
| iOS | 1.5 | Week 2; 1 additional Week 12 | iOS lead, designer/QA (shared) |
| Android | 1.5 | Week 2; 1 additional Week 12 | Android lead, designer/QA (shared) |
| Web / Portals | 1.5 | Week 4; 1 additional Week 12 | Full-stack React engineer, healthcare UX specialist |
| QA / Test | 2 | Week 4; 2 additional Week 12 | Test automation engineer, clinical validation specialist |
| Product / Program Mgmt | 1.5 | Week 0 | Product manager, scrum master |
| **Total Peak (Month 6)** | **13 FTE** | | |

**Non-Engineering Resources:**

| Function | Count | Cost Center |
|----------|-------|-------------|
| Regulatory Affairs | 1 FTE | Legal/Compliance |
| Clinical Affairs | 0.5 FTE | Chief Medical Officer's office |
| Hardware Design (CAD/Industrial) | 0.5 FTE (contract) | Manufacturing partner |
| Vendor Management | 0.5 FTE | Supply chain |

**Total payroll + contractor cost:** USD 2.1M over 9 months (including salaries, benefits, contractor fees).

## 1.4 Budget Overview

| Category | Cost (USD) | Notes |
|----------|-----------|-------|
| **Personnel (payroll + benefits)** | 2,100,000 | 13 FTE average over 9 months |
| **Hardware manufacturing (first 5,500 units)** | 650,000 | COGS: USD 180/unit (500 MVP + 5,000 post-MVP) |
| **Cloud infrastructure (AWS)** | 180,000 | Estimates: USD 800/month MVP, USD 3,500/month scaling |
| **Testing & validation (clinical study)** | 320,000 | IRB, PSG overnight studies (n=150), data analysis |
| **External contractors (regulatory, EHR integration)** | 280,000 | FDA consultant (USD 150K), FHIR integration specialist (USD 130K) |
| **Tools & licenses (software development)** | 85,000 | Xcode, Android Studio, Jira, GitHub Enterprise, ML platforms (SageMaker) |
| **Travel & operational** | 95,000 | Engineering team travel for manufacturing site visits, clinical partnerships |
| **Contingency (10%)** | 320,000 | Buffer for cost overruns, scope changes |
| **Total Phase 4 Budget** | **3,200,000** | **USD 3.2M for 9-month build cycle** |

**Budget allocation by phase:**
- MVP (Months 0-3): USD 1.2M (personnel, initial cloud setup, first manufacturing run)
- Post-MVP (Months 3-6): USD 1.3M (scaled manufacturing, healthcare integrations, regulatory prep)
- Scaling (Months 6-9): USD 0.7M (optimization, publication, pilot operations)

## 1.5 Success Criteria

**By end of Phase 4 (Month 9):**

1. **Hardware & Manufacturing:**
   - Device firmware production-ready; firmware version 1.0 released
   - 5,500+ units manufactured with <2% defect rate
   - COGS reduced to USD 140-160/unit (from initial USD 180)
   - Manufacturing partner capable of 10K+ units/month

2. **Cloud Backend:**
   - All core APIs production-ready; 99.9% uptime SLA maintained
   - Sleep stage ML model achieves 92%+ accuracy on hold-out test set
   - Data pipeline processes 1,000+ devices concurrently without latency degradation
   - HIPAA infrastructure audit passed (SOC 2 Type II in progress)

3. **Mobile Applications:**
   - iOS and Android apps available on App Store / Google Play
   - 5,000+ active users; 1,500+ paying subscribers
   - NPS 55+; onboarding completion rate 85%+
   - Zero critical crashes reported in production

4. **Healthcare & Enterprise:**
   - EHR integrations (Epic, Cerner) complete and tested
   - Healthcare provider portal live with 3+ pilot customers
   - Corporate wellness APIs ready for enterprise deployments
   - Peer-reviewed publication submitted to Journal of Clinical Sleep Medicine

5. **Regulatory & Compliance:**
   - FDA 510(k) submission filed (Week 16, Month 4)
   - FDA clearance received or expected (Month 6-8)
   - HIPAA and SOC 2 infrastructure documented and audited
   - Data retention policies and audit logging validated

---

# 2. Development Team Structure

## 2.1 Organizational Chart

```
CEO / Founder
 ├── VP Engineering (reports to CEO)
 │   ├── Engineering Lead - Firmware (2 FTE)
 │   │   ├── Embedded Systems Engineer (STM32, C/C++)
 │   │   └── Sensor Integration Specialist
 │   │
 │   ├── Engineering Lead - Backend (3 FTE)
 │   │   ├── Principal Backend Architect (Python, AWS)
 │   │   ├── ML/Data Engineer (TensorFlow, SageMaker)
 │   │   └── DevOps / Infrastructure Engineer
 │   │
 │   ├── Engineering Lead - Mobile (3 FTE)
 │   │   ├── iOS Lead (Swift, SwiftUI)
 │   │   ├── Android Lead (Kotlin, Jetpack)
 │   │   └── Shared QA / Designer (part-time across teams)
 │   │
 │   ├── Engineering Lead - Web & Portals (1.5 FTE)
 │   │   └── Full-Stack Engineer (React, TypeScript, Next.js)
 │   │
 │   └── QA & Test Engineering (2 FTE)
 │       ├── Test Automation Engineer
 │       └── Clinical Validation Specialist
 │
 ├── Head of Product
 │   └── Product Manager
 │   └── Scrum Master / Program Manager
 │
 ├── VP Regulatory & Clinical (reports to CEO)
 │   ├── Regulatory Affairs Manager
 │   └── Chief Medical Officer / Clinical Advisor
 │
 └── VP Operations (reports to CEO)
     └── Supply Chain / Manufacturing Manager
```

## 2.2 Core Engineering Teams

### Firmware Team (2 FTE)

**Responsibilities:**
- Embedded firmware development for STM32L496 microcontroller
- Sensor integration: radar (60 GHz), accelerometer, temperature
- WiFi and Bluetooth stack integration
- Power management, battery optimization
- Over-the-air (OTA) firmware update infrastructure
- Firmware unit testing and hardware-in-the-loop validation

**Key Hires:**
1. **Embedded Systems Lead** (Full-time, hire Week 0)
   - 5+ years embedded systems (IoT, wearables, medical devices)
   - Proficient in C/C++, RTOS (FreeRTOS), hardware debugging
   - Experience with ARM Cortex-M microcontrollers
   - Medical device or FDA experience preferred

2. **Sensor Integration Specialist** (Full-time, hire Week 2)
   - 3+ years sensor integration (radar, accelerometer, signal processing)
   - Experience with RF design, antenna tuning, signal conditioning
   - Proficient in MATLAB/Python for signal analysis
   - Radar or biomedical sensors preferred

**Key Deliverables (by week):**
- Week 0-2: Hardware bring-up; sensor communication (SPI, I2C) verified
- Week 2-4: Real-time signal conditioning pipeline operational; WiFi connectivity stable
- Week 4-8: Firmware v0.9 feature-complete; tested against PSG simultaneously for 50+ nights
- Week 8-12: Firmware v1.0 production-ready; manufacturing ready for tooling finalization

### Backend Team (3 FTE)

**Responsibilities:**
- REST API design and implementation
- AWS infrastructure provisioning (Lambda, API Gateway, DynamoDB, Kinesis)
- Sleep stage ML model training, validation, and deployment
- Data pipeline: ingestion, transformation, classification
- EHR integrations (HL7 FHIR, Epic, Cerner)
- Database schema design, migrations, indexing optimization
- DevOps: CI/CD pipelines, monitoring, alerting

**Key Hires:**
1. **Principal Backend Architect** (Full-time, hire Week 0)
   - 7+ years backend systems (Python, NodeJS, Java)
   - AWS expert: Lambda, RDS, DynamoDB, Kinesis, SageMaker
   - Experience with healthcare data systems (HIPAA, HL7)
   - Microservices architecture and event-driven design

2. **ML / Data Engineer** (Full-time, hire Week 2)
   - 4+ years ML engineering (TensorFlow, PyTorch, scikit-learn)
   - Experience with time-series models (LSTM, Transformers, HMM)
   - Familiar with SageMaker, AWS training pipelines
   - Sleep physiology or biomedical signals background helpful

3. **DevOps / Infrastructure Engineer** (Full-time, hire Week 4)
   - 5+ years AWS and infrastructure automation
   - Terraform, CloudFormation, Kubernetes (if applicable)
   - CI/CD pipelines (GitHub Actions, Jenkins)
   - Monitoring and alerting (CloudWatch, DataDog, PagerDuty)

**Key Deliverables (by week):**
- Week 0-2: AWS VPC, subnets, security groups, IAM roles provisioned
- Week 2-4: REST API skeleton complete; auth endpoints (login, register) functional
- Week 4-6: Sleep data ingestion pipeline (Kinesis → DynamoDB) operational
- Week 6-10: ML model training complete on PSG-labeled data; inference latency <2 seconds
- Week 10-12: EHR integration scaffolding ready (FHIR endpoints stubbed)
- Week 12-16: Healthcare APIs (provider patient list, study data export) production-ready

### Mobile Teams (iOS + Android, 3 FTE)

**Responsibilities:**
- Native iOS app development (Swift, SwiftUI)
- Native Android app development (Kotlin, Jetpack)
- OAuth authentication and token management
- Offline-first architecture and local data caching
- Push notifications and background sync
- Device pairing (Bluetooth, WiFi provisioning)
- Submission to App Store and Google Play

**Key Hires:**
1. **iOS Lead** (Full-time, hire Week 2)
   - 4+ years iOS development (Swift, SwiftUI)
   - App Store submission and review process familiarity
   - Background task frameworks, health kit integration
   - HIPAA-compliant mobile app experience preferred

2. **Android Lead** (Full-time, hire Week 2)
   - 4+ years Android development (Kotlin, Jetpack)
   - Google Play submission and review process familiarity
   - Background task management (WorkManager), health integration
   - HIPAA-compliant mobile app experience preferred

3. **Shared QA / Designer** (0.5 FTE each, hire Week 6)
   - Mobile UI/UX testing, user acceptance testing
   - Device compatibility testing (iOS 15+, Android 11+)
   - Performance profiling (battery drain, memory leaks)

**Key Deliverables (by week):**
- Week 2-4: Project scaffolding; OAuth integration; basic MVVM architecture
- Week 4-8: Onboarding flow complete; device pairing working; first sleep score display
- Week 8-10: Full dashboard with sleep timeline visualization; recommendations engine
- Week 10-12: App Store and Google Play submission; beta testing with 100+ users
- Week 12-14: App Store and Google Play approval; public launch

### Web & Portals Team (1.5 FTE)

**Responsibilities:**
- React/TypeScript frontend development
- Next.js server-side rendering (for security-sensitive pages)
- Healthcare provider portal (clinical dashboard, patient management)
- Corporate admin dashboard (analytics, ROI reporting)
- EHR integration UI components
- Responsive design, accessibility (WCAG AAA)

**Key Hire:**
1. **Full-Stack Engineer (React/Next.js)** (Full-time, hire Week 4)
   - 5+ years React / TypeScript / Next.js
   - Server-side rendering and security best practices
   - Healthcare / B2B SaaS UI experience
   - Data visualization (D3.js, Recharts)

2. **Healthcare UX Specialist** (Contract, 0.5 FTE, hire Week 8)
   - HIPAA-compliant healthcare UI/UX design
   - EHR workflow integration expertise
   - Clinical user research and feedback synthesis

**Key Deliverables (by week):**
- Week 4-8: Consumer web dashboard skeleton; healthcare provider portal scaffolding
- Week 8-12: Consumer portal fully functional (responsive, offline-ready)
- Week 12-16: Healthcare provider dashboard live; patient list, study data, PDF export
- Week 16-24: Corporate admin dashboard; ROI analytics, enrollment management

### QA & Test Engineering (2 FTE)

**Responsibilities:**
- Test automation (unit, integration, end-to-end)
- Clinical validation testing (device accuracy vs. PSG)
- Device reliability testing (MTBF, firmware stability)
- Mobile app testing across devices and OS versions
- Regression testing and release validation
- Documentation of test plans and results

**Key Hires:**
1. **Test Automation Engineer** (Full-time, hire Week 4)
   - 4+ years test automation (Selenium, Appium, Jest, pytest)
   - CI/CD integration and test reporting
   - Medical device or FDA validation experience

2. **Clinical Validation Specialist** (Full-time, hire Week 4)
   - Background in sleep medicine or clinical research
   - PSG scoring experience (AASM certification preferred)
   - Data collection and validation methodologies
   - FDA pre-submission experience

**Key Deliverables (by week):**
- Week 4-6: Unit test suite for firmware and backend (>80% code coverage)
- Week 6-10: Integration tests (device → cloud → app); load testing
- Week 10-12: Clinical validation protocol finalized; testing with 50+ subjects
- Week 12-36: Ongoing regression testing; clinical data analysis; regulatory documentation

## 2.3 Cross-Functional Dependencies

**Product & Engineering Sync:**
- Weekly sprint planning (Monday 10am, 1 hour) - VP Engineering, Product Manager, all team leads
- Bi-weekly product review (Friday 2pm, 1 hour) - Demo of completed features, stakeholder feedback
- Ad-hoc technical design reviews (as needed) - Architecture decisions, technical debt triage

**Engineering & Manufacturing:**
- Weekly manufacturing partner sync (Monday 3pm, 1 hour) - Production status, component sourcing, schedule
- Firmware release schedule tied to manufacturing milestones (new firmware every 2 weeks during MVP)

**Engineering & Regulatory/Clinical:**
- Bi-weekly regulatory sync (Thursday 10am, 1 hour) - FDA pre-submission, clinical study progress, documentation
- Clinical study oversight: weekly sync with principal investigator (PI) to review enrollment, data quality

**Engineering & Operations:**
- Weekly operations sync (Wednesday 10am, 0.5 hour) - Infrastructure costs, monitoring alerts, incident response
- Quarterly capacity planning review - infrastructure for anticipated user growth

## 2.4 External Partners & Vendors

**Hardware Manufacturing Partner:**
- **Selection criteria:** ISO 13485 medical device certified, SMT assembly capacity 10K+ units/month, experience with RF/analog circuitry
- **Recommended partners:** Flex (global), Wyle Electronics, ScanSource, or regional China-based ODM (Flextronics, Incap)
- **Contract terms:** NRE (non-recurring engineering) USD 80K for tooling, first 500 units at USD 180/unit, volume pricing USD 120/unit at 5K+ quantity
- **Lead time:** 12-16 weeks from design freeze to first production run
- **Responsibilities:** PCB assembly, component procurement, quality control, packaging, logistics

**AWS / Cloud Infrastructure:**
- **Support:** AWS Enterprise Support (USD 15K/month) for dedicated TAM, 1-hour response time
- **Services:** Lambda, API Gateway, DynamoDB, Kinesis, SageMaker, KMS, S3, CloudWatch, VPC
- **Estimated monthly cost:** USD 800 (MVP) → USD 3,500 (scaling)

**FDA Regulatory Consultant:**
- **Firm:** Regulatory consulting firm with 510(k) clearance track record (e.g., Spalinger & Associates, Sierra Biomedical)
- **Scope:** Pre-submission meeting facilitation, 510(k) dossier preparation, post-market surveillance setup
- **Cost:** USD 150K fixed-fee

**EHR Integration Specialist:**
- **Expertise:** FHIR API development, Epic integration, Cerner integration
- **Firm:** Third-party integration specialist (e.g., Veradigm, Allscripts consulting) or contract specialist
- **Cost:** USD 80-130K for Phase 1 (2-3 system integrations)

**Clinical Research Organization (CRO):**
- **Scope:** IRB coordination, patient recruitment, PSG overnight studies, data collection and validation
- **Firm:** Regional sleep center or CRO with IRB experience
- **Cost:** USD 320K total (included in regulatory budget)

---

# 3. Hardware Firmware Development

## 3.1 Microcontroller Architecture

**Processor Selection: STM32L496 (ARM Cortex-M4)**

The STM32L496 is chosen for its balance of processing power, low-power capability, and extensive peripheral set:

- **Core:** ARM Cortex-M4 at 80 MHz (sufficient for real-time sensor processing)
- **Memory:** 320 KB SRAM, 1 MB Flash (adequate for firmware + local data buffering)
- **Peripherals:** SPI (sensor communication), UART (debug), USB (firmware update), RTC (low-power clock)
- **Power consumption:** <10 mW sleep mode, ~50 mW active processing
- **Cost:** USD 4-6 per unit at volume (100K+)

**Firmware Architecture:**

```
┌─────────────────────────────────────────────────┐
│ Application Layer                               │
│ • Sleep stage classification (local, optional)  │
│ • WiFi/Bluetooth stack management              │
│ • Device state machine (awake/charging/sleep)  │
│ • OTA firmware update handler                  │
└────────────────┬────────────────────────────────┘
                 │
┌────────────────┴────────────────────────────────┐
│ Middleware / RTOS Layer (FreeRTOS)             │
│ • Task scheduling                              │
│ • Inter-task communication (queues)            │
│ • Timer management                             │
│ • Memory allocation                            │
└────────────────┬────────────────────────────────┘
                 │
┌────────────────┴────────────────────────────────┐
│ Hardware Abstraction Layer (HAL)                │
│ • Radar sensor SPI driver                      │
│ • Accelerometer I2C driver                     │
│ • Temperature sensor ADC driver                │
│ • WiFi module UART driver                      │
│ • LED / button GPIO driver                     │
└────────────────┬────────────────────────────────┘
                 │
┌────────────────┴────────────────────────────────┐
│ STM32L496 Hardware                             │
│ • SPI, I2C, UART, GPIO, ADC, RTC              │
└─────────────────────────────────────────────────┘
```

**Firmware Development Environment:**
- **IDE:** STM32CubeIDE (free, integrated debugging)
- **Compiler:** GCC ARM (arm-none-eabi-gcc)
- **RTOS:** FreeRTOS v10.4 (free, widely used in medical devices)
- **Version control:** Git; repository hosted on GitHub Enterprise
- **CI/CD:** GitHub Actions for automated builds and firmware size tracking

## 3.2 Sensor Integration & Signal Processing

### Radar Sensor (60 GHz mmWave)

**Integration Details:**
- **Sensor module:** Third-party 60 GHz radar module (e.g., Infineon BGT60LTR11 or Texas Instruments IWR1843)
- **Communication:** SPI at 10 MHz clock rate
- **Data format:** Raw IQ samples (in-phase and quadrature) at 1000 Hz sampling rate
- **Buffer requirement:** ~1 MB per 8-hour night (1000 samples/sec × 3600 sec × 8 hours × 4 bytes per IQ pair, compressed to ~500 KB gzip)

**Signal Conditioning (On-Device or Cloud):**

On-device processing (firmware):
1. Read raw IQ samples from radar via SPI (10 ms batches)
2. Apply windowing function (Hamming window) to reduce spectral leakage
3. Compute FFT (Fast Fourier Transform) to extract frequency components
4. Identify dominant frequency (heart rate) and bandwidth (breathing pattern)
5. Buffer processed features (not raw samples) for WiFi transmission

Cloud processing (AWS Lambda):
1. Receive buffered features + raw IQ (if needed for research)
2. Apply adaptive baseline correction (remove slow drift)
3. Detect motion artifacts and environmental noise
4. Prepare clean 30-second windows for ML classification

**On-Device Sleep Stage Classification (Optional, for Offline Support):**

A lightweight ML model (TensorFlow Lite, ~2-5 MB) can be compiled for the STM32 to enable local sleep stage inference when WiFi is unavailable. This requires:
- Quantized model (int8) to fit in flash memory
- Inference latency <500ms for 30-second window
- Fallback to cloud processing when online

## 3.3 Wireless Connectivity (WiFi & Bluetooth)

**WiFi Module (for primary data upload):**
- **Module:** ESP32-S3 or Infineon ModusToolbox WiFi combo module
- **Interface:** UART at 921.6 kbps
- **Protocol:** WiFi 5 GHz (802.11ac) for speed; 2.4 GHz fallback for range
- **Provisioning:** Bluetooth Low Energy (BLE) for initial setup (user scans QR code, app sends WiFi credentials via BLE)

**Bluetooth (for setup and low-power wake notification):**
- **Profile:** Bluetooth Low Energy (BLE), not classic Bluetooth
- **Characteristics:** Battery level, WiFi status, sync status
- **Latency:** Connection established <2 seconds from app launch
- **Power consumption:** ~5 mW active, <1 mW when idle

**Firmware Data Transmission:**

1. **On every sync (typically nightly, 2am-6am local time):**
   - WiFi module wakes up
   - Connects to SSID stored in non-volatile flash
   - Transmits ~500 KB of sensor data (gzipped) to AWS IoT Core via MQTT
   - Receives acknowledgment; logs last sync timestamp

2. **Retry logic (if upload fails):**
   - Retry every 30 minutes for up to 24 hours
   - Store up to 7 days of data locally (1 MB available flash after firmware)
   - After 7 days, oldest data is overwritten (acceptable loss; users can recover from cloud backup)

3. **OTA firmware updates:**
   - AWS IoT sends update notification (manifest + binary)
   - Device downloads binary in background (1-5 minutes at 5 Mbps)
   - Verify firmware signature (RSA-2048)
   - Reboot and apply update; rollback if integrity check fails

## 3.4 Power Management & Battery Optimization

**Battery Chemistry & Capacity:**
- **Type:** Lithium-ion polymer (Li-Po), 3.7V nominal
- **Capacity:** 2500 mAh
- **Expected lifespan:** 500 charge cycles (3-5 years consumer use)

**Power Budget Breakdown (8-hour sleep + 16-hour idle):**

| Component | Active (mW) | Idle/Sleep (mW) | Duty Cycle | Avg Power (mW) |
|-----------|------------|-----------------|-----------|----------------|
| Radar sensor | 500 | 0 | 100% during sleep | 62.5 |
| Microcontroller | 50 | 5 | 100% monitoring | 6.25 |
| WiFi module | 200 | 2 | ~5% sync time | 10 |
| Accelerometer | 3 | 0.5 | 100% | 0.375 |
| Charging circuit | 20 | 5 | Always-on | 2.5 |
| LED indicators | 10 | 0 | 10% (breathing animation) | 1 |
| **Total** | | | | **82.625 mW avg** |

**Estimated battery life:**
- 2500 mAh / 82.625 mW = ~30 hours of continuous operation
- **Accounting for sleep mode and lower WiFi duty:** 20-25 days between charges (exceeds target of 25-30 days)

**Battery Charging:**
- **Charger:** 5V/2A USB-C fast charger (standard)
- **Charge time:** 80% in 1 hour, 100% in 1.5 hours
- **Battery protection:** Integrated fuel gauge (TI BQ24250 or equivalent) prevents over-charging and monitors health

**Low-Power Modes:**

1. **Active mode (sleep tracking):** Radar + accelerometer + microcontroller fully active; WiFi in RX mode
2. **WiFi sync mode:** WiFi transmit active (20-30 seconds per night); other components in low-power
3. **Charging mode:** Battery charger active; device displays charging status on LED
4. **Deep sleep (not implemented for MVP):** All components off except RTC; wakes on timer or motion detection (future optimization)

## 3.5 Firmware Development Roadmap

**Week 0-2: Bring-Up**

| Task | Owner | Deliverable |
|------|-------|-------------|
| STM32 development board setup | Embedded Lead | Working dev environment; serial debug output |
| Radar module integration | Sensor Specialist | SPI communication verified; raw IQ samples readable |
| Accelerometer I2C driver | Sensor Specialist | Real-time acceleration values logged |
| LED/button GPIO | Embedded Lead | Status indicator functional |

**Week 2-4: Sensor Fusion**

| Task | Owner | Deliverable |
|------|-------|-------------|
| FreeRTOS multi-task architecture | Embedded Lead | Task scheduler running; inter-task queues working |
| Radar signal conditioning (FFT, baseline removal) | Sensor Specialist | Heart rate and breathing rate extraction |
| Accelerometer motion detection (arousals) | Sensor Specialist | Movement events timestamped and logged |
| Temperature sensor integration | Sensor Specialist | Ambient + device temperature readable |

**Week 4-6: Connectivity**

| Task | Owner | Deliverable |
|------|-------|-------------|
| ESP32 WiFi module UART driver | Embedded Lead | WiFi SSID scan, connection, DHCP |
| MQTT client library integration | Embedded Lead | Device publishes telemetry to AWS IoT Core |
| Bluetooth BLE provisioning flow | Embedded Lead | Mobile app can send WiFi credentials via BLE |
| Data buffering & compression | Sensor Specialist | 8-hour night compressed to <500 KB |

**Week 6-8: Integration & Stability**

| Task | Owner | Deliverable |
|------|-------|-------------|
| Full integration test (all sensors + WiFi) | Both engineers | 48-hour continuous operation; no crashes |
| Edge case handling (WiFi dropout, low battery, sensor timeout) | Embedded Lead | Graceful degradation; data not lost |
| Hardware-in-the-loop validation vs. PSG | Sensor Specialist | Simultaneous collection with reference device (n=5) |
| Firmware v0.9 release candidate | Embedded Lead | Code review complete; ready for manufacturing |

**Week 8-12: Manufacturing & Optimization**

| Task | Owner | Deliverable |
|------|-------|-------------|
| Manufacturing design review | Embedded Lead + Manufacturer | Design finalized for mass production; DFM review passed |
| Firmware updates OTA capability | Embedded Lead | Secure firmware update mechanism tested |
| Performance profiling & optimization | Sensor Specialist | Battery life validated 25+ days; latency optimized |
| Firmware v1.0 release | Embedded Lead | Production firmware deployed to first 500 units |

## 3.6 Testing & Validation

**Unit Testing (Firmware Components):**

- **Radar signal processing:** MATLAB script generates synthetic IQ samples; firmware FFT output verified against MATLAB reference
- **Accelerometer motion detection:** Shake device at known frequencies (1 Hz, 2 Hz); confirm frequency detection
- **WiFi connection:** Test WiFi module error states (no SSID, wrong password, timeout)
- **Battery fuel gauge:** Discharge battery to known percentages; fuel gauge read accuracy validated

**Integration Testing (Hardware):**

- **Device → Cloud:** Send 8 hours of data; verify arrival in AWS S3 with zero data loss
- **Device ↔ Mobile app (BLE):** Pair device with phone; confirm provisioning, status readout
- **Reliability:** 500-hour MTBF test (devices running continuously; count resets or crashes)

**Clinical Validation (vs. PSG):**

- **Study design:** 150-200 sleep patients recruited; same-night simultaneous PSG + device recording
- **PSG reference:** Certified sleep technician scores PSG using AASM standards
- **Device comparison:** Algorithm compares device-detected sleep stages vs. PSG scoring
- **Success criteria:** 
  - Sleep/wake accuracy: >95%
  - Sleep stage accuracy (kappa): >0.80
  - AHI sensitivity/specificity (for apnea detection): >90% / >85%

**Environmental Testing:**

- **Temperature range:** Operating 0-40°C; storage -10 to 60°C
- **Humidity:** 20-80% non-condensing
- **Drop test:** Device survives 1-meter drop onto hardwood floor
- **EMI/RFI immunity:** Device functions in environments with WiFi interference, microwaves, cordless phones

---

# 4. Cloud Backend Development

## 4.1 AWS Infrastructure Setup

**AWS Account & VPC Configuration (Week 0-1):**

1. **Create AWS account** dedicated to product (not shared with other projects)
2. **VPC networking:**
   - VPC CIDR: 10.0.0.0/16
   - Public subnet (API Gateway): 10.0.1.0/24
   - Private subnet (Lambda, RDS): 10.0.2.0/24
   - Isolated subnet (RDS replica): 10.0.3.0/24
   - NAT Gateway in public subnet for private-subnet egress

3. **Security groups:**
   - ALB security group: Inbound HTTPS (443), outbound all
   - Lambda security group: Outbound to RDS (port 5432), DynamoDB, S3
   - RDS security group: Inbound from Lambda only (port 5432)

4. **IAM roles and policies:**
   - Lambda execution role: Permissions for DynamoDB, Kinesis, S3, CloudWatch Logs, KMS
   - API Gateway role: Permissions to invoke Lambda functions
   - RDS IAM authentication role (for passwordless database access)

**Service Configuration (Week 1-2):**

| Service | Configuration | Cost (Monthly) |
|---------|---------------|----------------|
| **API Gateway** | REST API with OAuth2 authorizer; regional (us-east-1) | USD 3.50 per million requests (est. 50M/month = USD 175) |
| **Lambda** | 512 MB memory, 60-second timeout; provisioned concurrency 100 | USD 1,200 |
| **DynamoDB** | On-demand billing; users/sleep/timeline tables | USD 800 |
| **RDS PostgreSQL** | db.t3.medium (2 vCPU, 4 GB RAM); multi-AZ; 100 GB storage | USD 300 |
| **S3** | Standard storage; 100 GB/month average; 1 million requests | USD 50 |
| **Kinesis** | 10 shards; on-demand (auto-scaling); 24-hour retention | USD 150 |
| **SageMaker** | Training: On-demand (runs intermittently); Inference: Serverless | USD 500 (est.) |
| **KMS (encryption)** | Customer-managed keys; operations cost | USD 50 |
| **CloudWatch** | Logs (10 GB/month), Metrics, Alarms | USD 100 |
| **NAT Gateway** | Data processing charges | USD 50 |
| **Total MVP (Month 1-3)** | | **USD 3,275/month** |
| **Total Post-MVP (Month 4-6)** | | **USD 5,500/month** |
| **Total Scaling (Month 7-9)** | | **USD 8,000/month** |

## 4.2 Data Pipeline Architecture

**Real-Time Ingestion (Kinesis + Lambda):**

```
Device (MQTT)
    ↓
AWS IoT Core
    ↓
Kinesis Stream (raw sensor data)
    ├→ Lambda Consumer 1 (signal conditioning)
    │     ↓
    │  Kinesis Stream 2 (processed features)
    │     ↓
    │  DynamoDB (user sensor logs)
    │
    └→ Lambda Consumer 2 (archival)
          ↓
          S3 (raw sensor archive, gzipped)
```

**Batch Processing (Nightly Sleep Stage Classification):**

```
Scheduled Event (EventBridge, daily 8am UTC)
    ↓
Lambda Function (trigger ML classification)
    ↓
S3 (retrieve previous night's sensor data)
    ↓
SageMaker Endpoint (ML inference)
    ↓
Sleep stage predictions (wake, light, deep, REM)
    ↓
DynamoDB (store timeline)
    ↓
SNS (publish sleep summary)
    ↓
Mobile App (receive notification, fetch summary)
```

**Data Storage Strategy:**

1. **Hot data (DynamoDB):** Last 30 days of sleep summaries and user profiles (fast read/write)
2. **Warm data (RDS):** Healthcare study data, reimbursement codes, EHR sync logs (structured queries)
3. **Cold data (S3):** Raw sensor archives older than 90 days (regulatory retention, rarely accessed)
4. **Encrypted archive (S3 + Glacier):** 7-year retention for HIPAA compliance (cost-optimized)

## 4.3 ML Pipeline & Sleep Stage Classification

**Model Architecture & Training (Week 4-8):**

**Input:** 30-second window of sensor features
- Radar: Heart rate (instantaneous), breathing rate, chest motion amplitude
- Accelerometer: Movement intensity, dominant frequency
- Stacked into a 6-channel feature matrix (30 sec × 64 Hz = 1,920 samples per window)

**Architecture Options (choose one):**

1. **LSTM (Long Short-Term Memory) + Attention**
   - Input shape: (sequence_length=1920, features=6)
   - 2 LSTM layers (128 units each)
   - Attention layer (focuses on key motion patterns)
   - Output: 4-class softmax (wake, light, deep, REM)
   - Training time: 4-6 hours on GPU (n=1,000+ subjects × 8 hours/night = 8,000 nights PSG data)

2. **Transformer-based (more recent, potentially better)**
   - Multi-head self-attention instead of LSTM
   - Positional encoding to capture temporal patterns
   - Training time: 6-8 hours on GPU
   - Inference latency: Similar to LSTM (~100-200ms per night)

3. **Hybrid (LSTM backbone + CNN feature extraction)**
   - 1D CNN extracts local patterns from sensor raw data
   - LSTM captures temporal dependencies
   - Best of both worlds; training time ~8 hours

**Training Data:**

- **Source:** Phase 1 research identified 1,000+ publicly available PSG-labeled datasets (PhysioNet, MASS Database, ISRUC-SLEEP)
- **Augmentation:** Time-warping (stretch/compress segments), Gaussian noise injection, sensor dropout simulation
- **Train/val/test split:** 70% / 15% / 15% (stratified by sleep stage)

**Model Performance Targets (on hold-out test set):**

| Metric | Target | Method |
|--------|--------|--------|
| Overall accuracy | >92% | Macro-averaged across all sleep stages |
| Wake detection sensitivity | >95% | True positive rate for wake periods |
| Deep sleep detection specificity | >90% | True negative rate (minimize false wake in deep sleep) |
| REM detection accuracy | >85% | Balanced accuracy (less data, harder to detect) |
| Inference latency | <2 seconds | Per night's data on AWS Lambda |

**Model Deployment (Week 8-10):**

1. **Training pipeline (SageMaker Training Job):**
   - Input: PSG dataset (n=5,000 subjects × 8 nights = 40,000 nights)
   - Output: Trained model serialized as SavedModel (TensorFlow)
   - Hyperparameters: Learning rate 1e-3, batch size 32, epochs 50 with early stopping

2. **Model versioning:**
   - Version 1.0 (MVP): Trained on public datasets; baseline accuracy 92%+
   - Version 1.1 (Month 4): Fine-tuned on internal clinical study data
   - Version 1.2 (Month 6): Ensemble method (3 models voting) for robustness

3. **Inference deployment:**
   - Option A (Serverless, cheaper): AWS Lambda with TensorFlow Lite (quantized model, <2 MB)
   - Option B (Always-on, faster): SageMaker Endpoint (auto-scales, 100ms latency; costs USD 500-1000/month)
   - **MVP choice:** Option A (Lambda); transition to Option B when user base >10K

## 4.4 API Development & Documentation

**REST API Specification (OpenAPI 3.0):**

All endpoints documented in OpenAPI format (swagger.json); auto-generated Postman collection and web UI.

**Core Endpoints (MVP):**

```
# Authentication
POST /auth/register
POST /auth/login
POST /auth/refresh
POST /auth/logout

# Sleep Data
GET /sleep/summary/{userId}/{date}
GET /sleep/summary/{userId}?start={date}&end={date}&limit=30
GET /sleep/timeline/{userId}/{date}
GET /sleep/insights/{userId}

# User Profile
GET /user/profile
PUT /user/profile
GET /user/privacy-settings

# Community (MVP basic version)
GET /community/friends
GET /community/leaderboard?period=week

# Subscription
GET /subscription/status
POST /subscription/upgrade

# Health
GET /health (status check for monitoring)
```

**Healthcare Endpoints (Post-MVP):**

```
# Provider dashboards
GET /provider/patients?clinic_id={id}
GET /provider/patient/{patient_id}/study
POST /provider/patient/{patient_id}/export-report
POST /provider/ehr-integration/sync

# EHR Integration (FHIR)
GET /fhir/Patient/{patient_id}
POST /fhir/DiagnosticReport (sleep study results)
```

**Request/Response Examples (MVP):**

```json
// GET /sleep/summary/user123/2026-06-08
{
  "date": "2026-06-08",
  "userId": "user123",
  "sleepScore": 78,
  "totalSleepTime": 26640,  // seconds (7h 24m)
  "sleepOnsetLatency": 1200,  // seconds (20m)
  "sleepEfficiency": 0.92,
  "stageDistribution": {
    "wake": 0.08,
    "light": 0.43,
    "deep": 0.24,
    "rem": 0.25
  },
  "arousals": 8,
  "timestamp": "2026-06-08T07:54:00Z"
}

// POST /auth/login
Request:
{
  "email": "user@example.com",
  "password": "securepassword"
}

Response:
{
  "accessToken": "eyJhbGciOiJIUzI1NiIs...",
  "refreshToken": "eyJhbGciOiJIUzI1NiIs...",
  "expiresIn": 86400,  // seconds (24 hours)
  "user": {
    "userId": "user123",
    "email": "user@example.com",
    "subscriptionTier": "premium"
  }
}
```

**Error Handling:**

```json
{
  "error": "invalid_request",
  "error_description": "Missing required parameter: date",
  "error_code": 400,
  "timestamp": "2026-06-08T12:00:00Z"
}
```

**API Documentation (automated):**
- **Tool:** Swagger UI + ReDoc
- **Hosted at:** api.sleepdevice.com/docs (internal); separate public documentation
- **Postman collection:** Auto-generated from OpenAPI spec; importable into Postman/Insomnia

## 4.5 Database Schema & Migration Strategy

**DynamoDB Tables (NoSQL for user data):**

```
Table: Users
├─ PK: user_id (String)
├─ SK: (none; flat table)
└─ Attributes:
   ├─ email (String, GSI)
   ├─ password_hash (String, encrypted)
   ├─ subscription_tier (String: free, premium, plus)
   ├─ created_at (Number, Unix timestamp)
   ├─ profile: {
   │  ├─ age (Number)
   │  ├─ sex (String: M/F)
   │  ├─ timezone (String: America/New_York)
   │  └─ health_conditions (List: sleep_apnea, insomnia, narcolepsy)
   └─ last_login (Number)

Table: DailySleepSummary
├─ PK: user_id (String)
├─ SK: date#YYYY-MM-DD (String)
├─ GSI: date#created_at (for time-range queries)
└─ Attributes:
   ├─ sleep_score (Number: 0-100)
   ├─ total_sleep_time (Number: seconds)
   ├─ sleep_onset_latency (Number: seconds)
   ├─ sleep_efficiency (Number: 0-1)
   ├─ stage_distribution: {
   │  ├─ wake (Number: 0-1)
   │  ├─ light (Number: 0-1)
   │  ├─ deep (Number: 0-1)
   │  └─ rem (Number: 0-1)
   ├─ arousals (Number)
   ├─ quality_rating (String: low, medium, high)
   ├─ device_id (String, for multi-device support)
   ├─ created_at (Number)
   └─ updated_at (Number)

Table: SleepTimeline
├─ PK: user_id (String)
├─ SK: timestamp#YYYYMMDD#HHmmss (String, 30-second epochs)
├─ GSI: user_id#date (for fast date queries)
└─ Attributes:
   ├─ sleep_stage (String: wake, light, deep, rem)
   ├─ confidence (Number: 0-1)
   ├─ signal_quality (Number: 0-1)
   └─ corrected_at (Number, if user manually corrected)

Table: UserSocialGraph
├─ PK: user_id (String)
├─ SK: (none)
└─ Attributes:
   ├─ friends_list (List of user_ids)
   ├─ blocked_users (List of user_ids)
   └─ active_challenges (List of challenge_ids)
```

**RDS PostgreSQL Tables (Structured Healthcare Data):**

```sql
-- Clinics (healthcare providers)
CREATE TABLE clinics (
  clinic_id UUID PRIMARY KEY,
  clinic_name VARCHAR(255) NOT NULL,
  address VARCHAR(500),
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(clinic_name)
);

-- Patients in clinical study
CREATE TABLE patients (
  patient_id UUID PRIMARY KEY,
  clinic_id UUID REFERENCES clinics(clinic_id),
  patient_label VARCHAR(50) NOT NULL,  -- "Patient 001-M-67" (de-identified)
  age INT,
  sex CHAR(1),
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX(clinic_id)
);

-- Sleep studies (one per patient enrollment)
CREATE TABLE sleep_studies (
  study_id UUID PRIMARY KEY,
  patient_id UUID REFERENCES patients(patient_id),
  study_date DATE NOT NULL,
  nights_collected INT DEFAULT 0,
  nights_required INT DEFAULT 7,  -- Home sleep apnea test protocol
  ahi_score DECIMAL(5, 2),  -- Apnea-Hypopnea Index
  o2_nadir INT,  -- Minimum oxygen saturation %
  clinical_interpretation TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  INDEX(patient_id, study_date)
);

-- Reimbursement codes & billing
CREATE TABLE billing_transactions (
  transaction_id UUID PRIMARY KEY,
  user_id UUID,
  subscription_tier VARCHAR(50),
  amount_usd DECIMAL(10, 2),
  cpt_code VARCHAR(10),  -- For healthcare billing (e.g., 95800)
  billing_date DATE NOT NULL,
  status VARCHAR(50),  -- pending, completed, failed
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX(user_id, billing_date)
);
```

**Migration Strategy (Week 2-4):**

1. **Infrastructure as Code (Terraform):**
   - Version 1: DynamoDB tables only (MVP)
   - Version 2: Add RDS PostgreSQL (Month 2, healthcare pilot)
   - Version 3: Add read replicas and backup (Month 4, scaling)

2. **Data migration:**
   - No existing data to migrate (greenfield product)
   - Schema versioning: Application code checks schema version on startup; auto-migrates if needed

3. **Backup & recovery:**
   - DynamoDB: Continuous backups enabled (point-in-time recovery, 35-day window)
   - RDS: Automated snapshots every 24 hours; 30-day retention
   - S3: Versioning enabled; lifecycle policy moves old versions to Glacier after 90 days

## 4.6 Security & Compliance Infrastructure

**Encryption (Week 2-4):**

1. **At-rest encryption:**
   - DynamoDB: Customer-managed KMS key (created Week 2); default encryption enabled
   - RDS: KMS encryption enabled; separate master key for healthcare data
   - S3: Default SSE-S3; sensitive archives use customer-managed KMS key

2. **In-transit encryption:**
   - API Gateway: HTTPS only (TLS 1.3 minimum); HTTP requests redirected to HTTPS
   - Lambda to RDS: AWS Secrets Manager stores database credentials; rotated every 30 days
   - Mobile apps: Certificate pinning for API endpoints (prevent MITM attacks)

**Authentication & Authorization (Week 1-3):**

1. **OAuth 2.0 implementation:**
   - Authorization Code Flow for mobile apps
   - Client Credentials flow for service-to-service (e.g., healthcare partner integrations)
   - Implemented using AWS Cognito (managed OAuth provider) or custom JWT

2. **JWT tokens:**
   - Structure: `header.payload.signature` (HS256 algorithm)
   - Payload includes: `user_id`, `subscription_tier`, `roles`, `exp` (expiration), `iat` (issued-at)
   - Access token: 24-hour expiration
   - Refresh token: 30-day expiration; can be revoked immediately on logout

3. **Role-based access control (RBAC):**
   - Consumer: Can access own sleep data, subscribe to premium, join community
   - Healthcare provider: Can access assigned patients' study data, export reports
   - Corporate admin: Can access aggregate company data, not individual employees
   - Platform admin: Full access (audit, user management)

**API Security (Week 3-4):**

1. **Rate limiting:** 100 requests/minute per user (prevent abuse)
2. **Input validation:** All API inputs validated against OpenAPI schema
3. **CORS (Cross-Origin Resource Sharing):** Restricted to known domains (mobile app package ID, web domain)
4. **API keys (for healthcare/corporate integrations):** Issued per customer; rotated annually
5. **WAF (Web Application Firewall):** AWS WAF rules to detect SQL injection, XSS, DDoS

**HIPAA & SOC 2 Compliance (Week 4-12):**

1. **Business Associate Agreement (BAA):**
   - Standard BAA template developed Week 4; legal review Week 5
   - Covers: Permitted use of PHI, data breach notification, subcontractor management
   - Required for any healthcare customer

2. **Audit trail logging:**
   - All access to PHI logged with: timestamp, user_id, action (read/write/delete), data_element
   - Logs stored in CloudWatch Logs (encrypted, 1-year retention)
   - Accessible to healthcare customers for HIPAA compliance audits

3. **Data minimization:**
   - Device collects raw sensor data; only sleep stage timeline is persisted
   - Raw waveforms stored only if user opts-in for research
   - Automatic deletion after 7 years (HIPAA requirement for healthcare data)

4. **Incident response plan:**
   - Suspected breach detection: Automated CloudWatch alarms for unusual access patterns
   - Incident response team (VP Engineering, legal, clinical) activates within 1 hour
   - Affected users notified within 60 days (HIPAA requirement)
   - Regulatory reporting to HHS within 60 days if >500 records exposed

## 4.7 Backend Development Roadmap

| Week | Firmware | Backend | Mobile | Status |
|------|----------|---------|--------|--------|
| 0-2 | Infrastructure setup | AWS VPC, DynamoDB, API Gateway scaffolding | Project setup | On track |
| 2-4 | Sensor bring-up | Core REST APIs (auth, sleep/summary, user/profile) | OAuth integration | On track |
| 4-6 | WiFi connectivity | Sleep data ingestion pipeline; Kinesis + Lambda | Onboarding flow | On track |
| 6-8 | Integration test | ML model training begins; API load testing | Dashboard UI | On track |
| 8-10 | Firmware v0.9 | ML model deployed; endpoint latency <2s | Feature completion | On track |
| 10-12 | Manufacturing prep | Healthcare APIs scaffolding; billing | App Store submission | On track |
| 12-16 | Firmware v1.0 | EHR integration (Epic/Cerner); AI coaching engine | Healthcare portal beta | On track |
| 16-24 | Optimization | Scaling, caching (Redis), analytics | Corporate admin dashboard | On track |
| 24-36 | OTA updates | Advanced features (community, gamification) | Maintenance mode | On track |

---

# 5. Mobile & Web Application Development

## 5.1 iOS App Development (Swift)

**Project Structure (MVVM Architecture):**

```
SleepApp (iOS)
├─ Views (SwiftUI)
│  ├─ AuthenticationView (login, sign-up)
│  ├─ DashboardView (main sleep score, timeline)
│  ├─ InsightsView (patterns, recommendations)
│  ├─ CommunityView (friends, leaderboard)
│  └─ SettingsView (profile, subscription)
├─ ViewModels (Combine reactive)
│  ├─ AuthViewModel (OAuth flow, token management)
│  ├─ SleepDataViewModel (fetch, cache, transform API data)
│  ├─ InsightsViewModel (pattern detection, recommendation logic)
│  └─ SettingsViewModel (user profile, privacy settings)
├─ Models (Codable)
│  ├─ User
│  ├─ DailySleepSummary
│  ├─ SleepTimeline
│  └─ Insight
├─ Services
│  ├─ APIService (networking, OAuth interceptor)
│  ├─ StorageService (Core Data, local caching)
│  ├─ BluetoothService (device pairing via BLE)
│  └─ HealthKitService (Apple Health sync)
└─ Resources
   ├─ Assets (images, colors, strings)
   └─ Localizable.strings (multi-language support)
```

**Tech Stack:**
- **Language:** Swift 5.9+
- **UI Framework:** SwiftUI (modern declarative UI)
- **Reactive:** Combine (Apple's native reactive framework)
- **Networking:** URLSession + Alamofire (optional, for convenience)
- **Local Storage:** Core Data (relational) + Keychain (secure credentials)
- **Background tasks:** BackgroundTasks framework (sync while charging)
- **Analytics:** Firebase Analytics (optional; can use custom events)

**Key Features (MVP, Week 4-10):**

1. **Authentication (Week 4-5):**
   - OAuth 2.0 login/sign-up
   - Apple ID / Google Sign-In (social auth)
   - Biometric authentication (Face ID / Touch ID)
   - Token refresh and logout

2. **Onboarding (Week 5-6):**
   - Permission requests (location, calendar, health app)
   - Device pairing via BLE: Scan QR code, establish connection, send WiFi credentials
   - First-sleep guidance

3. **Dashboard (Week 6-8):**
   - Sleep score card (large, center of screen)
   - Sleep metrics row (scrollable): deep %, REM %, efficiency, etc.
   - Sleep timeline visualization (area chart, color-coded stages)
   - Daily recommendation card
   - Offline support: Display cached data if no internet

4. **Insights (Week 8-9):**
   - Weekly summary: total hours, trend
   - Personal patterns detection (e.g., "You sleep better on weekends")
   - Health correlations (if Health Kit data available)
   - AI recommendations (if backend coaching enabled)

5. **Settings (Week 9-10):**
   - Device management: battery level, WiFi status, placement check
   - Notifications: sleep score timing, reminder to go to bed
   - Subscription & account: current tier, billing, upgrade
   - Privacy: download data, delete account, data sharing consent

**Testing (iOS):**
- **Unit tests:** 80%+ coverage for ViewModels, Services
- **UI tests:** XCUITest for critical user flows (login, onboarding, dashboard)
- **Device testing:** iPhone 12/13/14/15 on iOS 15-17
- **Performance profiling:** Xcode Instruments to check memory leaks, battery drain

**App Store Submission (Week 10-11):**
- Build release version (optimization, code signing)
- TestFlight beta testing (100+ users, crash reporting)
- App Store review (typical 1-3 days approval)
- Soft launch in select countries (New Zealand, small market for feedback before US launch)

## 5.2 Android App Development (Kotlin)

**Project Structure (MVVM + Jetpack):**

```
SleepApp (Android)
├─ ui/
│  ├─ authentication/ (LoginActivity, SignUpActivity)
│  ├─ dashboard/ (DashboardFragment, SleepTimelineChart)
│  ├─ insights/ (InsightsFragment, PatternDetection)
│  ├─ community/ (CommunityFragment, LeaderboardAdapter)
│  └─ settings/ (SettingsFragment, PreferencesActivity)
├─ viewmodel/
│  ├─ AuthViewModel (handles OAuth, stored credentials)
│  ├─ SleepDataViewModel (queries local database, fetches from API)
│  └─ InsightsViewModel (pattern logic, recommendations)
├─ data/
│  ├─ local/ (Room database for offline cache)
│  │  ├─ UserDAO
│  │  ├─ SleepSummaryDAO
│  │  └─ SleepTimelineDAO
│  ├─ remote/ (Retrofit API client)
│  └─ repository/ (abstraction layer, offline-first logic)
├─ services/
│  ├─ APIService (Retrofit-based HTTP client)
│  ├─ BluetoothService (BLE device pairing)
│  ├─ WorkManager (background sync when charging)
│  └─ FirebaseMessaging (push notifications)
└─ res/
   ├─ layout/ (XML layouts)
   ├─ drawable/ (images, icons)
   └─ values/ (colors, strings, themes)
```

**Tech Stack:**
- **Language:** Kotlin 1.9+
- **Architecture:** MVVM with LiveData
- **Jetpack components:** Room (local DB), WorkManager (background tasks), DataStore (preferences), Navigation component
- **Networking:** Retrofit + OkHttp
- **JSON serialization:** Kotlinx Serialization or Gson
- **Analytics:** Firebase Analytics
- **Bluetooth:** Android Bluetooth Low Energy (BluetoothLE) APIs
- **Health integration:** Google Fit API or HealthConnect (emerging standard)

**Key Features (MVP, Week 4-10):**

Same as iOS (authentication, onboarding, dashboard, insights, settings). Kotlin/Jetpack provide similar functionality but Android-specific APIs.

**Important Android Considerations:**

1. **Permissions:** Request location, calendar, health app permissions at runtime (Android 6+)
2. **Background sync:** WorkManager (not deprecated; replaces legacy GCM/FCM-only approach)
3. **Battery optimization:** Doze mode can block background syncs; configure WorkManager for battery efficiency
4. **Fragment lifecycle:** Properly manage LiveData subscriptions to prevent memory leaks

**Testing (Android):**
- **Unit tests:** JUnit + Mockito (80%+ coverage for ViewModels)
- **Instrumented tests:** Espresso for UI testing (critical flows)
- **Device testing:** Android 11-14 on various device sizes (Pixel, Samsung)
- **Performance profiling:** Android Profiler for memory, CPU, battery

**Google Play Submission (Week 10-11):**
- Build release APK/AAB (App Bundle, preferred)
- Play Store review (typically 1-3 days approval; similar to App Store)
- Soft launch in select countries before worldwide rollout

## 5.3 Web Portal Development (React)

**Project Structure (Next.js + TypeScript):**

```
SleepApp (Web)
├─ src/
│  ├─ pages/
│  │  ├─ api/ (API routes; NextAuth.js endpoints)
│  │  │  ├─ auth/
│  │  │  │  ├─ [...nextauth].ts (OAuth callback)
│  │  │  │  └─ logout.ts
│  │  │  └─ user/ (user profile endpoints)
│  │  ├─ index.tsx (home / redirect to app if logged in)
│  │  ├─ login.tsx
│  │  ├─ signup.tsx
│  │  ├─ app/
│  │  │  ├─ dashboard.tsx (main dashboard)
│  │  │  ├─ insights.tsx
│  │  │  ├─ community.tsx
│  │  │  └─ settings.tsx
│  │  └─ _app.tsx (global wrapper, layout)
│  ├─ components/
│  │  ├─ SleepScoreCard.tsx
│  │  ├─ SleepTimeline.tsx (D3.js or Recharts)
│  │  ├─ Recommendation.tsx
│  │  └─ LeaderboardTable.tsx
│  ├─ hooks/
│  │  ├─ useSleepData.ts (fetch, cache sleep data)
│  │  └─ useAuth.ts (OAuth context)
│  ├─ lib/
│  │  ├─ apiClient.ts (wrapper around fetch)
│  │  ├─ auth.ts (NextAuth.js configuration)
│  │  └─ utils.ts (date formatting, sleep calculations)
│  └─ styles/
│     └─ globals.css (Tailwind CSS or styled-components)
├─ public/
│  ├─ images/
│  └─ favicon.ico
├─ next.config.js
├─ tsconfig.json
└─ package.json
```

**Tech Stack:**
- **Framework:** Next.js 14+ (React meta-framework with SSR/SSG)
- **Language:** TypeScript
- **Styling:** Tailwind CSS (utility-first) or Material-UI
- **State management:** Redux Toolkit (if complex state) or React Context + hooks
- **Charts:** Recharts (React-friendly) or D3.js (custom sleep timeline)
- **Authentication:** NextAuth.js (managed OAuth flow)
- **HTTP client:** Axios or native fetch
- **Testing:** Jest + React Testing Library

**Key Features (MVP, Week 6-12):**

1. **Authentication (Week 6-7):**
   - OAuth 2.0 via NextAuth.js
   - Session management (HTTP-only cookies, secure)
   - Password reset via email

2. **Dashboard (Week 7-9):**
   - Sleep score card
   - Metrics row (same as mobile)
   - Sleep timeline chart (interactive, hover for details)
   - Recommendation card
   - Responsive design (mobile, tablet, desktop)

3. **Insights (Week 9-10):**
   - Weekly/monthly trends
   - Personalized recommendations
   - Sleep quality patterns

4. **Settings (Week 10-11):**
   - Account profile management
   - Subscription & billing
   - Privacy & data download

5. **Responsive Design:**
   - Mobile-first approach
   - Breakpoints: 320px (mobile), 768px (tablet), 1024px (desktop)
   - Touch-friendly on mobile; mouse-friendly on desktop

**Deployment (Week 12):**
- **Hosting:** Vercel (recommended for Next.js; auto-scaling, CDN)
- **Domain:** api.sleepdevice.com (or custom domain)
- **HTTPS:** Auto-configured by Vercel
- **Environment variables:** GitHub Actions or Vercel dashboard for secrets (API keys, OAuth credentials)

## 5.4 Healthcare Provider Portal

**Portal Purpose:** Clinicians review sleep study data, manage patient cohorts, export reports for EHR.

**Key Features (Post-MVP, Weeks 12-16):**

1. **Patient Management:**
   - Patient list (search, filter by status)
   - Enroll patient in home sleep study
   - Issue device activation code (QR or PIN)
   - Monitor enrollment progress (devices shipped, data collection started)

2. **Clinical Data Review:**
   - Single patient view: Sleep study summary, AHI, O2 levels, sleep architecture
   - Data quality metrics: % nights with usable data, signal quality score
   - Comparison to reference population (age/sex normalization)
   - Trend analysis: Nightly variability, trajectory over time

3. **Reporting:**
   - Auto-generate PDF clinical report (polished, printable)
   - Export to EHR: HL7 FHIR DiagnosticReport
   - Reimbursement coding: Auto-populate CPT codes (95807, 95800, etc.)

4. **Integration with Epic/Cerner:**
   - Single sign-on (SSO) via SAML 2.0 or OAuth
   - Patient context-passthrough: Clinician clicks "Order Sleep Test" in Epic → patient pre-populated in sleep device portal
   - Bi-directional sync: Results written back to Epic patient chart

**Healthcare Portal Tech Stack:**
- Same as consumer web portal (Next.js, React, TypeScript)
- Additional components: Clinical data table, PDF export (Puppeteer or wkhtmltopdf), EHR integration middleware
- Compliance: HIPAA audit logging, access controls, encryption

## 5.5 Corporate Admin Dashboard

**Dashboard Purpose:** HR/Benefits managers monitor employee sleep health, measure ROI, manage enrollment.

**Key Features (Post-MVP, Weeks 12-16):**

1. **Company Overview:**
   - KPI cards: Enrollment %, active users %, average sleep score, projected health cost savings
   - Trend chart: Enrollment over time, engagement retention curve

2. **Employee Analytics:**
   - Department breakdown: Sleep metrics by department, identify high-risk groups
   - Demographics: Sleep trends by age, gender, tenure
   - Segmentation: Employees in sleep debt, at-risk for sleep disorders

3. **ROI Measurement:**
   - Health cost projection: Model predicts savings based on peer-reviewed research
   - Engagement proxy: Days active, feature usage, feature adoption rate
   - Comparative: Benchmark against industry sleep norms

4. **Administration:**
   - Employee enrollment: Invite employees via email, bulk upload (CSV)
   - Device shipping: Manage device assignment, tracking
   - Wellness content: Recommend company-specific coaching (e.g., shift-worker sleep guide)
   - Privacy controls: Ensure individual data is not exposed; only aggregate metrics visible

**Corporate Portal Tech Stack:**
- Same foundation as consumer/healthcare portals
- Additional components: Bulk enrollment, CSV export, ROI calculator, advanced analytics

## 5.6 Cross-Platform Development Roadmap

| Week | iOS | Android | Web | Healthcare Portal | Corporate Dashboard |
|------|-----|---------|-----|------|------|
| 4-5 | Auth setup | Auth setup | API scaffolding | — | — |
| 5-6 | Onboarding flow | Onboarding flow | Login pages | — | — |
| 6-7 | Dashboard component | Dashboard component | Dashboard page | — | — |
| 7-8 | Sleep timeline chart | Sleep timeline chart | Timeline chart (D3) | — | — |
| 8-9 | Insights tab | Insights tab | Insights page | — | — |
| 9-10 | Settings tab | Settings tab | Settings page | Patient list (scaffold) | KPI dashboard (scaffold) |
| 10-11 | App Store review | Play Store review | Responsive polish | Patient detail view | Enrollment management |
| 11-12 | Public launch | Public launch | Public launch | Report generation | ROI calculator |
| 12-16 | New features | New features | Feature expansion | EHR integration | Analytics expansion |
| 16-36 | Maintenance | Maintenance | Maintenance | Scaling | Scaling |

---

# 6. Sprint Planning & Development Cadence

## 6.1 Sprint Structure (2-week cycles)

**Sprint cadence:**
- 2-week sprints (standard for agile teams)
- Sprint planning: Monday 10am (1 hour)
- Daily standup: Monday-Friday 9:30am (15 min)
- Sprint review + retro: Friday 4pm (1 hour)

**Sprint planning agenda:**

1. **Product Backlog review** (10 min): PM presents prioritized features for next sprint
2. **Capacity planning** (5 min): Team confirms availability (vacation, known blockers)
3. **Estimation** (15 min): Team estimates story points (1, 2, 3, 5, 8) for each user story
4. **Sprint goal** (5 min): Team agrees on overarching goal (e.g., "MVP API complete and tested")
5. **Task breakdown** (15 min): Larger stories broken into tasks; owners assigned

**Daily standup (15 min format):**
- Each engineer: What I did yesterday, what I'm doing today, blockers
- Focus on blockers; solve offline if needed

**Sprint review (30 min):**
- Demo completed work to stakeholders (VP Engineering, CEO, clinical advisor)
- Gather feedback for prioritization

**Retro (30 min):**
- What went well, what didn't, action items for next sprint
- Track velocity (story points completed) to improve estimation

## 6.2 Week-by-Week Development Plan (Months 0-3 MVP)

### Week 1-2: Foundation

**Firmware Team:**
- STM32 development board bring-up; Hello World LED blink
- Radar sensor module evaluation; datasheet review
- Accelerometer I2C communication established

**Backend Team:**
- AWS account setup; VPC networking, security groups
- DynamoDB table schema design
- REST API scaffolding: auth endpoints skeleton

**Mobile Team:**
- Project setup (Xcode, Android Studio, next.js)
- OAuth integration scaffolding
- Design system setup (colors, typography, component library)

**QA Team:**
- Test automation environment setup (Selenium, Appium, Jest)
- Test plan development for critical user journeys

**Sprint Goal:** "Infrastructure ready; development environments operational"

### Week 3-4: MVP Core Features

**Firmware:**
- Radar + accelerometer signal conditioning functional
- Real-time feature extraction (heart rate, breathing rate, motion) working
- WiFi connectivity established; MQTT connection to AWS IoT Core

**Backend:**
- Auth APIs (login, register, logout) production-ready
- Sleep data ingestion pipeline operational (Kinesis → DynamoDB)
- ML model training infrastructure set up

**Mobile:**
- OAuth login flow working (can log in with email + password)
- Onboarding flow (permissions, device setup, first sleep) mostly done

**Sprint Goal:** "Device can connect to cloud; basic app auth working"

### Week 5-6: MVP Integration

**Firmware:**
- Firmware v0.8 feature-complete; being tested against PSG simultaneously
- Accuracy metrics collected: 92%+ preliminary validation

**Backend:**
- Sleep data APIs functional (/sleep/summary, /sleep/timeline)
- ML model first version trained; inference pipeline operational

**Mobile:**
- Dashboard component displaying mock sleep data (no real data yet)
- Insights tab showing sample recommendations
- App Store TestFlight beta ready (internal team testing)

**Sprint Goal:** "End-to-end data flow working (device → cloud → app)"

### Week 7-8: MVP Refinement & Testing

**Firmware:**
- Firmware v0.9 released; manufacturing review beginning
- 50-hour continuous device test; no crashes
- Power optimization: battery life validated 20+ days

**Backend:**
- All APIs load-tested; 99.9% uptime validated over 72-hour test
- ML model inference latency: <2 seconds per night confirmed
- HIPAA infrastructure scaffolding: encryption, audit logging enabled

**Mobile:**
- iOS & Android apps feature-complete for MVP
- User acceptance testing (UAT) with 30-50 internal beta users
- NPS and crash rate tracked

**Sprint Goal:** "MVP feature-complete; quality validation in progress"

### Week 9-10: Launch Prep

**Firmware:**
- Firmware v1.0 final release; signed and ready for manufacturing
- QA: Final compatibility test with first production batch (500 units)

**Backend:**
- Monitoring and alerting configured (CloudWatch, PagerDuty)
- Capacity planning for launch: auto-scaling policies in place
- Regulatory documentation drafted (FDA submission prep)

**Mobile:**
- iOS submitted to App Store; Android submitted to Google Play
- Marketing materials ready (screenshots, app description, privacy policy)
- Crash reporting and analytics tracking enabled

**Clinical:**
- IRB approval obtained for clinical validation study
- 20-30 PSG patients recruited; baseline data collection started

**Sprint Goal:** "Ready for public launch; all systems validated"

### Week 11-12: Launch & Post-Launch Monitoring

**Firmware:**
- Manufacturing production run completed (500 units); QC passed
- First devices shipping to beta customers

**Backend:**
- Real user traffic monitored; alerting responding to issues
- Database backups and disaster recovery tested

**Mobile:**
- App Store / Google Play approval received
- Public launch: announce on Twitter, press release, email list
- Support tickets reviewed; hotfixes deployed if critical issues found

**Clinical Study:**
- 50+ patients enrolled; simultaneous PSG + device nights ongoing
- Data quality checks; no major data corruption issues

**Sprint Goal:** "Public launch successful; monitoring active; customer support responsive"

## 6.3 Post-MVP Development (Months 3-6)

### Sprint Goals (Bi-Weekly):

**Sprint 7-8:** EHR Integration Phase 1
- Epic and Cerner FHIR API integration scaffolding
- Healthcare provider portal patient list view
- CPT code configuration

**Sprint 9-10:** AI Coaching Engine
- Recommendation algorithm: pattern detection from 2+ weeks of user data
- Cloud ML model enhancement: fine-tuning on internal clinical data
- In-app recommendation display

**Sprint 11-12:** Social & Community Features
- Friend list implementation; privacy controls
- Leaderboard (anonymized, opt-in)
- Weekly challenges feature

**Sprint 13-14:** Healthcare Provider Portal Phase 2
- Clinical data visualization (AHI trends, quality metrics)
- PDF report generation; EHR export
- First healthcare pilot customer deployment

**Sprint 15-16:** Scaling & Optimization
- Database query optimization; caching (Redis) for leaderboard
- COGS reduction: manufacturing process optimization
- Regulatory submission finalized (FDA 510(k) filing)

## 6.4 Scaling Phase (Months 6-9)

### Sprint Goals:

**Sprint 17-20:** Corporate Wellness Launch
- Corporate admin dashboard: KPI metrics, ROI calculator
- PEPM billing integration with benefits platforms
- Employee portal (white-labeled, company-branded)

**Sprint 21-24:** Healthcare Expansion
- 3+ health system EHR integrations live
- Reimbursement pathway: insurance coding and claims submission
- Clinical publication preparation

**Sprint 25-28:** Infrastructure & Performance
- Load testing for 100K+ concurrent users
- Database sharding for geographic distribution (future)
- Cost optimization: COGS down to USD 120/unit

**Sprint 29-36:** Long-Tail Features & Maintenance
- Offline sleep stage classification on-device
- Voice assistant integration (Alexa, Google Home)
- Multi-language support (Spanish, Mandarin)
- Ongoing monitoring, bug fixes, security patches

## 6.5 Definition of Done & QA Gates

**Definition of Done (for each user story):**

- [ ] Code written and self-reviewed
- [ ] Unit tests written (minimum 80% coverage)
- [ ] Code reviewed by team lead (at least 2 approvals for critical code)
- [ ] Manual QA testing passed (test plan executed)
- [ ] Integration tests passed (feature works with other components)
- [ ] Performance testing done (latency, memory, battery for device/mobile)
- [ ] Security review passed (no hardcoded credentials, input validation)
- [ ] Documentation updated (code comments, user guide if applicable)
- [ ] Deployed to staging environment; final QA sign-off

**QA Gates (Blockers for Sprint Completion):**

1. **Device Accuracy Gate (Week 4):**
   - Radar + accelerometer fusion achieves 92%+ accuracy vs. PSG
   - **Fail:** Accuracy <90%; blocks firmware release

2. **API Stability Gate (Week 6):**
   - 99.9% uptime under 100 concurrent users
   - <2 second API response time (p95)
   - **Fail:** Uptime <99.5% or response time >3 seconds; blocks backend release

3. **App Stability Gate (Week 10):**
   - Zero critical crashes in 7-day internal beta (50 users)
   - NPS >40 (internal team feedback)
   - **Fail:** >1 crash per 10,000 sessions or NPS <30; blocks App Store submission

4. **Clinical Study Quality Gate (Week 12):**
   - 150+ patients enrolled; 100+ complete nights collected
   - <5% data loss (corruption, sync failures)
   - **Fail:** Enrollment <100 or data loss >10%; blocks FDA submission prep

5. **Regulatory Gate (Month 4):**
   - FDA pre-submission meeting completed; pathway confirmed as 510(k)
   - Clinical study analysis complete; publication-ready
   - **Fail:** FDA indicates de novo pathway; timeline extends 6+ months

---

# 7. Manufacturing & Supply Chain

## 7.1 Hardware Manufacturing Partner Selection

**Partner Selection Criteria (by Week 1):**

1. **Certifications:**
   - ISO 13485 (medical device manufacturing standard)
   - ISO 9001 (quality management)
   - FDA compliance (able to support 510(k) submission)

2. **Capabilities:**
   - SMT (surface-mount technology) assembly, 10K+ units/month capacity
   - RF/analog PCB design expertise (60 GHz radar integration)
   - Full-service (component procurement, assembly, QC, packaging, logistics)
   - NRE (non-recurring engineering) capacity for design optimization

3. **Geographic considerations:**
   - Proximity to component suppliers (reduce lead times)
   - Regional expertise: Asia (cost-optimized), North America (speed)
   - Communication: English-speaking technical team

4. **Financial stability:**
   - Creditworthiness (can finance inventory)
   - Pricing: Competitive quotes; volume discounts at 5K, 10K, 25K

**Recommended Partners (2-3 for comparison, select 1):**

1. **Flex Electronics (global ODM):**
   - Pros: Scale, reliability, global logistics
   - Cons: Longer lead times, higher NRE
   - COGS estimate: USD 180/unit (500 qty) → USD 120/unit (10K qty)

2. **Regional China ODM (e.g., Incap, Flextronics regional):**
   - Pros: Fast turnaround, cost-optimized, quality improving
   - Cons: Communication challenges, IP concerns, lead time variability
   - COGS estimate: USD 160/unit (500 qty) → USD 100/unit (10K qty)

3. **Local (North America) contract manufacturer:**
   - Pros: Better communication, flexible, faster iterations
   - Cons: Higher cost, smaller batch sizes less optimal
   - COGS estimate: USD 220/unit (500 qty) → USD 150/unit (10K qty)

**Selection outcome by Week 2:** Select Flex (global, reliable) or regional China ODM (cost-optimized based on startup funding).

## 7.2 Component Procurement & BOM

**Bill of Materials (BOM) Cost Breakdown (500 unit batch):**

| Component | Qty/Unit | Unit Cost (USD) | Line Total (USD) | % of COGS |
|-----------|----------|-----------------|-----------------|-----------|
| **Processor & Sensors** | | | | |
| STM32L496 MCU | 1 | 4.50 | 4.50 | 2.5% |
| 60 GHz Radar Module | 1 | 35.00 | 35.00 | 19.4% |
| 3-Axis Accelerometer (LIS2DH12) | 1 | 3.20 | 3.20 | 1.8% |
| Temperature/Humidity Sensor | 1 | 1.50 | 1.50 | 0.8% |
| **Wireless & Power** | | | | |
| ESP32 WiFi Module | 1 | 12.00 | 12.00 | 6.7% |
| Bluetooth Module (BLE) | 0.5 | 5.00 | 2.50 | 1.4% |
| Li-Po Battery 2500mAh | 1 | 8.00 | 8.00 | 4.4% |
| Charging Circuit (BQ24250) | 1 | 2.50 | 2.50 | 1.4% |
| USB-C Connector | 1 | 0.80 | 0.80 | 0.4% |
| **Passive Components** | | | | |
| Resistors, capacitors, inductors (assorted) | ~100 | 0.05 | 5.00 | 2.8% |
| **PCB & Assembly** | | | | |
| PCB (4-layer, 5" x 3") | 1 | 8.00 | 8.00 | 4.4% |
| SMT Assembly (labor + consumables) | 1 | 25.00 | 25.00 | 13.9% |
| **Enclosure & Hardware** | | | | |
| Plastic Enclosure (injection molded) | 1 | 15.00 | 15.00 | 8.3% |
| LED Indicator + Button | 1 | 1.20 | 1.20 | 0.7% |
| Silicone feet, screws, gasket | 1 | 2.00 | 2.00 | 1.1% |
| **QC & Testing** | | | | |
| Factory testing (RF, battery, function) | 1 | 10.00 | 10.00 | 5.6% |
| **Packaging** | | | | |
| Box, foam insert, manual, QR card | 1 | 5.00 | 5.00 | 2.8% |
| **Manufacturing Overhead** | | | | |
| NRE allocation (per unit) | 1 | 12.00 | 12.00 | 6.7% |
| **TOTAL COGS (500 units)** | | | | **USD 180** |

**COGS Reduction Path (to USD 120 at 10K units):**

1. **Component cost reductions (negotiated volume discounts):**
   - Radar module: USD 35 → USD 28 (20% reduction at higher volume)
   - WiFi module: USD 12 → USD 9 (25% reduction)
   - Enclosure injection mold: NRE amortized over 10K units (USD 12 → USD 2 per unit)

2. **Manufacturing efficiency:**
   - SMT assembly labor: USD 25 → USD 15 (process optimization, higher volume)
   - Factory testing: USD 10 → USD 6 (automated test fixtures)

3. **Logistics savings:**
   - Bulk shipping, consolidation with other products

**Target COGS at 10K units:** USD 120-130 (33% reduction from USD 180)

## 7.3 Manufacturing Timeline & Scaling

**Manufacturing Milestones:**

| Week | Milestone | Qty | Notes |
|------|-----------|-----|-------|
| 1-2 | Design finalization | — | CAD, schematics, BOM locked |
| 3-4 | NRE & tooling initiation | — | Injection mold for enclosure; ~USD 80K |
| 5-8 | Component procurement | 600 | Order long-lead items (radar module, WiFi module) |
| 8-10 | First article run | 50 | Test batch for design validation |
| 10-12 | Pilot production run | 500 | First commercial batch; QC validation |
| 12-16 | Ramp-up to 5K/month | 5,000 | Scaling operations; supply chain stability |
| 16-24 | Production at 10K/month | 10,000+ | Meeting demand; cost optimization |

**Production Capacity:**
- **MVP (Week 10-12):** 500 units (internal team + early beta customers)
- **Post-MVP (Week 12-24):** 5,000-10,000 units/month (scaled manufacturing, supply chain)
- **Scaling (Month 6+):** 20,000+ units/month capacity (multiple shifts, expanded facilities)

**Supply Chain Risk Mitigation:**
- **Dual-source strategy:** Identify backup suppliers for critical components (radar, WiFi)
- **Inventory buffer:** Maintain 2-month safety stock of long-lead items
- **Supplier contracts:** Lock in pricing for 24+ months; volume commitments in exchange for discounts

## 7.4 Quality Assurance & Defect Management

**In-Manufacturing QC (per unit):**

1. **First article inspection (FAI):** Every component and PCB assembly checked for defects before production run
2. **Final assembly QC:**
   - Visual inspection: solder joints, component placement, enclosure fit
   - Electrical testing: Power-on, boot firmware, sensor communication
   - RF testing: WiFi signal strength, Bluetooth pairing
   - Battery: Charge/discharge cycle (1 cycle per device)

3. **Burn-in testing:** Devices operated continuously for 24 hours (accelerated stress test)

4. **Packaging QC:** Manual inspection of packaging, manual, QR codes

**Target Defect Rates:**
- DOA (Dead-On-Arrival): <1% (devices non-functional out-of-box)
- Cosmetic defects: <2% (scratches, discoloration; cosmetic only, fully functional)
- Overall quality target: <2% defects across all categories

**Incoming Component Inspection:**
- Random sampling: Test 5-10% of incoming components for specifications
- Supplier scorecards: Track defect rates, on-time delivery, responsiveness
- Regular audits: Quarterly on-site audits of manufacturing partner facilities

**Post-Launch Defect Tracking:**
- Return rate monitoring: Devices returned within 30 days of purchase
- Failure analysis: RMA (return merchandise authorization) process; root cause analysis for defects >0.5% rate
- Firmware OTA updates: Push fixes for any detected software issues

**Warranty & Replacement:**
- 1-year hardware warranty (covers manufacturer defects, not user damage)
- Replacement warranty period: Replaced devices also get 1-year coverage from original purchase date
- Customer support: Email support, knowledge base, video tutorials (in-house operations team)

---

# 8. Risk Mitigation & Contingency Planning

## 8.1 Technical Risk Register

| Risk | Impact | Probability | Mitigation | Contingency |
|------|--------|-------------|-----------|-------------|
| **Radar sensor accuracy <90% in real-world homes** (environmental noise, user placement errors) | Critical | Medium (40%) | Field study (50 homes); real-world data collection before FDA submission; algorithm tuning with Kalman filters | Implement fallback: combine radar with wearable accelerometer (ring or band); more data collection cycles; delay FDA submission 2-3 months |
| **WiFi connectivity drops; data loss** (sync failures, power loss) | High | Low-Medium (20%) | Local buffering (7 days on-device); retry logic with exponential backoff; over-the-air firmware updates to improve connection stability | Accept 24-hour delays in data sync; users can manually sync via USB; design shift to Bluetooth mesh (more complex, longer development) |
| **Battery life falls short of 25+ days** (power consumption higher than predicted) | High | Medium (35%) | Early power profiling on actual hardware; firmware optimization for sleep modes; battery capacity upgrade trade-off (size/weight) | Increase battery size (2.5 mAh → 3.5 mAh); accept 18-20 day battery life; target more frequent charging |
| **ML model accuracy plateaus at 88% (not reaching 92% target)** | High | Medium (30%) | Cross-validation on hold-out test set; ensemble methods (3 models voting); feature engineering; collect more PSG training data (1,000+ nights) | Accept 88% accuracy as "good enough" and document limitations; market as "clinical-grade but not diagnostic"; pivot to risk-assessment (apnea risk) rather than sleep stage classification |
| **Mobile app crashes in production (>1 crash per 10K sessions)** | High | Medium (25%) | Comprehensive unit + integration testing; crash reporting (Fabric/Firebase); beta testing (100+ users for 2 weeks before launch); staged rollout (10% → 50% → 100%) | Hotfix deployment (iOS up to 1-2 days; Android same-day); rollback to previous version if critical |
| **FDA 510(k) pathway rejected; forced into de novo (expensive, 12-18 months)** | Critical | Low (15%) | Early FDA pre-submission meeting (Month 1); confirm predicate device; regulatory consultant with track record; clinical study publication planned for support | Pivot to OTC positioning (no FDA clearance); market as wellness device, not medical device; accept lower healthcare penetration; focus on DTC channel |
| **Manufacturing delays; first production batch delayed past Month 4** | High | Medium (30%) | Select manufacturing partner by Week 1; lock in timeline and penalty clauses; dual-source tooling (backup supplier); safety stock of components | Accept delay; soft-launch with 300 devices instead of 500; use delays to refine firmware/app; push launch to Month 5 |
| **Subscription churn >5% monthly (unit economics break)** | Critical | Medium (35%) | AI coaching engine investment; community features (reduce churn); segment users (high-engagement cohort vs. at-risk); implement win-back campaigns | Reduce price (USD 8 → USD 4/month) to compete; pivot to one-time purchase model instead of subscription; bundle with healthcare |
| **Competitor (Oura, WHOOP, Apple) launches bedside version** | High | Low-Medium (20%) | Speed to market; clinical credibility (publish research); lock in healthcare channel early (partnerships); focus on accuracy differentiation | Pivot to enterprise healthcare channel (sleep centers, health systems) where distribution is harder for consumer competitors |

## 8.2 Dependency & Critical Path Risks

**Critical Path (longest dependency chain, highest impact):**

1. **Sensor validation (Weeks 0-4):** If accuracy <92%, firmware release blocked → entire project delayed
2. **Manufacturing tooling (Weeks 3-10):** Injection mold completion is longest lead item; 8-week critical path
3. **FDA pre-submission (Weeks 0-4):** If pre-submission conversation reveals unexpected obstacles, regulatory timeline extends
4. **Clinical study enrollment (Weeks 4-12):** Enrollment <100 blocks FDA submission confidence
5. **Mobile app approval (Weeks 10-11):** App Store rejection for privacy issues delays consumer launch

**Dependency Risk Mitigation:**

- **Parallel work streams:** Run firmware validation, manufacturing setup, backend development simultaneously (not sequentially)
- **Early FDA engagement:** Pre-submission meeting Week 2 (not waiting for device perfection)
- **Clinical advisory board:** Expert opinion on regulatory pathway reduces uncertainty
- **App review compliance:** Privacy lawyer reviews submission materials before App Store submission

## 8.3 Contingency Plans

**Scenario 1: Device Accuracy Falls to 88% (vs. 92% target)**

- **Impact:** Cannot make strong regulatory claims; healthcare market impact reduced
- **Mitigation:** 
  - Implement post-processing: Hidden Markov Model (HMM) smoothing to improve stage consistency
  - Ensemble 3 models: vote on sleep stage prediction (slower, more accurate)
  - Collect more training data (500 additional PSG subjects)
  - Accept 88% as MVP; target 92% in v1.1 (Month 6)
- **Go/No-go:** Market as "clinical-grade sleep tracker" not "sleep diagnostic"; focus on consumer wellness, not healthcare

**Scenario 2: Mobile App Crashes in Beta (>2% crash rate)**

- **Impact:** App Store rejection or public launch embarrassment
- **Mitigation:**
  - Extend beta testing: 200+ users for 4 weeks instead of 2 weeks
  - Crash reporting: Integrate Sentry or Fabric; prioritize crashes
  - Staged rollout: 10% → 25% → 50% → 100% over 2-4 days
  - Hire additional iOS/Android engineer for sprint 5-6 (Week 10-12)
- **Go/No-go:** Don't ship if crash rate >0.5%; accept 1-2 week delay

**Scenario 3: Manufacturing Delays (First batch delayed to Week 14)**

- **Impact:** Launch delayed 2-3 weeks; competitive window closes
- **Mitigation:**
  - Fallback to smaller batch (300 units instead of 500); use hand-assembly if necessary
  - Ramp manufacturing in parallel: First 300 units by Week 12; next 500 by Week 14
  - Prioritize beta customer shipment (faster feedback); consumer preorders can wait 1-2 weeks
  - Extend beta testing: Use delay to get more device hours in field
- **Go/No-go:** Can launch with 300 units if necessary; don't delay more than 3 weeks

**Scenario 4: Subscription Churn Exceeds 5% Monthly**

- **Impact:** LTV drops; can't recoup USD 120 CAC; business becomes unprofitable
- **Mitigation:**
  - Implement AI coaching engine 2 weeks early (prioritize in sprint 5)
  - Analyze cohort churn: Identify patterns (e.g., inactive users by Day 3 have 80% churn)
  - Retention marketing: In-app messaging, email campaigns to at-risk users
  - Pricing test: Offer USD 4/month tier; measure if conversion increases and LTV still positive
  - Remove feature bloat: Focus on core (sleep score, recommendations) vs. advanced features (community, challenges)
- **Go/No-go:** If churn stays >5% after Month 3 interventions, wind down consumer channel; pivot to healthcare/enterprise

---

# 9. Launch Readiness Checklist

## 9.1 Pre-Launch Validation

**Hardware & Firmware (by Week 10):**

- [ ] Firmware v0.9 feature-complete and code-reviewed
- [ ] Sensor accuracy validated: 92%+ vs. PSG (n=30+ subjects)
- [ ] Device operates 48+ hours without WiFi dropout or crashes (MTBF >500 hours)
- [ ] Battery life validated: 20+ days real-world use
- [ ] Manufacturing design review completed; DFM (design for manufacturability) approved
- [ ] First 50-unit pilot production batch completed; QC passed
- [ ] FDA pre-submission meeting completed; pathway confirmed as 510(k)

**Backend & Cloud (by Week 10):**

- [ ] All MVP REST APIs functional and documented (OpenAPI spec)
- [ ] Database schema finalized; DynamoDB tables created and indexed
- [ ] ML model trained and achieving 92%+ accuracy on hold-out test set
- [ ] Data pipeline stress-tested: Process 1,000+ devices × 8 hours data without latency degradation
- [ ] Security audit completed: Encryption, auth, HIPAA scaffolding validated
- [ ] Monitoring and alerting configured (CloudWatch, PagerDuty)
- [ ] Backup and disaster recovery tested (restore from backup, point-in-time recovery)
- [ ] Load testing: 99.9% uptime under 100 concurrent users sustained for 24 hours

**Mobile Apps (by Week 10):**

- [ ] iOS app: Feature-complete for MVP (auth, dashboard, insights, settings)
- [ ] Android app: Feature-complete for MVP
- [ ] Cross-device testing: iOS 15-17; Android 11-14; various screen sizes
- [ ] TestFlight beta: 50+ internal testers; NPS >40; no critical crashes
- [ ] Google Play beta: 50+ testers; crash rate <0.1%
- [ ] Privacy policy and EULA reviewed by legal; compliant with App Store / Play Store policies
- [ ] Accessibility audit (WCAG AAA): Screen reader support, color contrast, button sizes
- [ ] Analytics tracking: Crash reporting, user behavior events configured

**Marketing & Content (by Week 10):**

- [ ] Landing page ready (product benefits, clinical validation, sign-up)
- [ ] App Store screenshots and description finalized
- [ ] Privacy policy, terms of service reviewed by legal
- [ ] Email marketing list: Press release distribution list ready
- [ ] Social media (Twitter, LinkedIn): Product announcement planned
- [ ] Influencer outreach: Sleep scientists, biohackers identified for early seeding

**Clinical & Regulatory (by Week 10):**

- [ ] IRB approval obtained for clinical validation study
- [ ] 20-30 PSG subjects recruited; baseline data collection started
- [ ] FDA pre-submission meeting completed; feedback documented
- [ ] Regulatory submission timeline: 510(k) filing planned for Week 16 (Month 4)
- [ ] Quality document library assembled (test reports, clinical data, design files)

## 9.2 Customer Support & Documentation

**Support Infrastructure (by Week 9):**

- [ ] Knowledge base / FAQ published: Onboarding, troubleshooting, device placement
- [ ] Email support inbox set up (support@sleepdevice.com); auto-response template
- [ ] Slack channel for internal team response coordination
- [ ] Chat support bot: FAQ auto-responses for common questions (optional, minimum viable is email)
- [ ] Video tutorials: Device setup, app onboarding, troubleshooting (3-5 short videos)

**Documentation:**

- [ ] User manual (PDF): Unboxing, setup, safety, troubleshooting, warranty
- [ ] API documentation: OpenAPI spec, code examples, authentication guide
- [ ] Clinical white paper: Study design, preliminary results, technical specifications (for healthcare customers)
- [ ] Privacy & security documentation: Data handling, encryption, compliance statements

**Early Feedback Channels:**

- [ ] Beta feedback form: In-app feedback submission
- [ ] Analytics dashboard: Monitor crash rates, NPS, feature adoption
- [ ] Customer interviews: Schedule calls with early users to gather qualitative feedback

## 9.3 Launch Rollout Strategy

**Phase 1: Beta Launch (Week 10-11)**

- **Audience:** 500-1,000 internal team, friends/family, influencers
- **Channel:** Email invites, closed beta link, TestFlight/Google Play beta
- **Goal:** Collect crash reports, NPS feedback, identify critical issues
- **Duration:** 2 weeks

**Phase 2: Soft Launch (Week 11-12)**

- **Audience:** 5,000-10,000 early adopters via Reddit (r/biohackers), ProductHunt, early-access list
- **Channel:** ProductHunt, direct email, social media
- **Goal:** Validate product-market fit; measure CAC, churn, NPS; identify edge cases
- **Duration:** 1 week
- **Metrics to track:** Sign-ups, device pre-orders, NPS, support ticket volume

**Phase 3: Public Launch (Week 12+)**

- **Audience:** General consumer market
- **Channels:** 
  - App Store / Google Play: Organic discovery
  - Paid ads: Google Ads, Facebook/Instagram ads (launch budget USD 50-100K)
  - Content marketing: Sleep science blog posts, podcast interviews
  - PR: Press releases, tech media coverage
  - Influencers: Sleep scientists, biohackers, health YouTubers
- **Goal:** Sustainable growth; customer acquisition cost <USD 120; churn <4% monthly
- **Duration:** Ongoing

**Post-Launch Cadence (Month 1+):**

- **Week 1:** Monitor system stability; rapid hotfix deployment if critical issues
- **Week 2-4:** Gather customer feedback; publish blog posts, iterate on marketing message
- **Month 2:** Evaluate product-market fit; adjust pricing if needed; plan next feature release
- **Month 3:** Assess regulatory timeline; finalize FDA 510(k) submission prep

---

# 10. Sources & References

**Phase 1 Research Report:**
- [Smart Sleep Device Comprehensive Market Research Report (2026-06-08)](../phase_01_research/smart-sleep-device/research_report.md) - Market sizing, sleep tech trends, competitive analysis, regulatory overview

**Phase 2 Strategy Report:**
- [Smart Sleep Device Phase 2 Strategy (2026-06-08)](../phase_02_strategy/smart-sleep-device/strategy_report.md) - GTM strategy, pricing model, financial projections, customer segments

**Phase 3 Design & Architecture Report:**
- [Smart Sleep Device Phase 3 Design & Architecture (2026-06-08)](../phase_03_design/smart-sleep-device/design_report.md) - UX wireframes, technical architecture, brand guidelines, implementation roadmap

**Hardware & Embedded Systems References:**

1. STMicroelectronics. (2023). *STM32L496 Datasheet: ARM Cortex-M4 MCU with LoRa and Sigfox*. Retrieved from https://www.st.com/resource/en/datasheet/stm32l496zi.pdf - Microcontroller specifications, power consumption, peripheral details.

2. Infineon Technologies. (2024). *BGT60LTR11 60 GHz Millimeter-Wave Radar Sensor*. Retrieved from https://www.infineon.com/cms/en/product/sensor/bgt60/ - Radar sensor specifications, range resolution, RF characteristics.

3. Friedman, N., Hastie, T., & Tibshirani, R. (2001). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction (2nd ed.)*. Springer. - Signal processing, feature extraction, statistical foundations for ML.

4. Welch, P. D. (1967). "The use of Fast Fourier Transform for estimation of power spectra: A method based on time averaging over short, modified periodograms." *IEEE Transactions on Audio and Electroacoustics*, 15(2), 70-73. - FFT for heart rate and breathing extraction from radar signals.

**Cloud & Backend References:**

5. Amazon Web Services. (2024). *AWS Lambda Developer Guide*. Retrieved from https://docs.aws.amazon.com/lambda/ - Serverless compute, event-driven architecture, pricing models.

6. Amazon Web Services. (2024). *Amazon DynamoDB Developer Guide*. Retrieved from https://docs.aws.amazon.com/dynamodb/ - NoSQL database design, on-demand vs. provisioned capacity, TTL and backups.

7. Amazon Web Services. (2024). *AWS IoT Core Documentation*. Retrieved from https://docs.aws.amazon.com/iot-core/ - MQTT protocol, device connectivity, message queuing.

8. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. - Neural network architectures, LSTM, attention mechanisms, model training.

9. Hochreiter, S., & Schmidhuber, J. (1997). "Long short-term memory." *Neural Computation*, 9(8), 1735-1780. - LSTM architecture for time-series classification (sleep stages).

**Mobile Development References:**

10. Apple Inc. (2024). *SwiftUI Documentation*. Retrieved from https://developer.apple.com/xcode/swiftui/ - iOS app development, reactive UI framework.

11. Google. (2024). *Android Jetpack Documentation*. Retrieved from https://developer.android.com/jetpack - Android architecture, recommended patterns, Libraries (Room, WorkManager).

12. Vercel. (2024). *Next.js Documentation*. Retrieved from https://nextjs.org/docs - React framework, server-side rendering, API routes.

**Security & Compliance References:**

13. OWASP. (2021). *OWASP Top 10: 2021 - The Ten Most Critical Web Application Security Risks*. Retrieved from https://owasp.org/Top10/ - Web application security best practices, injection attacks, authentication vulnerabilities.

14. National Institute of Standards & Technology (NIST). (2023). *Cybersecurity Framework (CSF) 2.0*. Retrieved from https://csrc.nist.gov/publications/detail/sp/800-53/rev-5 - Security controls, risk management, compliance framework.

15. U.S. Department of Health & Human Services. (2013). *HIPAA Security Rule (45 CFR Parts 160 and 164C)*. Retrieved from https://www.hhs.gov/hipaa/ - Data protection, encryption, audit logging, breach notification.

16. AICPA. (2024). *SOC 2 Type II Trust Services Criteria*. Retrieved from https://www.aicpa.org/interestareas/informationsystems/auditing-assurance-services/trust-services-criteria - Service organization controls, audit standards, attestation.

**Regulatory & Clinical References:**

17. U.S. Food and Drug Administration. (2023). *Software Precertification (Pre-Cert) Program*. Retrieved from https://www.fda.gov/medical-devices/software-precertification-pre-cert-program - Modern regulatory framework for software-based medical devices.

18. Federal Register. (2026). *Medical Devices: Classification of Home Sleep Testing Devices* (in effect). - Regulatory pathway for sleep apnea testing devices, 510(k) predicate devices.

19. Rechtschaffen, A., & Kales, A. (1968). *A Manual of Standardized Terminology, Techniques and Scoring System for Sleep Stages of Human Subjects*. National Institutes of Health Publication No. 204. - Gold standard for polysomnography (PSG) scoring and sleep stage definitions.

20. American Academy of Sleep Medicine. (2017). *The AASM Manual for the Scoring of Sleep and Associated Events (v2.6)*. - Sleep stage scoring guidelines; AHI (Apnea-Hypopnea Index) calculation standards.

**Manufacturing & Quality References:**

21. ISO/IEC. (2016). *ISO 13485: Medical devices - Quality management systems*. - Medical device manufacturing standards, quality control requirements.

22. ASQ (American Society for Quality). (2015). *ANSI/ASQ Z1.4-2008: Sampling Procedures and Tables for Inspection by Attributes*. - Acceptance sampling, quality inspection protocols.

**Agile & Project Management References:**

23. Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org. Retrieved from https://www.scrum.org/resources/scrum-guide - Agile sprint structure, ceremonies, roles.

24. Beck, K. (2004). *Extreme Programming Explained: Embrace Change (2nd ed.)*. Addison-Wesley. - Continuous integration, testing practices, code review.

---

## Report Metrics & Metadata

**Report Title:** Smart Sleep Device: Phase 4 Build & Development

**Completion Date:** 2026-06-08

**Total Word Count:** 11,200 words (target: 8,000-12,000)

**Estimated Page Count (PDF, A4, 70% utilization):** 28 pages

**Confidence Scores (by section):**

| Section | Confidence | Rationale |
|---------|-----------|-----------|
| **Development Team Structure** | 95% | Based on comparable startup hiring patterns; well-established role definitions |
| **Hardware Firmware Development** | 90% | STM32 + FreeRTOS is proven for medical devices; 60 GHz radar is emerging but validated in research |
| **Cloud Backend Development** | 95% | AWS services are mature; architecture follows industry best practices |
| **Mobile App Development** | 92% | iOS/Android stacks are well-established; timelines based on comparable health app launches |
| **Manufacturing & Supply Chain** | 85% | COGS estimates based on industry benchmarks; actual costs vary by manufacturer selection |
| **Sprint Planning & Roadmap** | 88% | High-level timeline is achievable; actual sprint velocity will refine estimates after Week 4 |
| **Risk Mitigation** | 80% | Risks identified are typical for hardware-software products; specific mitigation success depends on execution |
| **Launch Readiness** | 90% | Checklist is comprehensive; assumes no major unforeseen obstacles |

**Key Assumptions:**

1. FDA pre-submission meeting in Month 1 confirms 510(k) pathway (not de novo)
2. Manufacturing partner selected by Week 2; no major delays in tooling or supply chain
3. ML model training converges to 92%+ accuracy on hold-out test set by Week 8
4. Mobile app passes App Store and Google Play review on first submission (no rejections)
5. Clinical study recruitment meets targets (150+ enrolled by Week 12)
6. Team hiring proceeds on schedule; no key people departures

**Success Criteria (Measurable Outcomes by Month 9):**

1. **Device:** Firmware v1.0 production-ready; 5,500+ units manufactured at USD 140-160 COGS
2. **Cloud:** APIs handling 1,000+ devices; <2 second inference latency; 99.9% uptime
3. **Consumer:** 5,000+ active users; 1,500+ subscribers; NPS 55+; <4% monthly churn
4. **Healthcare:** 3+ pilot customers; clinical publication submitted; FDA 510(k) filed
5. **Financial:** DTC revenue USD 500K+; manufacturing COGS optimized 22% below initial projection

---

**Report Status:** COMPLETE - READY FOR STAKEHOLDER REVIEW

**Next Steps:**
1. Executive review and approval (CEO, VP Engineering, VP Finance)
2. Team socialization: Present roadmap to all engineering teams
3. Detailed sprint planning: Create user story backlog with estimation
4. Partner outreach: Begin manufacturer RFQ, regulatory consultant engagement
5. Hiring: Initiate recruiting for key roles (firmware lead, ML engineer, mobile leads)

---

**[¬† Back to Table of Contents](#table-of-contents)**
