const redis = require("redis");
const client = redis.createClient({host: "redis"});

client.on("connect", () => {
console.log("Connected to Redis");
});

setInterval(() => {
client.incr("counter" , (err , counter) => {
if(err){
console.error("error incremanting counter:", err);
}else {
console.log("Counter:", counter);
}
});
}, 3000);

