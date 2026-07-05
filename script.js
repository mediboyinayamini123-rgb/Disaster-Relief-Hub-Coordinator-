const form = document.getElementById("emergencyForm");

const resultBox = document.getElementById("result");

const restockBtn = document.getElementById("restockBtn");


function getSeverityColor(severity) {

    switch (severity?.toUpperCase()) {

        case "LOW":
            return "#22c55e";

        case "MEDIUM":
            return "#f59e0b";

        case "HIGH":
            return "#ef4444";

        case "CRITICAL":
            return "#b91c1c";

        default:
            return "#3b82f6";
    }
}


form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const message = document.getElementById("message").value;

    resultBox.innerHTML = `
        <p style="color:white;">
            Analyzing emergency...
        </p>
    `;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/analyze",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );

        const data = await response.json();

        console.log(data);

        const severityColor = getSeverityColor(
            data.triage.severity
        );

        const resourcesHTML = Object.entries(
            data.resources
        ).map(([resource, details]) => {

            return `
                <div class="resource-item">

                    <div class="resource-header">

                        <span>${resource}</span>

                        <span>${details.quantity}</span>

                    </div>

                    <div class="resource-bar">

                        <div 
                            class="resource-fill"
                            style="
                                width:${Math.min(details.quantity, 100)}%;
                                background:${severityColor};
                            ">
                        </div>

                    </div>

                    <small>
                        Warehouse: ${details.warehouse}
                    </small>

                </div>
            `;
        }).join("");

        resultBox.innerHTML = `

            <div class="card">

                <h2>
                    Disaster Analysis Result
                </h2>

                <div class="severity-section">

                    <div class="severity-top">

                        <span>
                            Severity Level
                        </span>

                        <span
                            style="
                                color:${severityColor};
                                font-weight:bold;
                            "
                        >
                            ${data.triage.severity}
                        </span>

                    </div>

                    <div class="severity-track">

                        <div
                            class="severity-fill"
                            style="
                                background:${severityColor};
                                width:100%;
                            ">
                        </div>

                    </div>

                </div>

                <div class="info-grid">

                    <div class="info-card">

                        <h3>Location</h3>

                        <p>
                            ${data.triage.location}
                        </p>

                    </div>

                    <div class="info-card">

                        <h3>People Affected</h3>

                        <p>
                            ${data.triage.people_affected}
                        </p>

                    </div>

                </div>

                <div class="section-grid">

                    <div class="section-card">

                        <h3>
                            Needed Resources
                        </h3>

                        <ul>
                            ${Object.entries(
                                data.triage.needs
                            ).map(([key, value]) => `
                                <li>
                                    ${key}: ${value}
                                </li>
                            `).join("")}
                        </ul>

                    </div>

                    <div class="section-card">

                        <h3>
                            Allocated Resources
                        </h3>

                        ${resourcesHTML}

                    </div>

                </div>

                <div class="weather-card">

                    <h3>
                        Weather Intelligence
                    </h3>

                    <p>
                        Condition:
                        ${data.weather.condition}
                    </p>

                    <p>
                        Temperature:
                        ${data.weather.temperature} °C
                    </p>

                    <p>
                        Alert:
                        ${data.weather.alert}
                    </p>

                </div>

                <div class="route-card">

                    <h3>
                        Route Intelligence
                    </h3>

                    <p>
                        Recommended:
                        ${data.route.recommended_route}
                    </p>

                    <p>
                        Avoid:
                        ${data.route.avoid_route}
                    </p>

                </div>

                <div class="recommendation-card">

                    <h3>
                        AI Recommendation
                    </h3>

                    <p>
                        ${data.recommendation}
                    </p>

                </div>

                ${
                    data.shortage
                    ?
                    `
                    <div class="shortage-alert">

                        Resource shortage detected.
                        Additional supply coordination required.

                    </div>
                    `
                    :
                    ""
                }

            </div>
        `;

    } catch (error) {

        console.error(error);

        resultBox.innerHTML = `
            <p style="color:red;">
                Error connecting to backend
            </p>
        `;
    }
});


restockBtn.addEventListener("click", async () => {

    try {

        await fetch(
            "http://127.0.0.1:8000/restock",
            {
                method: "POST"
            }
        );

        alert(
            "Warehouse Restocked Successfully"
        );

    } catch (error) {

        console.error(error);

        alert(
            "Restock failed"
        );
    }
});
