from django.shortcuts import render, redirect
from .models import Member, SetList, LastUpdateDT
from .forms import MemberForm, SetListForm, MemberFilterForm
from django.utils import timezone
from django.db.models import Q

# Create your views here.
def index(request):
    data = SetList.objects.all()
    msg = ''
    member_update_dt, _ = LastUpdateDT.objects.get_or_create(id=1) # 不要だがID=2の新規生成時エラーになるかもしれないので入れている
    setlist_update_dt, _ = LastUpdateDT.objects.get_or_create(id=2)
    params = {
        'title':'セットリスト一覧',
        'message':msg,
        'data':data,
        'setlist_update_dt':timezone.localtime(setlist_update_dt.last_update_dt),
    }
    return render(request, 'entrysheet/index.html', params)

def editor_top(request):
    if request.method == 'POST':
        sel_member = request.POST['members']
        data = SetList.objects.filter(
            Q(vocal__name__contains=sel_member) | Q(guitar1__name__contains=sel_member) |
            Q(guitar2__name__contains=sel_member) | Q(bass__name__contains=sel_member) |
            Q(drum__name__contains=sel_member) |  Q(keyboard__name__contains=sel_member) |
            Q(other1__name__contains=sel_member) | Q(other2__name__contains=sel_member)
        )
    else:
        data = SetList.objects.all()
    # data = SetList.objects.all()
    member_data = Member.objects.all()
    member_update_dt, _ = LastUpdateDT.objects.get_or_create(id=1)
    setlist_update_dt, _ = LastUpdateDT.objects.get_or_create(id=2)
    member_filter_form = MemberFilterForm(request.POST)
    params = {
        'title':'セットリスト＆参加者編集',
        'message':'編集者用ページ',
        'data':data,
        'member_data':member_data,
        'member_update_dt':timezone.localtime(member_update_dt.last_update_dt),
        'setlist_update_dt':timezone.localtime(setlist_update_dt.last_update_dt),
        'member_filter_form':member_filter_form,
    }
    return render(request, 'entrysheet/editor_top.html', params)

def add_member(request):
    if (request.method=='POST'):
        obj = Member()
        member = MemberForm(request.POST, instance=obj)
        member.save()
        objDT, _ = LastUpdateDT.objects.get_or_create(id=1) # ID=1:Member, ID=2:SetList
        objDT.save()
        return redirect(to='/entrysheet/editor_top')
    params = {
        'title':'参加メンバー追加',
        'message':\
            '表示名の内容がセットリストの各パートに表示されます。<br>\
            整理番号は任意の値を設定可能(他の名前との重複OK)、一覧には整理番号の順に表示されます。',
        'form':MemberForm(),
    }
    return render(request, 'entrysheet/add_member.html', params)

def edit_member(request, num):
    obj = Member.objects.get(id=num)
    if (request.method == 'POST'):
        member = MemberForm(request.POST, instance=obj)
        member.save()
        objDT, _ = LastUpdateDT.objects.get_or_create(id=1) # ID=1:Member, ID=2:SetList
        objDT.save()
        return redirect(to='/entrysheet/editor_top')
    params = {
        'title':'参加メンバー編集',
        'message':\
            '整理番号、表示名をそれぞれ編集します。<br>\
            表示名の内容がセットリストの各パートに表示されます。<br>\
            整理番号は任意の値を設定可能(他の名前との重複OK)、一覧には整理番号の順に表示されます。',
        'form':MemberForm(instance=obj),
        'id':num,
    }
    return render(request, 'entrysheet/edit_member.html', params)

def delete_member(request, num):
    member = Member.objects.get(id=num)
    if (request.method == 'POST'):
        member.delete()
        objDT, _ = LastUpdateDT.objects.get_or_create(id=1) # ID=1:Member, ID=2:SetList
        objDT.save()
        return redirect(to='/entrysheet/editor_top')
    params = {
        'title':'参加メンバー削除',
        'message':'※※※表示されているメンバーを削除します※※※',
        'obj':member,
        'id':num,
    }
    return render(request, 'entrysheet/delete_member.html', params)

def add_setlist(request):
    if (request.method=='POST'):
        obj = SetList()
        setlist = SetListForm(request.POST, instance=obj)
        setlist.save()
        objDT, _ = LastUpdateDT.objects.get_or_create(id=2) # ID=1:Member, ID=2:SetList
        objDT.save()
        return redirect(to='/entrysheet/editor_top')
    params = {
        'title':'セットリスト追加',
        'message':\
            '追加する曲情報を入力してください。<br>\
            各パートのメンバーは事前に登録された参加メンバーから選択可能です。',
        'form':SetListForm(),
    }
    return render(request, 'entrysheet/add_setlist.html', params)

def edit_setlist(request, num):
    obj = SetList.objects.get(id=num)
    if (request.method == 'POST'):
        setlist = SetListForm(request.POST, instance=obj)
        setlist.save()
        objDT, _ = LastUpdateDT.objects.get_or_create(id=2) # ID=1:Member, ID=2:SetList
        objDT.save()
        return redirect(to='/entrysheet/editor_top')
    params = {
        'title':'セットリスト編集',
        'message':\
            '曲情報をそれぞれ編集してください。<br>\
            各パートのメンバーは事前に登録された参加メンバーから選択可能です。',
        'form':SetListForm(instance=obj),
        'id':num,
    }
    return render(request, 'entrysheet/edit_setlist.html', params)

def delete_setlist(request, num):
    setlist = SetList.objects.get(id=num)
    if (request.method == 'POST'):
        setlist.delete()
        objDT, _ = LastUpdateDT.objects.get_or_create(id=2) # ID=1:Member, ID=2:SetList
        objDT.save()
        return redirect(to='/entrysheet/editor_top')
    params = {
        'title':'セットリスト削除',
        'message':'※※※表示されているセットリストを削除します※※※',
        'obj':setlist,
        'id':num,
    }
    return render(request, 'entrysheet/delete_setlist.html', params)
