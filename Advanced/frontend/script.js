const API_URL = "http://127.0.0.1:8000";

const fileInput = document.getElementById("fileInput");
const uploadBtn = document.getElementById("uploadBtn");
const uploadStatus = document.getElementById("uploadStatus");

const questionInput = document.getElementById("questionInput");
const askBtn = document.getElementById("askBtn");

const answerBox = document.getElementById("answerBox");
const sourcesBox = document.getElementById("sourcesBox");


// =========================
// Upload Document
// =========================

uploadBtn.addEventListener("click", async () => {

    const file = fileInput.files[0];

    if (!file) {
        uploadStatus.textContent = "Please select a PDF first.";
        return;
    }

    if (file.type !== "application/pdf") {
        uploadStatus.textContent = "Please upload a PDF file only.";
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    uploadStatus.textContent = "Uploading and indexing...";

    uploadBtn.disabled = true;

    try {

        const response = await fetch(`${API_URL}/api/upload`, {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Upload failed");
        }

        uploadStatus.textContent =
            `✅ ${data.message} (${data.chunks_added} chunks added)`;

    } catch (error) {

        uploadStatus.textContent =
            `❌ Error: ${error.message}`;

    } finally {

        uploadBtn.disabled = false;
    }
});


// =========================
// Ask Question
// =========================

askBtn.addEventListener("click", async () => {

    const question = questionInput.value.trim();

    if (!question) {
        answerBox.innerHTML =
            "<p>Please enter a question.</p>";
        return;
    }

    answerBox.innerHTML =
        "<p>🤔 Thinking...</p>";

    sourcesBox.innerHTML = "";

    askBtn.disabled = true;

    try {

        const response = await fetch(`${API_URL}/api/ask`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Request failed");
        }

        // Answer
        answerBox.innerHTML = `
            <h3>🤖 Answer</h3>
            <p>${escapeHtml(data.answer)}</p>
        `;


        // Sources
        if (data.sources && data.sources.length > 0) {

            sourcesBox.innerHTML = `
                <h3>📚 Sources</h3>
            `;

            data.sources.forEach((source, index) => {

                let sourceText = source;

                let filename = "Uploaded Document";
                let page = "Unknown";

                const sourceMatch =
                    source.match(/'source': '([^']+)'/);

                const pageMatch =
                    source.match(/'page': (\d+)/);

                if (sourceMatch) {
                    filename = sourceMatch[1];
                }

                if (pageMatch) {
                    page = pageMatch[1];
                }

                sourcesBox.innerHTML += `
                    <div class="source-card">
                        <strong>Source ${index + 1}</strong>
                        <p>📄 ${escapeHtml(filename)}</p>
                        <p>📖 Page ${page}</p>
                    </div>
                `;
            });

        } else {

            sourcesBox.innerHTML =
                "<p>No sources found.</p>";
        }

    } catch (error) {

        answerBox.innerHTML =
            `<p>❌ Error: ${escapeHtml(error.message)}</p>`;

    } finally {

        askBtn.disabled = false;
    }
});


// =========================
// Security helper
// =========================

function escapeHtml(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}