# Indie Games Flaunt #

A website where indie game developers can share their games.

## Terms ##

*flaunt* - display (something) ostentatiously, especially in order to provoke envy or admiration or to show defiance.

*Indie game* - a video game, commonly created by an individual or a small team without the support of a video game publisher.

Indie games are mostly found on dedicated websites that cater to the needs of developers as opposed to casual users. These sites (usually forums) are aimed at computer savvy individuals and as such can be off putting to more casual users - the interfaces can be difficult to navigate and can be difficult to use on mobile devices. This website attempts to give developers a place to share their games whilst at the same time catering to casual gamers. The user interface is designed to be easy to navigate on mobile as well as desktop computers. 
 
## UX ##

**External users goal:**
A casual game player can browse the site and download a game they wish to play.

**External users goal:**
A game developer can share their game.

**Site owners goal:**
Promote indie game development by providing a website where developers have access to a large audience of casual game players as well as indie developers themselves.

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

A Bootstrap template was select, titled "Heroic Features". It appears to have much of the intended layout goals already implemented out of the box such as the nav bar and standout, easy to read text.

![](img/readme_img/heroic_features.png)

Image 2. Heroic Features

Below we see the final chosen design for the main page. We see a Jumbotron as well as three cards. What is not clear from the image is that the cards are intended to be housed within a carousel object. This will allow the user to scroll and cycle through all of the games available in the database.

![](img/readme_img/main_desktop.png)

Image 3. Wireframe of the main page as seen from a desktop computer

Below we see the main page as it should look from a smartphone.

![](img/readme_img/main_mobile.png)

Image 4. Wireframe of the main page as seen on a smartphone

Dedicated game screen

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

# Technologies Used #

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

Other tests

1. Go to the main page.
2. Click the "Action" link in the navbar.
3. The user should be directed to a page containing a list of all the games that are stored under the category "action".

1. Go to the main page.
2. Click the "Puzzle" link in the navbar.
3. The user should be directed to a page containing a list of all the games that are stored under the category "puzzle".

1. Go to the main page.
2. Click the "Random" button.
3. The user should be directed to a page containing all of the details of a game stored in the database.
4. Click the "Home" button.
5. Again click the random button.
6. The user should be again directed to a page containing all of the details of another game stored in the database.

1. Go to the main page.
2. Click the "Share" button.
3. The user should be directed to the "share.html" page.
4. Click the "home" button.
5. The user should be directed to the main page and no information should have been added to the database.

1. Go to the main page.
2. Click the "Share" button.
3. The user should be directed to the "share.html" page.
4. Enter the details of a game.
5. The user should be directed to the main page and the game details submitted should now be visible on the main page.

Deployment

The following steps were taken to deploy the website online.

1. An account was created with Heroku.

2. A new Heroku app was created.

3. The heroku app was linked to the projects GitHub repository.

4. Heroku was set to automatically update with each commit

# Rough work section (to be removed) #

***

**Git quick links**

…or create a new repository on the command line

echo "# IGF" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/andrewdempsey2018/IGF.git
git push -u origin master

…or push an existing repository from the command line

git remote add origin https://github.com/andrewdempsey2018/IGF.git
git push -u origin master

…or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

***

**DB Info**

IGF_DB

app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@andrewcluster-igjjx.mongodb.net/IGF_DB?retryWrites=true&w=majority

IGF_COLL

***

Heroku Info

igf

https://igf.herokuapp.com/

***

add to technologies used

Click==7.0
dnspython==1.16.0
Flask==1.1.1
Flask-PyMongo==2.3.0
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
pymongo==3.9.0
Werkzeug==0.16.0


***