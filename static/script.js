// ------------------------------
// 📘 Library Catalog JS Script
// ------------------------------

// Show a loading overlay while submitting forms
document.addEventListener("DOMContentLoaded", () => {
  const loading = document.createElement("div");
  loading.id = "loading";
  loading.innerHTML = "⏳ Loading, please wait...";
  Object.assign(loading.style, {
    display: "none",
    position: "fixed",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    backgroundColor: "rgba(0, 0, 0, 0.7)",
    color: "white",
    padding: "20px 30px",
    borderRadius: "10px",
    fontSize: "18px",
    zIndex: "9999",
  });
  document.body.appendChild(loading);

  const addBookForm = document.getElementById("addBookForm");
  const searchForm = document.getElementById("searchForm");

  // Function to show loading spinner
  function showLoading() {
    loading.style.display = "block";
  }

  // Function to hide loading spinner
  function hideLoading() {
    loading.style.display = "none";
  }

  // Handle "Add Book" form submission
  if (addBookForm) {
    addBookForm.addEventListener("submit", (e) => {
      showLoading();
      setTimeout(() => {
        hideLoading();
        alert("✅ Book added successfully!");
        addBookForm.reset();
      }, 1000); // simulate short delay
    });
  }

  // Handle "Search" form submission
  if (searchForm) {
    searchForm.addEventListener("submit", () => {
      showLoading();
    });
  }

  // Fade-in animation for book cards
  const cards = document.querySelectorAll(".card");
  cards.forEach((card, index) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(20px)";
    setTimeout(() => {
      card.style.transition = "opacity 0.8s ease, transform 0.8s ease";
      card.style.opacity = "1";
      card.style.transform = "translateY(0)";
    }, index * 100);
  });
});
