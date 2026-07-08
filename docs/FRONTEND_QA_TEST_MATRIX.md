# ClimateGuard AI - Frontend QA Test Matrix

Start here: [Frontend Docs Index](FRONTEND_DOCS_INDEX.md)

This document converts the frontend blueprint into an execution-ready QA matrix.
Use it for manual QA, UAT, and automation planning.

Style baseline for all test observations:

- Validate against the weather-light premium visual language used in the UI structure.
- Prefer bright, clear, climate-readable layouts with white cards and soft sky backgrounds.
- Treat dark, crowded, or low-contrast weather views as UX defects when readability is affected.

---

## 1) Execution Rules

- Test each case on Desktop, Tablet, and Mobile breakpoints.
- Validate success, loading, empty, and error states where applicable.
- Capture evidence (screenshot/video/log) for failed cases.
- Mark each test as: `Pass`, `Fail`, `Blocked`, or `Not Run`.

Status template:

| Status | Meaning |
|---|---|
| Pass | Behavior matches expected result |
| Fail | Behavior deviates from expected result |
| Blocked | Cannot execute due to dependency/environment |
| Not Run | Test not executed yet |

---

## 2) Dashboard Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| DASH-001 | Dashboard | Dashboard loads successfully | App is running | Open `/` | Page header and core sections render without crash |
| DASH-002 | Dashboard | KPI cards render data | Backend reachable | Load dashboard | Risk Score, AI Models, Predictions, Alerts cards show values |
| DASH-003 | Dashboard | Quick action navigation works | Dashboard loaded | Click each quick action button | User is routed to mapped destination screen |
| DASH-004 | Dashboard | Map block default state | Dashboard loaded | Observe interactive map area | Map area appears with default location and no visual break |
| DASH-005 | Dashboard | Recent predictions list | Historical data exists | Open dashboard | Recent predictions panel shows latest rows in order |
| DASH-006 | Dashboard | AI insights panel | Insights available | Open dashboard | AI insight text/cards are visible and readable |
| DASH-007 | Dashboard | Loading state | Slow network simulation | Reload dashboard | Skeleton/spinner appears before content loads |
| DASH-008 | Dashboard | Error state | Backend unavailable | Reload dashboard | User-friendly error message shown with retry option |

---

## 3) Climate Profiling Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| PROF-001 | Climate Profiling | Screen renders | App running | Open `/climate-profiles` | Screen sections load correctly |
| PROF-002 | Climate Profiling | Location selector fields | Screen loaded | Inspect selector controls | Country/State/District/Coordinates inputs are present |
| PROF-003 | Climate Profiling | Summary metrics display | Valid location selected | Trigger profile load | Temperature/Rainfall/Humidity/Wind/Pressure shown with units |
| PROF-004 | Climate Profiling | Historical trend chart | Profile data available | Scroll to trends section | Historical chart renders with proper axis labels |
| PROF-005 | Climate Profiling | Monthly chart interactions | Chart loaded | Hover chart points/bars | Tooltip values are accurate and readable |
| PROF-006 | Climate Profiling | Download profile action | Data loaded | Click download control | File downloads successfully and is non-empty |

---

## 4) Rainfall Prediction Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| RAIN-001 | Rainfall Prediction | Screen renders | App running | Open `/rainfall` | All prediction blocks render |
| RAIN-002 | Rainfall Prediction | Location input validation | Screen loaded | Enter invalid coordinates | Validation error appears, no prediction request sent |
| RAIN-003 | Rainfall Prediction | Period selector behavior | Screen loaded | Switch 7/30/Seasonal | Selection updates and chart refreshes accordingly |
| RAIN-004 | Rainfall Prediction | Prediction API success | Backend reachable | Submit prediction | Chart, probability gauge, confidence score update |
| RAIN-005 | Rainfall Prediction | Explanation text | Prediction completed | Check explanation section | Explanation mentions key contributors/factors |
| RAIN-006 | Rainfall Prediction | API failure handling | Backend returns error | Submit prediction | Error toast/message shown, UI remains usable |

