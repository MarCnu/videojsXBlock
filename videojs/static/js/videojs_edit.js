/* Javascript for videojsXBlock. */
function videojsXBlockInitStudio(runtime, element) {

    $(element).find('.action-cancel').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function() {
        var data = {
            'display_name': $('#videojs_edit_display_name').val(),
            'url': $('#videojs_edit_url').val(),
            'allow_download': $('#videojs_edit_allow_download').val(),
            'source_text': $('#videojs_edit_source_text').val(),
            'source_url': $('#videojs_edit_source_url').val(),
            'start_time': $('#videojs_edit_start_time').val(),
            'end_time': $('#videojs_edit_end_time').val()
        };

        $('.xblock-editor-error-message', element).html();
        $('.xblock-editor-error-message', element).css('display', 'none');
        var handlerUrl = runtime.handlerUrl(element, 'save_videojs');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                window.location.reload(false);
            } else {
                $('.xblock-editor-error-message', element).html('Error: '+response.message);
                $('.xblock-editor-error-message', element).css('display', 'block');
            }
        });
    });
}