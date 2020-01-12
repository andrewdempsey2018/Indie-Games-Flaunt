# Indie Games Flaunt #

Indie Games Flaunt is a website developed with two main purposes:

1. To provide a central location where indie game developers can share their games.
2. To provide a central location where indie game fans and casual gamers can find the latest indie games as well as older releases.

## Terms ##

*flaunt* - display (something) ostentatiously, especially in order to provoke envy or admiration or to show defiance.

*Indie game* - a video game, commonly created by an individual or a small team without the support of a video game publisher.

## The problem & solution##

Indie games are mostly found on dedicated websites that cater to the needs of developers as opposed to casual users. These sites (usually forums) are aimed at computer savvy individuals and as such can be off putting to more casual users - the interfaces can be difficult to navigate and can be difficult to use on mobile devices. These forum site are also quite fractured - many different websites to share indie games results in some games going undiscovered or at the very least, having a very limited audience.

This website aims to be a central location where all of the latest indie game releases can be shared by both developers and players. Using this website, developers can be confident that their game will reach the largest audience and players can be confident that they have access to all of the latest releases as well as having access to all of the older releases. The website should be responsive so as to work on as many devices as possible - meaning the largest audience as possible can be targeted.

## UX ##

**External user goals**

1. A casual game player can browse the site and download a game they wish to play.
2. A game developer can share their game.

**Site owners goal**

Promote indie game development by providing a website where developers have access to a large audience of casual game players. Provide entertainment to casual game players as well as indie game fans by providing them with information on all of the latest indie games.

## User stories ##

User story 1: As a casual video game player, it is great that there is a central hub of information about all of the latest indie game releases. The website allows me to easily select and play any game I am interested in.

User story 2: As an independent game developer, it is great to have a website where I can share my work with the community. The interface makes it easy for me to share the location of my game as well as a description.

User story 3: As a casual games player with little free time, I like to play games whilst commuting. The website, with its responsive interface allows me to browse and play the latest indie game releases on my smartphone.

User story 4: As an indie game developer, I noticed that one of my games posted on the website had a broken link. I used the edit button to update the information in the "link" field.

## Design & prototyping ##

The central design goal of the website is to be easy to use for casual gamers - intended to be the largest visitor demographic. As such, it is designed with mobile as well as desktop devices in mind. The user interface is easy to navigate on a multitude of devices.

Below we see an early mock up of the design on a desktop computer. Note the large, standout text and relative lack of clutter.

![](img/readme_img/early_sketch.png)

Image 1. Early design

A Bootstrap template was selected, titled "Heroic Features". It appears to have much of the intended layout goals already implemented out of the box such as the nav bar, bold text and responsiveness.

![](img/readme_img/heroic_features.png)

Image 2. Heroic Features

Below we see the final chosen design for the main page. We see a Jumbotron as well as three cards. What is not clear from the image is that the cards are intended to be housed within a carousel object. This will allow the user to scroll and cycle through all of the games available in the database.

![](img/readme_img/main_desktop.png)

Image 3. Wireframe of the main page as seen from a desktop computer

Below we see the main page as it should look from a smartphone.

![](img/readme_img/main_mobile.png)

Image 4. Wireframe of the main page as seen on a smartphone

**Dedicated game screen**

Here we see a mock up of what the user will see if they were to click on a particular game. The game's title is displayed in large letters along with a large screenshot.  A textual description of the game is displayed alongside another screenshot. The developers name is provided (this is also a link that points to all of the developers other games). The link to the game is provided at the bottom of the page. Not shown in this wireframe is functionality to share a particular game to a social media feeds such as Facebook and Twitter etc.

![](img/readme_img/game_dedicated_desktop.png)

Image 5. Dedicated game screen on a desktop computer

Below is the dedicated game screen as seen on a mobile device

![](img/readme_img/game_dedicated_mobile.png)

Image 6. Dedicated game screen on a mobile device

