async function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value;
  if (!message) return;

  const chatbox = document.getElementById("chatbox");
  chatbox.innerHTML += `<div><b>👤 나:</b> ${message}</div>`;

  const res = await fetch("http://localhost:5001/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  const data = await res.json();
  chatbox.innerHTML += `<div><b>🤖 챗봇:</b> ${data.response}</div>`;
  chatbox.scrollTop = chatbox.scrollHeight;
  input.value = "";
}
// ⌨️ Enter 키 누르면 전송
document.getElementById("userInput").addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});