from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# swap site
class Site(BaseModel):
    site_name = models.CharField(max_length=200, blank=False)

# 유동성 풀 대상 1일 KSP 분배 수량
class KspStandard(BaseModel):
    amount = models.PositiveIntegerField(default=0)

# token
class Token(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    token_address = models.CharField(max_length=200, blank=True)
    token_image = models.ImageField(upload_to='token/',blank=True)
# Pool
class Pool(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    contract_address = models.CharField(max_length=50)
    LP_amount = models.BigIntegerField(default=0)

# Pool Token
class PoolToken(BaseModel):
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    # TODO : Decimal filed data confirm (decimal:18)
    token_amount = models.DecimalField(max_digits=30,decimal_places=18)

# Reward Code
class RewardCode(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

# Reward
class Reward(BaseModel):
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    reward_code = models.ForeignKey(RewardCode, on_delete=models.CASCADE)
    amount = models.FloatField()





