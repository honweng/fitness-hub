# 🧘‍♂️ Fitness Hub (Yoga & Dumbbell Workout Web Apps)

Self-hosted, lightweight personal fitness portals with AI-generated visual guides, yoga mobility flows, and prescriptive biomechanical dumbbell routines. 

Designed for **HonWeng** and hosted locally on a **Raspberry Pi 5** behind **Cloudflare Tunnels**.

---

## 🌟 Live Portals
* **Yoga Flow:** [https://yoga.honweng.com](https://yoga.honweng.com)
* **Dumbbell Blast:** [https://dumbbell.honweng.com](https://dumbbell.honweng.com)

---

## 📂 Repository Structure
```
fitness-hub/
├── yoga/                      # Yoga Flow Web App
│   ├── index.html             # Multi-phase yoga routine with timers & audio
│   └── images/                # Phase illustrations (male_phase1.jpg - male_phase5.jpg)
├── workout/                   # 45-Min Dumbbell Workout App
│   ├── index.html             # Prescriptive execution matrix & cues
│   └── images/                # Exercise visual guides (lower, push, pull)
├── server.py                  # Multi-host Python HTTP server for dual-domain routing
├── systemd/                   # Systemd user service definitions for boot persistence
│   ├── kaia-yoga.service
│   ├── kaia-tunnel.service
│   └── kaia-boot-notify.service
└── README.md
```

---

## 🏋️ Dumbbell Routine Overview (45 Mins)
1. **Phase 0: Yoga Mobility Warm-Up (5 Mins)**
   * Child's Pose, Cat-Cow Segmented Flow, Thread the Needle, Downward Dog with Pedal, World's Greatest Stretch.
2. **Phase 1: Lower Body Power (12 Mins • 3 Sets × 10–12 Reps)**
   * Goblet Squats, Dumbbell Reverse Lunges, Romanian Deadlifts (RDLs).
3. **Phase 2: Upper Body Push (10 Mins • 3 Sets × 10–12 Reps)**
   * Standing Overhead Press, Dumbbell Floor Press, Bent-Over Tricep Kickbacks.
4. **Phase 3: Upper Body Pull (10 Mins • 3 Sets × 10–12 Reps)**
   * Single-Arm Dumbbell Row, Standing Bicep Curls, Bent-Over Reverse Flys.
5. **Phase 4: Finisher & Decompression (8 Mins)**
   * Dumbbell Thrusters (2-Min AMRAP) + Static Cool-Down (Pigeon Pose, Chest & Hamstring holds).

---

## 🚀 Deployment & Hosting

### 1. Unified Virtual Host Server (`server.py`)
Both `yoga.honweng.com` and `dumbbell.honweng.com` are served by a single lightweight Python server on port `8081` that inspects the incoming `Host` header to route to the correct application folder.

```bash
python3 server.py
```

### 2. Cloudflare Tunnel Ingress
Traffic is proxied from Cloudflare edge through `cloudflared` without opening public router ports:
```yaml
ingress:
  - hostname: yoga.honweng.com
    service: http://localhost:8081
  - hostname: dumbbell.honweng.com
    service: http://localhost:8081
```

---

*Crafted with 🦊 by Kaia & HonWeng.*
