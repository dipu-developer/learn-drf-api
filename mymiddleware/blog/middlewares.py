from django.shortcuts import HttpResponse
# function base middleware
def my_middleware(get_response):
    print("one time inizalation")
    def my_functioon(requset):
        print("Inside the function and before views")
        response= get_response(requset)
        print("this is after views function")
        return response
    return my_functioon

# class base middleware
class MyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time inizalations in class")
    
    def __call__(self,request, *args, **kwds):
        print("this is before view function")
        response = self.get_response(request)       #they cheack if the next middleware present the go otherwise go views
        print("this is after view funciton")
        return response
    
class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_view(request,*args, **kwargs):
        return HttpResponse("this is before view")    # use when response before view
        # return None # this run when want to run all middleware and then view
     
class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_exception(self ,request,exception):
        msg = exception
        print(msg)
        class_name = exception.__class__.__name__
        print(class_name)   #ZeroDivisionError
        return HttpResponse(msg)    # use when response before view
        # return None # this run when want to run all middleware and then view
        