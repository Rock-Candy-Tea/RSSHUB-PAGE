
---
title: 'JFinal-layui-pro v2.6 新增用户选择器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.qinhaisenlin.com/upload/img/document/0/1_2021061715213486.png'
author: 开源中国
comments: false
date: Thu, 17 Jun 2021 16:34:00 GMT
thumbnail: 'https://www.qinhaisenlin.com/upload/img/document/0/1_2021061715213486.png'
---

<div>   
<div class="content">
                                                                                            <p>JFinal-layui-pro-v2.6 新增用户选择器：</p> 
<p>先看效果图：</p> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/document/0/1_2021061715213486.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/document/0/1_2021061714530279.png" referrerpolicy="no-referrer"></p> 
<p>1、在表单中引用用户选择器函数：#@getUser(inputId,inputName,dataType)：</p> 
<pre>inputId：标签的ID属性，
inputName：标签的name属性
dataType：1多选用户，0单选用户
</pre> 
<pre><div class="layui-row layui-col-space1 task-row">
        #set(req=true)
        #@colStart("用户多选",6)
    #@getUser('userId','sysUser.id',1)
        #@colEnd()
        
        #@colStart("用户单选",6)
            #@getUser('userId2','sysUser.id2',0)
#@colEnd()
</div>
</pre> 
<p>2、设置选中值，在引用标签前面#set(value=选择的用户id)</p> 
<pre><div class="layui-row layui-col-space1 task-row">
        #set(req=true)
        #@colStart("用户多选",6)
            #set(value='admin,superadmin')
    #@getUser('userId','sysUser.id',1)
        #@colEnd()
        
        #@colStart("用户单选",6)
            #set(value=sysUser.ids??)
            #@getUser('userId2','sysUser.id2',0)
#@colEnd()
</div>
</pre> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/document/0/1_2021061715031381.png" referrerpolicy="no-referrer"></p> 
<p>3、设置必填：#set(req=true)</p> 
<pre><div class="layui-row layui-col-space1 task-row">
        #set(req=true)
        #@colStart("用户多选",6)
            #set(value='admin,superadmin')
    #@getUser('userId','sysUser.id',1)
        #@colEnd()
        
        #set(req=true)
        #@colStart("用户单选",6)
            #set(value=sysUser.ids??,req=true)
            #@getUser('userId2','sysUser.id2',0)
#@colEnd()
</div>
</pre> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/document/0/1_2021061715052482.png" referrerpolicy="no-referrer"></p> 
<p>4、设置禁用属性：#set(disabled=true)</p> 
<pre><div class="layui-row layui-col-space1 task-row">
        #set(req=true)
        #@colStart("用户多选",6)
            #set(value='admin,superadmin',disabled=true)
    #@getUser('userId','sysUser.id',1)
        #@colEnd()
        
        #set(req=true)
        #@colStart("用户单选",6)
            #set(value=sysUser.ids??,req=true)
            #@getUser('userId2','sysUser.id2',0)
#@colEnd()
</div>
</pre> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/document/0/1_2021061715073383.png" referrerpolicy="no-referrer"></p> 
<p>5、默认是只向后台传递用户id信息，没有向后端传递用户姓名，如果同时要保存用户姓名信息，则开启#set(saveUserName=true),那么就会同时向后端传递用户id和用户姓名，用户姓名的参数这是用户id的参数后面加上‘Name’，例如：userId，userIdName</p> 
<pre><div class="layui-row layui-col-space1 task-row">
        #set(req=true)
        #@colStart("用户多选",6)
            #set(value='admin,superadmin',disabled=true)
    #@getUser('userId','sysUser.id',1)
        #@colEnd()
        
        #set(req=true)
        #@colStart("用户单选",6)
            #set(value=sysUser.ids??,req=true,saveUserName=true)
            #@getUser('userId2','sysUser.id2',0)
#@colEnd()
</div>
</pre> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/document/0/1_2021061715163584.png" referrerpolicy="no-referrer"></p> 
<p>6、用户选择器也可以用在列表的条件查询中：</p> 
<pre>#@formStart()

#@queryStart('名称')
   <input type="search" name="name" autocomplete="off" class="layui-input" placeholder="名称"/>
#@queryEnd()

#@queryStart('分类')
   <input type="search" name="type" autocomplete="off" class="layui-input" placeholder="标识键"/>
#@queryEnd()

#set(showLabel=true)
#@queryStart('用户')
    #@getUser('userId','userId',0)
#@queryEnd()

#@formEnd()
</pre> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/document/0/1_2021061715191285.png" referrerpolicy="no-referrer"></p> 
<p><strong> 专业版演示系统</strong><span style="color:#333333">：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.qinhaisenlin.com%3A8081%2F" target="_blank">JFinal-layui极速开发企业应用系统</a><span style="color:#333333">    账号：admin/123456</span></p>
                                        </div>
                                      
</div>
            