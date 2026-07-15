# VortexTech Cyber Security Internship — Week 2

## What this is

Week 2 of the VortexTech cyber security internship. This week I moved from theory into actually building and running security tools. Two things this week: a password strength checker I wrote in Python, and an Nmap port scan on my local machine.

## What I built

**1. Password Checker (`password_checker.py`)**
A Python script that takes a password and rates it Weak / Medium / Strong based on length, character variety, and whether it's on a common-password blacklist. Also gives specific tips for improvement.

To run it:
```bash
python password_checker.py
```
No external libraries needed, just base Python 3.

**2. Nmap Port Scan**
I installed Nmap and ran a version scan (`nmap -sV 127.0.0.1`) on my own machine. Documented what ports were open, what services they correspond to, and what the security implications are.

## Files

| File | Description |
|------|-------------|
| `password_checker.py` | Python password evaluator script |
| `week2-report.md` | Full write-up, scan results, and reflection |
| `password_checker_output.jpg` | Screenshot of the script running |
| `nmap_scan_output.jpg` | Screenshot of Nmap scan results |

## Note on port scanning

I only scanned my own machine (localhost / 127.0.0.1). Never scan networks or devices you don't own.
