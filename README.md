# 📝 AI Blog Generator with LLaMA 2

Welcome to **AI Blog Generator**, a powerful Streamlit web app that generates personalized blog content using the LLaMA 2 model! Whether you're a researcher, data scientist, or a general reader, this tool helps you craft high-quality blogs in seconds. 🚀

## 🔥 Features

- ✍️ **Generate Blogs Instantly**: Create engaging blogs by simply entering a topic.
- 🎯 **Target Audience Customization**: Tailor content for Researchers, Data Scientists, or Common People.
- ⚙️ **Advanced Settings**: Adjust Temperature and Max Tokens to control creativity and content length.
- 🌐 **Modern UI**: Clean, interactive, and responsive design for a seamless experience.

## 📂 Project Structure

```
blog-generator/
├── app.py                 # Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── Model/                 # Model directory
│   └── llama-2-7b-chat.ggmlv3.q4_0.bin
├── assets/                # Images or additional assets
└── .gitignore             # Ignored files and folders
```

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/blog-generator.git
   cd blog-generator
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

4. **Access the App**
   Open your browser and go to `http://localhost:8501`.

## 🛠️ Usage

1. **Enter a Blog Topic** ✍️
2. **Select the Target Audience** 🎯
3. **Adjust Advanced Settings (Optional)** ⚙️
4. **Click 'Generate Blog'** 🎉
5. **Enjoy your AI-generated blog!** 📜

## 🧩 Dependencies

- [Streamlit](https://streamlit.io/)  
- [LangChain](https://python.langchain.com/)  
- [CTransformers](https://github.com/marella/ctransformers)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## 🌐 Deployment (Optional)

### Deploy on **Streamlit Cloud**
1. Sign in to [Streamlit Cloud](https://streamlit.io/cloud).
2. Click **New App** → Select this GitHub repository.
3. Set the **main file path** to `app.py`.
4. Click **Deploy** and share your app! 🌍

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---


