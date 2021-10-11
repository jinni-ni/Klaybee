from django.contrib import admin
from .models import Site, KspStandard, Token, Pool, PoolToken, Reward, RewardCode

# Register your models here.
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass

@admin.register(Pool)
class PoolAdmin(admin.ModelAdmin):
    pass

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass

@admin.register(KspStandard)
class KspStandardAdmin(admin.ModelAdmin):
    pass

@admin.register(PoolToken)
class PoolTokenAdmin(admin.ModelAdmin):
    pass

@admin.register(RewardCode)
class RewardCodeAdmin(admin.ModelAdmin):
    pass


