# p4a-service-sticky
Demonstrates Kivy p4a sticky service.

This undocumented feature was introduced in [kivy/python-for-android#643](https://github.com/kivy/python-for-android/pull/643).
It makes it possible to use Android service [START_STICKY](https://developer.android.com/reference/android/app/Service#START_STICKY).


## Run
Debug, deploy and run:
```sh
buildozer android debug deploy run
```
Check the logs:
```sh
buildozer android adb -- logcat -s python,service,AndroidRuntime
```

## Feature/Bug
1) First the feature:

Closing the foreground app by just hitting the back button would keep the service running.
This can be verified by checking the `logcat` and checking the service is still running:
```
09-11 16:44:09.854  8091  8108 I service : service: 4
09-11 16:44:10.856  8091  8108 I service : service: 5
09-11 16:44:11.857  8091  8108 I service : service: 6
...
```

2) Then the bug:

Now by killing the foreground app e.g. via Android square/overview button and closing, the service will also be killed.
It's getting killed because it's actually running in the app main process.
However it should be restarted thanks to the `sticky` flag added.
But when it tries to restart it crashes with the error below:
```
09-11 17:44:16.362  8127  8127 E AndroidRuntime: FATAL EXCEPTION: main
09-11 17:44:16.362  8127  8127 E AndroidRuntime: Process: org.test.myapp:service_service, PID: 8127
09-11 17:44:16.362  8127  8127 E AndroidRuntime: java.lang.RuntimeException: Unable to start service org.test.myapp.ServiceService@27628fb with null: java.lang.NullPointerException: Attempt to invoke virtual method 'android.os.Bundle android.content.Intent.getExtras()' on a
null object reference
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at android.app.ActivityThread.handleServiceArgs(ActivityThread.java:3495)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at android.app.ActivityThread.-wrap23(ActivityThread.java)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1674)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at android.os.Handler.dispatchMessage(Handler.java:105)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at android.os.Looper.loop(Looper.java:156)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at android.app.ActivityThread.main(ActivityThread.java:6523)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at java.lang.reflect.Method.invoke(Native Method)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:942)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:832)
09-11 17:44:16.362  8127  8127 E AndroidRuntime: Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'android.os.Bundle android.content.Intent.getExtras()' on a null object reference
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at org.kivy.android.PythonService.onStartCommand(PythonService.java:68)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        at android.app.ActivityThread.handleServiceArgs(ActivityThread.java:3476)
09-11 17:44:16.362  8127  8127 E AndroidRuntime:        ... 8 more
```
See [full log here](https://gist.github.com/AndreMiras/6498dd65bf61cb6d51d7b9bd6986c6a0).
