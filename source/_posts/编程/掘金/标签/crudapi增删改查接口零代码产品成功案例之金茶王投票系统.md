
---
title: 'crudapi增删改查接口零代码产品成功案例之金茶王投票系统'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://help.crudapi.cn/img/crudapi-success-story/vote/kamcha1.png'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 23:11:52 GMT
thumbnail: 'https://help.crudapi.cn/img/crudapi-success-story/vote/kamcha1.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">crudapi增删改查接口零代码产品成功案例之金茶王投票系统</h1>
<h2 data-id="heading-1">简介</h2>
<p>2020年由于疫情原因，金茶王投票活动改成线上云投票，所以需要一套投票系统进行比赛。参赛选手包括两种类型，分别为餐厅和师傅，投票通过微信公众号页面进行，为了防止作弊，每人每天可以为3位师傅和3个餐厅投票，投票持续时间为一个星期，最终根据票数进行排名。</p>
<h2 data-id="heading-2">UI界面原型</h2>
<p><img src="https://help.crudapi.cn/img/crudapi-success-story/vote/kamcha1.png" alt="kamcha1" loading="lazy" referrerpolicy="no-referrer">
<img src="https://help.crudapi.cn/img/crudapi-success-story/vote/kamcha2.png" alt="kamcha2" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">技术框架</h2>
<p>项目采用前后端分离的方式，数据库采用MySql，后端API采用Java+Spring boot，前端H5采用Vue+Quasar, 由于该项目业务逻辑主要就是基本表单的crud增删改查，所以非常适合用crudapi进行二次开发，通过配置实现RESTful API和后台管理Web，前端H5页面单独定制开发即可。</p>
<h2 data-id="heading-4">数据库表单</h2>
<p>主要业务表单包括候选人（包括师傅和餐厅），赛区，投票活动，活动报名，投票记录等</p>
<p><img src="https://help.crudapi.cn/img/crudapi-success-story/vote/tablerelation.png" alt="tablerelation" loading="lazy" referrerpolicy="no-referrer">
不同表之间建立表关联</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfb3b9384a814124ba2108248c0838ac~tplv-k3u1fbpfcp-watermark.image" alt="candidate" loading="lazy" referrerpolicy="no-referrer">
师傅和餐厅共用候选人candidate表，根据类型type字段进行区分，restaurant表示餐厅，chef表示师傅。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bd14333e1f044bd8dd8abee91a00e3f~tplv-k3u1fbpfcp-watermark.image" alt="voteLog" loading="lazy" referrerpolicy="no-referrer">
投票记录voteLog表，通过唯一性索引uq_vote_log_token限制刷票</p>
<p>包含设计表单到配置，工作量大概一个小时左右。</p>
<h2 data-id="heading-5">后端API</h2>
<p>表单和表关系配置好了，对应的crud增删改查RESTful API也就自动生成了，后端基本完成了80%工作量，然后再集成微信自动登录和阿里云OSS图片上传，剩余工作2天之内完成，</p>
<h2 data-id="heading-6">后台管理Web</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1650dd71e384194a30ce9e8362ad56e~tplv-k3u1fbpfcp-watermark.image" alt="admin" loading="lazy" referrerpolicy="no-referrer">
用途主要是管理员编辑餐厅、师傅信息、查看投票结果和导出数据，crudapi默认页面已经基本满足需求。</p>
<h2 data-id="heading-7">前端H5</h2>
<p>定制开发，15个工作日完成开发和测试。</p>
<h2 data-id="heading-8">小结</h2>
<p>本文主要介绍了金茶王投票系统，利用了crudapi增删改查接口零代码产品进行二次开发，节约了大量时间，总共开发时间18人天。最终按时并高质量完成任务，2020国际金茶王大赛圆满成功。</p>





























<table><thead><tr><th>名称</th><th>采用框架</th><th>类型</th><th>时间</th></tr></thead><tbody><tr><td>Java API</td><td>crudapi</td><td>Java SDK集成</td><td>3天</td></tr><tr><td>后台管理Web</td><td>crudapi-admin-web</td><td>直接使用产品</td><td>0天</td></tr><tr><td>前端H5</td><td>Vue + Quasar</td><td>定制</td><td>15天</td></tr></tbody></table>
<h2 data-id="heading-9">附crudapi产品</h2>
<h4 data-id="heading-10">简介</h4>
<p>crudapi是crud+api组合，表示增删改查接口，是一款零代码可配置的产品。使用crudapi可以告别枯燥无味的增删改查代码，让您更加专注业务，节约大量成本，从而提高工作效率。
crudapi的目标是让处理数据变得更简单，所有人都可以免费使用！
无需编程，通过配置自动生成crud增删改查RESTful API，提供后台UI管理业务数据。基于主流的开源框架，拥有自主知识产权，支持二次开发。</p>
<h4 data-id="heading-11">demo演示</h4>
<p>crudapi属于产品级的零代码平台，不同于自动代码生成器，不需要生成Controller、Service、Repository、Entity等业务代码，程序运行起来就可以使用，真正0代码，可以覆盖基本的和业务无关的CRUD RESTful API。</p>
<p>官网地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrudapi.cn" target="_blank" rel="nofollow noopener noreferrer" title="https://crudapi.cn" ref="nofollow noopener noreferrer">crudapi.cn</a><br>
测试地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdemo.crudapi.cn%2Fcrudapi%2Flogin" target="_blank" rel="nofollow noopener noreferrer" title="https://demo.crudapi.cn/crudapi/login" ref="nofollow noopener noreferrer">demo.crudapi.cn/crudapi/log…</a></p>
<h4 data-id="heading-12">源码地址</h4>
<ol>
<li>GitHub地址</li>
</ol>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcrudapi%2Fcrudapi-admin-web" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/crudapi/crudapi-admin-web" ref="nofollow noopener noreferrer">github.com/crudapi/cru…</a></p>
<ol start="2">
<li>Gitee地址</li>
</ol>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fcrudapi%2Fcrudapi-admin-web" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/crudapi/crudapi-admin-web" ref="nofollow noopener noreferrer">gitee.com/crudapi/cru…</a></p>
<p>由于网络原因，GitHub可能速度慢，改成访问Gitee即可，代码同步更新。</p></div>  
</div>
            