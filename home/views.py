from django.shortcuts import render,HttpResponse, redirect
from home.models import BlogPost,SearchQuery, BlogComment, Like
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from home.templatetags import extras

# Create your views here.
# HTML Pages 
def home(request):
    allPost = BlogPost.objects.all()
    print(allPost)
    context = {'allPost':allPost}
    return render(request,'index.html',context)

def myblog(request):
    allPost = BlogPost.objects.all()
    print(allPost)
    context = {'allPost':allPost}
    return render(request,'myblog.html',context)


# My API's
def signup(request):
    if request.method == 'POST':
        email    = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        myuser   = User.objects.create_user(username=username,email=email,password=password)
        myuser.save()
        messages.success(request, 'Account created successfully')
        return redirect('http://127.0.0.1:8000/')
    else:
        messages.error(request, 'Unable to create your account')
        return redirect('http://127.0.0.1:8000/')

def UserLogout(request):
    #if request.method == 'POST':
    logout(request)
    messages.success(request, 'Profile Logged Out Successfully.')
    return redirect('http://127.0.0.1:8000/')

def loginUser(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome '+loginusername+'! Your Profile Successfully Logged In')
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.warning(request, 'Invalid Username or Password')
            return redirect('http://127.0.0.1:8000/')

def search(request):
    query = request.GET['query']
    if len(query) > 78:
        post = []
    else:
        postTitle = BlogPost.objects.filter(title__icontains = query)
        postContent = BlogPost.objects.filter(content__icontains = query)
        postAuthor = BlogPost.objects.filter(author__icontains = query)
        post = postTitle.union(postContent,postAuthor)
    param = {'post':post, 'query':query}
    # If search result not found in the server then we will store the search value in the database for future purpose
    if len(post) == 0 and len(query) < 78:
        val = SearchQuery(searchValue = query)
        val.save()
    return render(request,'search.html',param)

def blogpost(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)
    context = {'post':post, 'comments':comments, 'user':request.user, 'repDict':repDict}
    #print(repDict)
    return render(request,'blogpost.html',context)

def blogComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = BlogPost.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno =="":
        #parent = request.POST['parrent']
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, 'Your comment has been posted successfully')
            return redirect(f'/myblog/{post.slug}')
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post,parent=parent)
            comment.save()
            messages.success(request, 'Your reply has been posted successfully')
            return redirect(f'/myblog/{post.slug}')

def PostBlog(request):
    if request.method == "POST" and request.FILES['blogthumb']:
        title = request.POST['title']
        content = request.POST['content']
        blogthumb = request.FILES['blogthumb']
        author = request.user
        slug = request.POST['slug']
        timeStamp = datetime.now()
        postBlog = BlogPost(title=title,content=content,blogthumb=blogthumb,author=author,slug=slug,timeStamp=timeStamp)
        postBlog.save()
        messages.success(request, 'Your blog has been posted successfully')
        return redirect(f'/myblog/{postBlog.slug}')

def save(self): 
    user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password']) 
    user.email = self.cleaned_data['email']
    user.save()
    return user

def liked_post(request):
    user = request.user
    if request.method=="POST":
        post_id = request.POST.get('post_id')
        post_obj = BlogPost.objects.get(sno=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect(f'/myblog/{post_obj.slug}')


def delete_record(request):
    user = request.user
    if request.method == "POST":
        tag_id = request.POST.get('post_delete')
        author = BlogPost.objects.filter(sno=tag_id).delete()
        messages.success(request, 'Your post hasbeen deleted successfully')
        return redirect('/myblog/')
