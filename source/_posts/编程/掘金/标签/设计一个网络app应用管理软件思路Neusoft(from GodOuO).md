
---
title: '设计一个网络app应用管理软件思路Neusoft(from GodOuO)'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=5084'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 20:21:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=5084'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>安卓技术设计一个网络app应用管理软件，本地利用SQLite存储应用列表信息存储，可以在在线或离线情况下可以实现获得历史app应用软件信息。可以对本地app应用软件进行权限管理，删除更新等。请写出设计思路，以及运用的技术。</p>
</blockquote>
<h2 data-id="heading-0">设计流程</h2>
<ul>
<li>原型设计
<ol>
<li>功能结构布局</li>
<li>各页面设计</li>
<li>页面间业务逻辑设计</li>
</ol>
</li>
<li>UI设计
<ol>
<li>APP UI</li>
<li>后台 UI</li>
</ol>
</li>
<li>开发
<ol>
<li>服务器端：编写接口协议文档，服务器环境架设(阿里云服务等)，设计数据库和编写API接口</li>
<li>APP端：根据UI设计图开始界面开发，UI开发完毕进入与服务器接口对接，通过服务器定义接口获取数据，编写功能逻辑代码。</li>
<li>Web端：根据前端业务逻辑，后台有相应功能匹配，编写对应逻辑代码。</li>
</ol>
</li>
<li>测试调试
<ol>
<li>APP网络应用管理系统软件开发编写中及其完成后，整体进行黑白盒测试，追踪BUG进度状态，定义优先级，高效有序完成问题的处理。</li>
</ol>
</li>
<li>发布
<ol>
<li>至少两轮内部及小范围公测后进行应用市场上架</li>
</ol>
</li>
<li>运营迭代
<ol>
<li>正式投放市场后，根据市场及其用户反馈进行修正或调整APP，如需更新功能，则将重新规划新版本</li>
</ol>
</li>
<li>日常维护
<ol>
<li>在网络应用管理软件正常运作中，即使达到稳态，也可能激发隐藏BUG，需要有关人员进行及时调研和修复，日常需要留住值守</li>
</ol>
</li>
</ul>
<h2 data-id="heading-1">根目录下的"AndroidManifest.xml"文件，用以向Android系统声明所需Android权限等运行应用所需的条件。</h2>
<h2 data-id="heading-2">SQLite。是一款轻型的数据库</h2>
<ul>
<li>新建一个类，命名为MySQLiteOpenHelper,并将其继承自SQLiteOpenHelper:</li>
<li>加入构造方法</li>
<li>加入数据通过手写sql语句，运行execSQL();方法或者通过Android API,将数据封装到contentValues中</li>
<li>删除改动数据通过手写sql语句，运行execSQL();方法或者通过Android API</li>
<li>查询数据通过rawQuery()方法或者通过Android API</li>
<li>当须要保证多条语句同一时候运行成功，否则。回滚</li>
</ul>
<h2 data-id="heading-3">删除应用权限管理</h2>
<ul>
<li>通过Shared User id,拥有同一个User id的多个APK可以配置成运行在同一个进程中</li>
<li>对于一个APK来说，如果要使用某个共享UID的话，必须做三步：
<ol>
<li>在Manifest节点中增加android:sharedUserId属性。</li>
<li>在Android.mk中增加LOCAL_CERTIFICATE的定义。</li>
<li>把APK的源码放到packages/apps/目录下，用mm进行编译</li>
</ol>
</li>
<li>应用程序的Android.mk中有一个LOCAL_CERTIFICATE字段，由它指定用哪个key签名，未指定的默认用testkey</li>
</ul></div>  
</div>
            