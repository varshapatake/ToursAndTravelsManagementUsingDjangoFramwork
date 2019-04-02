from django.contrib import admin
from .models import Customer,AdminInfo,RegisterPackageInfo,PackageCosts,MyBankDetails,Shedule,PaymentStatus
admin.site.register(Customer)
admin.site.register(AdminInfo)
admin.site.register(RegisterPackageInfo)
admin.site.register(PackageCosts)
admin.site.register(MyBankDetails)
admin.site.register(Shedule)
admin.site.register(PaymentStatus)
