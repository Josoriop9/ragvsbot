# Hello World RAG - Chatbot Comparison

This project demonstrates how to implement a basic chatbot using RAG (Retrieval-Augmented Generation) in Streamlit. It compares a RAG-powered chatbot with a standard chatbot, using fictitious data from a restaurant menu.

## Project Structure

- `app.py`: Main code for the Streamlit application.
- `menu.txt`: Text file containing the restaurant menu.
- `requirements.txt`: File with the necessary Python dependencies.

## Requirements

- Python 3.7 or higher
- OpenAI account with a valid API key

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/Hello_World_RAG.git
   cd Hello_World_RAG
   ```

2. **Create a virtual environment and activate it**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key**:
   
   - Open the `app.py` file.
   - Replace `"your-api-key-here"` with your OpenAI API key.

5. **Run the application**:

   ```bash
   streamlit run app.py
   ```

6. **Upload the `menu.txt` file** when prompted in the application interface.

## Usage

You can ask questions about the restaurant menu in both chats. The RAG chat uses the retrieval technique to enhance responses, while the standard chat responds without using the menu data.

## Example Questions

- "What is the chef's specialty?"
- "What drink do you recommend to pair with the risotto?"
- "What desserts do you offer that are not too sweet?"

## Contribution

If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
