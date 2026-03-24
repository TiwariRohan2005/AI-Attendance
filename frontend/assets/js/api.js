const BASE = "http://localhost:8000";

async function fetchAttendance() {
  const res = await fetch(BASE + "/attendance", {
    headers: getAuthHeader()
  });
  return res.json();
}

async function registerUser(data) {
  const res = await fetch(BASE + "/register", {
    method: "POST",
    headers: getAuthHeader(),
    body: JSON.stringify(data)
  });
  return res.json();
}

async function checkin(data) {
  const res = await fetch(BASE + "/checkin", {
    method: "POST",
    headers: getAuthHeader(),
    body: JSON.stringify(data)
  });
  return res.json();
}