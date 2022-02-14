import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ImageBackground,
  SafeAreaView,
  FlatList,
  Image,
  RefreshControl,
} from 'react-native';

const GameFlatList = ({navigation, gotData, refreshing, onRefresh}) => {
  const Item = ({index, name, provider, avatarUrl, rating, genre, gameId}) => (
    <View style={styles.item}>
      <View style={styles.index_container}>
        <Text style={styles.game_name}>{index}</Text>
      </View>
      <View style={styles.avatar_container}>
        <Image
          source={{
            uri: avatarUrl,
          }}
          style={styles.avatar_image}
          resizeMode="contain"
        />
      </View>
      <View style={styles.text_container}>
        <Text
          style={styles.game_name}
          onPress={() => {
            navigation.navigate('Game', {game_id: gameId});
          }}>
          {name}
        </Text>
        <Text style={styles.genre_str}>{genre}</Text>
        <View style={styles.detail_container}>
          <Text style={styles.provider_name}>{provider}</Text>
          <View style={styles.rating_container}>
            <Image
              source={require('../assets/RatingStar.png')}
              style={styles.rating_image}
              resizeMode="contain"
            />
            <Text style={styles.rating_str}>{rating}</Text>
          </View>
        </View>
      </View>
    </View>
  );

  const renderItem = ({item}) => (
    <Item
      gameId={item.id}
      index={item.index}
      name={item.name}
      provider={item.provider}
      avatarUrl={item.logo}
      rating={item.rating}
      genre={item.genre}
    />
  );
  function RenderList(data) {
    return (
      <SafeAreaView style={styles.container}>
        <FlatList
          data={data}
          renderItem={renderItem}
          keyExtractor={item => item.id}
          refreshControl={
            <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
          }
        />
      </SafeAreaView>
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
        <Text style={styles.provider_name}>Loading</Text>
      </View>
    );
  }
  if (gotData === null) {
    return RenderLoading();
  } else if (gotData === undefined) {
    return RenderFailed();
  } else {
    return RenderList(gotData);
  }
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  background: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    paddingTop: 20,
    paddingBottom: 10,
  },
  item: {
    backgroundColor: '#ffffff',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-evenly',
    borderRadius: 15,
  },
  index_container: {
    width: '7%',
    flexDirection: 'row',
    justifyContent: 'flex-start',
    alignSelf: 'center',
    marginRight: 10,
  },
  text_container: {
    width: '73%',
    flex: 1,
    flexDirection: 'column',
    marginHorizontal: 16,
    justifyContent: 'space-between',
  },
  detail_container: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'flex-start',
  },
  avatar_container: {
    width: '20%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  rating_container: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'center',
  },
  avatar_image: {
    flex: 1,
    width: 80,
    height: 80,
  },
  rating_image: {
    width: 20,
    height: 20,
  },
  genre_str: {
    fontSize: 18,
    color: '#9B9B9B',
    fontWeight: 'bold',
  },
  game_name: {
    fontSize: 20,
    color: 'black',
    fontWeight: 'bold',
  },
  provider_name: {
    flex: 4,
    fontSize: 14,
    color: '#9B9B9B',
  },
  rating_str: {
    flex: 4,
    fontSize: 14,
    color: '#9076FB',
  },
});

export default GameFlatList;
