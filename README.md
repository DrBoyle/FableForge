# FableForge

## Overview
FableForge is a podcast script generation tool that leverages the power of OpenAI's GPT-3 model to create dynamic and engaging podcast scripts. 

Whether you're a seasoned podcaster or just starting out, FableForge simplifies the script writing process, giving you more time to focus on what matters most - telling your story.

## Features
* Interactive user prompts to determine the subject matter, tone, style, and length of the podcast.
* Outline creation for the podcast episode.
* Section-by-section narration generation in line with the previously determined style and tone.
* Opportunity to provide feedback and tweak the generated outlines and narrations until satisfaction.
* Final scripts are written to a file which can be referenced later.

## Installation
1. Clone this repository: `git clone https://github.com/username/FableForge.git`
2. Navigate to the FableForge directory: `cd FableForge`
3. Install the required Python packages: `pip install -r requirements.txt` (You may have to use `pip3` if Python 2 is also installed.)
4. Add your OpenAI API key to the environment variables: `export OPENAI_API_KEY='your-api-key'`
5. Run the script: `python FableForge.py`

## Usage
After running `FableForge.py`, you'll be prompted to provide details about your podcast episode. Based on your input, FableForge will generate a detailed episode outline and narrations for each section.

You will have the opportunity to review and provide feedback on the generated content until you're satisfied. The final episode outline and complete narration will then be written to text files for your convenience.

## Requirements
* Python 3.6 or above
* OpenAI Python package
* OpenAI API key

## Note
The usage of the GPT-3 API is not free and can result in costs. Please ensure you're aware of the costs associated with using your API key.

Enjoy creating amazing podcast scripts with FableForge!
