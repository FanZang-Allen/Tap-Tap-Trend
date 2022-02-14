import 'react-native';
import React from 'react';
import ProfileScreen from '../view_components/ProfileScreen';
import renderer from 'react-test-renderer';

test('Profile Rendered Page', () => {
  const snap = renderer.create(<ProfileScreen />).toJSON();
  expect(snap).toMatchSnapshot();
});
