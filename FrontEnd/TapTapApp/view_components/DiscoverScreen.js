import React, {Component} from 'react';
import {Text, View, StyleSheet, TextInput, Button} from 'react-native';
import GameList from '../model/GameList';
import GameFlatList from './GameFlatList';
import MultiSelect from 'react-native-multiple-select';

class DiscoverScreen extends Component {
  items = [
    {id: 'Card'},
    {id: 'Shooter'},
    {id: 'ACGN'},
    {id: 'Roguelike'},
    {id: 'Unriddle'},
    {id: 'Word'},
    {id: 'Music'},
    {id: 'Otome game'},
    {id: 'Simulation'},
    {id: 'Sandbox'},
    {id: 'Open World'},
    {id: 'MMORPG'},
    {id: 'Chinese Style'},
    {id: 'Racing'},
    {id: 'Puzzle'},
    {id: 'Steam-ported'},
    {id: 'Survival'},
    {id: 'MOBA'},
    {id: 'Idle'},
    {id: 'Tower Defence'},
    {id: 'Pixel'},
    {id: 'Healing'},
    {id: 'Apocalypse'},
    {id: 'Fighting'},
    {id: 'Addictive'},
  ];
  constructor(props) {
    super(props);
    this.state = {
      selectedItems: [],
      rating: '0',
      gameData: null,
    };
    this.baseUrl = 'http://10.0.2.2:5000/api/search?query=';
  }

  onSelectedItemsChange = selectedItems => {
    this.setState({selectedItems});
  };
  onChangeRating = newRating => {
    this.setState({rating: newRating});
    console.log(newRating);
  };

  fetachGameData = event => {
    event.preventDefault();
    let queryStr = '';
    if (this.state.selectedItems.length > 0) {
      let genreQuery = `Genre: ${this.state.selectedItems[0]}`;
      for (let i = 1; i < this.state.selectedItems.length; i++) {
        genreQuery += ` AND ${this.state.selectedItems[i]}`;
      }
      queryStr += genreQuery + ';';
    }
    queryStr += `Rating: > ${this.state.rating};`;
    console.log(queryStr);
    const gameClass = new GameList(this.baseUrl + queryStr, null);
    gameClass.FetchData().then();
    setTimeout(() => this.setState({gameData: gameClass.GetData()}), 3000);
  };

  render() {
    const {selectedItems} = this.state;
    return (
      <View style={styles.container}>
        <View style={styles.header_container}>
          <Text style={styles.header}>Discover Games</Text>
          <View style={styles.genre_picker}>
            <MultiSelect
              hideTags
              items={this.items}
              uniqueKey="id"
              onSelectedItemsChange={this.onSelectedItemsChange}
              selectedItems={selectedItems}
              selectText="Pick Genres"
              searchInputPlaceholderText="Search Genres..."
              altFontFamily="ProximaNova-Light"
              displayKey="id"
              submitButtonText="Confirm"
            />
          </View>
          <View style={styles.rating_container}>
            <Text style={styles.rating_text}>Rating {'>'}</Text>
            <TextInput
              style={styles.rating_input}
              onChangeText={this.onChangeRating}
              value={this.state.rating}
              placeholder="useless placeholder"
              keyboardType="numeric"
            />
            <Button title="Search" onPress={this.fetachGameData} />
          </View>
        </View>
        <GameFlatList
          gotData={this.state.gameData}
          navigation={this.props.navigation}
          refreshing={false}
          onRefresh={() => console.log('This screen not suppport refresh')}
        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  header_container: {
    height: '28%',
    margin: 20,
  },
  header: {
    flex: 1,
    fontSize: 25,
    fontWeight: 'bold',
    alignSelf: 'center',
    color: '#000000',
  },
  genre_picker: {
    margin: 10,
    marginHorizontal: 60,
  },
  rating_container: {
    flexDirection: 'row',
    marginHorizontal: 60,
    justifyContent: 'flex-start',
  },
  rating_input: {
    height: 40,
    width: 90,
    borderWidth: 1,
    padding: 10,
    fontWeight: 'bold',
    marginHorizontal: 10,
  },
  rating_text: {
    fontSize: 20,
    fontWeight: 'bold',
    alignSelf: 'center',
    color: '#000000',
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

export default DiscoverScreen;
