
---
title: 'kefu.js 在线客服系统 v1.2，增加语音功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0306/171845_27fa6313_429922.png'
author: 开源中国
comments: false
date: Fri, 23 Apr 2021 19:54:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/0306/171845_27fa6313_429922.png'
---

<div>   
<div class="content">
                                                                                            <table cellspacing="0" style="width:634px"> 
 <thead> 
  <tr> 
   <th><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0306/171845_27fa6313_429922.png" referrerpolicy="no-referrer"></th> 
   <th><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0306/171852_eab00bf0_429922.png" referrerpolicy="no-referrer"></th> 
   <th> </th> 
  </tr> 
 </thead> 
</table> 
<p> </p> 
<h1 style="text-align:left">更新说明</h1> 
<p>1. 聊天中增加语音功能<br> 2. 简化二次开发代码，将获取用户信息等初始化方式直接内置到了kefu.init() 方法中<br> 3. 隐藏掉当前尚未完善的聊天中发送订单、商品的功能（这两个主要是为其他项目二次开发使用的）<br> 4. 增加限制，不允许自己给自己发送消息<br> 5. 客服后台增加快速体验功能，设置完后就能快速体验效果<br> 6. 修复设置好客服头像，刷新后变回原本的bug（实际已成功修改）<br> 7. 消息记录从阿里云日志服务独立出来，全部采用ElasticSearch存储。</p> 
<p> </p> 
<h2 style="text-align:left">懒人极速体验代码</h2> 
<p style="text-align:left">新建一个HTML文件，其内容如下，直接用浏览器打开即可看到效果。适用于懒人。</p> 
<div style="text-align:left"> 
 <div> 
  <pre><!DOCTYPE html>
<html lang="zh-cn"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>DEMO</title>
</head>
<body>
<script src="https://res.weiunity.com/wm/wm.js"></script>
<script src="https://res.weiunity.com/kefu/dev/h5Pc/h5Pc.js"></script>
<button onclick="kefu.ui.chat.entry('365fef747a9e493fb631b621ee36eed1');">打开PC端客服聊天窗口</button>
</body>
</html></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            