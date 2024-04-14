const SM4 = require("gm-crypt").sm4;

var payload = "xxx";

let sm4Config = {
    key: "B6*40.2_C9#e4$E3",
    mode: "ecb",
    cipherType: "base64"
};
let sm4 = new  SM4(sm4Config);

var result = sm4.decrypt(payload);

console.log("解密:" + result)