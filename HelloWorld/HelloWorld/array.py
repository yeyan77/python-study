# -*- conding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

def array_form(request):
    return render_to_response('full_permutation.html')

def array(request):
    request.encoding = 'utf-8'
    if 'n' in request.GET:
        count = 1
        list = []
        input_n = int(request.GET['n'])
        while count <= input_n:
            list.append(count)
            count+=1

        message =  perm(list,0,len(list))

    else:
        message = '数字不可以为空'

    return HttpResponse(message)


def perm(arr,begin,end):
    message = ""
    if end==begin:
        message = message + "{"
        for i in range(0,end):
            if i>0:
                message = message + ","

            message = message + str(arr[i])

        message = message + "}"
    else:
        for j in range(begin,end):
            swap(begin,j,arr);
            message = message + perm(arr,begin+1,end)
            swap(begin,j,arr)

    return message


def swap(i1,i2,arr):
    temp = arr[i2]
    arr[i2] = arr[i1]
    arr[i1] = temp