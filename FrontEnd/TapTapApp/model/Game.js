import fetch from 'node-fetch';
import {baseUrl, headers} from './Config';

class Game {
  constructor(requesID, testMode) {
    this.fetchUrl = baseUrl + '/api/game';
    if (testMode !== undefined) {
      this.fetchUrl = 'http://127.0.0.1:5000/api/game';
    }
    this.requestList = [requesID];
    this.success = false;
    this.errorMsg = undefined;
  }

  SetData(queryResult) {
    if (queryResult.length === 0) {
      this.gameInfo = null;
    } else {
      this.gameInfo = queryResult[0];
      let genreStr = 'Genre: ';
      for (let i = 0; i < queryResult[0].genre.length; i++) {
        genreStr += `${queryResult[0].genre[i]}, `;
      }
      genreStr = genreStr.slice(0, -2);
      this.gameInfo.genre = genreStr;
      for (let i = 0; i < queryResult[0].posts.length; i++) {
        this.gameInfo.posts[i].link = queryResult[0].posts_link[i];
        this.gameInfo.posts[i].id = i;
      }
      for (let i = 0; i < queryResult[0].reviews.length; i++) {
        this.gameInfo.reviews[i].link = queryResult[0].reviews_link[i];
        this.gameInfo.reviews[i].id = i;
      }
      if (this.gameInfo.reviews.length === 0) {
        this.gameInfo.reviews = undefined;
      }
      if (this.gameInfo.posts.length === 0) {
        this.gameInfo.posts = undefined;
      }
    }
  }

  GetData() {
    return this.gameInfo;
  }

  async FetchData() {
    try {
      let response = await fetch(this.fetchUrl, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(this.requestList),
      });
      console.log('yes');
      let response_data = await response.json();
      if (response.status !== 200) {
        this.errorMsg = response_data.Error_message;
      } else {
        this.success = true;
        this.SetData(response_data['Query Result']);
      }
    } catch (e) {
      console.log(e);
    }
  }

  async MockFetch() {
    return fetch(this.fetchUrl, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(this.requestList),
    }).then(res => res.json());
  }
}

export default Game;
