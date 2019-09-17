const readline = require('readline')
const send = require('.')

const SESSDATA = process.argv.slice(-4)[0]
const csrf = process.argv.slice(-4)[1]
const roomid = process.argv.slice(-4)[2]
const msg = process.argv.slice(-4)[3]
console.log(SESSDATA)
send({ SESSDATA, csrf, roomid, msg }).catch(console.error)

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
//   terminal: false
// })

// rl.prompt();

// rl.on('line', line => {
//   const [SESSDATA, csrf, roomid, ...message] = line.split(' ')
//   const msg = message.join(' ')
//   send({ SESSDATA, csrf, roomid, msg }).catch(console.error)
// })