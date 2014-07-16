/* Javascript for videojsXBlock. */
function videojsXBlock(runtime, element) {

    $(element).find('.action-cancel').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function() {
        var data = {
            'display_name': $(videojs_edit_display_name).context.value,
            'url': $(videojs_edit_url).context.value
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

    $(function ($) {
        /* Here's where you'd do things on page load. */
        // To include data-setup inside the HTML, with the Python string builder :
        // data-setup="{{&quot;playbackRates&quot;:[0.75,1,1.25,1.5,1.75,2]}}"
        $('.video-js').each(function(index) {
            videojs(this), {'playbackRates':[0.75,1,1.25,1.5,1.75,2]}, function() {
            });
        });
    });
}