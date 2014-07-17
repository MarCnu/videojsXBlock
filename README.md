videojsXblock
=========

This XBlock to use the Video.js player (www.videojs.com) instead of the default one.

- True full screen allowed
- More video speeds available : | 0.75 | 1 | 1.25 | 1.5 | 1.75 | 2 | by default (customize it easily by editing 
videojsXBlock / videojs / static / js / videojs_view.js)

### Install / Update the XBlock ###
See https://github.com/polimediaupv/paellaXBlock installation

    # Move to the folder where you want to download the XBlock
    cd /edx/app/edxapp
    # Download the XBlock
    sudo -u edxapp git clone https://github.com/MarCnu/videojsXBlock.git
    # Install the XBlock
    sudo -u edxapp /edx/bin/pip.edxapp install videojsXBlock/
    # Upgrade the XBlock if it is already installed, using --upgrade
    sudo -u edxapp /edx/bin/pip.edxapp install videojsXBlock/ --upgrade
    # Remove the installation files
    sudo rm -r videojsXBlock

### Reboot if something isn't right ###

    sudo /edx/bin/supervisorctl -c /edx/etc/supervisord.conf restart edxapp:

### Activate the XBlock in your course ###
Go to Settings -> Advanced Settings and set `advanced_modules` to `["videojs"]`.

### Use the XBlock in a unit ###
Add a Advanced -> VideoJS Xblock in your unit.
