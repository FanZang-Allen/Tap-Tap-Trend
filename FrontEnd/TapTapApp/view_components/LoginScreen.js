import React from 'react';
import {useState} from 'react';
import {
  View,
  Text,
  ImageBackground,
  StyleSheet,
  Button,
  TextInput,
  Alert,
} from 'react-native';
import {user_data, baseUrl, headers, ChangeUser} from '../model/Config';

const LoginScreen = ({navigation}) => {
  const [backText, setBackText] = useState('');
  const [showLogin, setShowLogin] = useState(true);
  const [inputID, setInputID] = useState('');
  const [inputPassword, setInputPassword] = useState('');

  function onChangePassword(newPassword) {
    setInputPassword(newPassword);
  }

  function onChangeID(newID) {
    setInputID(newID);
  }

  function pressBack() {
    setBackText('');
    setShowLogin(true);
  }

  async function pressSignIn() {
    if (inputID === '') {
      Alert.alert('Error', 'Please input a user name', [
        {text: 'OK', onPress: () => console.log('OK Pressed')},
      ]);
    } else if (inputPassword === '') {
      Alert.alert('Error', 'Please input a password', [
        {text: 'OK', onPress: () => console.log('OK Pressed')},
      ]);
    } else {
      try {
        const fetchUrl = baseUrl + `/api/user/info?id=${inputID}`;
        let response = await fetch(fetchUrl, {
          method: 'GET',
        });
        let response_data = await response.json();
        if (response.status !== 200) {
          Alert.alert('Error', 'Connection Error', [
            {text: 'OK', onPress: () => console.log('OK Pressed')},
          ]);
        } else {
          ChangeUser(response_data['Query Result'][0]);
        }
      } catch (e) {
        console.log(e);
      }
      if (user_data.password !== inputPassword) {
        Alert.alert('Error', 'Incorrect uid or password.', [
          {text: 'OK', onPress: () => console.log('OK Pressed')},
        ]);
      } else {
        setInputID('');
        setInputPassword('');
        navigation.navigate('Home');
      }
    }
  }

  async function pressSignUp() {
    if (showLogin === true) {
      setBackText('< Back');
      setShowLogin(false);
      return;
    } else {
      if (inputID === '') {
        Alert.alert('Error', 'Please input a user name', [
          {text: 'OK', onPress: () => console.log('OK Pressed')},
        ]);
      } else if (inputPassword === '') {
        Alert.alert('Error', 'Please input a password', [
          {text: 'OK', onPress: () => console.log('OK Pressed')},
        ]);
      } else {
        try {
          const fetchUrl = baseUrl + '/api/user/add';
          const data = {user_name: inputID, password: inputPassword};
          let response = await fetch(fetchUrl, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data),
          });
          let response_data = await response.json();
          if (response.status !== 200) {
            Alert.alert('Error', response_data.Error_message, [
              {text: 'OK', onPress: () => console.log('OK Pressed')},
            ]);
          } else {
            Alert.alert('Success', response_data.Response, [
              {text: 'OK', onPress: () => console.log('OK Pressed')},
            ]);
            setInputID('');
            setInputPassword('');
          }
        } catch (e) {
          console.log(e);
        }
      }
    }
  }

  return (
    <View style={styles.container}>
      <ImageBackground
        source={require('../assets/Background.png')}
        style={styles.background}>
        <Text style={styles.header}>TapTap Trend</Text>
        <View style={styles.input_container}>
          <Text style={styles.back_text} onPress={pressBack}>
            {backText}
          </Text>
          <TextInput
            style={styles.text_input}
            onChangeText={onChangeID}
            value={inputID}
            placeholder={showLogin ? 'UID' : 'UserName'}
            keyboardType={showLogin ? 'numeric' : 'default'}
          />
          <TextInput
            style={styles.text_input}
            onChangeText={onChangePassword}
            value={inputPassword}
            placeholder="Password"
            keyboardType="numeric"
          />
          <View style={styles.margin_container}>
            {showLogin && <Button title="Sign in" onPress={pressSignIn} />}
          </View>
          <View style={styles.margin_container}>
            <Button title="Sign Up" color="#F5A623" onPress={pressSignUp} />
          </View>
        </View>
      </ImageBackground>
    </View>
  );
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
  header: {
    fontSize: 36,
    color: '#ffffff',
    fontStyle: 'italic',
    fontWeight: 'bold',
    marginBottom: 30,
  },
  back_text: {
    fontSize: 18,
    marginBottom: 10,
  },
  margin_container: {
    marginBottom: 20,
    marginHorizontal: 10,
  },
  text_input: {
    height: 35,
    width: 210,
    borderWidth: 1,
    padding: 10,
    fontWeight: 'bold',
    marginBottom: 20,
    marginHorizontal: 10,
  },
  input_container: {
    width: 270,
    height: 320,
    backgroundColor: '#ffffff',
    flexDirection: 'column',
    justifyContent: 'flex-start',
    borderRadius: 15,
    padding: 20,
  },
  avatar_image: {
    width: '30%',
    height: '20%',
    borderRadius: 100,
  },
  text_container: {
    width: '90%',
    height: '45%',
    justifyContent: 'space-evenly',
  },
  bio_container: {
    width: '90%',
    height: '10%',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'baseline',
  },
  bio_scrollview: {
    flex: 1,
  },
  navigation_container: {
    width: '90%',
    height: '15%',
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  navigation_text: {
    color: '#4A08DB',
    fontSize: 24,
    fontWeight: 'bold',
    textDecorationLine: 'underline',
  },
  text: {
    color: 'white',
    fontSize: 24,
  },
  footer_text: {
    color: 'white',
    fontSize: 16,
  },
});

export default LoginScreen;
