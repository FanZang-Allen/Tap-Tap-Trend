/* eslint-disable react-hooks/rules-of-hooks */
/* eslint-disable react-native/no-inline-styles */
import React from 'react';
import {useState, useEffect} from 'react';
import {
  View,
  Text,
  StyleSheet,
  ImageBackground,
  Image,
  ScrollView,
  Button,
} from 'react-native';
import Game from '../model/Game';
import ReviewFlatList from './ReviewFlatList';
import PostFlatList from './PostFlatList';
import {InFavourite, user_data, baseUrl, headers} from '../model/Config';

const GameScreen = ({navigation, route, gotData}) => {
  const [selectedTab, setSelectedTab] = useState(1);
  const [gameData, setgameData] = useState(null);
  const [like, setLike] = useState(InFavourite(route.params.game_id));

  function renderHeader(data) {
    return (
      <View>
        <View style={styles.header_container}>
          <Image
            source={{
              uri: data.logo,
            }}
            style={styles.game_image}
            resizeMode="contain"
          />
          <View style={styles.header}>
            <Text style={styles.game_name}>{data.name}</Text>
            <Text style={styles.provider_name}>{data.provider}</Text>
            <Text style={styles.dev_name}>Dev Onboard</Text>
          </View>
        </View>
        <View style={styles.tab_bar}>
          <View
            style={
              selectedTab === 1 ? styles.focused_tab : styles.unfocused_tab
            }>
            <Text style={styles.tab_text} onPress={() => setSelectedTab(1)}>
              Detail
            </Text>
          </View>
          <View
            style={
              selectedTab === 2 ? styles.focused_tab : styles.unfocused_tab
            }>
            <Text style={styles.tab_text} onPress={() => setSelectedTab(2)}>
              Review
            </Text>
          </View>
          <View
            style={
              selectedTab === 3 ? styles.focused_tab : styles.unfocused_tab
            }>
            <Text style={styles.tab_text} onPress={() => setSelectedTab(3)}>
              Group
            </Text>
          </View>
        </View>
      </View>
    );
  }
  function renderDetail(data) {
    let header = renderHeader(data);
    return (
      <View style={styles.container}>
        {header}
        <View style={styles.detail_container}>
          <View style={styles.info_container}>
            <Text
              style={
                styles.download_text
              }>{`Downloads: ${data.downloads}`}</Text>
            <Text
              style={
                styles.download_text
              }>{`Followers: ${data.followers}`}</Text>
            <Text style={styles.download_text}>{data.genre}</Text>
            <Text style={styles.about_header}>About</Text>
          </View>
          <View style={styles.rating_container}>
            <Image
              source={require('../assets/Favourite.png')}
              style={styles.rating_image}
              resizeMode="contain"
            />
            <Text style={styles.rating_text}>{data.rating}</Text>
          </View>
        </View>
        <View style={{flex: 1, backgroundColor: '#ffffff'}}>
          <ScrollView style={styles.about_scrollView}>
            <Text style={styles.about_text}>{data.intro}</Text>
          </ScrollView>
        </View>
        <View style={{backgroundColor: '#ffffff'}}>
          <View style={{margin: 10}}>
            <Button
              title={like ? 'Remove From Favourite' : 'Add to Favourite'}
              onPress={changeFavourite}
            />
          </View>
        </View>
      </View>
    );
  }

  if (gotData !== undefined) {
    return renderDetail(gotData);
  }

  useEffect(() => {
    let fetchCalled = false;
    async function intialFetch() {
      const gameClass = new Game(route.params.game_id);
      await gameClass.FetchData();
      if (gameClass.success === false) {
        setgameData(undefined);
      } else {
        setgameData(gameClass.GetData());
      }
    }
    if (fetchCalled === false) {
      intialFetch();
      fetchCalled = true;
    }
  }, [route.params.game_id]);

  async function changeFavourite() {
    const fetchUrl =
      baseUrl +
      `/api/user/favourite?user_id=${user_data.id}&game_id=${route.params.game_id}`;
    if (like === true) {
      try {
        let response = await fetch(fetchUrl, {
          method: 'DELETE',
          headers: headers,
        });
        let response_data = await response.json();
        if (response.status !== 200) {
          console.log(response_data.Error_message);
        } else {
          const index = user_data.favourite_list.indexOf(route.params.game_id);
          user_data.favourite_list.splice(index, 1);
          setLike(false);
          console.log(response_data.Response);
        }
      } catch (e) {
        console.log(e);
      }
    } else {
      try {
        let response = await fetch(fetchUrl, {
          method: 'PUT',
          headers: headers,
        });
        let response_data = await response.json();
        if (response.status !== 200) {
          console.log(response_data.Error_message);
        } else {
          user_data.favourite_list.push(route.params.game_id);
          setLike(true);
          console.log(response_data.Response);
        }
      } catch (e) {
        console.log(e);
      }
    }
  }

  function renderReview() {
    let header = renderHeader(gameData);
    return (
      <View style={styles.container}>
        {header}
        <ReviewFlatList
          gotData={gameData.reviews}
          navigation={navigation}
          refreshing={false}
          onRefresh={() => console.log('This screen not suppport refresh')}
        />
      </View>
    );
  }
  function renderGroup() {
    let header = renderHeader(gameData);
    return (
      <View style={styles.container}>
        {header}
        <PostFlatList
          gotData={gameData.posts}
          navigation={navigation}
          refreshing={false}
          onRefresh={() => console.log('This screen not suppport refresh')}
        />
      </View>
    );
  }
  function RenderFailed() {
    return (
      <View style={styles.container}>
        <ImageBackground
          source={{
            uri: 'https://scottleejenkins.files.wordpress.com/2014/07/werwerwerwerwerwer.jpg',
          }}
          style={styles.background}
        />
      </View>
    );
  }
  function RenderLoading() {
    return (
      <View style={styles.background}>
        <Text>Loading</Text>
      </View>
    );
  }
  if (gameData === null) {
    return RenderLoading();
  } else if (gameData === undefined) {
    return RenderFailed();
  } else {
    if (selectedTab === 1) {
      return renderDetail(gameData);
    } else if (selectedTab === 2) {
      return renderReview();
    } else {
      return renderGroup();
    }
  }
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  header_container: {
    height: 120,
    backgroundColor: '#426A70',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
  },
  game_image: {
    flex: 1,
    width: 100,
    height: 100,
    margin: 10,
  },
  rating_image: {
    flex: 1,
    width: 40,
    height: 40,
    marginTop: 15,
  },
  header: {
    flex: 3,
    flexDirection: 'column',
    justifyContent: 'space-between',
    marginVertical: 10,
  },
  game_name: {
    fontSize: 23,
    fontWeight: 'bold',
    color: '#ffffff',
  },
  provider_name: {
    marginTop: 2,
    fontSize: 19,
    color: '#ffffff',
  },
  dev_name: {
    fontSize: 18,
    color: '#0B0730',
  },
  detail_container: {
    height: 160,
    backgroundColor: '#ffffff',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
  },
  info_container: {
    flex: 7,
    flexDirection: 'column',
    justifyContent: 'space-between',
    marginVertical: 10,
    marginHorizontal: 10,
  },
  rating_container: {
    flex: 3,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
  },
  download_text: {
    color: '#9B9B9B',
    fontSize: 18,
    fontWeight: 'bold',
  },
  rating_text: {
    flex: 2,
    color: '#4E40F8',
    fontSize: 30,
    fontWeight: 'bold',
  },
  background: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    paddingTop: 20,
    paddingBottom: 10,
  },
  tab_bar: {
    flexDirection: 'row',
    justifyContent: 'space-evenly',
    height: 50,
  },
  tab_text: {
    fontSize: 20,
    color: 'black',
    fontWeight: 'bold',
    alignSelf: 'center',
  },
  about_header: {
    marginTop: 5,
    color: 'black',
    fontSize: 22,
    fontWeight: 'bold',
    textDecorationLine: 'underline',
  },
  about_scrollView: {
    marginHorizontal: 10,
  },
  about_text: {
    color: 'black',
    fontSize: 16,
  },
  focused_tab: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'white',
    borderColor: 'blue',
    borderBottomWidth: 2,
  },
  unfocused_tab: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'white',
    borderColor: 'blue',
    borderBottomWidth: 0,
  },
});

export default GameScreen;
