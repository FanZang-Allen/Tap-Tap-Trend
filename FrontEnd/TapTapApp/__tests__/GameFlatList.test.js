import 'react-native';
import React from 'react';
import GameFlatList from '../view_components/GameFlatList';
import renderer from 'react-test-renderer';

let testData = [
  {
    genre: 'PVP · PUBG · Online',
    id: '82354',
    index: 1,
    logo: 'https://img.tapimg.com/market/icons/4cf4ff9eb0d623a2ae9cf5ecc49879c3_360.png?imageMogr2/auto-orient/strip',
    name: 'Fortnite',
    provider: 'Epic Games',
    rating: '6.9',
    region: 'Global',
  },
];

test('Game Flat List Rendered Page', () => {
  const snap = renderer
    .create(
      <GameFlatList
        gotData={testData}
        refreshing={false}
        onRefresh={() => console.log('This screen not suppport refresh')}
      />,
    )
    .toJSON();
  expect(snap).toMatchSnapshot();
});
