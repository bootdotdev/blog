import fetch from "node-fetch";
const siteMapUrl = "https://blog.boot.dev/sitemap.xml";
const googleEndpoint = `http://www.google.com/ping?sitemap=${siteMapUrl}`;
const yandexEndpoint = `https://webmaster.yandex.ru/ping?sitemap=${siteMapUrl}`;

module.exports.handler = async () => {
  const resp = await fetch(googleEndpoint);
  console.log("Google status code:", resp.status);

  const resp2 = await fetch(yandexEndpoint);
  console.log("Yandex status code:", resp2.status);

  return { statusCode: 200, body: "" };
};
