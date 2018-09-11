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
buildozer android adb -- logcat | grep -e python -e service
```
