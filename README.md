**For educational and non-profit uses only. All trademarks, logos and brand names are the property of their respective owners.**

# kickbase-analysis

This repository contains some python code for retrieving data from the kickbase API and also a react web app for visualization.

## Deployment with GitHub Pages

The data collection and building of the web app is automated by cron jobs and runs daily. The results are published to this GitHub Pages website https://roman-la.github.io/kickbase-analysis/.
If you are interested in how I set it up, check out this guide https://github.com/gitname/react-gh-pages.

## Run locally

If you are interested in running the code for your own league locally, follow this small guide. But keep in mind, that there could occur some problems if your account is part of several leagues or challenges. In that case, you might need to make a small adaption to the file data/api_manager.py.

Assuming you have python 3.10 already setup, run the following commands to setup the environment and run the code for data collection:

```
cd data/
pip install pipenv
pipenv install
python -m pipenv run python main.py --kbuser ${{ secrets.KB_MAIL }} --kbpw ${{ secrets.KB_PW }} --ignore draft_bot Jimmy Alex
```

The resulting .json files need to be copied to the frontend folder:

```
cp data/*.json frontend/src/data
```

After that, assuming you have Node 18.x and npm setup, run the following commands to start the development server (reachable under http://localhost:3000/kickbase-analysis):

```
cd frontend/
npm install
npm start
```

## Contact

Feel free to contact me on discord (r0man51) or open an issue if you have any questions.
