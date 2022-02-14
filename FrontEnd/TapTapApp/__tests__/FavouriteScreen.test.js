import 'react-native';
import React from 'react';
import FavouriteScreen from '../view_components/FavouriteScreen';
import renderer from 'react-test-renderer';

test('Profile Rendered Page', () => {
  const snap = renderer.create(<FavouriteScreen />).toJSON();
  expect(snap).toMatchSnapshot();
});