Below we see a mockup of what will happen when a user clicks one of the navbar links. The user will be taken to a page that lists all of the game available in that particular category. In this case, the imaginary user has clicked on the "action" category and is presented with a list of all the action games currently in the database.

![](img/readme_img/action_desktop.png)

Image 7. All games of a particular category, desktop view

Below we see a mockup of the same screen except this time on a mobile device.

![](img/readme_img/action_mobile.png)

Image 8. All games of a particular category, mobile view

Below we see a mockup of the "share game" screen. Here a user will enter the details of a game such as its title, developer and some screenshots of the game. Upon clicking submit, the game will be posted to the database and be immediately viewable on the website.

![](img/readme_img/share_desktop.png)

Image 9. Share a game, desktop

Below we see the same functionality except this time on a mobile device.

![](img/readme_img/share_mobile.png)

Image 10. Share a game mobile

## Database design and implementation ##

Below we see a plan of what data will need to be held by the database.

![](img/readme_img/database_plan.png)

Image 11. Database planning

Title (text): the games title.

Genre (text): can be either action, puzzle, sports or educational.

Developer (text): the name of the games developer.

Short description (text): A short description of the game to be used on the cards on the main screen.

Long description (text): A full description of the game which is viewable when the user clicks the "More info" button to see a full breakdown on the game.

Link (text): A link to the game. This could either be a link to a web based game or a direct download link.

Screenshot 1,2,3 (text): A url to an image of the game.

**Database setup**

