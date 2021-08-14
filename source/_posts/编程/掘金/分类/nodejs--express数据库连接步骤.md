
---
title: 'nodejs--express数据库连接步骤'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5795'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 21:53:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=5795'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>第一步:打开xampp,启动(start)mysql,打开shell命令<br>
第二部:用vscode新建一个后缀名为sql的文件<br>
第四部:在VScode界面中输入<br></p>
<pre><code class="copyable">                #设置客户端连接服务端的编码
                set names utf8
                #如果存在该数据库，则丢弃该数据库
                drop database if exist 数据库名
                #创建数据库，设置编码格式
                creat database 数据库名  charset=utf8
                #进入数据库
                use 数据库名
                #创建数据表格
                creat table 表名();
                #插入数据
                insert into 表名 values
                ();
                ();
                ();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第五步:返回第一步打开shell窗口,输入 mysql -uroot<sql文件的绝对路径，然后回车<br></p>
<pre><code class="copyable">    注意：mysql空格-uroot mysql和-uroot之间有空格，-u和root之间没有空格
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第六步：有错误返回vscode界面，找寻错误，没有错误，输入mysql -uroot回车<br>
第七步：show databases; 回车，use 数据库名; show tables 回车打开数据库中的表格，desc 表名;查询数据结构，select * from 表名  查询数据内容<br>
第八步:创建MVC三层架构，即model(模型)&#123;数据库操作&#125;，view(视图)&#123;用户与系统之间交互&#125;，controller(控制器)&#123;业务逻辑操作&#125;，所以创建routes文件，app.js(服务器) pool.js(连接池)以及view文件夹(这里不做赘述)<br>
第九步：把文件用终端打开，输入npm install express和npm install mysql
第十步:用vscode打开pool.js,输入以下内容</p>
<pre><code class="copyable">                const mysql=require("mysql")
                const pool=mysql.creatpool(
                hostname:"",
                port:"",
                user:"",
                password:"",
                root:"",
                databases:"",
                connectionLimit:""
               );
               model.exports=pool
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第十一步:用vscode打开app.js,输入以下内容</p>
<pre><code class="copyable">               const express=require("express");
               const router=require("routes下的JS文件")
               const app=express();
               app.listen(8080);
               //解析为json格式
               app.use(express,urlencoded)&#123;
                   extends:false
               &#125;
               app.use('给路由添加前缀',router);
               app.use((err,req,res,next)=>&#123;
               console.log(err);
               res.status(500).send(&#123;
                   code:500,
                   msg:"服务器端错误"
               &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第十二步:用vscode打开routes下的js文件</p>
<pre><code class="copyable">                const express=require("express");
                const pool=require("连接池路径");
                const router=require("router");
                
                router.(请求方法(post/get/delect/put))('/路由'funaction(req,res,next)&#123;
                    let obj=req.body;
                    var sql="";
                    if(obj,user)&#123;
                    res.send(&#123;
                        code:400,
                        msg:""
                        &#125;)
                        
                    &#125;
                    pool.query(sql,[obj],funaction(err,result)&#123;
                        try&#123;
                            console.log(result);
                            res.send(&#123;
                            code:"400",
                            msg:"数据访问成功"
                            &#125;)
                        &#125;catch&#123;
                            if(err)&#123;
                            next(err);
                            return;
                            &#125;
                        &#125;
                    &#125;)
                &#125;)
                model.exports=router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第十三步:在终端输入node app,启动服务器，将<a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">httP://IP地址:端口号/前缀/路由</a> 复制到apipost软件中有返回结果就代表成功了否则检查代码</p></div>  
</div>
            