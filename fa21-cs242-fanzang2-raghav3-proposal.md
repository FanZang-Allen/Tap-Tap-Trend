# A Mobile App called TapTap Trend
Fan Zang (fanzang2) | Moderator: Raghav Saini (raghav3)

This is a mobile app providing user with selected content from TapTap.

## Abstract
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

## Brief Timeline
- Week 1:
1. Design MongoDB database schema.
2. Build scrapers to gather game information,ranking list, and posts in community.
3. Design simple command line interface to show stored info in database.
- Week 2:
1. Build a RESTful API to manipulate data in week 1
2. Design query parser for querying games based on genres and rating.
3. Extend command line interface to be more interactive and include API functions
- Week 3:
1. Build front end mobile app and render content correctly.
2. Connect to backend database using api form week 2.
3. Develop account system and store user information.



## Rubrics
### Week 1
| Category  | Total Score Allocated | Detailed Rubrics                                                            |
|-----------|:---------:|-------------------------------------------------------------------------------|
|  MongoDB  |  4  |  0: Didn't implement anything <br> 1: use env. for security <br> 2: successfully connect to database <br> 4: design suitable schema and implement proper attributes|
|  Web Scraper|  5  |  0: Didn't implement anything <br> 1: Properly report error <br> 2.5: successfully scrape ranking list by regions <br> 4: successfully scrape games of different genres <br> 5: successfully scrape all detail info of games |
|  Command Line Interface |  4  |  0: Didn't implement anything <br> 1: CLI able to show result in json <br> 2.5: CLI able to show games name & id in ranking list and genres. <br> 4: CLI able to show detail info of game by id |
|  Pylint |  2  |  0: Didn't setup pylint <br> 0.5: set up pylint <br> 2: average score greater than 8.5 |
|  Unit Test |  5  |  0: No unit test <br> +0.5：each unit test |
|  Manual Test Plan |  5  |  0: No manual test plan <br> 1: If test include only environment setup <br> 3: test contains only some content(< 6 pages)  <br> 5: well-composed test plans covering all aspects(8-10 pages)|

- Grade sheet link: https://docs.google.com/spreadsheets/d/1p_NWJSJ_ag_wD3ySQc5DFzuSNEoLx79bsjKsvhn6yZI/edit?usp=sharing

### Week 2
| Category  | Total Score Allocated | Detailed Rubrics                                                            |
|-----------|:---------:|-------------------------------------------------------------------------------|
|  API |  5  |  0: Didn't implement anything <br> 1.5: Implement routes that support getting ranking list & detailed info of 1 game <br> 3.5: implemented routes that support advance query (combined with query parser) of database <br> 5: implement routes that support adding user information <br> -0.5: for not reporting error for each route <br> -0.5: for not returning valid JSON|
|  Query Parser |  5  |  0: Didn't implement anything <br> 1: support logic operator 'NOT'  <br> 2: support logic operator 'AND' <br> 3: support comparison operator '<' and '>' <br> 4  support query games based on genres <br> 5: support query games based on rating  |
|  Interactive CLI |  4  |  0: Didn't implement anything <br> 1: make CLI interactive <br> 2: support function of CLI in week 1 <br> 4: support all api call functions |
|  Pylint |  1  |  0: Didn't setup pylint <br> 0.5: set up pylint <br> 1: average score greater than 8.5 |
|  Unit Test |  5  |  0: No unit test <br> +0.5：each unit test  |
|  Manual Test Plan For Postman |  5  |  0: No manual test plan <br> +1: each route test |

- Grade sheet link: https://docs.google.com/spreadsheets/d/1hBcEG2dnkFpezC2zIrTGXJdXltbvFhoylNg3Z5dhOq4/edit?usp=sharing

### Week 3
| Category  | Total Score Allocated | Detailed Rubrics                                                            |
|-----------|:---------:|-------------------------------------------------------------------------------|
|  Render Content  |  5  |  <br> +1: Sign In/Out View are implemented <br> +1: Ranking List View are implemented <br> +1: Game Genre View are implemented <br> +1: Discover Game View are implemented <br> +1: Favourite Game List View are implemented|
|  Model classes |  4  |  -1: if JSON object used directly as a model <br> -1: if no handling of errors <br> -1: No separation between model and view <br> -1: Not using api from week 2  |
|  Account System |  4  |  0: No account system <br> 1: support sign in feature <br> 2: support sign up feature <br> 3: show favourite list of different user correctly <br> 4: Support password changing feature|
|  ESLint |  2  |  -2: if ESLint is not properly set up or there is an error reported <br> -1: if there is a warning report  |
|  Unit Tests |  5  |  0: No unit test <br> +1：for each unit test of model class |
|  Snapshot tests |  5  |  0: No Snapshot tests <br> -1: For each untested screen <br> -1: loading screen is not tested |

- Grade sheet link: https://docs.google.com/spreadsheets/d/1-Puyo10db6Tp_w6X_vzZlpmJgWMa9_WaW8vF7dHBb0M/edit?usp=sharing


