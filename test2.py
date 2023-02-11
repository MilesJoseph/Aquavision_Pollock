import gi
gi.require_version('Gst','1.0')
gi.require_version('GstVideo','1.0')
gi.require_version('GstRtspServer','1.0')
from gi.repository import GLib, Gst, GstVideo, GstRtspServer

Gst.init(None)

mainloop = GLib.MainLoop()
server = GstRtspServer.RTSPServer()
server.set_service("8550")
mounts = server.get_mount_points()

factory = GstRtspServer.RTSPMediaFactory()

factory.set_launch('( v4l2src device=/dev/video0 io-mode=2 ! image/jpeg, width=640, height=480, framerate=30/1, format=MJPG ! jpegparse ! rtpjpegpay name=pay0 pt=96 )')
mounts.add_factory("/camera1", factory)
server.attach(None)

print("stream ready at rtsp://127.0.0.1:554/camera1")
mainloop.run()
