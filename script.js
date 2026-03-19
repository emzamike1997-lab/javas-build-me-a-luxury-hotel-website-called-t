// Add event listener to book now button
document.querySelector("button").addEventListener("click", function() {
    alert("Book now button clicked");
});

// Add event listener to navigation links
document.querySelectorAll("nav a").forEach(function(link) {
    link.addEventListener("click", function(event) {
        event.preventDefault();
        // Add logic to navigate to corresponding section
    });
});