---

## 5) Heatwave Prediction Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| HEAT-001 | Heatwave Prediction | Screen renders | App running | Open `/heatwave` | Layout and controls appear correctly |
| HEAT-002 | Heatwave Prediction | Forecast day selector | Screen loaded | Change forecast days | Forecast chart horizon updates |
| HEAT-003 | Heatwave Prediction | Prediction output | Backend reachable | Run prediction | Probability and severity indicator appear |
| HEAT-004 | Heatwave Prediction | Severity color mapping | Prediction available | Observe severity chip | Low/Moderate/High map to correct design tokens |
| HEAT-005 | Heatwave Prediction | Recommendations adapt | Severity available | Compare low vs high outputs | Preventive recommendations update by severity |

---

## 6) Anomaly Detection Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| ANOM-001 | Anomaly Detection | Screen renders | App running | Open `/anomaly` | Main sections and controls display |
| ANOM-002 | Anomaly Detection | Timeline rendering | Data available | Run detection | Timeline shows anomaly points/events |
| ANOM-003 | Anomaly Detection | Events table sorting | Table loaded | Sort by score/time | Rows reorder correctly |
| ANOM-004 | Anomaly Detection | Anomaly score card | Detection complete | Observe score panel | Score and confidence are shown |
| ANOM-005 | Anomaly Detection | Historical comparison | Baseline data exists | Open comparison section | Current vs historical view is visible and coherent |

---

## 7) Climate Risk Score Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| RISK-001 | Climate Risk Score | Screen renders | App running | Open `/risk-score` | Screen sections load successfully |
| RISK-002 | Climate Risk Score | Score scale integrity | Score available | Inspect displayed score | Score is between 0 and 100 |
| RISK-003 | Climate Risk Score | Category mapping | Score available | Verify category label | Label matches configured score band |
| RISK-004 | Climate Risk Score | Contributors list | Data available | Check contributors panel | At least Temperature/Rainfall/Humidity/Wind/Pressure appear |
| RISK-005 | Climate Risk Score | Regional comparison chart | Data available | View comparison section | Region chart/table renders and is readable |

---

## 8) Explainable AI Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| XAI-001 | Explainable AI | Screen renders | App running | Open `/explainable-ai` | Explainability sections appear |
| XAI-002 | Explainable AI | Feature ranking | Prediction available | Open feature list | Features sorted by contribution magnitude |
| XAI-003 | Explainable AI | Contribution chart | Data available | Inspect contribution chart | Positive and negative impacts are distinguishable |
| XAI-004 | Explainable AI | Confidence visibility | Prediction available | View summary area | Confidence score is present near summary |
| XAI-005 | Explainable AI | Narrative explanation quality | Explanation returned | Read AI explanation text | Text is coherent, actionable, and climate-domain relevant |
| XAI-006 | Explainable AI | Model information panel | Metadata available | Open model info section | Model name/version/date are displayed |

---

## 9) Reports Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| REPT-001 | Reports | Screen renders | App running | Open `/reports` | Search/filter/date controls and table render |
| REPT-002 | Reports | Search behavior | Reports exist | Enter search query | Results filtered to matching rows |
| REPT-003 | Reports | Date filter behavior | Reports exist | Apply date range | Results constrained to selected dates |
| REPT-004 | Reports | Export PDF | Results present | Click Export PDF | Valid non-empty PDF downloaded |
| REPT-005 | Reports | Export Excel | Results present | Click Export Excel | Valid non-empty Excel file downloaded |
| REPT-006 | Reports | Export CSV | Results present | Click Export CSV | Valid non-empty CSV downloaded |
| REPT-007 | Reports | Table pagination/sort | Many rows present | Change page/sort column | Behavior is correct and stable |

---

