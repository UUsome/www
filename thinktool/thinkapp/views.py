from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Sort_Detail, Frame_title, Frame_content, Solution

# Create your views here.
def testindex(request):
    return render(request,'thinkapp/index.html')


#### 分类（增删改查）

class SortAdd(View):
    def get(self, request):
        return render(request, 'thinkapp/SortAdd.html')
    def post(self, request):
        name = request.POST.get("name")
        SortDetailI = Sort_Detail()
        SortDetailI.name = name
        SortDetailI.save()
        return redirect(to='SortList')

# 类型列表
def SortList(request):
    allSort = Sort_Detail.objects.all()
    context = {}
    context['allSort'] = allSort
    return render(request,'thinkapp/sortlist.html',context)


#### 框架 （增删改查）
class FrameAdd(View):
    def get(self, request):
        Sort_id = Sort_Detail.objects.all()
        context = {}
        context['Sort_id'] = Sort_id
        return render(request, 'thinkapp/FrameAdd.html', context)
    def post(self, request):
        Num = request.POST.get("Num") #问题个数
        name=request.POST.get("nameT")
        Sort_id = request.POST.get("Sort_id")
        FrameTI = Frame_title()
        FrameTI.name=name
        FrameTI.Sort_id = Sort_id #Sort_id
        # CaseTitleInstance.user=request.user
        FrameTI.save()
        t_id = FrameTI.id
        for i in range(int(Num)):
            FrameCI=Frame_content()
            FrameCI.Frame_title_id = t_id
            FrameCI.name=request.POST.get("Cname"+str(i+1))
            FrameCI.sub_title = request.POST.get("sub_title"+str(i+1))
            FrameCI.save()
        return  redirect(to='frameList')


# 框架列表
def frameList(request):
    FrameT = Frame_title.objects.all()
    FrameSort = Sort_Detail.objects.all()
    context = {}
    context['FrameT'] = FrameT
    context['FrameSort'] = FrameSort
    return render(request,'thinkapp/frameList.html', context)


# 展示框架下所有方案列表
def framedetail(request,frameT_id):
    frameT = Frame_title.objects.get(pk=frameT_id)
    frameC = Frame_content.objects.filter(Frame_title_id=frameT_id)
    context = {}
    context['frameT'] = frameT
    context['frameC'] = frameC
    return render(request,'thinkapp/framedetail.html', context)



####  方案 （增删改查）
class SolutionAdd(View):
    def get(self, request,frameT_id):
        frameT = Frame_title.objects.get(pk=frameT_id)
        frameC = Frame_content.objects.filter(Frame_title_id=frameT_id)
        frameCNum=Frame_content.objects.filter(Frame_title_id=frameT_id).count()
        context = {}
        context['frameT'] = frameT
        context['frameC'] = frameC
        context['frameCNum'] = frameCNum
        return render(request, 'thinkapp/SolutionAdd.html', context)
    def post(self, request,frameT_id):
        frameCNum = request.POST.get("frameCNum")
        for i in range(int(frameCNum)+1):
            V_id = request.POST.get("frameid" + str(i))
            if int(V_id) > -1:
                SolutionI = Solution()
                SolutionI.is_title = request.POST.get("is_title" + str(i))
                SolutionI.F_id = V_id
                SolutionI.name = request.POST.get("solution" + str(i))
                SolutionI.save()
        return redirect(to='frameList')
        # return render(request, 'thinkapp/index.html')

# F标题，S标题
def solutiontail(request,frameT_id):
    frameT = Frame_title.objects.filter(id=frameT_id)
    solution = Solution.objects.filter(is_title=1).filter(F_id=frameT_id)
    context = {}
    context['frameT'] = frameT
    context['solution'] = solution
    return render(request,'thinkapp/solutiontail.html', context)



