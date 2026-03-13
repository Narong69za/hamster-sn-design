/**
 * ============================================================
 * SN HAMSTER STATUS ENGINE
 * Version : 1.1.0
 * Module  : hamster-status.js
 * Purpose : Fetch hamster kombat season2 account status
 * Author  : SN
 * ============================================================
 */

const axios = require("axios")
const https = require("https")

/* ------------------------------------------------------------
   HTTPS AGENT (FIX CERT / TLS)
------------------------------------------------------------ */

const httpsAgent = new https.Agent({
  keepAlive: true,
  rejectUnauthorized: false,
  maxSockets: 10
})

/* ------------------------------------------------------------
   CONFIG
------------------------------------------------------------ */

const TOKENS = [
  "TOKEN_ACCOUNT_1",
  // "TOKEN_ACCOUNT_2"
]

const API_SYNC = "https://api.g.hamsterverse.io/season2/sync"
const API_ACCOUNT = "https://api.g.hamsterverse.io/account-info"
const API_IP = "https://api.g.hamsterverse.io/ip"

const ORIGIN = "https://app-nginx.g.hamsterverse.io"

/* ------------------------------------------------------------
   AXIOS INSTANCE
------------------------------------------------------------ */

const client = axios.create({

  timeout: 20000,

  httpsAgent: httpsAgent,

  headers: {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Origin": ORIGIN,
    "Referer": ORIGIN
  }

})

/* ------------------------------------------------------------
   UTIL
------------------------------------------------------------ */

function numberFormat(num) {
  if (!num) return "0"
  return Number(num).toLocaleString("en-US")
}

function formatDate(date) {
  if (!date) return "-"
  const d = new Date(date)
  return d.toLocaleString()
}

function line() {
  console.log("===================================================")
}

/* ------------------------------------------------------------
   API CALL
------------------------------------------------------------ */

async function fetchSync(token) {

  const res = await client.post(
    API_SYNC,
    {},
    {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }
  )

  return res.data
}

async function fetchAccount(token) {

  const res = await client.get(
    API_ACCOUNT,
    {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }
  )

  return res.data
}

async function fetchIP() {

  const res = await client.get(API_IP)

  return res.data
}

/* ------------------------------------------------------------
   STATUS DISPLAY
------------------------------------------------------------ */

function showStatus(index, account, sync, ip) {

  const user = sync.hydraUser || {}

  line()
  console.log(`ACCOUNT : account${index+1}`)
  console.log(`USER ID : ${user.id || "-"}`)
  console.log(`NAME    : ${account.name || "-"}`)
  console.log(`AVATAR  : ${account.avatar || "-"}`)
  line()

  console.log("GAME DATA")
  console.log("---------------------------------------------------")

  console.log("HAMSTER GOLD :", numberFormat(user.totalSeason2HamsterGold))
  console.log("PASSIVE / HR :", numberFormat(user.earnPassivePerHour))

  if (user.tokenSeason2) {
    console.log("TOKEN S2-1 :", numberFormat(user.tokenSeason2.token1))
    console.log("TOKEN S2-2 :", numberFormat(user.tokenSeason2.token2))
    console.log("TOKEN S2-3 :", numberFormat(user.tokenSeason2.token3))
  }

  console.log("WITHDRAW STATE :", user.withdraw ? user.withdraw.state : "-")

  console.log("")
  console.log("SYNC INFO")
  console.log("---------------------------------------------------")

  console.log("ACCOUNT CREATED :", formatDate(user.createdAt))
  console.log("LAST SYNC       :", formatDate(user.lastSyncAt))

  console.log("")
  console.log("NETWORK")
  console.log("---------------------------------------------------")

  if (ip) {
    console.log("IP       :", ip.ip)
    console.log("CITY     :", ip.city)
    console.log("COUNTRY  :", ip.country)
    console.log("ASN      :", ip.asn)
  }

  line()
}

/* ------------------------------------------------------------
   MAIN ENGINE
------------------------------------------------------------ */

async function runAccount(index, token) {

  try {

    const [sync, account, ip] = await Promise.all([
      fetchSync(token),
      fetchAccount(token),
      fetchIP()
    ])

    showStatus(index, account, sync, ip)

  } catch (err) {

    if (err.response) {
      console.log("ENGINE ERROR :", err.response.data)
    } else {
      console.log("ENGINE ERROR :", err.message)
    }

  }

}

async function main() {

  console.clear()

  console.log("")
  console.log("SN HAMSTER STATUS ENGINE")
  console.log("")

  for (let i = 0; i < TOKENS.length; i++) {

    await runAccount(i, TOKENS[i])

  }

}

main()
