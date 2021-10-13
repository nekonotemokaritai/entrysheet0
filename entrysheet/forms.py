from django import forms
from django.forms import widgets
from.models import Member, SetList

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['number', 'name']
        labels = {
            'number':'整理番号',
            'name':'表示名',
        }

class SetListForm(forms.ModelForm):
    class Meta:
        model = SetList
        fields = ['complete','number','title','artist','link','vocal','guitar1','guitar2','bass','drum','keyboard','other1','other2']
        labels = {
            'complete':'メンバー成立ならチェック',
            'number':'整理番号',
            'title':'曲名',
            'artist':'アーティスト',
            'link':'動画リンク(空白可)',
            'vocal':'Vocal',
            'guitar1':'Guitar1',
            'guitar2':'Guitar2',
            'bass':'Bass',
            'drum':'Drum',
            'keyboard':'Keyboard',
            'other1':'その他1',
            'other2':'その他2',
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'曲名'}),
            'artist':forms.TextInput(attrs={'class':'form-control','placeholder':'アーティスト名'}),
            'link':forms.TextInput(attrs={'class':'form-control','placeholder':'YouTube動画リンク(空白でもOK)'}),
            # 'vocal': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'vocal': forms.Select(attrs={'class':'form-control-sm'}),
            'guitar1': forms.Select(attrs={'class':'form-control-sm'}),
            'guitar2': forms.Select(attrs={'class':'form-control-sm'}),
            'bass': forms.Select(attrs={'class':'form-control-sm'}),
            'drum': forms.Select(attrs={'class':'form-control-sm'}),
            'keyboard': forms.Select(attrs={'class':'form-control-sm'}),
            'other1': forms.Select(attrs={'class':'form-control-sm'}),
            'other2': forms.Select(attrs={'class':'form-control-sm'}),
        }
    
    # complete = models.BooleanField()
    # number = models.IntegerField()
    # title = models.CharField(max_length=100)
    # artist = models.CharField(max_length=32)
    # link = models.URLField()
    # vocal = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='setlist_vocal')
    # guitar1 = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='setlist_guitar1')
    # guitar2 = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='setlist_guitar2')
    # bass = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='setlist_bass')
    # drum = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='setlist_drum')
    # keyboard = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='setlist_keyboard')
    # other1 = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='setlist_other1')
    # other2 = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='setlist_other2')

class MemberFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MemberFilterForm, self).__init__(*args, **kwargs)
        self.fields['members'] = forms.ChoiceField(
            label='抽出するメンバーを選択', required=False,
            choices=[('-','-')] + [(item.name, item.name) for item in Member.objects.all()],
            widget=forms.Select(attrs={'class':'form-control'}),
        )
