# DA Account Health Tracker
*Started: May 14, 2026*

> **PURPOSE:** Track account health signals over time to infer where Jeff stands on the DA platform. Since DA provides zero direct feedback, we reverse-engineer it from observable data. The AI updates this every session.

---

## 📈 HEALTH SCORE METHODOLOGY

We track 7 metrics. Each tells us something different:

| # | Metric | What It Reveals | How We Measure |
|---|--------|----------------|----------------|
| 1 | **Project Count** | Overall account standing | Count projects on dashboard every session |
| 2 | **Pay Tier Distribution** | Whether DA trusts you with premium work | Bucket projects into tiers: $40+, $28-39, $24-27, <$24 |
| 3 | **Qualification Offers** | Whether DA is opening new doors | Count available qualifications |
| 4 | **Email Cadence** | How actively DA is recruiting you for tasks | Track direct project emails (not Slack forwards) |
| 5 | **Project Churn** | Whether disappearances are you or platform-wide | Cross-reference with Reddit |
| 6 | **Performance Feedback** | Direct quality signal (rare) | Watch for feedback emails from DA |
| 7 | **Activity Level** | Whether inactivity is hurting your standing | Track sessions per week, hours logged |

### Health Grade Scale
- **A** = Premium projects available ($40+/hr), growing qualifications, direct invites, positive feedback
- **B** = Solid mid-tier ($26-28/hr), stable project count, new qualifications appearing, no red flags
- **C** = Only base-tier ($20-24/hr), flat or declining project count, no new invites
- **D** = Significant project loss, no new qualifications, potential quality flags
- **F** = Dashboard empty, no emails, possible account issue

---

## 📊 SESSION SNAPSHOTS

### Session: May 14, 2026 — 11:08 PM ET

**Dashboard:**
- Total Projects: 21
- Qualifications Available: 32
- Surveys: 0
- Report Time: 1 (pending)
- Inbox Unread: 81

**Pay Tier Breakdown:**
| Tier | Count | Projects |
|------|-------|----------|
| $40+/hr | 0 | (TH8 gone — tasks claimed) |
| $28-39/hr | 4 | Metis MORT ($28), Metis MGCL ($28), Metis MRCC ($28), Metis MIOS ($28) |
| $24-27/hr | 7 | Acheron ($26), R&R Acheron ($26), Circe ($27), R&R Circe ($27), Styx R&R ($25), Pecan Macaroon ($26), Grapefruit x2 ($24) |
| <$24/hr | 0 | — |
| Unpaid/Reference | 10 | Qualifications, gateways, read-only, chat projects |

**Emails This Session:**
- 1 direct project invite (TH8 — 1:34 AM)
- 1 referral offer ("unlocked special referral offer" — May 12)
- 3 Slack/Metis admin forwards (Caleb — site outage + recovery)
- 1 new project notification (Grapefruit)

**Reddit Cross-Reference:**
- Platform-wide outage confirmed (Cloudflare Host Error, multiple posts)
- Drought confirmed across premium tier (post: "complete decline in engaging, well-paying generalist tasks")
- Some workers seeing dashboards refill ("projects are back" — dry for 2 months, now 3 new projects)
- Worker dropped from 80+ to 16 projects — Jeff at 21 is above this floor
- No reports of mass project removal or account flags today

**Activity:**
- Hours worked today: 5.0 (TH8)
- Earnings today: $200
- Tasks completed: 4 evaluations (Jellyfish Hero, Cooking Sim, Chess Commentary, URL Shortener)

**Health Grade: B+**
- ✅ 21 projects (above Reddit floor of 16)
- ✅ Direct project invite received (TH8 email)
- ✅ Referral program unlocked (performance signal)
- ✅ No quality flags or warnings
- ✅ Multiple project families (6 families)
- ⚠️ No $40+/hr projects currently on board (platform-wide drought, not personal)
- ⚠️ No performance feedback email received yet (blind spot)
- ⚠️ Coding entry test incomplete ($50+/hr tier locked)
- ❓ Unknown: Whether TH8 email was targeted or mass blast
- ❓ Unknown: Quality scores on submitted work

---

## 📉 TRENDS (Updated Each Session)

| Date | Projects | Top Rate | Quals | Emails | Grade | Notes |
|------|----------|----------|-------|--------|-------|-------|
| May 14 | 21 | $28/hr (Metis) | 32 | TH8 invite + referral | B+ | TH8 gone, drought platform-wide |

*Add a row every session. After 5+ sessions, trends become visible.*

---

## 🔍 THINGS TO WATCH FOR

### Positive Signals (Grade Goes Up)
- [ ] New $40+/hr project appears on dashboard
- [ ] Performance feedback email with "Outstanding" or "Good" rating
- [ ] New project family you haven't seen before appears
- [ ] Qualification count increases without you completing any (= DA added new ones for you)
- [ ] Direct email invites increasing in frequency
- [ ] Coding entry test completed → $50+/hr projects unlocked

### Warning Signals (Grade Goes Down)
- [ ] Project count drops below 15 while Reddit says theirs are stable/growing
- [ ] Highest-paying project drops below $26/hr
- [ ] Qualifications start disappearing (DA pulled invites)
- [ ] No direct emails for 2+ weeks
- [ ] Performance feedback with "Needs Improvement"
- [ ] Rate & Review tasks appear for projects you've worked on (possible quality audit)

### Critical Signals (Immediate Action)
- [ ] Project count drops to single digits
- [ ] "Your account has been flagged" or similar warning
- [ ] Payment delays or issues
- [ ] Loss of access to a project family you were actively working on
- [ ] Dashboard completely empty

---

## 🧪 EXPERIMENTS TO RUN

### Experiment 1: Activity vs. Project Availability
**Hypothesis:** Logging more hours correlates with more projects appearing.
**Method:** Track hours worked vs. project count over 2 weeks. Does working 20+ hrs/week lead to more projects than 5 hrs/week?
**Status:** Not started — need 2+ weeks of data

### Experiment 2: Qualification Completion → Premium Access
**Hypothesis:** Completing qualifications (Bluebird, Coding Test) directly unlocks higher-paying projects.
**Method:** Complete one qualification, track what new projects appear within 48 hours.
**Status:** Not started — Coding Test in progress

### Experiment 3: Profile Skills Impact
**Hypothesis:** Adding/changing skills on DA profile affects which projects appear.
**Method:** Note current skills, change them, track project changes over 1 week.
**Status:** Not started — need to check current profile skills

---

*This tracker is updated every session. The AI reads it on startup alongside the Project Dossier.*
