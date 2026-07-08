# ClimateGuard AI - Release Readiness Checklist

Start here: [Frontend Docs Index](FRONTEND_DOCS_INDEX.md)

This document defines objective release gates for frontend and integrated climate prediction flows.
It maps QA pass rates, open defect thresholds, and go/no-go criteria.

Visual quality alignment:

- Release candidates must stay consistent with the weather-light premium design baseline defined in the UI structure document.

---

## 1) Release Decision Framework

Use one of three outcomes per release candidate:

- Go: All mandatory gates pass.
- Conditional Go: Non-blocking gaps accepted by product and engineering leads.
- No-Go: Any blocker gate fails.

Decision owners:

- Product Owner
- QA Lead
- Engineering Lead

---

## 2) Quality Gates (Mandatory)

| Gate ID | Gate | Threshold | Status (Pass/Fail) | Notes |
|---|---|---|---|---|
| GATE-01 | Build Integrity | Frontend build succeeds with 0 blocking errors |  |  |
| GATE-02 | App Availability | Core routes load without crash |  |  |
| GATE-03 | API Health | `/health` is healthy in target environment |  |  |
| GATE-04 | Core Flow Validation | Rainfall, Heatwave, Anomaly, Profile flows validated |  |  |
| GATE-05 | Regression Coverage | 100% of critical test cases executed |  |  |
| GATE-06 | Accessibility Baseline | Keyboard navigation and contrast checks pass |  |  |
| GATE-07 | Security/Secrets Check | No exposed secrets or unsafe client config |  |  |
| GATE-08 | Release Notes Ready | Scope, known issues, and rollback details prepared |  |  |

A failed mandatory gate should default to No-Go unless explicitly waived.

---

## 3) QA Pass Rate Criteria

### 3.1 Target Pass Rates

| Test Scope | Minimum Pass Rate |
|---|---|
| Critical tests | 100% |
| High-priority tests | >= 98% |
| Full regression suite | >= 95% |

### 3.2 Coverage Requirement

- All critical screens must be tested:
  - Dashboard
  - Climate Profiling
  - Rainfall Prediction
  - Heatwave Prediction
  - Anomaly Detection
  - Climate Risk Score
  - Explainable AI

### 3.3 Evidence Requirement

- Failed tests must include defect IDs.
- Blocked tests must include blocker reason and owner.

---

## 4) Open Defect Thresholds

### 4.1 Hard Stop Rules

Release must be No-Go if any of the following exists:

- Any open S1 defect.
- More than 2 open S2 defects in release scope.
- Any unresolved defect that breaks a core prediction flow.

### 4.2 Allowed Open Defects for Go

| Severity | Maximum Open Allowed | Conditions |
|---|---|---|
| S1 | 0 | Never allowed |
| S2 | 0-2 | Must have approved workaround and fix target date |
| S3 | <= 8 | Must be documented in known issues |
| S4 | <= 20 | Deferred to backlog with owner |

### 4.3 Defect Aging Rule

- Any S2 defect open for more than 7 days requires leadership review.
- Any defect reopened twice must be escalated in triage.

---

## 5) Go/No-Go Decision Matrix

| Condition | Decision |
|---|---|
| All mandatory gates pass, pass-rate targets met, defect thresholds within limits | Go |
| Minor gate deviation with approved mitigation and no S1 | Conditional Go |
| Any hard stop rule triggered | No-Go |

Conditional Go requires explicit sign-off from Product, QA, and Engineering leads.

---

## 6) Pre-Release Checklist (Execution)

Mark each item as Yes/No.

### 6.1 Build and Environment

- [ ] Frontend build succeeds in release pipeline.
- [ ] Backend service boots successfully in target environment.
- [ ] API base URL and environment variables are correct.
- [ ] Open-Meteo integration endpoint reachable and returning valid payload.

### 6.2 Functional Verification

- [ ] Dashboard loads KPIs and summary data.
- [ ] Rainfall flow works end-to-end.
- [ ] Heatwave flow works end-to-end.
- [ ] Anomaly flow works end-to-end.
- [ ] Climate profile flow works end-to-end.

### 6.3 UX and Accessibility

- [ ] Responsive behavior validated (desktop/tablet/mobile).
- [ ] Keyboard navigation validated.
- [ ] Critical color contrast checks passed.
- [ ] Weather-light premium visual consistency validated on key screens.
- [ ] Empty/error/loading states verified for API failures.

### 6.4 Data and Reporting

- [ ] Reports export actions function and produce valid files.
- [ ] History screen reflects recent prediction runs.
- [ ] Explainable AI sections render required insight blocks.

### 6.5 Operational Readiness

- [ ] Monitoring/alerting for API health is active.
- [ ] Rollback instructions are tested and available.
- [ ] Release notes and known issues are published.
- [ ] On-call owner assigned for release window.

---

## 7) Risk Assessment Table

| Risk Area | Example Risk | Probability (L/M/H) | Impact (L/M/H) | Mitigation | Owner |
|---|---|---|---|---|---|
| Integration | Weather API timeout spikes |  |  | Retry and timeout fallback UI |  |
| Data Accuracy | Incorrect severity mapping |  |  | Threshold validation tests |  |
| UX | Mobile layout overlap |  |  | Responsive QA sweep |  |
| Operations | Missing rollback notes |  |  | Pre-release release-note gate |  |

Use this table in the final go/no-go meeting.

---

## 8) Release Sign-Off Sheet

| Role | Name | Decision (Go/Conditional Go/No-Go) | Signature/Approval | Timestamp |
|---|---|---|---|---|
| Product Owner |  |  |  |  |
| QA Lead |  |  |  |  |
| Engineering Lead |  |  |  |  |

---

## 9) Post-Release Validation Checklist

- [ ] Smoke tests pass in production-like environment.
- [ ] No new S1/S2 incidents in first monitoring window.
- [ ] Key user journeys validated after deployment.
- [ ] Release dashboard metrics within normal range.
- [ ] Any hotfixes documented and linked to defect IDs.

---

## 10) Rollback Trigger Criteria

Rollback should be initiated if any condition is met:

- Core route or prediction flow unavailable for > 10 minutes.
- New S1 defect detected post-release.
- Data integrity issue affecting predictions or reports.
- Error rate exceeds agreed threshold for 15+ minutes.

---

## 11) Related Documents

- [Frontend UI Structure](FRONTEND_UI_STRUCTURE.md)
- [Frontend Clickable Blueprint](FRONTEND_CLICKABLE_BLUEPRINT.md)
- [Frontend QA Test Matrix](FRONTEND_QA_TEST_MATRIX.md)
- [Bug Report Template Pack](BUG_REPORT_TEMPLATE_PACK.md)
