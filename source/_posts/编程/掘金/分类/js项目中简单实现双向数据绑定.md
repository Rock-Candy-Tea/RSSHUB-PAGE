
---
title: 'js项目中简单实现双向数据绑定'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aeb843db7ada408e9b2920f333c0f2a7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 09:23:56 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aeb843db7ada408e9b2920f333c0f2a7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第29天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p><strong>双向数据绑定</strong> 指的是当对象的属性发生变化时能够同时改变对应的UI，反之亦然。换句话说，如果我们有一个user对象，这个对象有一个name属性，无论何时你对user.name设置了一个新值，UI也会展示这个新的值。同样的，如果UI包含一个用于数据用户名字的输入框，输入一个新值也会导致user对象的name属性发生相应的改变。</p>
<p>许多流行的javascript框架，像Ember.js,Angular.js或者KnockoutJS都会把双向数据绑定作为其中的主要特性来宣传。这并不意味着从头开始实现它很难，也不意味着当我们需要这种功能的时候，使用这些框架是我们唯一的选择。内部的潜在思想事实上是相当基础的，实现它可以归纳为以下三点：</p>
<ul>
<li>我们需要一种方式确定哪个UI元素绑定在哪个属性上。</li>
<li>我们需要监控属性和UI的变化</li>
<li>我们需要把所有绑定的对象和UI元素的变化传播出去。</li>
</ul>
<h2 data-id="heading-1">发布订阅者模式</h2>
<p>发布-订阅模式其实是一种对象间一对多的依赖关系，当一个对象的状态发送改变时，所有依赖于它的对象都将得到状态改变的通知。<br>
订阅者（Subscriber）把自己想订阅的事件注册（Subscribe）到调度中心（Event Channel），当发布者（Publisher）发布该事件（Publish Event）到调度中心，也就是该事件触发时，由调度中心统一调度（Fire Event）订阅者注册到调度中心的处理代码。</p>
<h4 data-id="heading-2">结果</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aeb843db7ada408e9b2920f333c0f2a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">调用</h4>
<p>html  调用 端 绑定 data-bind-phone="name"</p>
<pre><code class="copyable">
  <ul>  

     <li class="block-phone fix bd-bottom">  

          <label for="J_verificationPhone" data-bind-phone="tishi"><span>手机号</span></label>  

          <input  class="fix1" id="J_verificationPhone" data-bind-phone="name" name="phone"  type="text" />  

          <button class="right J_clickTime"  type="button">

            <span class="award-messages-btn2 J_messagesBtn1">获取验证码</span>

            <span class="award-messages-btn2 J_messagesBtn2 none"><i>60</i>s后重发</span>

          </button>

     </li>  

     <li class="block-verification fix">  

          <label for="J_verificationCode"><span>验证码</span></label>  

          <input class="fix1" data-bind-code="tishi" id="J_verificationCode" data-bind-phone="name" name="verification-code" class="" type="" />  

     </li> 

  </ul>  

<span class="copy-code-btn">复制代码</span></code></pre>
<p>js 调用 看下面代码注释</p>
<p>/**</p>
<p> * function verficationCallback 回调方法</p>
<p> * [$btn1 description]</p>
<p> * data-bind-phone="name"</p>
<p> * @ message &#123;[type]&#125;   发生变化的字段phone</p>
<p> * @ prop_name &#123;[type]&#125;  字段的value  name</p>
<p> * @ target &#123;[type]&#125;      目标jsdom对象;</p>
<p> * @ targetValue &#123;[type]&#125;  目标jsdom对象的value</p>
<p> */// 监听回调函数，函数会拿到targetvalue 的值， target js dom对象，便于对变化的字段进行操作！！！</p>
<pre><code class="copyable">

var User= require('../../entry/module/twoWayAudio.js');


var phone = new User('phone',verficationCallback);


 function verficationCallback(message,prop_name,target,targetValue)&#123;



&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入的源代码 twoWayAudio</p>
<pre><code class="copyable">
function DataBinder(object_id,verficationCallback)&#123;  



// 创建一个简单的pubSub对象

var pubSub = &#123;

callbacks: &#123;&#125;,

on: function(msg,callback) &#123;

this.callbacks[msg] = this.callbacks[msg] || [];

this.callbacks[msg].push(callback);

&#125;,

publish: function(msg) &#123;

\


this.callbacks[msg] = this.callbacks[msg] || [];

for (var i = 0,len = this.callbacks[msg].length; i < len; i++) &#123;

this.callbacks[msg][i].apply(this,arguments);

&#125;;

&#125;

&#125;,

data_attr = "data-bind-" + object_id,

message   = object_id + ":change",

changeHandler = function(event) &#123;



var target = event.target || event.srcElement, // IE8兼容

prop_name = target.getAttribute(data_attr);



if (prop_name && prop_name !== "") &#123;



if(verficationCallback)&#123;

var targetValue = target.value;

verficationCallback (message,prop_name,target,targetValue);

&#125;

pubSub.publish(message,prop_name,target.value);

&#125;

&#125;;



// 监听事件变化，并代理到pubSub

if (document.addEventListener) &#123;

document.addEventListener("keyup",changeHandler,false);

&#125; else&#123;

// IE8使用attachEvent而不是addEventListenter

document.attachEvent("onkeyup",changeHandler);

&#125;;

// pubSub将变化传播到所有绑定元素

pubSub.on(message,function(event,prop_name,new_val)&#123;

var elements = document.querySelectorAll("[" + data_attr + "=" +prop_name + "]"),

tag_name;

for (var i = 0,len = elements.length; i < len; i++) &#123;

tag_name = elements[i].tagName.toLowerCase();

if (tag_name === "input" || tag_name === "textarea" || tag_name === "select") &#123;

elements[i].value = new_val;

&#125; else&#123;

elements[i].innerHTML = new_val;

&#125;;

&#125;;

&#125;)

return pubSub;

&#125;



function User(uid,verficationCallback) &#123;  

var binder = new DataBinder(uid,verficationCallback),

  user   = &#123;

  attribute : &#123;&#125;,

  // 属性设置器使用数据绑定器pubSub来发布

  set : function(attr_name,val) &#123;

  this.attribute[attr_name] = val;

  binder.publish(uid + ":change",attr_name,val,this);

  &#125;,

  get : function(attr_name) &#123;

  return this.attribute[attr_name];

  &#125;,

  _binder : binder

  &#125;;

binder.on(uid + ":change",function(event,attr_name,new_val,initiator) &#123;

if (initiator !== user) &#123;

user.set(attr_name,new_val);

&#125;

&#125;);

return user;

&#125;

module.exports = User;



// phone.set( "name", "lwl" );  



// phone.set( "tishi", "提示" );  



<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-4">替代解决方案</h6>
<p>上面只是在掩饰双向数据绑定，其实这种需求可以更简单的实现 嘿嘿</p>
<pre><code class="copyable">
 $('.block-phone #phone')[0].oninput=function()&#123;

 console.log($(this))

&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            