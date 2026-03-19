// Add event listener to book now button
document.querySelector("button").addEventListener("click", function() {
    alert("Booking form will be implemented soon");
});

// Add event listener to navigation links
document.querySelectorAll("nav a").forEach(function(link) {
    link.addEventListener("click", function(event) {
        event.preventDefault();
        // Add smooth scrolling effect
        document.querySelector(link.getAttribute("href")).scrollIntoView({ behavior: "smooth" });
    });
});