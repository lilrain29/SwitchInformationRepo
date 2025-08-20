from django.db import models

class Switch(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название коммутатора")
    placement = models.CharField(max_length=100, verbose_name="Расположение", default="")
    serialNum = models.CharField(max_length=50, verbose_name="Серийный номер", default="")
    inventoryNum = models.CharField(max_length=50, verbose_name="Инвентарный номер", default="")
    macAddr = models.CharField(max_length=50, verbose_name="MAC-Адрес", default="")
    ip_address = models.GenericIPAddressField(verbose_name="IP-адрес", protocol="IPv4")
    ports_count = models.PositiveIntegerField(verbose_name="Количество портов")

    def __str__(self):
        return f"{self.name} ({self.ip_address})"


class Port(models.Model):
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE, related_name="ports")
    number = models.PositiveIntegerField(verbose_name="Номер порта")
    connected_device = models.CharField(max_length=200, blank=True, null=True, verbose_name="Подключенное устройство")
    ip_address = models.GenericIPAddressField(verbose_name="IP-адрес устройства", blank=True, null=True, protocol="IPv4")
    device_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Название устройства")
    portType = models.CharField(max_length=50, choices=[
        ('TRUNK', 'TRUNK'),
        ('ACCESS', 'ACCESS')
    ], verbose_name="Тип порта", default="")
    status = models.CharField(max_length=50, choices=[
        ('up', 'Включен'),
        ('down', 'Выключен')
    ], verbose_name="Состояние")
    vlanNum = models.CharField(max_length=50, blank=True, null=True, verbose_name="VLAN")
    upLink = models.CharField(max_length=50, blank=True, null=True, verbose_name="Up Link")
    addInfo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Дополнительная информация")
    cabPlacement = models.CharField(max_length=100, blank=True, null=True, verbose_name="Расположение")
    def __str__(self):
        return f"{self.switch.name} - Порт {self.number}"