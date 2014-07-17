""" videojsXBlock main Python class"""

import pkg_resources
from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment

class videojsXBlock(XBlock):

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "video"

    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
        default="Video JS",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")

    url = String(display_name="Video URL",
        default="http://vjs.zencdn.net/v/oceans.mp4",
        scope=Scope.content,
        help="The URL for your video. This can be a YouTube URL or a link to an .mp4, .ogg, or .webm video file hosted elsewhere on the Internet.")
    
    allow_download = Boolean(display_name="Video Download Allowed",
        default=True,
        scope=Scope.content,
        help="Allow students to download this video.")

    '''
    Util functions
    '''
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    '''
    Main functions
    '''
    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        context = {
            'display_name': self.display_name,
            'url': self.url,
            'allow_download': self.allow_download
        }
        html = self.render_template('static/html/videojs_view.html', context)
        
        frag = Fragment(html)
        frag.add_css(self.load_resource("static/css/video-js.min.css"))
        frag.add_css(self.load_resource("static/css/videojs.css"))
        frag.add_javascript(self.load_resource("static/js/video-js.js"))
        frag.add_javascript(self.load_resource("static/js/videojs_view.js"))
        frag.initialize_js('videojsXBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            'display_name': self.display_name,
            'url': self.url,
            'allow_download': self.allow_download
        }
        html = self.render_template('static/html/videojs_edit.html', context)
        
        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/videojs_edit.js"))
        frag.initialize_js('videojsXBlockInitStudio')
        return frag

    @XBlock.json_handler
    def save_videojs(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.url = data['url']
        self.allow_download = True if data['allow_download'] == "True" else False 
        
        return {
            'result': 'success',
        }
