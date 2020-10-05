var crypto = require("crypto");

// Cosmos DB アカウントのプライマリ/セカンダリキー（読み取り/書き込みキーのみ利用可能）
var inputKey = "{アカウントキー}";

var today = new Date().toUTCString();

// x-ms-date ヘッダとして使用
console.log(today);

// 各パラメータについて
// verb: GET, POST, PUT 等
// resourseType: dbs, colls, docs, users 等
// resouceId: dbs/{DB名}, dbs/{DB名}/colls/{コンテナ名} 等

// 以下はDB下にあるユーザーを表示する場合の例
// HTTP リクエストに使用するトークンを生成
// authorization ヘッダとして使用
console.log(getAuthorizationTokenUsingMasterKey("GET", "users", "dbs/db1", today, inputKey))

function getAuthorizationTokenUsingMasterKey(verb, resourceType, resourceId, date, masterKey)
{
    var key = new Buffer.from(masterKey, "base64");

    var text = (verb || "").toLowerCase() + "\n" +
               (resourceType || "").toLowerCase() + "\n" +
               (resourceId || "") + "\n" +
               date.toLowerCase() + "\n" +
               "" + "\n";

    var body = new Buffer.from(text, "utf8");

    var signature = crypto.createHmac("sha256", key).update(body).digest("base64");

    var MasterToken = "master";

    var TokenVersion = "1.0";

    return encodeURIComponent("type=" + MasterToken + "&ver=" + TokenVersion + "&sig=" + signature);
}