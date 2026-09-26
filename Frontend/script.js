
const API_URL = "http://127.0.0.1:8000/chat";

const chatForm =
document.getElementById("chatForm");
const messageInput =
document.getElementById("messageInput");
const messages =
document.getElementById("messages");

const thinking =
document.getElementById("thinking");
const sendButton =
document.getElementById("sendButton");

const welcomeScreen =
document.getElementById("welcomeScreen");
const themeToggle =
document.getElementById("themeToggle");

const promptCards =
document.querySelectorAll(".prompt-card");

/* -------------- Conversation ID -------------- */

let conversationId =
localStorage.getItem("conversation_id");

if (!conversationId) {
    conversationId =
crypto.randomUUID();

   localStorage.setItem(
    "conversation_id",
    conversationId
   );
}

/* -------------- Theme -------------- */

const savedTheme =
    localStorage.getItem("theme") || "light";

document.documentElement.dataset.theme = savedTheme;

themeToggle.textContent =
    savedTheme === "dark" ? "☾" : "☼";

themeToggle.addEventListener("click"
, () => {

    const currentTheme =

document.documentElement.dataset.theme;

    const newTheme =
       currentTheme === "dark" ?
"light" : "dark"

document.documentElement.dataset.theme =
          newTheme;

    localStorage.setItem(
        "theme",
        newTheme
    );

    themeToggle.textContent =
       newTheme === "dark" ? "☾" : "☼";
})

/* -------------- Add message to UI -------------- */

function addMessage(role, content) {

    const message =
document.createElement("div");

  message.className = 'message $ {role}';

     const messageContent =

document.createElement("div");

    messageContent.className =
        "message-content";

    messageContent.textContent = content;

message.appendChild(messageContent);

    messages.appendChild(message);

    message.scrollIntoView({
        behavior: "smooth",
        block: "end"
    });
}

/* -------------- Thinking state -------------- */

function setThinking(isThinking) {

    thinking.classList.toggle(
        "hidden",
        !isThinking
    );

    sendButton.disabled = isThinking;

    if (isThinking) {

        sendButton.classList.remove("active");

        sendButton.classList.add("thinking");
    } else {

        sendButton.classList.remove("thinking");

        if (messageInput.value.trim()) {

            sendButton.classList.add("active");
        } else {

            sendButton.classList.remove("active")
        }
    }
}

/* -------------- Send Message -------------- */

async function sendMessage(message) 
{

    const cleanMessage =
message.trim();

    if (!cleanMessage) {
        return;
    }

    welcomeScreen.style.display =
"none";

   addMessage(
    "user",
    cleanMessage
   );

   messageInput.value = "";

   setThinking(true);

   try{

    const response = await
fetch(API_URL, {

    method: "POST",

    headers: {
        "Content-Type":
"application/json"
    },

    body: JSON.stringify({

        conversation_id:
           conversationId,

        message:
           cleanMessage,

        username:
           "Guest"
    })
});

   const data = await
response.json();

    if (!response.ok) {

        throw new Error(
            data.detail ||
            "Something went wrong."
        );
    }

    addMessage(
        "assistant",
        data.response
    );

   } catch (error) {

    console.error(error);

    addMessage(
        "assistant",
        "I couldn't connect to the AI service right now. Please try again."
    );
   } finally {

        setThinking(false);
   }
}

/* -------------- Form Submit -------------- */

chatForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();

        await sendMessage(
            messageInput.value
        );

    }
);

/* -------------- Enter = Send -------------- */
/* -------------- Shift + Enter = New Line -------------- */

messageInput.addEventListener(
    "keydown",
    (event) => {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

chatForm.requestSubmit();
        }
    }
);

/* -------------- Auto-Grow Textarea -------------- */

messageInput.addEventListener("input", () => {
    messageInput.style.height =
"auto";

    messageInput.style.height = 
        '$ {Math.min(messageInput.scrollHeight, 150)}px';

        if (messageInput.value.trim()) {
            sendButton.disabled = false;

            sendButton.classList.add("active");
        } else {
            sendButton.disabled = true;

            sendButton.classList.remove("active");
        }
});

/* -------------- Quick Prompts -------------- */

promptCards.forEach((card) => {

    card.addEventListener(
        "click",
        () => {

            const text =

card.querySelector("span").textContent;

            let prompt = "";

            if (text === "Explain something") {

                prompt = "Explain a difficult question to me in a simple way.";
            } else if (text === "Help me learn") {

                prompt = "Help me create a practical study plan.";
            } else if (text === "Brainstorm ideas") {

                prompt = "Help me brainstorm some useful project ideas.";
            }

            messageInput.value = prompt;

            messageInput.focus();
        }
    );
});