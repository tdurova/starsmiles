# StarSmiles: AI-Powered Dental Radiography Classification API

StarSmiles is a deep learning-powered API designed to classify dental X-rays, automating the detection of conditions like cavities, implants, and impacted teeth. Developed during the Le Wagon bootcamp, this project highlights my skills as a **Machine Learning Engineer** with strong **backend development** and **project management** experience.

## Key Highlights

- **Automated Dental Diagnosis**: Classifies X-rays into dental conditions (Cavity, Fillings, Implants, etc.).
- **FastAPI Integration**: Exposes the model via a production-ready API for seamless integration with dental clinics.
- **Efficient Preprocessing & Training**: Custom pipeline to handle and preprocess dental X-ray images.
- **Scalable Architecture**: Designed for future improvements, retraining, and deployment with Docker.

## Installation & Usage

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/project-starsmiles.git
   cd project-starsmiles
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Run the API:**
   ```
   uvicorn starsmiles.api.fast:app --reload
   ```
4. **Use the API:** Send a POST request with an X-ray image to `/predict`.
