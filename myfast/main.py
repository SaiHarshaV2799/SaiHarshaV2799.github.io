from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

resume = '''SAI VEERLA
 +1 (573) 647-3355 ▪ saiharshav323@gmail.com ▪ linkedin.com/in/sai-harsha-vardhan
Summary
Motivated master's student in Information Science and Technology with a focus on cybersecurity analysis, data science, and machine learning. Experienced in front-end web development and ML, having completed a stock market prediction project using logistic regression, feature scaling, and SMOTE for class balancing. Proficient in HTML, CSS, JavaScript, ReactJS, Python, and SQL, with strong skills in data visualization and analysis. Demonstrated ability to lead teams in complex cybersecurity and ML projects, extracting actionable insights. Seeking internship opportunities to further expand technical skills in a collaborative environment.

Technical Skills
•	Programming: Python, C, R, JavaScript, PHP, SQL
•	Web Development: HTML, CSS, JavaScript, ReactJS, AngularJS, Bootstrap, AJAX
•	Machine Learning & Data Science: Deep Learning, TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn
•	Cybersecurity & Cloud: SAS, Oracle HCM (OTL & Absence Management)
•	Engineering Tools: CATIA, DELMIA, SIMULIA, AutoCAD, NX10, ANSYS, CAD/CAM
•	Database & Automation: MySQL, SQLite, Selenium, BeautifulSoup, Google Gemini AI, PyAutoGUI, Excel

Projects and Research Work
Advanced Stock Market Prediction ML Model		                                                        August 2024 – Present                      - Developed an LSTM-based stock prediction model for enhanced forecasting accuracy based on historical data. This project moves beyond traditional regression models to leverage the power of deep learning for enhanced accuracy.  					                                                        - Implemented sophisticated data preprocessing techniques, including handling missing values, feature scaling using `StandardScaler`, and normalization of the target variable to improve model training and generalization.		       			                                                     - Achieved significant performance, evidenced by a low-test loss of 0.0277 and demonstrated the model's ability to capture trends in stock data through real-time predictions. The model's predictions were consistently within a 2% margin of the actual closing prices, showcasing a high degree of accuracy and reliability.        			     			                                       - Utilized the `Adam` optimizer for efficient model training and `MSELoss` as the loss function, along with the use of the CPU or GPU using CUDA for performance optimization.  						 	                    - Demonstrated real-time prediction capabilities by feeding the trained model the last sequence of data to predict the next closing stock price.                               - Leveraged Python libraries such as Pandas, NumPy, PyTorch, and Scikit-learn for data manipulation, model building, and evaluation. The model was optimized for GPU utilization to accelerate the training and evaluation process.  						                     - Implemented a training loop that prints actual and predicted values for the first batch of the epoch every 10 epochs, demonstrating active model monitoring. 							                       - Calculated the predicted stock price in the original scale, emphasizing the practical applicability of the model.
Automated Job Application and AI Resume Tailoring System					         Aug 2024 – Dec 2024 - Developed a fully automated system to identify relevant job openings on LinkedIn, extract job descriptions, and tailor a resume for each application using an AI model. 			  		                                             - Employed Selenium and Chrome WebDriver for web scraping and browser automation, including login, search filtering, and interaction with dynamic web elements. 							                       - Utilized Beautiful Soup for parsing job description text from HTML. 							                       - Integrated Google's Gemini AI model via the generativeai library to create custom, ATS-friendly resumes based on extracted job descriptions and a master resume file, outputting a revised `.docx` document. 							                    - Implemented precise UI interactions using `pyautogui` to navigate and manipulate UI elements, bypassing complexities and streamlining automation.							                       - Incorporated a SQLite database to store job role, description, generated resume text, and application link, allowing for tracking and preventing duplicate submissions.							                      - Streamlined the job search process by filtering jobs based on user-defined criteria, ensuring relevance.				                         - Demonstrated end-to-end automation capabilities, starting with browser navigation to document generation and database management, dramatically improving efficiency in the job search process. 
Credit Limit Optimization for Customer Segments (Business Intelligence) 					      Aug 2024 - Dec 2024                - Performed data analysis using a synthetic dataset of 1,000 customers, focusing on optimizing credit limits to balance revenue growth and risk management. 						                                        - Conducted data preprocessing tasks, including cleaning, standardizing, and enriching features like demographics, financial metrics, and reward program participation. 							                          - Implemented K-Means clustering to segment customers into three groups: High Engagement, Medium Activity, and Low Engagement.                                   - Developed targeted strategies for each segment, such as personalized credit limits, tailored marketing campaigns, and user-friendly reward programs.                                           - Utilized Python libraries (Pandas, NumPy, Faker) for data generation and statistical analysis.					                                - Delivered actionable insights through data visualization and clustering analysis to support decision-making. 	                      
Web Developer		                                                        Aug 2023 - Dec 2023                      - Developed a dynamic web application utilizing HTML, CSS, JavaScript, PHP, SQL, and AJAX for adding and retrieving country data from a MySQL database.                                       					                                                    - Implemented robust error-handling mechanisms to prevent duplicate entries and handle non-existing countries, improving data integrity and user experience.			                                                                                     - Designed and integrated interactive charts using Chart.js to visualize data, enhancing user engagement and application functionality.        	                       - Ensured a seamless user experience by applying responsive design principles and optimizing front-end performance.
CyberSec Insight: Analyzing and Visualizing Security Vulnerabilities Over Time in the US 			        Aug 2023 - Dec 2023   - Led cybersecurity vulnerability analysis using Python libraries like Pandas, NumPy, Matplotlib, and Seaborn. 	                                                - Preprocessed and visualized data from the National Vulnerability Database, focusing on severity levels and vulnerability distributions.	              - Identified the top 5 companies with the highest number of vulnerabilities, improving security prioritization strategies.			             - Created scatter plots and heatmaps to visualize CVSS scores and severity distributions, enabling informed decision-making.      	
YouTube Series Transcript Analysis: A Text-Mining Approach                                                                                               Aug 2023 - Dec 2023 - Conducted an analysis of the Chinese drama My Girlfriend is an Alien using SAS Enterprise Miner, implementing a text-mining pipeline involving data collection, parsing, pre-processing, clustering, and topic modeling.	                        	                                                                                    - Extracted key themes influencing viewer engagement and provided insights to improve content strategy for future releases.                                                            - Leveraged clustering and topic modeling techniques to highlight thematic coherence, aiding in audience behavior analysis.	
Professional Experience
Student Assistant 											               Jan 2024 – Jan 2025 Missouri University of Science and Technology    								      	               - Supported data analysis and visualization tasks, employing Excel for data processing and chart creation. 				                        - Developed a Python-based automation program to collect data and generate charts from Thermo-Calc software, streamlining data workflows.                          - Applied data preprocessing techniques to ensure data quality and readiness for analysis, enabling effective insights.			
Front end web developer										                                              DEV GLOBAL SERVICES								                                            Sept 2021 – July 2023 - Played a pivotal supporting role in the realm of front-end web development at DEV GLOBAL SERVICES, an overseas educational consultancy specializing in guiding aspiring students towards successful academic pursuits abroad. 						                            - Utilized a skillful blend of HTML, CSS, JavaScript and Bootstrap framework to craft intuitive and user-centric web pages, ensuring seamless user experiences. Led efforts in website maintenance and enhancement, adeptly incorporating user feedback for iterative improvements. 	                           - Maintained a steadfast commitment to upholding elevated graphic standards, contributing to the visual and functional integrity of the website.                           - Technologies Used: HTML | CSS | Bootstrap | JavaScript | Angular | Responsive Design	
Education
Missouri University of Science and Technology                                                                                                                           Aug 2023 – May 2025            Masters in Major: Information Science and Technology, Miner: Data 
Certifications
- Course completion certificate from Kaggle in python.	                					                       	             - Course completion certificate from DataCamp in R. 									            - Second level of course Applied robotic control (ARC).                                                                                                                                                               - Data analytics essentials certificate from cisco.
'''

# Configure Google Gemini API
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key="api_key")
model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp", system_instruction=f"you will only answer the questions directly with high creativity, only if the questions are on my resume stored at {resume} and the response should be like I answered them not AI and not say based on resume.")

@app.post("/generate/")
async def generate_text(request: dict):
    prompt = request.get("prompt", "")
    if not prompt:
        return {"response": "Please provide a valid prompt."}

    response = model.generate_content(contents=prompt)
    return {"response": response.text}
