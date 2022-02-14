import 'react-native';
import React from 'react';
import ReviewFlatList from '../view_components/ReviewFlatList';
import renderer from 'react-test-renderer';

let testData = [
  {
    avatar_url:
      'https://img3.tapimg.com/avatars/etag/FhWKmP9njgQkVuntFY9xQpxIgfvg.png?imageMogr2/auto-orient/strip/thumbnail/!300x300r/gravity/Center/crop/300x300/format/jpg/interlace/1/quality/40',
    content: 'looks great',
    device: ' Vivo V1955A ',
    id: 0,
    link: 'https://www.taptap.io/review/2148582585',
    rating: '5.0',
    review_time: '22 hr ago',
    reviewer: '康太郎',
  },
];

test('Game Flat List Rendered Page', () => {
  const snap = renderer
    .create(
      <ReviewFlatList
        gotData={testData}
        refreshing={false}
        onRefresh={() => console.log('This screen not suppport refresh')}
      />,
    )
    .toJSON();
  expect(snap).toMatchSnapshot();
});
