
---
title: 'VUE基础知识：第二课数据绑定、指令、事件，语法糖'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8846763093404f06b6544b91a46781d4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 19:14:46 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8846763093404f06b6544b91a46781d4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先写一个代码</p>
<pre><code class="copyable"><div id="dateApp">
        &#123;&#123;date&#125;&#125;
    </div>
     <script src="https://cdn.bootcdn.net/ajax/libs/vue/2.6.14/vue.js"></script>
<script>
/*需求：在页面中实时显示当前时间*/
var app = app Vue(&#123;
el:"#dateApp",
data:&#123;
  date:new Date()
  &#125;,
  mounted:function()&#123;
  var _this = this; //this代表的就是vue实例
  this.timer = setInterval(function()&#123; //加上定时器，美1000ms，this里面的date就会更新一次。
  _this.date = new Date();
  &#125;,1000)
  &#125;,
  beforeDestory:function()&#123; //在vue销毁之前，清除定时器
  if(this.timer)&#123;
  clearInterval(this.timer)
  &#125;
  &#125;
  &#125;)
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-0">过滤器</h3>
<p>过滤器如何使用
&#123;&#123;date | formatDate &#125;&#125;,管道符“|”后面加上要定义的过滤器的名字。</p>
<pre><code class="copyable"><body>
    <div id="dateApp">
        &#123;&#123;date | formatDate&#125;&#125;
    </div>
     <script src="https://cdn.bootcdn.net/ajax/libs/vue/2.6.14/vue.js"></script>
      
    <script>
        //在月份，日期，小时小于10的时候补0
        var plusDate = function(value)&#123;
            return value<10 ? '0'+value :value
        &#125;
        var app = new Vue (&#123;
            el:'#dateApp',
            data:&#123;
                date:new Date()
            &#125;,
            //定义过滤器
            filters:&#123;
                //默认的value就是要过滤的内容
               formatDate: function(value)&#123;
                   //将字符串转换为date类型
                   var date = new Date(value)
                   var year  = date.getFullYear();
                   var month = plusDate(date.getMonth()+1);
                   var day = plusDate(date.getDate());
                   var hours = plusDate(date.getHours());
                   var min = plusDate(date.getMinutes());
                   var sec = plusDate(date.getSeconds());
                   //将整理好的数据返回；
                   return year + '--'+month +'--'+day+'  '+hours+'--'+min+'--'+sec;
               &#125;
            &#125;,
            mounted:function()&#123;
                var _this = this;
                this.timer = setInterval(function()&#123;
                    _this.date = new Date();
                &#125;,1000)
            &#125;,
            beforeDestroy:function()&#123;
                if(this.timer)&#123;
                    clearInterval(this.timer)
                &#125;
            &#125;

        &#125;)
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8846763093404f06b6544b91a46781d4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">指令和事件</h3>
<p>指令，它带有前缀v-，能帮我们快速完成DOM操作，循环渲染，显示和隐藏。
本节目标v-text,v-html,v-blind,v-on;</p>
<ol>
<li>v-text:解析文本；和&#123;&#123;&#125;&#125;的功能一样； &#123;&#123;apple&#125;&#125;和<span></span></li>
<li>v-html:解析html,<span></span></li>
<li>v-bind:基本用途是动态更新HTML元素上的属性，比如id、class等；</li>
</ol>
<p>绑定活得属性,下面这个就是活属性。</p>
<pre><code class="copyable"><style>
.transRed&#123;
background-color:red;&#125;
</style>
<div v-bind:class = "ClassName"></div>
var app = new Vue(&#123;
el:
data:&#123;
className:'transRed'&#125;,&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>v-on:他用来绑定事件监听器，为按钮添加监听事件，</li>
</ol>
<p>&#123;&#123;countnum&#125;&#125;//执行这个count方法，这个方法写在：</p>
<pre><code class="copyable">var app = new Vue(&#123;
el:
datda:&#123;
countnum:0
&#125;
methods:&#123;
count:function()&#123;
this.countnum = this.countnum +1;
&#125;
&#125;,&#125;)
### 语法糖：备注
v-on可以直接用@符号来代替；
v-bind可以用：符号来代替；


 
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            