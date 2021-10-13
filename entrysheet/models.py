from django.db import models

# Create your models here.
def get_or_create_default_member1():
    member_name, _ = Member.objects.get_or_create(number=0, name='募集中')
    return member_name

def get_or_create_default_member2():
    member_name, _ = Member.objects.get_or_create(number=-1, name='なし')
    return member_name


class Member(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=32)

    def __str__(self):
        # return '<Member: id = ' + str(self.id) + ' , ' + self.name + ' 整理番号:' + str(self.number) + ' >'
        return '<' + '整理番号:' + str(self.number) + '>' + self.name

    class Meta:
        ordering = ('number',)


class SetList(models.Model):
    complete = models.BooleanField()
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=32, blank=True)
    link = models.URLField(blank=True)
    vocal = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=get_or_create_default_member1, related_name='setlist_vocal')
    guitar1 = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=get_or_create_default_member1, related_name='setlist_guitar1')
    guitar2 = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=get_or_create_default_member1, related_name='setlist_guitar2')
    bass = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=get_or_create_default_member1, related_name='setlist_bass')
    drum = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=get_or_create_default_member1, related_name='setlist_drum')
    keyboard = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=get_or_create_default_member1, related_name='setlist_keyboard')
    other1 = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=get_or_create_default_member2, related_name='setlist_other1')
    other2 = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=get_or_create_default_member2, related_name='setlist_other2')

    def __str__(self):
        return '<整理番号:' + str(self.number) + '>' + self.title + ' (' + self.artist + ')'
    
    class Meta:
        ordering = ('number',)


class LastUpdateDT(models.Model):
    last_update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<' + str(self.last_update_dt) + '>'
