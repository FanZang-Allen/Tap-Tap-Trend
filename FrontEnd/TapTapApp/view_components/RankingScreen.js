import React from 'react';
import {useState, useEffect} from 'react';
import {View, Text, StyleSheet} from 'react-native';
import {Picker} from '@react-native-picker/picker';
import {baseUrl} from '../model/Config';
import GameList from '../model/GameList';
import GameFlatList from './GameFlatList';

const RankingScreen = ({navigation, testMode}) => {
  const [selectedRegion, setSelectedRegion] = useState('USA');
  const [gameData, setgameData] = useState(null);
  const regionUrl = baseUrl + '/api/rank?region=';

  async function fetchData() {
    const gameClass = new GameList(regionUrl + selectedRegion, null);
    await gameClass.FetchData();
    if (gameClass.success === false) {
      setgameData(undefined);
    } else {
      setgameData(gameClass.GetData());
    }
  }

  async function switchRegion(itemValue) {
    setSelectedRegion(itemValue);
    setgameData(null);
    fetchData();
  }

  useEffect(() => {
    let fetchCalled = false;
    async function intialFetch() {
      const gameClass = new GameList(regionUrl + selectedRegion, null);
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
  }, [regionUrl, selectedRegion]);

  return (
    <View style={styles.container}>
      <View style={styles.header_container}>
        <Text style={styles.header}>Top 15 Mobile Games</Text>
        <Picker
          selectedValue={selectedRegion}
          onValueChange={switchRegion}
          style={styles.region_picker}>
          <Picker.Item label="USA" value="USA" />
          <Picker.Item label="World" value="World" />
          <Picker.Item label="China" value="Taiwan" />
          <Picker.Item label="Japan" value="Japan" />
          <Picker.Item label="Korea" value="Korea" />
          <Picker.Item label="India" value="India" />
          <Picker.Item label="Vietnam" value="Vietnam" />
        </Picker>
      </View>
      <GameFlatList
        gotData={gameData}
        navigation={navigation}
        refreshing={false}
        onRefresh={() => console.log('This screen not suppport refresh')}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  header_container: {
    height: '10%',
    margin: 20,
  },
  header: {
    fontSize: 25,
    fontWeight: 'bold',
    alignSelf: 'center',
    color: '#000000',
  },
  region_picker: {
    width: '45%',
    alignSelf: 'center',
  },
  background: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    paddingTop: 20,
    paddingBottom: 10,
  },
});

export default RankingScreen;
