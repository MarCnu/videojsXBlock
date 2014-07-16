/* Javascript for videojsXBlock. */
function videojsXBlockInitView(runtime, element) {
    // To include data-setup inside the HTML, with the Python string builder :
    // data-setup="{{&quot;playbackRates&quot;:[0.75,1,1.25,1.5,1.75,2]}}"
    console.log('Init View outside');

    var video = $(element).find('video:first');
    videojs(video, {playbackRates:[0.75,1,1.25,1.5,2]}, function() {});

}