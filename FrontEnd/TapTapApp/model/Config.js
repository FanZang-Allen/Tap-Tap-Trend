export const user_data = {
  favourite_list: [],
  user_name: 'Allen',
  id: '1',
  password: '',
};

export const baseUrl = 'http://10.0.2.2:5000';

export const headers = {
  'Content-Type': 'application/json',
  Accept: 'application/json',
};

export function ChangeUser(data) {
  user_data.user_name = data.user_name;
  user_data.favourite_list = data.favourite_list;
  user_data.id = data.id;
  user_data.password = data.password;
}

export function InFavourite(game_id) {
  return user_data.favourite_list.includes(game_id);
}
