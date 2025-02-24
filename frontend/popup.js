document.addEventListener("DOMContentLoaded", function () {
  const darkModeToggle = document.getElementById("darkModeToggle");
  const body = document.body;
  const inputText = document.getElementById("inputText");
  const summarizeButton = document.getElementById("summarizeButton");
  const outputText = document.getElementById("outputText");

  // Dark Mode Toggle
  darkModeToggle.addEventListener("click", function () {
      body.classList.toggle("dark-mode");
  });

  // Summarization Request
  summarizeButton.addEventListener("click", async function () {
      const text = inputText.value.trim();
      if (!text) {
          outputText.value = "Please enter some text.";
          return;
      }

      try {
          const response = await fetch("http://localhost:8000/generate_summary", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ text: text }),
          });

          if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
          }

          const data = await response.json();
          outputText.value = data.summary;
      } catch (error) {
          outputText.value = "Error generating summary.";
          console.error("Request failed:", error);
      }
  });
});
