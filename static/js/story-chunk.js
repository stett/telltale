$(function() {


    function setSelectionRange(input, selectionStart, selectionEnd) {
        if (input.setSelectionRange) {
            input.focus();
            input.setSelectionRange(selectionStart, selectionEnd);
        } else if (input.createTextRange) {
            var range = input.createTextRange();
            range.collapse(true);
            range.moveEnd('character', selectionEnd);
            range.moveStart('character', selectionStart);
            range.select();
        }
    }

    function setCaretPos (input, pos) {
        setSelectionRange(input, pos, pos);
    }

    // Set the max chars text values
    $('#chunk-content-max-chars').text(max_story_chunk_size);
    $('#chunk-leadin-max-chars').text(max_story_leadin_size);

    // Select the content and leadin objects
    var $content = $('#chunk-content');
    var $leadin = $('#chunk-leadin');

    // Make leadin invisible to begin with
    $leadin.css({opacity: 0});

    // Default the cursor position to the beginning of the chunk content
    $content.focus();
    setCaretPos($content[0], 0);

    // When the "main body" label is clicked, focus on the main body area. Same for leadin.
    $('#prev-chunk-leadin').click(function() {$content.focus(); });
    $('#chunk-content-label').click(function() {$content.focus(); });
    $('#chunk-leadin-label').click(function() {$leadin.focus(); });

    // Check for updates to the chunk-content
    $content.on('input', function(e) {
        if ($content.text().length > max_story_chunk_size) {
            $content.text($content.text().substring(0, max_story_chunk_size));
        }
        $('#chunk-content-chars').text($content.text().length)
    })

    // Check for updates to chunk-leadin
    $leadin.on('input', function(e) {
        if ($leadin.text().length > max_story_leadin_size) {
            $leadin.text($leadin.text().substring(0, max_story_leadin_size));
        }
        $('#chunk-leadin-chars').text($leadin.text().length)
    })

    // On change of focus, update the label divs
    $content.focus(function(e) {
        $('#chunk-content-label').addClass('active');
        $('#chunk-leadin-label').removeClass('active');

        if ($leadin.text().length == 0) {
            $leadin.css({opacity: 0});
        }
    });
    $leadin.focus(function(e) {
        console.log(e);
        $('#chunk-content-label').removeClass('active');
        $('#chunk-leadin-label').addClass('active');
        $leadin.css({opacity: 1});
    });

    // On submit, copy the contents from the fake story chunk content field into the real one
    $('#story-chunk-form').submit(function() {
        $('#id_content').val($('#chunk-content').text());
        $('#id_leadin').val($('#chunk-leadin').text());
    });
});