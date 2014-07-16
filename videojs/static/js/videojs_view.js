/* Javascript for videojsXBlock. */
function videojsXBlockInitView(runtime, element) {
    /* Weird behaviour :
     * In the LMS, element is the DOM container.
     * In the CMS, element is the jQuery object associated*
     * So here I make sure element is the jQuery object */
    if(element.innerHTML) element = $(element);
    
    // To include data-setup inside the HTML, with the Python string builder :
    // data-setup="{{&quot;playbackRates&quot;:[0.75,1,1.25,1.5,1.75,2]}}"
    console.log('Init videojsXBlock view');
    
    var video = element.find('video:first');
    videojs(video, {playbackRates:[0.75,1,1.25,1.5,1.75,2]}, function() {});

}