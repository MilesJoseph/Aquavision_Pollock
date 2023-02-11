import gi
gi.require_version('Gst','1.0')
gi.require_version('GstVideo','1.0')
gi.require_version('GstRtspServer','1.0')
from gi.repository import GLib, Gst, GstVideo, GstRtspServer

Gst.init(None)

mainloop = GLib.MainLoop()
server = GstRtspServer.RTSPServer()
mounts = server.get_mount_points()

factory = GstRtspServer.RTSPMediaFactory()

factory.set_launch('( v4l2src device=/dev/video1 io-mode=2 ! image/jpeg, width=640, height=480, framerate=30/1, format=MJPG ! jpegparse ! rtpjpegpay name=pay0 pt=96 )')
mounts.add_factory("/camera2", factory)
server.attach(None)

print("stream ready at rtsp://127.0.0.1:8554/camera2")
mainloop.run()
