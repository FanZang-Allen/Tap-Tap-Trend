import Game from '../model/Game';

test('Game Construtor', () => {
  const testGame = new Game('82354');
  expect(testGame.success).toBe(false);
  expect(testGame.errorMsg).toBe(undefined);
  expect(testGame.requestList).not.toBeUndefined();
});

test('Game Fetch Data', async () => {
  const testGame = new Game('82354', true);
  await testGame.FetchData();
  expect(testGame.success).toBe(true);
  expect(testGame.errorMsg).toBe(undefined);
  expect(testGame.gameInfo).not.toBeUndefined();
}, 20000);

test('Game Get Data', async () => {
  const testGame = new Game('82354', true);
  await testGame.FetchData();
  let data = testGame.GetData();
  expect(typeof data.downloads).toBe('string');
  expect(typeof data.followers).toBe('string');
  expect(typeof data.genre).toBe('string');
  expect(typeof data.id).toBe('string');
  expect(typeof data.intro).toBe('string');
  expect(typeof data.provider).toBe('string');
  expect(typeof data.rating).toBe('string');
  expect(typeof data.logo).toBe('string');
}, 8000);
