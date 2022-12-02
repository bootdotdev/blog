import fetch from "node-fetch";
const siteMapUrl = "https://blog.boot.dev/sitemap.xml";
const googleEndpoint = `http://www.google.com/ping?sitemap=${siteMapUrl}`;
const yandexEndpoint = `https://webmaster.yandex.ru/ping?sitemap=${siteMapUrl}`;
const bingEndpoint = `http://www.bing.com/webmaster/ping.aspx?siteMap=${siteMapUrl}`;

module.exports.handler = async () => {
  const resp = await fetch(googleEndpoint);
  console.log("Google status code:", resp.status);

  const resp2 = await fetch(yandexEndpoint);
  console.log("Yandex status code:", resp2.status);

  const resp3 = await fetch(bingEndpoint);
  console.log("Bing status code:", resp3.status);
  return { statusCode: 200, body: "" };
};