1. An account was created on [https://cloud.mongodb.com](https://cloud.mongodb.com)
2. A database was created called `IGF_DB` (short for Indie Games Flaunt database)
3. 

Theme

As the website is to be used to host video games and is to be used by persons who are interested in video games, it was decided that the look and feel of the website should be inspired by video games and their history. Fonts chosen evoke 80's computer aesthetic.

Color scheme

The color palette below is that of the Nintendo Entertainment system. From this palette, five colours were chosen to be used throughout the site. This palette was chosen in the hopes of evoking a 80's/90's video game feel.

http://www.thealmightyguru.com/Games/Hacking/Wiki/index.php/NES_Palette

![](img/readme_img/palette_nes.png)

Image 12. Color palette from the Nintendo Entertainment System

The website Coolors was used to generate a five color palette based on the nes palette above.

![](img/readme_img/palette_final.png)

Image 13. Final chosen palette

Features

Carousel of cards

On the main screen all games are displayed on an interactive carousel containing cards that have short description and screen shot. The cards contain a button that will link the user to a more detailed description of the game. The carousel can be scrolled by clicking the left and right arrows on top of and below the carousel. The arrows are implemented twice in order to allow better user experience of mobile users who would otherwise have needed to scroll to the top of the screen every time that want to change a slide.

Share a game

Users can click the share button and enter the details of a game they wish to share with the community.

Promote the site on social media

At the bottom of the main page there are links to common social media websites. These can be used to promote the website.

Responsive design

The website works on both mobile and desktop devices meaning the largest possible target audience can be obtained.

Random game

The random game button on the main screen sends the user to a dedicated game screen of a random game contained in the database.

Edit a game description

On the dedicated game page for every game, the user can click the edit button to allow them to change the details of any games in the database.

Delete a game from the database

A user can select a game and from its dedicated page, press the delete button to remove it from the database.

Features Left to Implement

*allow only users who submitted a game to edit it. As it stands, any user can edit any submitted game. Study <spencer recommendation> to gain knowledge of how to do this.

*implement "honey pot" and other authentication procedures to ensure the website cannot be abused by web bots and spammed.

*allow users to upload their own screenshot from their personal computers as opposed to only allowing them to use urls for the sharing of screenshots.

*The use of cards within a carousel caused some problems during development. Due to the fact that the cards are by default, flexible, there exists a problem where the images contained inside the cards can be different sizes. In a future update, the cards would be much better presented if they were fixed size.

*Even with the low colour count on the palette used, the addition of screenshots during development caused a somewhat saturated look to emerge on the website. In future builds, experimenting with a more limited palette may bring about more aesthetically pleasing results.

*The buttons for the carousel are not responsive at the moment, this needs to be fixed.

*need to test what happens if two games with the same name are entered

*Currently, the category pages are seperate HTML files for each of the four categories, these could be refactored into one page to cut down on the source code size.

# Technologies Used #

**Flask**

**Gunicorn**

## Font Awesome ##

Font Awesome is linked via CDN to provide the icons used throughout the website. The "fort" icon (https://fontawesome.com/icons/fort-awesome?style=brands) looks similar to the iconic castle in the Super Mario Bros. franchise. This was chosen as the home button as it fit the theme of the website very well.

Font Awesome link:

[https://fontawesome.com](https://fontawesome.com)

## Coolors ##

Coolors is a color scheme generator that outputs a five colour palette of complementary colors based on some initial inputs. The output contains information on the RGB and hex values used in the palette.

Coolors link:

[https://coolors.co/](https://coolors.co/)

## Pencil ##

The Pencil prototyping tool was used to create the wireframes seen in this document.

Pencil link:

[https://pencil.evolus.vn/](https://pencil.evolus.vn/)

## Computer languages ##

Django, HTML, CSS, Javascript, Python, Markdown.

## Git & GitHub ##

Used for version control.

GitHub link:

[https://github.com](https://github.com)

## Heroic Features ##

Bootstrap template used for the main page layout by Start Bootstrap.

Heroic Features link:

[https://startbootstrap.com/templates/heroic-features/](https://startbootstrap.com/templates/heroic-features/)

## Small Business ##

Bootstrap template used for the dedicated game page layout by Start Bootstrap.

[https://startbootstrap.com/templates/small-business/](https://startbootstrap.com/templates/small-business/)

## Notepad++ ##

Text editing software used for all coding tasks.

Notepad++ link:

[https://notepad-plus-plus.org](https://notepad-plus-plus.org)

## Tomorrow font ##

Described by its creator as:

"Tomorrow is a geometric family ranging from a neutral Thin weight to a vibrant contrast-based Black. It is an excellent fit for small sizes and big headlines. Easy to read and hard to forget."

Tomorrow link:

[https://github.com/MonicaRizzolli/Tomorrow](https://github.com/MonicaRizzolli/Tomorrow)

## Odibee Sans font ##

Odibee Sans link:

[github.com/barnard555/odibeesans](github.com/barnard555/odibeesans)

# Testing #

The website was tested on various devices with a number of different screen sizes and operating systems. The website was found to be well responsive in all tests.

**Other tests**

**Test 1 - Action link**

1. Go to the main page.
2. Click the "Action" link in the navbar.
3. The user should be directed to a page containing a list of all the games that are stored under the category "action".

**Test 2 - Puzzle link**

1. Go to the main page.
2. Click the "Puzzle" link in the navbar.
3. The user should be directed to a page containing a list of all the games that are stored under the category "puzzle".

**Test 2 - Sports link**

1. Go to the main page.
2. Click the "Sports" link in the navbar.
3. The user should be directed to a page containing a list of all the games that are stored under the category "sports".

**Test 2 - Educational link**

1. Go to the main page.
2. Click the "Educational" link in the navbar.
3. The user should be directed to a page containing a list of all the games that are stored under the category "educational".

**Test 3 - Random button**

1. Go to the main page.
2. Click the "Random" button.
3. The user should be directed to a page containing all of the details of a game stored in the database.
4. Click the "Home" button.
5. Again click the random button.
6. The user should be again directed to a page containing all of the details of another game stored in the database.

**Test 4 - Share button**

1. Go to the main page.
2. Click the "Share" button.
3. The user should be directed to the "share.html" page.
4. Click the "home" button.
5. The user should be directed to the main page and no information should have been added to the database.

**Test 5 - Sharing a game**

1. Go to the main page.
2. Click the "Share" button.
3. The user should be directed to the "share.html" page.
4. Enter the details of a game.
5. Click the share button.
6. The user should be directed to the main page and the game details submitted should now be visible on the main page.
7. Click the category of game entered in step 4 on the navbar.
8. The game that was entered should now be visible on the bottom of the list in the category page.

**Test 6 - Deleting a game**

1. Select a game from the main page.
2. Click the delete button.
3. The user should be directed to the main page. From here, confirm that the game delted in the previous step has in fact been deleted.
4. The game should not be available for viewing.

**Test X - Navigation**

1. Go to the main page
2. Click the link on the navbar entitles 'Action'
3. The user should be redirected to the page that contains all of the games in the Action category
4. Click the Home icon on the navbar
5. The user should be redirected to the main page once again
6. Click the link on the navbar entitles 'Puzzle'
7. The user should be redirected to the page that contains all of the games in the Puzzle category

**Test 7 - Editing a game (no changes made)**

**Test 8 - Editing a game (changes made)**

**Tests 8, 9, 10 - Social media links**

**Test 11 - Responsivness**

**Test 12, 13 - Feedback**

1. Go to the main page.
2. Hover the mouse over the links in the navbar, the social media links in the footer as well as the buttons in the jumbotron.
3. All of these elements should respond to the users hover. The links should grow larger whilst hovered over and the buttons should change colour whilst hovered over.

**Test 14 - User experience**

This test involved the participation of volunteers. The aim was to determine if the user interface was intuitive to a casual user.

The first volunteer was asked to navigate to the Action category using an IPhone. They were then to select one game and attempt to play that game. The user was able to cayy out these tasks with ease.

The second user was asked to select a random game by using the random button on the main page using a desktop computer. They were then asked to edit the title of that game by using the edit button. The user completed the task with relative ease but did  report that the text on the edit screen was hard to read. This test resulted in the darkening of text on the edit screen.

**Test X - Entering games with identical names**

It is not uncommon in the indie games scene for two or more games to share the same name. This test was designed to ensure the website would be able to handle such a situation.

1. Go to the main page
2. Click the share game button
3. Enter the following details

    "Title: Elephant Quest
    
    Developer: ArmorGames
    
    Genre: Action
    
    Link: https://elephant quest.com
    
    Short description: Super fun action platformer
    
    Description: Fast paced action game where the user controls an elephant that can fire laser cannons. Save the other elephants by shooting enemies and collecting powerups. Arrow Keys/WASD to move, mouse to shoot.
    
    Screenshots 1, 2 & 3: https://imgur.com/el1.jpg, https://imgur.com/el2.jpg, https://imgur.com/el3.jpg"

4. Repeat step 3 but enter a developer named `"other developer"`
5. Navigate to the "Action" category page.
6. The two games should be visible.
7. Click on each game and ensure they show that they were developed by different developers.

**Deployment (web)**

The following steps were taken to deploy the website online:

1. An account was created with Heroku.
2. A new Heroku app was created.
3. Gunicorn server was installed with the command: `$ pip install gunicorn` See above for more information regarding Gunicorn.
4. A file named "Procfile" was created containing information about Gunicorn that is needed by Heroku.
5. The heroku app was linked to the GitHub repository of Indie Games Flaunt.
6. Heroku was set to automatically update with each commit.
7. From the MongoDB website under the network access tab, an IP address of 0.0.0.0/0 was entered for the website's database. This IP address is what is known as a whitelist IP meaning that all traffic will be allowed to interact with the database (including Heroku)
8. An enviornment variable was added to the Heroku app for the website with the key "MONGO_URI". This key contains values that link to the websites database as well as password details. Having the database access restricted to this enviornment variable keeps the data safe.

**Deployment (local)**

In order to deploy this website on a local machine, the following steps would need to be taken:
1. 

