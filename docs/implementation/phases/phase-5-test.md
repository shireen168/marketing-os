# Phase 5: Testing (Day 7-8)

**Goal:** Rigorous testing. Health data = zero tolerance for bugs.

**Skills:** 7  
**Outcome:** QA passed, beta ready, rollout strategy locked  
**End checkpoint:** `/context-save`

---

## Skill 28: `/qa`

**Full QA testing. User behavior, edge cases, regressions.**
- Test: Sleep tracking accuracy (compare to manual entry)
- Test: Battery drain over 8-hour sleep tracking
- Test: Sync reliability when device goes offline
- Test: UI still works on Day 50 of continuous tracking
- Output: QA report + bug tracker

**Next:** Skill 29 (`/qa-only`)

---

## Skill 29: `/qa-only`

**Edge case testing. Timezone changes, DST, offline.**
- Test: User travels East (loses 8 hours) → does tracking sync break?
- Test: DST change (spring forward) → does midnight become 1am?
- Test: Offline for 3 days → does sync queue overflow?
- Test: Battery at 1% → does app crash?
- Output: Edge case bug fixes

**Next:** Skill 30 (`/benchmark`)

---

## Skill 30: `/benchmark`

**Performance testing. Battery drain, sync latency, memory.**
- Measure: Battery drain per night (1%? 5%? 20%?)
- Measure: Sync latency (how long until cloud sees data?)
- Measure: Memory footprint (on 4GB phone, how much RAM used?)
- Measure: CPU usage during sleep tracking (constant or periodic?)
- Output: Performance baseline + optimization roadmap

**Next:** Skill 31 (`/benchmark-models`)

---

## Skill 31: `/benchmark-models`

**Compare sleep tracking algorithms.**
- Model A: Simple (low motion = deep sleep, zero motion = deep sleep)
- Model B: Complex (PPG + accelerometer + temperature + humidity)
- Model C: ML-based (trained on 1000 labeled sleep sessions)
- Test: Accuracy vs battery vs latency for each
- Output: Model comparison + chosen algorithm

**Next:** Skill 32 (`/careful`)

---

## Skill 32: `/careful`

**High-stakes rollout planning. Health data = no room for error.**
- Rollout: Beta → 1% users → 10% → 100%
- Kill switch: If crash rate > 5%, auto-revert
- Monitoring: Alert if 10+ users report sleep data loss
- Failsafe: Health data can never be silently dropped
- Output: Rollout checklist + monitoring rules

**Next:** Skill 33 (`/canary`)

---

## Skill 33: `/canary`

**Safe rollout to beta users only.**
- Release: To closed beta group only (100-1000 users)
- Collect: Crash reports, accuracy feedback, battery data
- Gate: Don't go public until 99.5% uptime + zero data loss
- Monitor: User feedback on accuracy, battery, UX friction
- Output: Beta launch complete, ready for Phase 6

**Next:** Skill 34 (`/browse`)

---

## Skill 34: `/browse`

**Visual testing. Screenshots, responsive design, dark mode.**
- Test: Onboarding on iPhone SE (small screen)
- Test: Sleep graph on iPad (large screen)
- Test: Dark mode compatibility
- Screenshots: Use for app store listing
- Output: Visual approval + app store screenshots ready

**Next:** Save your work (`/context-save`)

---

## 🔄 Checkpoint: `/context-save`

**Save all testing + rollout decisions.**

Use this at end of Day 8:
```
/context-save
# Captures: QA results, performance benchmarks, 
#           rollout strategy, screenshots, beta feedback
```

**Resume Day 9 morning** with `/context-restore` before Phase 6.

---

## What You Have Now

✓ QA passed (no obvious bugs)  
✓ Edge cases handled (timezone, offline, DST)  
✓ Performance acceptable (battery, latency, memory)  
✓ Algorithm chosen (accuracy vs performance tradeoff)  
✓ Rollout strategy locked (safe beta first)  
✓ Beta ready (100-1000 users testing)  
✓ Visual approved (screenshots ready)  
✓ Zero data loss guarantee (health data protected)  
✓ All decisions saved (zero context loss)

---

## Next Phase

→ [**Phase 6: Launch (Day 8-10)**](./phase-6-launch.md)  
Resume with `/context-restore` before starting Phase 6.

