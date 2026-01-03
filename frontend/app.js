let chartInstance = null;

async function analyzeLogs() {
  const fileInput = document.getElementById("logFile");
  const status = document.getElementById("status");
  const timerEl = document.getElementById("timer");
  const timeTakenEl = document.getElementById("timeTaken");

  if (!fileInput.files.length) {
    status.textContent = "Please select a file.";
    status.className = "text-red-600";
    return;
  }

  const startTime = performance.now();
  timerEl.classList.add("hidden");

  status.textContent = "Analyzing logs…";
  status.className = "text-blue-600 animate-pulse";

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  try {
    const response = await fetch("/analyze", {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      const text = await response.text();
      throw new Error(`HTTP ${response.status}: ${text}`);
    }

    const data = await response.json();
    console.log("Analysis result:", data);

    // ===== SUMMARY =====
    document.getElementById("summary").classList.remove("hidden");
    document.getElementById("totalLines").textContent = data.summary.total_lines;
    document.getElementById("errors").textContent = data.summary.errors;
    document.getElementById("warnings").textContent = data.summary.warnings;
    document.getElementById("critical").textContent = data.summary.critical;

    // ===== TIMER =====
    const duration = Math.round(performance.now() - startTime);
    timeTakenEl.textContent = duration;
    timerEl.classList.remove("hidden");

    // ===== CHART =====
    renderChart(data.summary);

    status.textContent = "Analysis complete.";
    status.className = "text-green-600";

  } catch (err) {
    console.error("Frontend error:", err);
    status.textContent = "Frontend error – check console.";
    status.className = "text-red-600";
  }
}

function renderChart(summary) {
  const section = document.getElementById("chartSection");
  section.classList.remove("hidden");

  const ctx = document.getElementById("severityChart");

  if (chartInstance) {
    chartInstance.destroy();
  }

  chartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Errors", "Warnings", "Critical"],
      datasets: [{
        label: "Count",
        data: [summary.errors, summary.warnings, summary.critical],
        backgroundColor: ["#ef4444", "#facc15", "#a855f7"]
      }]
    },
    options: {
      animation: { duration: 700 },
      scales: { y: { beginAtZero: true } }
    }
  });
}
