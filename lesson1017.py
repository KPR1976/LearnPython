garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

garbled = garbled[::-1]
message = garbled[::2]
garbled = garbled[::-1]

print message
print garbled
