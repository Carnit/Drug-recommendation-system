# 🏥 Drug Recommendation System

## 🌟 Project Showcase

**This project was showcased at Ideathon2k24 held at Chandigarh Group of Colleges**

## 📖 Overview

The **Drug Recommendation System** is an innovative machine learning-based solution designed to assist healthcare providers in making personalized medication recommendations to patients. This university project leverages advanced algorithms to analyze medicine descriptions, reasons for use, and other characteristics to suggest suitable alternative medications, ultimately improving patient outcomes and enhancing the quality of healthcare delivery.

The system uses natural language processing (NLP) and cosine similarity to find medicines with similar properties, enabling healthcare providers to offer alternatives when a specific medicine is unavailable, contraindicated, or not preferred by the patient.

## 🎯 Objectives

- **Personalized Healthcare**: Provide tailored medication recommendations based on individual patient profiles
- **Clinical Decision Support**: Assist healthcare professionals in making informed treatment decisions
- **Data-Driven Insights**: Utilize patient reviews and medical data to recommend optimal medications
- **Improved Patient Outcomes**: Enhance treatment effectiveness through intelligent drug selection

## 🔬 Key Features

### 🤖 Machine Learning Algorithms

- **Content-Based Filtering**: Suggests drugs based on medication characteristics and descriptions
- **Text Analysis**: Processes medicine descriptions and reasons to understand medication purposes
- **Similarity Matching**: Identifies medicines with similar properties using cosine similarity

### 📊 Core Technologies

#### 1. Cosine Similarity

- **Application**: Applied to find similar medicines based on their descriptions and reasons
- **Purpose**: Measures the similarity between medicine vectors in a multi-dimensional space
- **Benefit**: Enables accurate recommendation of similar medicines based on content features

#### 2. Natural Language Processing (NLP)

- **Data Processing**: Extracts meaningful information from medicine descriptions and reasons
- **Techniques**: Text cleaning, stopword removal, stemming, and vectorization
- **Enhancement**: Improves recommendation accuracy by understanding medicine descriptions and uses

#### 3. Predictive Analytics

- **Health Disorder Prediction**: Predicts potential health conditions based on patient symptoms and history
- **Drug Efficacy Analysis**: Analyzes medication effectiveness based on user reviews and clinical data
- **Risk Assessment**: Evaluates potential drug interactions and contraindications

## 🏗️ System Architecture

The system follows a comprehensive approach combining:

1. **Data Collection & Preprocessing**
   - Drug review datasets (Kaggle Repository)
   - Cleaning and normalizing medicine data
   - Text processing of medicine descriptions and reasons

2. **Feature Engineering**
   - Text vectorization using CountVectorizer
   - Stopword removal for better text analysis
   - Stemming to normalize word variations
   - Cosine similarity calculation for recommendations

## 📈 Benefits for Healthcare

### For Healthcare Providers

- **Enhanced Decision Making**: Data-driven insights for treatment planning
- **Time Efficiency**: Quick access to relevant medication options
- **Risk Mitigation**: Identification of potential drug interactions
- **Evidence-Based Recommendations**: Backed by patient reviews and clinical data

### For Patients

- **Personalized Treatment**: Medications tailored to individual needs
- **Improved Outcomes**: Higher likelihood of treatment success
- **Reduced Side Effects**: Better medication compatibility
- **Informed Choices**: Access to peer reviews and effectiveness data

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Machine Learning**: scikit-learn, pandas, numpy
- **Natural Language Processing**: NLTK
- **Data Visualization**: matplotlib, seaborn
- **Web Framework**: Streamlit
- **Image Processing**: PIL (Python Imaging Library)

## 📊 Dataset Information

The system utilizes the <https://www.kaggle.com/datasets/saratchendra/medicine-recommendation/data> dataset

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.7+
pip (Python package installer)
```

### Installation

```bash
# Clone the repository
git clone https://github.com/Carnit/Drug-recommendation-system.git

# Navigate to project directory
cd Drug-recommendation-system

# Install required dependencies
pip install -r requirements.txt
```

### Usage

```bash
# First run the medicine-recommend.ipynb
# clean the data
# Or run the data cleaning script to prepare your data
python data_cleaning.py

# then run teh below command 
jupyter notebook

# At last run the web application with Streamlit
streamlit run app.py
```

### Important Note

The project relies on two large pickle files that aren't included in the repository due to size constraints:

- `similarity.pkl` (~3.76 GB): Contains similarity vectors for medicine recommendations
- `medicine_dict.pkl` (~2.53 GB): Contains the processed medicine dictionary

These files are generated by running the data processing scripts on the medicine dataset.

### Ideathon2k24 Showcase

This project was successfully **showcased at Ideathon2k24** held at **Chandigarh Group of Colleges**, demonstrating its potential impact on healthcare innovation and digital transformation in medical practice.

**Event Highlights:**

- Demonstrated practical application of AI in healthcare
- Showcased integration of multiple machine learning techniques
- Received recognition for innovative approach to drug recommendation
- Contributed to advancing healthcare technology solutions

## 🔮 Future Enhancements

- **Real-time Integration**: Connect with hospital management systems
- **Mobile Application**: Develop user-friendly mobile interface
- **Advanced ML Models**: Implement deep learning techniques
- **Drug Interaction Checker**: Enhanced safety features
- **Multi-language Support**: Expand accessibility
- **Clinical Trial Integration**: Incorporate latest research data

## 🤝 Contributing

We welcome contributions to improve this drug recommendation system! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add some NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This system is designed for educational and research purposes. It should **not be used as a substitute for professional medical advice, diagnosis, or treatment**. Always consult with qualified healthcare professionals before making medical decisions.

## ⏭️ Next Steps

1. To identify medicines based on salt components.
2. To use dataset which provide us.
   - Paitent ratings of the medicines.
   - Doctor ratings of the medicines.
3. To use the Patients sysmptoms to effectively identify the required medicine.

## 👥 Team

- **Developer**: [Carnit](https://github.com/Carnit)
- **Institution**: University Project
- **Showcase**: Ideathon2k24, Chandigarh Group of Colleges

## 📞 Contact

For questions, suggestions, or collaboration opportunities, please reach out through:

- GitHub Issues: [Create an Issue](https://github.com/Carnit/Drug_recommendation_system/issues)
- GitHub Profile: [@Carnit](https://github.com/Carnit)

---

**Made with ❤️ for advancing healthcare technology through machine learning**
