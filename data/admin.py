from django.contrib import admin

from data.models import Body, Meeting, Membership, Motion, Person, Session


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1


class SessionInline(admin.TabularInline):
    model = Session
    extra = 0


class BodyAdmin(admin.ModelAdmin):
    inlines = (SessionInline,)


class MeetingAdmin(admin.ModelAdmin):
    pass


class MotionAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


class SessionAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


admin.site.register(Body, BodyAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Motion, MotionAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Session, SessionAdmin)

admin.site.site_header = 'Student Government Data Archive'
admin.site.site_title = 'SG Data Archive'
admin.site.index_title = 'Administration'

