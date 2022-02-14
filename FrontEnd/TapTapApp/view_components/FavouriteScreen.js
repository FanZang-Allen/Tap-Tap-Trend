import React from 'react';
import {useState, useEffect, useCallback} from 'react';
import {SafeAreaView, StyleSheet} from 'react-native';
import GameFlatList from './GameFlatList';
import GameList from '../model/GameList';
import {baseUrl, user_data} from '../model/Config';

const FavouriteScreen = ({navigation}) => {
  const [refreshing, setRefreshing] = useState(false);
  const [gameData, setgameData] = useState(null);
  const fetchUrl = baseUrl + '/api/game';

  const onRefresh = useCallback(() => {
    setRefreshing(true);
    async function fetchFavourite() {
      const gameClass = new GameList(fetchUrl, user_data.favourite_list);
      await gameClass.FetchData();
      if (gameClass.success === false) {
        setgameData(undefined);
        setRefreshing(false);
      } else {
        setgameData(gameClass.GetData());
        setRefreshing(false);
      }
    }
    fetchFavourite();
  }, [fetchUrl]);

  useEffect(() => {
    let fetchCalled = false;
    async function intialFetch() {
      const gameClass = new GameList(fetchUrl, user_data.favourite_list);
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
  }, [fetchUrl]);

  return (
    <SafeAreaView style={styles.container}>
      <GameFlatList
        gotData={gameData}
        navigation={navigation}
        refreshing={refreshing}
        onRefresh={onRefresh}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});

export default FavouriteScreen;
