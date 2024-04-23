# electoral-bonds-website

## Contents
1. Installation Process for the Website
2. Some Screenshots
3. Usage and the Functionalities

## I. Installation Process for the Website
1. Establish a database named 'dcc' in SQL.
2. Utilize two CSV files, 'individual.csv' and 'political_party.csv,' to populate tables within the 'dcc' database. These files contain the financial transactions made by individuals or companies and political parties who have encashed the money.
3. Create a SQL user using the command: CREATE USER 'testing'@'%' IDENTIFIED BY 'password'; GRANT ALL PRIVILEGES ON . TO 'testing'@'%' WITH GRANT OPTION;
4. In your terminal, install Flask and Flask-MySQLdb by executing: pip install Flask Flask-MySQLdb.
5. In the electrol_bonds.py file, specify your MYSQL password as a string on the first line of code.
6. Launch the website by running the main.py file, which will be accessible at localhost. Visit the link displayed in the terminal to access the website.

## II. Some Screenshots
![Screenshot (646)](https://github.com/Paras-Shirvale/electoral-bonds-website/assets/167887758/568ac1f6-65f2-4a77-b0a5-1a88e8bfd4d8)
![Screenshot (647)](https://github.com/Paras-Shirvale/electoral-bonds-website/assets/167887758/f6ea03ad-f028-4f89-b5c6-a7c6a7eea77b)
![Screenshot (648)](https://github.com/Paras-Shirvale/electoral-bonds-website/assets/167887758/4589b731-1f12-4b93-950f-c6957f75b489)
![Screenshot (649)](https://github.com/Paras-Shirvale/electoral-bonds-website/assets/167887758/b3b9ed0f-4790-4c73-a792-4c01bcb5043d)
![Screenshot (650)](https://github.com/Paras-Shirvale/electoral-bonds-website/assets/167887758/b2909caf-ce62-4761-aa17-f41f3d1855aa)

## III. Usage and the Functionalities
1. In this project, I used a carousel to enhance the website's front-end design, making it more attractive while showcasing the six questions. A carousel is a slideshow tool that rotates through multiple items, like images or text, on a webpage. It's excellent for visually displaying content interactively and engagingly.
2. Question 1 will be displayed on the carousel's first slide. There is a search bar to enter the bond number and a submit button to submit the entered number, and then you will be redirected to another page showing the answer to question 1. There is a button to go back to the main page on the answer page.
3. Question 2 will be displayed on the second slide with a dropdown list functionality to select the political party's name and a button to show the answer. A table will be shown on the answer page with the bar graph as mentioned in the question. Also, a button is provided to download the chart.
4. Question 3 will be displayed on the second slide with a dropdown list functionality to select the company name and a button to show the answer. A table will be shown on the answer page with the bar graph as mentioned in the question. Also, a button is provided to download the chart.
5. In Questions 4 and 5, a dropdown list is used with a button directing to the answer page, which shows the table.
6. On the last slide, the Pie chart is displayed with the download button and a button to go to the main page.
