import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  SafeAreaView,
  FlatList,
  Image,
  RefreshControl,
} from 'react-native';

const ReviewFlatList = ({navigation, gotData, refreshing, onRefresh}) => {
  const Item = ({
    name,
    time,
    avatarUrl,
    rating,
    content,
    play_time,
    device,
  }) => (
    <View style={styles.item}>
      <View style={styles.header_container}>
        <View style={styles.avatar_container}>
          <Image
            source={{
              uri: avatarUrl,
            }}
            style={styles.avatar_image}
            resizeMode="contain"
          />
        </View>
        <Text style={styles.user_name}>{name}</Text>
        <View style={styles.rating_container}>
          <Image
            source={require('../assets/RatingStar.png')}
            style={styles.rating_image}
            resizeMode="contain"
          />
          <Text style={styles.rating_str}>{rating}</Text>
        </View>
        <Text style={styles.detial_str}>{time}</Text>
      </View>
      <View style={styles.content_container}>
        <ScrollView style={styles.content_scrollView}>
          <Text style={styles.content_text}>{content}</Text>
        </ScrollView>
      </View>
      <View style={styles.detail_container}>
        <Text style={styles.detial_str}>{play_time}</Text>
        <Text style={styles.detial_str}>{device}</Text>
      </View>
    </View>
  );

  const renderItem = ({item}) => (
    <Item
      name={item.reviewer}
      time={item.review_time}
      avatarUrl={item.avatar_url}
      rating={item.rating}
      content={item.content}
      play_time={item.play_time === undefined ? 'Played 0 min' : item.play_time}
      device={item.device === undefined ? 'Unknown Device' : item.device}
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
      <View style={styles.background}>
        <Text style={styles.provider_name}>Not Available</Text>
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
    flexDirection: 'column',
    justifyContent: 'space-evenly',
    borderRadius: 15,
  },
  header_container: {
    height: '30%',
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'flex-start',
    alignItems: 'center',
  },
  content_container: {
    height: '60%',
    flex: 1,
  },
  content_scrollView: {
    marginLeft: 17,
    marginTop: 5,
  },
  content_text: {
    fontSize: 14,
    color: 'black',
    fontWeight: 'bold',
  },
  detail_container: {
    height: '10%',
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'flex-start',
    alignItems: 'center',
    marginLeft: 15,
  },
  detial_str: {
    flex: 1,
    fontSize: 14,
    color: '#9B9B9B',
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
    marginLeft: 5,
  },
  avatar_image: {
    flex: 1,
    width: 35,
    height: 35,
  },
  rating_image: {
    width: 20,
    height: 20,
  },
  user_name: {
    fontSize: 16,
    color: 'black',
    fontWeight: 'bold',
  },
  rating_str: {
    flex: 4,
    fontSize: 14,
    color: '#9076FB',
  },
  provider_name: {
    flex: 4,
    fontSize: 14,
    color: '#9B9B9B',
  },
});

export default ReviewFlatList;
