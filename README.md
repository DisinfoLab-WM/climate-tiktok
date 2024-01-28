# Climate Disinformation TikTok Research Tools

### Installation & Setup

Create a virtual environment using `python3 -m venv venv` and activate it using `source venv/bin/activate`.

Install the required packages using `pip3 install -r requirements.txt` and configure Playwright (if you have not previously used it on your system) with `python3 -m playwright install`.
 
### Linting & Formatting

The project uses flake8, Black, and isort for maintaining continuity and style. These can all be executed with:

```bash
make format
```