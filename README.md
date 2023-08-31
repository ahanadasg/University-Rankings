# University Rankings Visualization Project

## Overview
This project involves scraping university ranking data from a Wikipedia page, processing the data, and creating visualizations to compare university rankings and locations. The project aims to provide insights into the rankings of universities across different years and locations.

## Prerequisites
- Python (3.6 or higher)
- Libraries: pandas, matplotlib, requests, beautifulsoup4

## Installation
1.	To download the project from the GitHub website, navigate to the repository on your web browser. On the repository page, locate the green "Code" button. Click on it to reveal a dropdown menu. From the dropdown menu, click on the "Download ZIP" option. This will download a ZIP file containing the entire repository to your computer.

2.	 Install the required libraries using pip:
   ```
   pip install pandas matplotlib requests beautifulsoup4 numpy
   ```

## Steps to Replicate
1.	Open Google Colab or Jupyter Notebook and upload the `scrape_rankings.ipynb` notebook. Run the code to scrape the university rankings table from Wikipedia and store it in an Excel file. Alternatively, you can download it in .py format and run it on your computer in your terminal.

2.	Go to the Files section in Colab/Jupyter. You can view the `qs_world_university_rankings.xlsx` excel file. Download the excel file in your computer which contains the scrapped data of university rankings. It contains the name of the universities, the rankings in year 2023 and year 2024 respectively. You can also download it in .py format and run it on your computer in your terminal.



3.	Now, upload the `add_locations.ipynb` notebook. Open it and upload the `qs_world_university_rankings.xlsx` in the Files section. Now, run the code to add locations of the respective university. Go to the files section and download `qs_world_university_rankings_with_locations.xlsx to your computer. You can also download it in .py format and run it on your computer in your terminal.


4.	Next, we will generate visualizations using matplotlib to compare rankings and display locations. Upload `create_visualization.ipynb` notebook. In the Files section, upload `qs_world_university_rankings_with_locations.xlsx`. Now, run the code to view the visualizations of ranking and locations. You can also download it in .py format and run it on your computer in your terminal.

5.	You can also refer to ‘uni_rankings.ipynb’ which contains the compiled code for the above mentioned steps for easy access. 


## Results
The project provides visualizations that allow you to compare university rankings across different years and locations. The bar plot shows rankings for each university in 2024 and 2023, while the pie chart displays the distribution of university locations.


## License
This project is licensed under the [MIT License](LICENSE).
