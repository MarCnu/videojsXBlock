/* Javascript for videojsXBlock. */
function videojsXBlockInitView(runtime, element) {

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