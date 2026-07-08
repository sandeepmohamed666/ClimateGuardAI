# ClimateGuard AI - Clickable Frontend Blueprint

Start here: [Frontend Docs Index](FRONTEND_DOCS_INDEX.md)

This document is a weather-light premium frontend blueprint for planning and validation.
It defines route map, component hierarchy, and acceptance checklists without implementation code.

Visual language alignment:

- Light-first weather tone with calm sky-inspired accents
- Clean white cards over soft background surfaces
- Minimal and readable information hierarchy for climate insights

---

## Blueprint Navigation

- [1. Route Map](#1-route-map)
- [2. Global Layout Blueprint](#2-global-layout-blueprint)
- [3. Component Hierarchy](#3-component-hierarchy)
- [4. Screen Blueprints](#4-screen-blueprints)
- [5. Screen Acceptance Checklists](#5-screen-acceptance-checklists)
- [6. State and Data Contract Map](#6-state-and-data-contract-map)
- [7. Interaction and UX Rules](#7-interaction-and-ux-rules)
- [8. Analytics and Event Blueprint](#8-analytics-and-event-blueprint)
- [9. Accessibility Checklist](#9-accessibility-checklist)
- [10. Definition of Done](#10-definition-of-done)

---

## 1) Route Map

### Primary App Routes

| Route | Screen Name | Purpose | Data Source |
|---|---|---|---|
| `/` | Dashboard | Overview of platform health, quick actions, KPIs, and live map/charts | `/health`, `/predict/from-location` |
| `/climate-profiles` | Climate Profiling | Region climate summary, trends, and profile classification | `/weather/current`, `/predict/from-location` (mode: `profile`) |
| `/rainfall` | Rainfall Prediction | Rainfall probability and confidence over selected period | `/weather/current`, `/predict/from-location` (mode: `rainfall`) |
| `/heatwave` | Heatwave Prediction | Heatwave probability, severity, and recommendations | `/weather/current`, `/predict/from-location` (mode: `heatwave`) |
| `/anomaly` | Anomaly Detection | Detect unusual climate patterns and anomaly score | `/weather/current`, `/predict/from-location` (mode: `anomaly`) |
| `/risk-score` | Climate Risk Score | Unified risk category and factor contributions | Aggregated from prediction APIs |
| `/explainable-ai` | Explainable AI | Feature importance and model reasoning | Explainability endpoint or transformed prediction outputs |
| `/reports` | Reports | Search/filter previous reports and export | Report service or generated artifacts |
| `/maps` | Maps | Layered climate map and regional comparison | Weather + prediction overlays |
| `/history` | History | Past predictions and trend review | History storage service |
| `/settings` | Settings | Preferences and configuration | Local/user profile settings |
| `/help` | Help | Product support and glossary | Static content |

### Route Grouping

- `Core Intelligence`: `/`, `/climate-profiles`, `/rainfall`, `/heatwave`, `/anomaly`, `/risk-score`, `/explainable-ai`
- `Operational`: `/reports`, `/maps`, `/history`
- `System`: `/settings`, `/help`

---

## 2) Global Layout Blueprint

```text
AppShell
├─ TopNav (search, alerts, profile)
├─ Sidebar (primary navigation)
├─ BreadcrumbBar
├─ MainViewport
│  ├─ PageHeader
│  ├─ ContentSections
│  └─ StickyActionBar (contextual actions)
└─ GlobalLayers
   ├─ ToastHost
   ├─ DialogHost
   └─ CommandPalette
```

### Layout Rules

- Top navigation is sticky.
- Sidebar is collapsible and persists expanded/collapsed state.
- Main viewport uses a 12-column responsive grid.
- KPI cards appear above fold on desktop and stacked on mobile.
- Dialogs can use light glassmorphism; cards remain solid white.

### Weather-Light UI Direction

- Base background should remain bright and airy (`#F8FAFC` with soft accent `#EEF6FF`).
- Climate states should use clear semantic colors only (Success/Warning/Danger), never neon-heavy palettes.
- Map and chart containers should preserve high contrast and low visual noise for forecast readability.

---

## 3) Component Hierarchy

```text
App
└─ AppShell
   ├─ TopNav
   │  ├─ Brand
   │  ├─ GlobalSearch
   │  ├─ AlertsBell
   │  └─ UserMenu
   ├─ SidebarNav
   │  ├─ NavSection(Core Intelligence)
   │  ├─ NavSection(Operational)
   │  └─ NavSection(System)
   ├─ BreadcrumbBar
   ├─ PageContainer
   │  ├─ DashboardPage
   │  ├─ ClimateProfilePage
   │  ├─ RainfallPage
   │  ├─ HeatwavePage
   │  ├─ AnomalyPage
   │  ├─ RiskScorePage
   │  ├─ ExplainableAIPage
   │  ├─ ReportsPage
   │  ├─ MapsPage
   │  ├─ HistoryPage
   │  ├─ SettingsPage
   │  └─ HelpPage
   └─ GlobalUI
      ├─ ToastNotifications
      ├─ LoadingOverlays
      └─ ErrorBoundaryViews
```

### Shared UI Blocks

- `KpiCard`
- `FilterPanel`
- `DateRangePicker`
- `LocationSelector`
- `ChartCard`
- `MapCard`
- `DataTable`
- `InsightPanel`
- `ExportActions`
- `StatusBadge`

---

## 4) Screen Blueprints

### 4.1 Dashboard

Sections:

- Welcome Hero
- Quick Actions
- KPI Row: Risk Score, AI Models, Predictions, Alerts
- Interactive Climate Dashboard (map + current status)
- Recent Predictions
- AI Insights

Primary CTAs:

- Climate Analysis
- Generate Prediction
- View Risk Score
- AI Assistant

### 4.2 Climate Profiling

Sections:

- Location Selector
- Climate Summary Metrics
- Historical Trend Block
- Monthly Charts
- Download/Export Profile

### 4.3 Rainfall Prediction

Sections:

- Location + Prediction Period
- Predicted Rainfall Chart
- Probability Gauge
- Confidence Score
- Prediction Explanation

### 4.4 Heatwave Prediction

Sections:

- Location + Forecast Days
- Temperature Forecast
- Heatwave Probability
- Severity Indicator
- Preventive Recommendations

### 4.5 Anomaly Detection

Sections:

- Dataset/Location Selector
- Anomaly Timeline
- Detected Events Table
- Anomaly Score Summary
- Historical Comparison

### 4.6 Climate Risk Score

Sections:

- Overall Risk (0-100)
- Category Band (Low/Moderate/High/Extreme)
- Risk Contributors
- Regional Comparison

### 4.7 Explainable AI

Sections:

- Prediction Summary
- Feature Importance
- Contribution Chart
- Confidence Score
- Narrative Explanation
- Model Information

### 4.8 Reports

Sections:

- Search + Filters + Date Range
- Report List/Table
- Export Actions (PDF/Excel/CSV)

### 4.9 Maps

Sections:

- Layer Controls
- Interactive Map Canvas
- Region Comparison
- Legend

### 4.10 History

Sections:

- Search + Filter
- Previous Analyses List
- Download Results

### 4.11 Settings

Sections:

- General
- Appearance
- Notifications
- Location Preferences
- AI Model Preferences
- API Keys
- Security
- About

---

## 5) Screen Acceptance Checklists

Use these as QA and sign-off criteria.

### 5.1 Dashboard Checklist

- [ ] Welcome message and subtitle render correctly.
- [ ] All 4 KPI cards are visible and populated.
- [ ] Quick action buttons are actionable and route correctly.
- [ ] Interactive map area loads with default location state.
- [ ] Recent Predictions list shows latest entries.
- [ ] AI Insights panel displays at least one recommendation.
- [ ] Loading and error states are visible when APIs fail.

### 5.2 Climate Profiling Checklist

- [ ] Location selector supports country/state/district/coordinates.
- [ ] Climate summary metrics load with units.
- [ ] Historical trend section renders with date axis.
- [ ] Monthly chart supports hover tooltip.
- [ ] Download action exports profile artifact.

### 5.3 Rainfall Prediction Checklist

- [ ] Period selector supports 7/30/seasonal views.
- [ ] Rainfall chart updates based on selected period.
- [ ] Probability gauge displays value and band color.
- [ ] Confidence score appears with last-updated timestamp.
- [ ] Explanation block references top contributors.

### 5.4 Heatwave Prediction Checklist

- [ ] Forecast days selector updates chart horizon.
- [ ] Heatwave probability updates after prediction request.
- [ ] Severity indicator displays category with color token.
- [ ] Preventive recommendations adapt to severity level.

### 5.5 Anomaly Detection Checklist

- [ ] Timeline highlights anomaly points.
- [ ] Detected events table supports sorting and filtering.
- [ ] Anomaly score card displays score and confidence.
- [ ] Historical comparison shows previous baseline window.

### 5.6 Climate Risk Score Checklist

- [ ] Overall score shown on a 0-100 scale.
- [ ] Category band maps score to correct label.
- [ ] Contributor panel shows at least 5 factors.
- [ ] Regional comparison visual is present and readable.

### 5.7 Explainable AI Checklist

- [ ] Feature importance list is ranked.
- [ ] Contribution chart visually maps positive/negative effects.
- [ ] Confidence score is visible near the prediction summary.
- [ ] Narrative explanation is readable and domain-relevant.
- [ ] Model info includes model name/version/date.

### 5.8 Reports Checklist

- [ ] Search and filters apply without page refresh.
- [ ] Date range filtering narrows result set.
- [ ] Export buttons generate non-empty files.
- [ ] Table supports pagination and sorting.

### 5.9 Maps Checklist

- [ ] Layer toggles for temperature/rainfall/heatwave/risk work.
- [ ] Legend updates when layer changes.
- [ ] Region comparison panel updates on map selection.

### 5.10 History Checklist

- [ ] Prior analyses are listed with timestamp and type.
- [ ] Search/filter narrows list instantly.
- [ ] Download result opens correct artifact.

### 5.11 Settings Checklist

- [ ] Each settings category is accessible.
- [ ] Preference changes persist after reload.
- [ ] Sensitive settings require confirmation.

---

## 6) State and Data Contract Map

### Global State Domains

- `session`: authenticated user, role, profile meta
- `ui`: sidebar state, theme, toast queue, command palette
- `location`: selected geo scope and coordinates
- `filters`: date range, module filters, report filters
- `predictions`: rainfall/heatwave/anomaly/profile outputs
- `risk`: aggregated score and category
- `history`: previous runs and downloadable artifacts

### API Contract References

- `GET /health`
- `GET /weather/current?latitude={lat}&longitude={lon}`
- `POST /predict/from-location`
  - request: `latitude`, `longitude`, `mode`
  - modes: `rainfall | heatwave | anomaly | profile`

---

## 7) Interaction and UX Rules

- First contentful section appears within 2 seconds on standard network.
- Skeleton loaders are used for map, charts, and tables.
- Every user-triggered prediction action has clear pending/success/error feedback.
- Empty states provide a next step action.
- Export actions show completion toast with file name.
- Destructive settings actions require confirmation.

---

## 8) Analytics and Event Blueprint

Track at minimum:

- `nav_item_clicked`
- `prediction_requested`
- `prediction_completed`
- `prediction_failed`
- `map_layer_toggled`
- `report_exported`
- `settings_updated`

Event payload baseline:

- `screen`
- `module`
- `timestamp`
- `location_scope`
- `request_id`

---

## 9) Accessibility Checklist

- [ ] All interactive controls have keyboard access.
- [ ] Visible focus state on all focusable elements.
- [ ] Color contrast meets WCAG AA for text and controls.
- [ ] Form controls have labels and helper/error text.
- [ ] Charts have textual summaries for screen readers.
- [ ] Map interactions provide non-visual alternatives for key insights.

---

## 10) Definition of Done

A screen is complete when:

- All required sections from this blueprint are present.
- Acceptance checklist for that screen is fully checked.
- Loading, empty, and error states are implemented.
- Responsive behavior is validated for desktop/tablet/mobile.
- Accessibility checks pass for keyboard and contrast.
- API-dependent widgets use the defined contract and handle failures.

---

## Related Document

- [Frontend UI Structure](FRONTEND_UI_STRUCTURE.md)
- [Frontend QA Test Matrix](FRONTEND_QA_TEST_MATRIX.md)
- [Bug Report Template Pack](BUG_REPORT_TEMPLATE_PACK.md)
- [Release Readiness Checklist](RELEASE_READINESS_CHECKLIST.md)
