This code is for the user of Weibo (one of the biggest social board in China) to do some complaint work without seeing the illegal information but just print in the links.

For it is faced to Chinese user, the language in it is Chinese.


Here’s your translated content in a **GitHub-friendly markdown format**:

---

# **Preparation Steps**
- **Mac**: Open the terminal and enter:
  ```sh
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/ChromeProfile"
  ```
- **Windows**: Press **Win + R** to open "Run", type `cmd` to open the command prompt, then enter:
  ```sh
  chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenium\ChromeProfile"
  ```
  **Note**: Chrome needs to be in the system path. If it is not, use the following command instead:
  ```sh
  "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium\ChromeProfile"
  ```
  The path before the command points to the original Chrome installation location.

After running the command, **open Weibo in the newly launched Chrome window and log in**.  
(This specific Chrome window will be used for the automated process, ensuring that your Weibo account remains logged in. Do not close this window.)

---

## **Usage Instructions**
- **If you prefer running the code directly in a Jupyter Notebook**, use the `Weibo_Complaint.ipynb` file.
- **If you want to run Python directly**, you can ignore the notebook file.

### **Installation**
Before running the script, install the required dependencies in the terminal:
```sh
pip install streamlit selenium webdriver-manager
```

### **Running the Application**
Start the application by running the following command in the terminal:
```sh
streamlit run app.py
```
This will **automatically open a webpage**, where you can enter the Weibo complaint link and click the **"Start Complaint"** button at the bottom.

### **Stopping the Application**
If you **close the browser tab**, you may notice that the terminal does not accept new commands.  
To stop the process, press **`Ctrl + C`** in the terminal.

---

## **Customizing the Complaint Text**
If you want to modify the complaint text:
1. Open the `app.py` file.
2. Locate the **preset complaint content** inside the script.
3. Replace it with your desired text.
4. **Make sure to keep the original single quotes** to enclose the Chinese text properly.

Example:
```python
complaint_text = 'Your custom complaint message here'
```
Ensure that the Chinese content is **enclosed in English single quotes (`'`),** without deleting them.

---
