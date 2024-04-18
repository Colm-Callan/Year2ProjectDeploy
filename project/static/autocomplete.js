$(document).ready(function() {
    $('#search-bar').autocomplete({
        source: '/autocomplete/',
        minLength: 2,
        select: function(event, ui) {
            console.log('Selected:', ui.item.value);
        }
    });
});
