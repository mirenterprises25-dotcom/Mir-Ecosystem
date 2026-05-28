# How to Open and Access the MIR-Ecosystem

Whether you want to work on the application on your own computer or access it from a mobile phone via the web, this guide explains exactly what steps to take and what URLs to open.

---

## 1. Opening the Application on Your Local System

When you run the application locally on your laptop, it is private and completely secure. It is not exposed to the public internet.

**Step-by-Step Instructions:**
1. Open the **Docker Desktop** application on your computer and make sure the Docker engine is running.
2. Open a terminal (PowerShell) and navigate to the project folder:
   ```powershell
   cd "f:\Self Projects\MIR-ECOSYSTEM — ENTERPRISE AI OPERATING SYSTEM"
   ```
3. Type the following command and hit Enter:
   ```powershell
   docker-compose up -d
   ```
   *(This tells Docker to start up all the databases, the AI backend, and the UI frontend in the background).*
4. Open your web browser (Chrome, Edge, Safari, etc.).
5. **To view the Dashboard UI:** Type `http://localhost:3000` into the address bar.
6. **To view the API Documentation:** Type `http://localhost:8000/docs` into the address bar.

When you are done working and want to shut the system down, run:
```powershell
docker-compose down
```

---

## 2. Opening the Application on the Web (Publicly)

If you follow the deployment guide (`docs/guides/cloud_hosting_options.md`) and deploy your system to a cloud server (like DigitalOcean), the application will run 24/7 on the internet.

**Step-by-Step Instructions:**
1. You do **not** need to open Docker or the terminal on your personal laptop. The cloud server handles everything.
2. Open any web browser on any device (your laptop, an iPad, your mobile phone).
3. Type your server's **Public IP Address** (e.g., `http://165.22.45.99:3000`) or your custom domain name (e.g., `https://www.mir-ecosystem.com`) into the address bar.
4. You will instantly see the Dashboard UI.

*(Note: Until you deploy the code to a cloud server, Option 2 will not work. Stick to Option 1 for now!)*
