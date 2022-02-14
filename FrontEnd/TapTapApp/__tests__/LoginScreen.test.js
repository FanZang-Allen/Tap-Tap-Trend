import 'react-native';
import React from 'react';
import LoginScreen from '../view_components/LoginScreen';
import renderer from 'react-test-renderer';

test('Login Rendered Page', () => {
  const snap = renderer.create(<LoginScreen />).toJSON();
  expect(snap).toMatchSnapshot();
});
