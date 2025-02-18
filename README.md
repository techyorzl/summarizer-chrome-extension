# T5-Summarizer 🚀  

This repository contains a **summarization tool** built as a Chrome extension, using a transformer-based model to generate concise summaries of text.  

## 📌 Project Overview  
The initial goal was to **fine-tune the T5 base model** on the **CNN/Daily Mail dataset** for improved summarization performance. However, due to **compute limitations**, the fine-tuning process was infeasible within the available resources—my **Kaggle notebook crashed** due to memory constraints.  

As a result, the final implementation **uses a pre-trained model via Hugging Face’s `pipeline`**, ensuring efficient summarization while maintaining quality.  

## 📂 Repository Contents  
- **🔬 Fine-Tuning Attempt:**  
  - Contains the Kaggle notebook where I attempted fine-tuning.  
  - Highlights the challenges faced due to compute limitations.  
- **⚡ Final Implementation:**  
  - A FastAPI backend serving the summarization model.  
  - A simple Chrome extension that integrates with the backend.  
- **📈 Future Improvements:**  
  - If better computational resources become available, I plan to **revisit fine-tuning** for optimized performance.  

## 🔧 Installation & Usage  
1. Clone this repository:  
   ```sh
   git clone https://github.com/yourusername/summarizer-chrome-extension.git
