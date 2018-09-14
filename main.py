from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform


class MyApp(App):

    def build(self):
        self.start_service()
        return Label(text='Hello world')

    def start_service(self):
        if platform == 'android':
            from jnius import autoclass
            package_name = 'myapp'
            package_domain = 'org.test'
            service_name = 'service'
            service_class = '{}.{}.Service{}'.format(
                package_domain, package_name, service_name.title())
            service = autoclass(service_class)
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            argument = ''
            service.start(mActivity, argument)


if __name__ == '__main__':
    MyApp().run()
