import fetch from 'node-fetch';
import {headers} from './Config';

class GameList {
  constructor(fetchUrl, requestList) {
    this.fetchUrl = fetchUrl;
    this.requestList = requestList;
    this.success = false;
    this.errorMsg = undefined;
  }

  SetData(queryResult) {
    this.gameCount = queryResult.length;
    let game_list = [];
    let index = 1;
    queryResult.forEach(data => {
      let gameInfo = {};
      gameInfo.id = data.id;
      gameInfo.name = data.name;
      gameInfo.provider = data.provider;
      gameInfo.rating = data.rating.trim();
      if (data.region !== null) {
        gameInfo.region = data.region.trim();
      } else {
        gameInfo.region = 'Unknown';
      }
      gameInfo.logo = data.logo;
      gameInfo.index = index;
      let genreStr = data.genre[0];
      if (data.genre.length >= 2) {
        genreStr += ` · ${data.genre[1]}`;
      }
      if (data.genre.length >= 3) {
        genreStr += ` · ${data.genre[2]}`;
      }
      gameInfo.genre = genreStr;
      index += 1;
      game_list.push(gameInfo);
    });
    this.gameList = game_list;
  }

  GetData() {
    return this.gameList;
  }

  async FetchData() {
    try {
      let response = null;
      if (this.requestList === null) {
        response = await fetch(this.fetchUrl, {
          method: 'GET',
        });
      } else {
        response = await fetch(this.fetchUrl, {
          method: 'POST',
          headers: headers,
          body: JSON.stringify(this.requestList),
        });
      }
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
    if (this.requestList === null) {
      return fetch(this.fetchUrl, {
        method: 'GET',
      }).then(res => res.json());
    } else {
      return fetch(this.fetchUrl, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(this.requestList),
      }).then(res => res.json());
    }
  }
}

export default GameList;
