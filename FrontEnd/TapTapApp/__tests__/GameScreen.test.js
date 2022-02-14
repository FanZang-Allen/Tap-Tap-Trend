import 'react-native';
import React from 'react';
import GameScreen from '../view_components/GameScreen';
import renderer from 'react-test-renderer';

let testData = {
  downloads: '7047196',
  followers: '1295060',
  genre: 'Genre: PVP, PUBG, Online, RPG, Multiplayer, Shooter',
  id: '82354',
  intro: 'Drop.',
  logo: 'https://img.tapimg.com/market/icons/4cf4ff9eb0d623a2ae9cf5ecc49879c3_360.png?imageMogr2/auto-orient/strip',
  name: 'Fortnite',
  posts: undefined,
  posts_link: [],
  provider: 'Epic Games',
  rating: '6.9',
  region: ' Global ',
};

test('Game Rendered Page', () => {
  const snap = renderer
    .create(<GameScreen gotData={testData} route={{params: {game_id: '1'}}} />)
    .toJSON();
  expect(snap).toMatchSnapshot();
});
