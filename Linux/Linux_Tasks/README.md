# 🐧 Linux Tasks – User Management & Login Banner

This folder contains **practical Linux Bash tasks** to demonstrate real-world DevOps skills.  
Each task focuses on **automation, system administration, and Linux best practices**.

---

## Task 01: User Management & Login Banner

### Objective
Automate the creation of a Linux user, add them to the sudo group, and set a login banner message.

### Skills Covered
- User creation & management (`adduser`, `usermod`)  
- Linux groups and sudo permissions  
- Setting system login banners (`/etc/motd`)  
- Bash scripting with safe execution checks  

### Features
- Creates a new user (`developer`) if not already present  
- Adds the user to the `sudo` group  
- Sets a custom login message: `Welcome DevOps Engineer! Keep growing 🚀`  
- Safe to run multiple times without errors  

### How to Run
```bash
cd Linux_Tasks

chmod +x Task01_user_management_login_banner.sh
./Task01_user_management_login_banner.sh

