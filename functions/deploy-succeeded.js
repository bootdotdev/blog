const http = require("http");
const siteMapUrl = "https://blog.boot.dev/sitemap.xml";
const endpoint = `http://www.google.com/ping?sitemap=${siteMapUrl}`;

module.exports.handler = (event, context, callback) => {
  http.get(endpoint, () => callback(null, { statusCode: 200, body: "" }));
};
