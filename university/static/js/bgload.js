document.addEventListener('DOMContentLoaded', function () {
    // Get all loading container elements
    var loadingContainers = document.querySelectorAll('.loading-container');

    // Loop through each loading container
    loadingContainers.forEach(function (container) {
        // Get the background image elements within this container
        var loadingImage = container.querySelector('.loading-src');
        var actualImage = container.querySelector('.loaded-src');

        // Create a new Image object
        var tempImg = new Image();

        // Get the source URL from the data-src attribute of the actual image
        var imageUrl = actualImage.getAttribute('data-src');
        actualImage.style.display = 'none';

        // Set the src attribute of the temporary image to the image URL
        tempImg.src = imageUrl;

        // When the temporary image is fully loaded, update the actual background image
        tempImg.onload = function () {
            // Set the background image
            actualImage.style.backgroundImage = "url('" + imageUrl + "')";
            // Hide the loading image
            loadingImage.style.display = 'none';
            // Show the actual image
            actualImage.style.display = 'block';
        };
    });
});
