import 'react-native';
import React from 'react';
import RankingScreen from '../view_components/RankingScreen';
import renderer from 'react-test-renderer';

test('Ranking Rendered Page', () => {
  const snap = renderer.create(<RankingScreen />).toJSON();
  expect(snap).toMatchSnapshot();
});
