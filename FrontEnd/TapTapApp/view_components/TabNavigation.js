/* eslint-disable react-native/no-inline-styles */
import React from 'react';
import {View, Text, StyleSheet, Image} from 'react-native';
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';

import RankingScreen from './RankingScreen';
import DiscoverScreen from './DiscoverScreen';
import FavouriteScreen from './FavouriteScreen';
import ProfileScreen from './ProfileScreen';

const Tab = createBottomTabNavigator();

const TabNavigation = () => {
  return (
    <Tab.Navigator
      screenOptions={{
        headerShown: false,
        tabBarShowLabel: false,
        tabBarStyle: styles.tab_bar,
      }}>
      <Tab.Screen
        name="Ranking"
        component={RankingScreen}
        options={{
          tabBarIcon: ({focused}) => (
            <View style={styles.tab_view}>
              <Image
                source={require('../assets/ranking.png')}
                resizeMode="contain"
                style={styles.tab_image}
              />
              <Text
                style={{
                  color: focused ? '#4F18E8' : '#9B9B9B',
                  fontSize: 14,
                  fontWeight: 'bold',
                }}>
                Ranking
              </Text>
            </View>
          ),
        }}
      />
      <Tab.Screen
        name="Discover"
        component={DiscoverScreen}
        options={{
          tabBarIcon: ({focused}) => (
            <View style={styles.tab_view}>
              <Image
                source={require('../assets/Discover.png')}
                resizeMode="contain"
                style={styles.tab_image}
              />
              <Text
                style={{
                  color: focused ? '#4F18E8' : '#9B9B9B',
                  fontSize: 14,
                  fontWeight: 'bold',
                }}>
                Discover
              </Text>
            </View>
          ),
        }}
      />
      <Tab.Screen
        name="Favourite"
        component={FavouriteScreen}
        options={{
          tabBarIcon: ({focused}) => (
            <View style={styles.tab_view}>
              <Image
                source={require('../assets/Favourite.png')}
                resizeMode="contain"
                style={styles.tab_image}
              />
              <Text
                style={{
                  color: focused ? '#4F18E8' : '#9B9B9B',
                  fontSize: 14,
                  fontWeight: 'bold',
                }}>
                Favourite
              </Text>
            </View>
          ),
        }}
      />
      <Tab.Screen
        name="Profile"
        component={ProfileScreen}
        options={{
          tabBarIcon: ({focused}) => (
            <View style={styles.tab_view}>
              <Image
                source={require('../assets/Profile.png')}
                resizeMode="contain"
                style={styles.tab_image}
              />
              <Text
                style={{
                  color: focused ? '#4F18E8' : '#9B9B9B',
                  fontSize: 14,
                  fontWeight: 'bold',
                }}>
                Profile
              </Text>
            </View>
          ),
        }}
      />
    </Tab.Navigator>
  );
};

const styles = StyleSheet.create({
  tab_image: {
    width: 30,
    height: 30,
  },
  tab_bar: {
    backgroundColor: '#ffffff',
    borderRadius: 25,
    height: 75,
  },
  tab_view: {
    alignItems: 'center',
    justifyContent: 'center',
    top: 5,
  },
});

export default TabNavigation;
