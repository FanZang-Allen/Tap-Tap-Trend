import 'react-native';
import React from 'react';
import PostFlatList from '../view_components/PostFlatList';
import renderer from 'react-test-renderer';

let testData = [
  {
    avatar_url:
      'https://img3.tapimg.com/third_avatars/8ae34ff7a2161faa5f1ad252d8cbfed4.jpg?imageMogr2/auto-orient/strip/thumbnail/!300x300r/gravity/Center/crop/300x300/format/jpg/interlace/1/quality/40',
    content: 'uhm what? I won in rank match then this happened',
    id: 0,
    link: 'https://www.taptap.io/moment/201170072394272916',
    post_time: '5 days ago',
    poster: 'Andrei Gariguez',
    type: ' General ',
    views: ' 35 Views ',
  },
];

test('Game Flat List Rendered Page', () => {
  const snap = renderer
    .create(
      <PostFlatList
        gotData={testData}
        refreshing={false}
        onRefresh={() => console.log('This screen not suppport refresh')}
      />,
    )
    .toJSON();
  expect(snap).toMatchSnapshot();
});
