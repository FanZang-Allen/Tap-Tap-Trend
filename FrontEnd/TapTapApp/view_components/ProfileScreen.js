import React from 'react';
import {useState} from 'react';
import {user_data, baseUrl, headers} from '../model/Config';
import {View, Text, StyleSheet, TextInput, Image, Button} from 'react-native';

const ProfileScreen = ({navigation}) => {
  const [inputPassword, setInputPassword] = useState('');
  const [inputName, setInputName] = useState('');
  const [message, setMessage] = useState('');

  function onChangePassword(newPassword) {
    setInputPassword(newPassword);
  }

  function onChangeName(newName) {
    setInputName(newName);
  }

  async function changePassword() {
    if (inputPassword === '') {
      setMessage('Please input a new password');
      return;
    }
    try {
      const fetchUrl =
        baseUrl +
        `/api/user/password?id=${user_data.id}&password=${inputPassword}`;
      let response = await fetch(fetchUrl, {
        method: 'PUT',
        headers: headers,
      });
      let response_data = await response.json();
      if (response.status !== 200) {
        setMessage(response_data.Error_message);
      } else {
        setMessage('Successfully Change Password.');
        user_data.password = inputPassword;
        setInputPassword('');
      }
    } catch (e) {
      console.log(e);
    }
  }

  async function changeName() {
    if (inputName === '') {
      setMessage('Please input a new name');
      return;
    }
    try {
      const fetchUrl =
        baseUrl + `/api/user/name?id=${user_data.id}&name=${inputName}`;
      let response = await fetch(fetchUrl, {
        method: 'PUT',
        headers: headers,
      });
      let response_data = await response.json();
      if (response.status !== 200) {
        setMessage(response_data.Error_message);
      } else {
        setMessage('Successfully Change Name.');
        user_data.user_name = inputName;
        setInputName('');
      }
    } catch (e) {
      console.log(e);
    }
  }

  return (
    <View style={styles.container}>
      <View style={styles.header_container}>
        <Image
          source={require('../assets/Unknown.jpeg')}
          resizeMode="contain"
          style={styles.avatar_image}
        />
        <View style={styles.name_container}>
          <Text style={styles.user_name}>{user_data.user_name}</Text>
          <Text style={styles.user_id}>{`Uid: ${user_data.id}`}</Text>
        </View>
        <View style={styles.log_out_button}>
          <Button
            title="Log Out"
            onPress={() => {
              navigation.navigate('Login');
            }}
          />
        </View>
      </View>
      <View style={styles.body_container}>
        <View style={styles.button_container}>
          <TextInput
            style={styles.text_input}
            onChangeText={onChangePassword}
            value={inputPassword}
            keyboardType="numeric"
          />
          <View style={styles.log_out_button}>
            <Button title="Change Password" onPress={changePassword} />
          </View>
        </View>
        <View style={styles.button_container}>
          <TextInput
            style={styles.text_input}
            onChangeText={onChangeName}
            value={inputName}
            keyboardType="default"
          />
          <View style={styles.log_out_button}>
            <Button title="Change UserName" onPress={changeName} />
          </View>
        </View>
        <Text style={styles.message_text}>{message}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'flex-start',
    alignItems: 'center',
    backgroundColor: '#ffffff',
    padding: 20,
  },
  header_container: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'flex-start',
    alignItems: 'center',
  },
  name_container: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'space-around',
  },
  user_name: {
    fontSize: 24,
    color: 'black',
    fontWeight: 'bold',
  },
  user_id: {
    fontSize: 16,
    color: '#9B9B9B',
  },
  log_out_button: {
    flex: 1,
    height: 40,
    width: 60,
    alignItems: 'center',
    marginTop: 10,
  },
  body_container: {
    flex: 3,
    flexDirection: 'column',
    justifyContent: 'flex-start',
    alignItems: 'center',
  },
  button_container: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  text_input: {
    flex: 1,
    height: 40,
    width: 120,
    borderWidth: 1,
    padding: 10,
    fontWeight: 'bold',
    marginHorizontal: 10,
  },
  background: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    paddingTop: 20,
    paddingBottom: 10,
  },
  avatar_image: {
    flex: 1,
    width: 70,
    height: 70,
    borderRadius: 50,
  },
  message_text: {
    flex: 1,
    fontSize: 18,
    color: 'black',
    fontWeight: 'bold',
  },
});

export default ProfileScreen;
