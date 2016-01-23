# Turker

Toolkit to convert cpickle files of articles with sentences to turk csv files.

## Usage

Run the tool using the following command:

	python gen_input.py <PATH_TO_DATA> <PATH_TO_OUTPUT_CSV_FILE>

## Input format

We generate a pickle file for each article. The format of each pickle file is as follows:

	{
		sentences 	: 	<LIST OF SENTENCES>,
		title 		:	<TITLE>,
		url 		: 	<URL>
	}

## Output format

The columns of the output csv are as follows:

title | link | selection | target 
--- | --- | --- | ---
Uranus | https://en.wikipedia.org/wiki/Uranus | In 1986, images from Voyager 2 showed Uranus as a virtually featureless planet in visible light without the cloud bands or storms associated with the other giants. However, terrestrial observers have seen signs of seasonal change and increased weather activity in recent years as Uranus approached its equinox. The wind speeds on Uranus can reach 250 meters per second. Uranus had been observed on many occasions prior to its discovery as a planet, but it was generally mistaken for a star. The earliest recorded sighting was in 1690 when John Flamsteed catalogued Uranus as 34 Tauri and observed it at least six times. The French astronomer, Pierre Lemonnier, observed Uranus at least twelve times between 1750 and 1769, including on four consecutive nights. | Uranus had been observed on many occasions prior to its discovery as a planet, but it was generally mistaken for a star.