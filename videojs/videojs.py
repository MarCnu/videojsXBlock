""" videojsXBlock main Python class"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

class videojsXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # Values : [other (default), video, problem]
    icon_class = "video"

    display_name = String(display_name="Display Name",
        default="Video JS",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")

    url = String(display_name="Video URL",
        default="http://vjs.zencdn.net/v/oceans.mp4",
        scope=Scope.content,
        help="The URL for your video. This can be a YouTube URL or a link to an .mp4, .ogg, or .webm video file hosted elsewhere on the Internet.")
    
    allowDownload = String(display_name="Video Download Allowed",
        default="True",
        scope=Scope.content,
        help="Allow students to download this video.")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/videojs_view.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/video-js.min.css"))
        frag.add_css(self.resource_string("static/css/videojs.css"))
        frag.add_javascript(self.resource_string("static/js/video-js.js"))
        frag.add_javascript(self.resource_string("static/js/videojs_view.js"))
        frag.initialize_js('videojsXBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        html = self.resource_string("static/html/videojs_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/videojs_edit.js"))
        frag.initialize_js('videojsXBlockInitStudio')
        return frag

    @XBlock.json_handler
    def save_videojs(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.url = data['url']
        self.allowDownload = "True" if data['allow_download'] == "True" else "False" 
        
        return {
            'result': 'success',
        }
