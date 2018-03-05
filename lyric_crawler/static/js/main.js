$('.clickable-row').on("click", function() {
    window.location = '?link=' + $(this).data("href");
});