## 10) Maps Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| MAP-001 | Maps | Screen renders | App running | Open `/maps` | Map canvas and control panel are visible |
| MAP-002 | Maps | Layer toggles | Map loaded | Toggle temperature/rainfall/heatwave/risk | Layer visibility updates correctly |
| MAP-003 | Maps | Legend updates by layer | Layers available | Switch layers | Legend labels/colors update with active layer |
| MAP-004 | Maps | Region selection | Map loaded | Select a region | Region comparison panel updates with selected region |

---

## 11) History Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| HIST-001 | History | Screen renders | App running | Open `/history` | History list and filters render |
| HIST-002 | History | Search/filter behavior | History exists | Apply query/filter | List updates to matched entries |
| HIST-003 | History | Entry details view | History exists | Open an entry | Correct analysis details are shown |
| HIST-004 | History | Download result | Artifact available | Click download on entry | Correct file downloads |

---

## 12) Settings Test Matrix

| Test ID | Screen | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| SET-001 | Settings | Categories visible | App running | Open `/settings` | All settings groups are listed |
| SET-002 | Settings | Appearance preference persistence | Settings editable | Change theme/layout preference and reload | Preference persists after reload |
| SET-003 | Settings | Notification settings persistence | Settings editable | Update notification toggles and reload | Notification preferences persist |
| SET-004 | Settings | Sensitive action confirmation | Sensitive action present | Trigger sensitive change | Confirmation step required before apply |
| SET-005 | Settings | API key field protection | API key setting present | Enter/update key | Input masked and securely handled in UI |

---

## 13) Cross-Screen and Non-Functional Matrix

| Test ID | Scope | Test Case | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| XSYS-001 | Navigation | Sidebar routing | App running | Click each sidebar route | Correct screen opens, active item highlighted |
| XSYS-002 | Navigation | Breadcrumb correctness | Nested screen opened | Inspect breadcrumb | Breadcrumb reflects current route path |
| XSYS-003 | Feedback | Toast behavior | Trigger success and error flows | Perform operations | Proper success/error toasts displayed |
| XSYS-004 | Responsiveness | Mobile layout | Small viewport | Navigate key screens | No overlap/cutoff; controls remain usable |
| XSYS-005 | Responsiveness | Tablet layout | Medium viewport | Navigate key screens | Grid and spacing adapt correctly |
| XSYS-006 | Accessibility | Keyboard navigation | App loaded | Tab through controls | Logical tab order with visible focus indicators |
| XSYS-007 | Accessibility | Contrast compliance | App loaded | Verify key text/background pairs | Meets WCAG AA contrast threshold |
| XSYS-010 | Visual Consistency | Weather-light premium consistency | App loaded | Review key screens for visual baseline | Background, cards, and semantic colors match weather-light design language |
| XSYS-008 | Reliability | API timeout handling | Simulate slow/timeout API | Trigger data load | Graceful timeout message and retry option |
| XSYS-009 | Reliability | Offline handling | Disable network | Refresh or trigger action | Offline-aware error shown; app does not crash |

---

## 14) Traceability to Blueprint

| Blueprint Section | QA Coverage |
|---|---|
| Route Map | Sections 2-13 |
| Global Layout Blueprint | Sections 2 and 13 |
| Component Hierarchy | Sections 2-13 |
| Screen Blueprints | Sections 2-12 |
| Acceptance Checklists | Full matrix |
| Accessibility | Sections 13 and 9 in blueprint |
| Definition of Done | Full matrix closure criteria |

---

## 15) Test Execution Log Template

Copy this table for daily execution tracking.

| Date | Tester | Build Version | Environment | Test ID | Status | Defect ID | Notes |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | Name | vX.Y.Z | Dev/Staging/Prod | DASH-001 | Pass/Fail/Blocked/Not Run | BUG-123 | Observation |

---

## Related Documents

- [Frontend UI Structure](FRONTEND_UI_STRUCTURE.md)
- [Frontend Clickable Blueprint](FRONTEND_CLICKABLE_BLUEPRINT.md)
- [Bug Report Template Pack](BUG_REPORT_TEMPLATE_PACK.md)
- [Release Readiness Checklist](RELEASE_READINESS_CHECKLIST.md)
