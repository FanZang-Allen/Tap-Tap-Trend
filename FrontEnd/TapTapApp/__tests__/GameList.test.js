import GameList from '../model/GameList';

test('Game List Construtor', () => {
  const testGame = new GameList(
    'http://127.0.0.1:5000/api/rank?region=USA',
    null,
  );
  expect(testGame.success).toBe(false);
  expect(testGame.errorMsg).toBe(undefined);
  expect(testGame.fetchUrl).not.toBeUndefined();
});

test('Game List Fetch Data', async () => {
  const testGame = new GameList(
    'http://127.0.0.1:5000/api/rank?region=USA',
    null,
  );
  await testGame.FetchData();
  expect(testGame.success).toBe(true);
  expect(testGame.errorMsg).toBe(undefined);
  expect(testGame.gameList).not.toBeUndefined();
}, 20000);

test('Game List Get Data', async () => {
  const testGame = new GameList(
    'http://127.0.0.1:5000/api/rank?region=USA',
    null,
  );
  await testGame.FetchData();
  let data = testGame.GetData()[0];
  expect(typeof data.name).toBe('string');
  expect(typeof data.genre).toBe('string');
  expect(typeof data.id).toBe('string');
  expect(typeof data.provider).toBe('string');
  expect(typeof data.rating).toBe('string');
  expect(typeof data.logo).toBe('string');
}, 8000);
