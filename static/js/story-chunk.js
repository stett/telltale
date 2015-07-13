$(function() {

    // On submit, copy the contents from the fake story chunk content field into the real one
    $('#story-chunk-form').submit(function() {
        $('#id_content').val($('#chunk-content').html());
    });

});