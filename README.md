<div align="center">

# Hridam Biswas

**IEEE Researcher · ML Engineer · KIIT University**

[![Portfolio](https://img.shields.io/badge/Portfolio-hridambiswas.github.io-0ea5e9?style=flat-square)](https://hridambiswas.github.io)
[![Email](https://img.shields.io/badge/Email-hridambiswas2005%40gmail.com-ea4335?style=flat-square)](mailto:hridambiswas2005@gmail.com)

</div>

---

## About

I build production ML systems — from clinical decision support to autonomous trading bots. My work sits at the intersection of statistical rigor and real-world deployment constraints.

Currently focused on:
- **Statistical arbitrage** on NSE (pairs trading, z-score mean reversion)
- **Clinical ML** — multi-label disease detection with causal structure
- **Autonomous perception** — V2V collaborative sensing for urban safety

---

## Projects

### [Iron-Sentry](https://github.com/Hridambiswas/iron-sentry) — Autonomous NSE Pairs Trading Bot
Fully autonomous stat-arb system monitoring NSE equity pairs 24/7. OLS hedge ratio on log returns, z-score entry/exit with ghost-order guard, Telegram alerts, and paper trading mode for live validation before capital deployment.

`Python` · `asyncio` · `yfinance` · `SQLite WAL` · `Telegram Bot API`

---

### [ComorbidNet](https://github.com/Hridambiswas/comorbidnet) — Correlated Multi-Disease Detection
Detects T2D, Hypertension, Metabolic Syndrome, and CKD simultaneously using Classifier Chains that propagate disease predictions as features — capturing the metabolic cascade that independent models miss. SHAP interaction values explain per-disease attribution.

`XGBoost` · `Classifier Chains` · `SHAP` · `VIF Analysis` · `Clinical ML`

---

### [CreditSense](https://github.com/Hridambiswas/creditsense) — Real-Time Credit Risk API
Ensemble ML credit scorer (Logistic Regression + Random Forest + Gradient Boosting) served as a FastAPI backend. Trained on 23K+ real loan records. One-click deploy on Render.

`FastAPI` · `scikit-learn` · `VotingClassifier` · `Render` · `Python`

---

### [V2V Perception Pipeline](https://github.com/Hridambiswas/v2v-perception) — HACK4IMPACT Track 2
Three-stage autonomous driving pipeline: DeepLabV3 semantic segmentation → XOR delta zone detection → 48K-param decision CNN. Designed for vehicle-to-vehicle hazard sharing in occluded urban environments.

`PyTorch` · `DeepLabV3` · `OpenCV` · `SQLite` · `Computer Vision`

---

## Tech Stack

```
Languages   Python · SQL
ML/DL       XGBoost · scikit-learn · PyTorch · SHAP
Finance     yfinance · NSE · Statistical Arbitrage
Backend     FastAPI · asyncio · SQLite
DevOps      GitHub Actions · Render · Telegram Bot API
```

---

<div align="center">

*Building things that work in production, not just notebooks.*

</div>
