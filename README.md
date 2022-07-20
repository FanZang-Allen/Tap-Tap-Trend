# Tap Tap Trend
> Full stack app for Tap Tap

For more information about Tap Tap, please refer to [Wiki](https://zh.wikipedia.org/wiki/TapTap).

![](https://upload.wikimedia.org/wikipedia/zh/a/a9/TapTap_logo.png)

## Get Started

Check Manual Test Plan to know how to install the app to mobile phones.
Type python command_line_interface to start back end system.

##Project Description

### Project Purpose
The purpose of this project is to help users easily obtain information about trending mobile games, discover
fascinating games and browse strategies or anecdotes shared by players in this game circle. 

### Project Motivation
Very often, when people open app store to find current popular mobile games, they can only get ranking list about 
trending games in their regions or countries. Additionally, most reviews about games in app stores are not from users
who are actually playing this game, but from those who have uninstalled the game. As more and more games include social 
features, players pay more attention to whether the game circle is active.However, all of this information is not provided
in common app stores.

TapTap,a third party game download application platform as well as a game community, solves these problems,but it is only famous
among Chinese. TapTap has over 1.1 million daily active users, over 6 million monthly active users and over 22 million total users.
It contains ranking list of games by more than six countries including the United States, China, Japan and Korean. It 
also creates community group for each game where many players share thoughts and funny moments. 

Therefore, I want to develop a mobile app that help users quickly get trending content in TapTap.


## Technical Specification
- Platform: Cross-platform app (React Native)
- Programming Languages: JavaScript / Python for Flask backend and scraping
- Stylistic Conventions: Airbnb JavaScript Style Guide/PEP 8 guide
- SDK: Facebook SDK for React Native (possible for social login)
- Database: MongoDB
- IDE: Visual Studio Code, Pycharm
- Tools/Interfaces: Mobile devices
- Target Audience: Anyone interested in mobile games

## Functional Specification
### Features
- Displaying ranking list of popular mobile games by regions.
- Displaying popular mobile games based on genres.
- Displaying detail information of each game including title, genre,rating,reviews, provider, number of downloads, number of followers,
introduction of game,and posts from players in game community.
- Support account system and allow users to add game to their favourite list.
- Support discover feature: allow users to find games based on genres or rating.

### UI Sketch
- Start Screen

![](https://i.ibb.co/BjbVjLN/Final-project-start-screen.jpg)

- Ranking List Screen (Show as default screen after login succeed)

![](https://i.ibb.co/f8G9Nx1/Ranking-Screen.jpg)

- Discovery Screen (Show after discover button is clicked)

![](https://i.ibb.co/NpXKZwX/Discover-Screen.jpg)

- Discovery Screen (Show after favourite button is clicked)

![](https://i.ibb.co/9mX9LDY/Favourite-Screen.jpg)

- Profile Screen (Show after Profile button is clicked)

![](https://i.ibb.co/LP1z0d0/Profile-Screen.jpg)

- Game Info Screen (Show after 'Details' text is clicked)

![](https://i.ibb.co/nbWtfCf/Game-Info-Screen.jpg)

### Scope of the project
- This app currently might be only deployed on localhost
- Ranking list only contains top 10 games
- Not all genres of games are included in this app and each genre only contain at most 50 games
- Only recent 10 posts in game community is showed in this app.
- Only recent 10 reviews about a game is showed in this app.

## Release History

* 1.0 
    * ADD: Game & Ranking & Genre scraper
    * ADD: Database connection
    * ADD: Command line interface to control the scraper
    * ADD: Unit test for all classes
* 2.0 
    * ADD: Flask RESTful API
    * ADD: User System
    * ADD: Command line interface with API function
    * ADD: Postman manual test

    
## Contributor

Fan Zang - fanzang2@illinois.edu


