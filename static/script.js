document.addEventListener("DOMContentLoaded", () => {
    const citySelect     = document.getElementById("city");
    const localitySelect = document.getElementById("locality");
    const cityChips      = document.querySelectorAll(".city-chip");
    const form           = document.querySelector("form");
    const predictBtn     = document.querySelector(".predict-btn");

    let localityData = {};

    // ── Load locality data ──
    fetch("/static/localities.json")
        .then(r => r.json())
        .then(data => {
            localityData = data;
        })
        .catch(() => {
            console.warn("Could not load localities.json");
        });

    // ── Populate localities when city changes ──
    citySelect.addEventListener("change", () => {
        const city = citySelect.value;
        populateLocalities(city);
        highlightCityChip(city);
    });

    function populateLocalities(city) {
        localitySelect.innerHTML = "";

        if (!city || !localityData[city]) {
            const opt = document.createElement("option");
            opt.value = "";
            opt.textContent = city ? "No localities found" : "Select city first";
            localitySelect.appendChild(opt);
            return;
        }

        const defaultOpt = document.createElement("option");
        defaultOpt.value = "";
        defaultOpt.textContent = `Select locality in ${city.charAt(0).toUpperCase() + city.slice(1)}`;
        localitySelect.appendChild(defaultOpt);

        localityData[city].forEach(locality => {
            const opt = document.createElement("option");
            opt.value = locality;
            // Capitalise first letter of each word for display
            opt.textContent = locality.replace(/\b\w/g, c => c.toUpperCase());
            localitySelect.appendChild(opt);
        });
    }

    // ── City chips: clicking scrolls to predict and selects city ──
    cityChips.forEach(chip => {
        chip.addEventListener("click", () => {
            const cityName = chip.textContent.trim().toLowerCase();
            citySelect.value = cityName;
            populateLocalities(cityName);
            highlightCityChip(cityName);
            document.getElementById("predict")
                .scrollIntoView({ behavior: "smooth", block: "start" });
        });
    });

    function highlightCityChip(city) {
        cityChips.forEach(c => c.classList.remove("active"));
        cityChips.forEach(c => {
            if (c.textContent.trim().toLowerCase() === city) {
                c.classList.add("active");
            }
        });
    }

    // ── Loading state on form submit ──
    if (form) {
        form.addEventListener("submit", () => {
            predictBtn.disabled = true;
            predictBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Calculating…`;
        });
    }

    // ── Scroll result into view if prediction exists ──
    const result = document.querySelector(".result-card");
    if (result) {
        setTimeout(() => {
            result.scrollIntoView({ behavior: "smooth", block: "nearest" });
        }, 200);
    }
});
