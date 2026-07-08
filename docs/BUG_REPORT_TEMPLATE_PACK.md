# ClimateGuard AI - Bug Report Template Pack

Start here: [Frontend Docs Index](FRONTEND_DOCS_INDEX.md)

This pack standardizes defect reporting for frontend testing and triage.
It is aligned with the QA matrix and clickable blueprint documents.

Visual language note:

- Log visual defects against the weather-light premium baseline (bright background, clear card contrast, climate-readable color semantics).

---

## 1) Severity Rubric

Use this rubric to assign business and technical impact.

| Severity | Label | Definition | User Impact | Release Impact | Target Response | Target Fix |
|---|---|---|---|---|---|---|
| S1 | Critical | Core flow blocked, data loss, security risk, or app crash with no workaround | Major outage for many users | Release blocker | 1 hour | Same day |
| S2 | High | Key feature broken or incorrect results with limited workaround | High impact for affected users | Likely release blocker | 4 hours | 1-2 days |
| S3 | Medium | Feature partially broken, UI mismatch, or non-critical logic error | Moderate impact | Can release with risk acceptance | 1 business day | 3-5 days |
| S4 | Low | Cosmetic issue, copy issue, minor usability polish | Low impact | Not a blocker | 2 business days | Next sprint |

### Severity Decision Rules

- If prediction outputs are wrong for valid input, classify at least S2.
- If routing prevents access to a primary screen, classify S1 or S2.
- If issue only affects one browser/device with workaround, typically S3.
- If issue is visual only and no functional loss, usually S4.
- If weather readability is reduced by low contrast, dense layout, or dark-heavy styling drift, classify at least S3.

---

## 2) Priority Rubric

Priority determines execution order after severity is assigned.

| Priority | Meaning | When to Use |
|---|---|---|
| P0 | Immediate | Active incident, release blocker, legal/security risk |
| P1 | Urgent | High customer impact, near-term release commitment |
| P2 | Planned | Important but not urgent, schedule in current sprint |
| P3 | Backlog | Nice-to-have or low frequency issue |

Mapping guidance:

- S1 -> P0
- S2 -> P1
- S3 -> P2
- S4 -> P3

---

## 3) Reproducible Bug Report Format

Copy this template for each defect.

```text
Bug ID:
Title:
Module/Screen:
Environment: (Dev/Staging/Prod)
Build Version:
Browser/Device:
Reporter:
Date/Time:

Severity: (S1/S2/S3/S4)
Priority: (P0/P1/P2/P3)

Preconditions:
1.
2.

Steps to Reproduce:
1.
2.
3.

Expected Result:

Actual Result:

Reproducibility: (Always/Often/Intermittent/Rare)
Repro Rate: (e.g., 5/5, 3/5)

Impact Scope:
- Users affected:
- Regions affected:
- Features affected:

Workaround:

Attachments:
- Screenshot(s):
- Video:
- Console log:
- Network trace:

Linked QA Test Case IDs:

Notes:
```

---

## 4) Fast Entry Templates

### 4.1 Functional Defect

```text
Title: [Functional] Rainfall prediction request fails on valid coordinates
Module/Screen: Rainfall Prediction
Severity: S2
Priority: P1
Steps:
1. Open Rainfall Prediction
2. Enter valid latitude and longitude
3. Click Predict
Expected: Probability, confidence, and explanation shown
Actual: Error message shown, no prediction returned
Linked QA ID: RAIN-004
```

### 4.2 UI/UX Defect

```text
Title: [UI] KPI cards overlap on tablet viewport
Module/Screen: Dashboard
Severity: S3
Priority: P2
Steps:
1. Open Dashboard on tablet viewport
2. Observe KPI row
Expected: Cards wrap cleanly with no overlap
Actual: Cards overlap and hide values
Linked QA ID: DASH-002, XSYS-005
```

### 4.3 Data Accuracy Defect

```text
Title: [Data] Heatwave severity label does not match score band
Module/Screen: Heatwave Prediction
Severity: S2
Priority: P1
Steps:
1. Trigger heatwave prediction with high-temperature scenario
2. Observe score and severity chip
Expected: Severity category matches configured thresholds
Actual: Severity displays lower category than score indicates
Linked QA ID: HEAT-004
```

---

## 5) Triage Workflow

### 5.1 Workflow Stages

1. Intake
2. Validation
3. Classification
4. Assignment
5. Fix and Verification
6. Closure

### 5.2 Status Lifecycle

| Status | Owner | Exit Criteria |
|---|---|---|
| New | QA | Report includes reproducible steps and evidence |
| Triaged | QA Lead or Product | Severity, priority, owner, and target release set |
| In Progress | Developer | Root cause identified and fix in development |
| Ready for QA | Developer | Fix merged and deployed to test environment |
| Verified | QA | Retest passed with evidence |
| Closed | QA Lead or Product | Verification complete and no regressions observed |
| Reopened | QA | Issue persists or regressed |

### 5.3 Triage Meeting Checklist

- Confirm reproducibility and environment details
- Confirm affected module and linked QA test IDs
- Assign severity and priority using rubric
- Decide release impact and fix target
- Assign owner and due date
- Record risks and dependencies

---

## 6) SLA and Ownership Guidance

| Severity | Engineering Ack | Triage Complete | Fix ETA Set | QA Retest SLA |
|---|---|---|---|---|
| S1 | 1 hour | 2 hours | Same day | Within 4 hours of deploy |
| S2 | 4 hours | Same day | 1-2 days | Within 1 business day |
| S3 | 1 business day | 2 business days | 3-5 days | Within 2 business days |
| S4 | 2 business days | 3 business days | Next sprint | As scheduled |

---

## 7) Exit Criteria for Closure

A bug can be closed only if all are true:

- Repro steps no longer produce issue in target build
- Expected behavior matches QA matrix requirement
- No major side-effect in adjacent module
- Evidence attached (screenshot/video/log)
- Linked test case marked Pass

---

## 8) Defect Naming Convention

Use a consistent title pattern:

`[Type] [Screen/Module] Short symptom statement`

Examples:

- [Functional] Rainfall Prediction returns error on valid input
- [UI] Dashboard KPI card text truncates on mobile
- [Data] Risk Score category mismatched with score threshold
- [Performance] Maps layer switch takes over 5 seconds

---

## 9) Recommended Labels for Tracker

- `area:dashboard`
- `area:climate-profile`
- `area:rainfall`
- `area:heatwave`
- `area:anomaly`
- `area:risk-score`
- `area:explainable-ai`
- `area:reports`
- `area:maps`
- `area:history`
- `area:settings`
- `type:functional`
- `type:ui`
- `type:data`
- `type:performance`
- `severity:s1|s2|s3|s4`
- `priority:p0|p1|p2|p3`

---

## 10) Related Documents

- [Frontend UI Structure](FRONTEND_UI_STRUCTURE.md)
- [Frontend Clickable Blueprint](FRONTEND_CLICKABLE_BLUEPRINT.md)
- [Frontend QA Test Matrix](FRONTEND_QA_TEST_MATRIX.md)
- [Release Readiness Checklist](RELEASE_READINESS_CHECKLIST.md)
