# AICoach_BOT

AICoach_BOT is a friendly customer support chatbot designed to assist coaches with AI Strategy and automation. Powered by the OpenAI GPT-3.5-turbo model, it can answer questions in both English and Swedish in a very pedagogical and helpful way. This bot was inspired by the work of Mark Craddock and was adapted by Patrik Artell.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this bot, you need the following:

- Python 3.7 or later
- An OpenAI API key, which is used to access the GPT-3.5-turbo model powering the bot (you can get one [here](https://beta.openai.com/signup/))

### Installing

1. Clone this repository to your local machine.
2. Install the required Python dependencies by running `pip install -r requirements.txt`.
3. Create a .env file in the root of your project and insert your key there, like this (replace 'YOUR_KEY' with your actual OpenAI API key):

    OPENAI_API_KEY='YOUR_KEY'

4. Run `streamlit run AICoach_BOT.py` to start the application.

## Built With

- [OpenAI](https://www.openai.com/) - The AI model used
- [Streamlit](https://streamlit.io/) - The web framework used

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/ControX/AICoach_BOT).

## Authors

- **Patrik Artell** - *Initial work* - [ControX](https://github.com/ControX)

See also the list of [contributors](https://github.com/ControX/AICoach_BOT/contributors) who participated in this project.

## License

This project is licensed under the Creative Commons Attribution Share Alike 4.0 International license - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Mark Craddock](https://github.com/tractorjuice), for the original [Wardley Chatbot](https://github.com/tractorjuice/wardley_chat_bot)
- [OpenAI](https://www.openai.com/),for providing the powerful GPT-3.5-turbo model that powers this bot

## Contributing

Feel free to contribute! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for how you can be a part of this project.
