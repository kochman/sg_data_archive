from django.contrib import admin

from data.models import Body, Meeting, Motion, Person, Session

class BodyAdmin(admin.ModelAdmin):
    pass


class MeetingAdmin(admin.ModelAdmin):
    pass


class MotionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Body, BodyAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Motion, MotionAdmin)
admin.site.register(Person)
admin.site.register(Session)

