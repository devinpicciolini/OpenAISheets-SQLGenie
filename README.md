# Welcome to the OpenAI and Google Sheets Integration

This code allows you to use the power of the OpenAI API to generate SQL queries based on a user's prompt and the structure of a table in a Google Sheet. The code uses the Google Sheets API to access the data in the sheet, and the Pandas library to convert the data to a DataFrame.

## Getting Started

1. Clone the repository: 
git clone https://github.com/devinpicciolini/OpenAISheets-SQLGenie.git

Copy code

2. Install the required dependencies: 
pip install -r requirements.txt

Copy code

3. Create a credentials.json file with the credentials for accessing Google Sheets API from the Google Developer Console.

4. Add the credentials.json file to the root directory of the project.

5. Replace the `openai.api_key` value in the code with your OpenAI API key.

6. Run the script by executing the following command in your terminal:
python openAIPandas.py

Copy code

7. Enter the URL of the Google Sheet and the sheet name when prompted.

8. Enter your query prompt when prompted.

9. The generated query will be displayed on the terminal.

## Security

- Use environment variables or a separate configuration file to store sensitive information such as API keys. This way, the keys will not be committed to the repository and will not be visible to others.

- Remove any hardcoded sensitive information from the code, such as credentials or API keys.

- Use encryption for sensitive information, such as user credentials.

- Make sure to keep all dependencies and libraries up to date to ensure that any known vulnerabilities are patched.

- Do not push the credentials.json file to the repository, it should be ignored by git and should be placed locally.

## Built With

- [OpenAI](https://openai.com/) - The AI platform used
- [Google Sheets API](https://developers.google.com/sheets/api) - Used to access and manipulate data in Google Sheets
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis library for Python
- [gspread](https://gspread.readthedocs.io/en/latest/) - A Python library for connecting to Google Sheets

## Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Create a new Pull Request

## Author

- [Devin Picciolini](https://github.com/devinpicciolini)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Hat tip to anyone who's code was used
- Inspiration
- etc

This is a general guide for the README of your code, please adjust it according to your project and your preferences.
