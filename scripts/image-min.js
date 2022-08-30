const sharp = require("sharp");
const fs = require("fs");

const directory = "./static/img";
const srcDir = `raw`;

const maxWidth = 800;

fs.readdirSync(srcDir).forEach(async (file) => {
  try {
    const src = `${srcDir}/${file}`;
    const dest = `${directory}/${maxWidth}/${file}.webp`;

    if (file === `${maxWidth}`) {
      return;
    }

    if (file.includes(".gif")) {
      fs.copyFileSync(src, dest);
      return;
    }

    await sharp(src)
      .resize(maxWidth, null, { withoutEnlargement: true }) // width, height
      .webp()
      .toFile(dest);

    fs.unlinkSync(src);

    console.log(`minified to: ${dest}`);
  } catch (err) {
    console.log(err, file);
  }
});
