(function () {
  document.querySelectorAll("pre > code").forEach(function (codeBlock) {
    const button = document.createElement("button");
    button.type = "button";

    const img = new Image();

    img.src = "/icons/clipboard.svg";
    img.alt = "Copy to clipboard button";

    const successImg = new Image();

    successImg.src = "/icons/clipboard-success.svg";
    successImg.alt = "Copied to clipboard";

    button.className =
      "absolute w-6 h-6 m-4 right-0 cursor-pointer outline-none focus:opacity-50";

    const pre = codeBlock.parentNode;
    const highlight = pre.parentNode;

    highlight.className = "highlight relative";

    button.addEventListener("click", function () {
      navigator.clipboard.writeText(codeBlock.innerText).then(function () {
        button.blur();

        btnNode.appendChild(successImg);
        btnNode.removeChild(img);
        setTimeout(() => {
          btnNode.appendChild(img);
          btnNode.removeChild(successImg);
        }, 2000);
      });
    });

    const btnNode = pre.parentNode.insertBefore(button, pre);

    btnNode.appendChild(img);
  });
})();
