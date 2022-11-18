from .models import SiteSetting, SystemSettings

def get_siteoption(request):
    siteoption= SiteSetting.objects.first()
    systemoption= SystemSettings.objects.first()
    return {'siteoption':siteoption,'systemoption':systemoption}