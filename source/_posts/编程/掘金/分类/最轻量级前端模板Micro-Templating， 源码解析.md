
---
title: '最轻量级前端模板Micro-Templating， 源码解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7196'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 20:02:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=7196'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第21天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">关于模板</h2>
<p>关于模板，写页面的人们其实一直在用，asp.net , jsp , php, nodejs等等都有他的存在，当然那是服务端的模板。</p>
<p>前端模板，作为前端人员肯定是多少有接触的，Handlebars.js,JsRender,Dust.js,Mustache.js,Underscore templates,Angularjs,<strong>Vuejs,reactjs</strong>到处都离不开模板的影子。</p>
<h2 data-id="heading-1">Micro-Templating解析在线测试</h2>
<p class="codepen"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fxiangwenhu%2Fpen%2FdJdGBj%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/xiangwenhu/pen/dJdGBj/" ref="nofollow noopener noreferrer">MicroTemplating</a></p>

<h2 data-id="heading-2">Micro-Templating模板</h2>
<p>本文主要是分析一下jQuery的创始人的Micro-Templating，麻雀虽小缺五张俱全。</p>
<p><strong>到这里可别笑，说用什么jQuery的，jQuery的思想绝对是异常的优秀，霸榜十多年， React也不过是最近两年才赶超。</strong></p>
<p>先贴出作者的源码:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Simple JavaScript Templating</span>
<span class="hljs-comment">// John Resig - https://johnresig.com/ - MIT Licensed</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">var</span> cache = &#123;&#125;;
   
  <span class="hljs-built_in">this</span>.tmpl = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tmpl</span>(<span class="hljs-params">str, data</span>)</span>&#123;
    <span class="hljs-comment">// Figure out if we're getting a template, or if we need to</span>
    <span class="hljs-comment">// load the template - and be sure to cache the result.</span>
    <span class="hljs-keyword">var</span> fn = !<span class="hljs-regexp">/\W/</span>.test(str) ?
      cache[str] = cache[str] ||
        tmpl(<span class="hljs-built_in">document</span>.getElementById(str).innerHTML) :
       
      <span class="hljs-comment">// Generate a reusable function that will serve as a template</span>
      <span class="hljs-comment">// generator (and which will be cached).</span>
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">"obj"</span>,
        <span class="hljs-string">"var p=[],print=function()&#123;p.push.apply(p,arguments);&#125;;"</span> +
         
        <span class="hljs-comment">// Introduce the data as local variables using with()&#123;&#125;</span>
        <span class="hljs-string">"with(obj)&#123;p.push('"</span> +
         
        <span class="hljs-comment">// Convert the template into pure JavaScript</span>
        str
          .replace(<span class="hljs-regexp">/[\r\t\n]/g</span>, <span class="hljs-string">" "</span>)
          .split(<span class="hljs-string">"<%"</span>).join(<span class="hljs-string">"\t"</span>)
          .replace(<span class="hljs-regexp">/((^|%>)[^\t]*)'/g</span>, <span class="hljs-string">"$1\r"</span>)
          .replace(<span class="hljs-regexp">/\t=(.*?)%>/g</span>, <span class="hljs-string">"',$1,'"</span>)
          .split(<span class="hljs-string">"\t"</span>).join(<span class="hljs-string">"');"</span>)
          .split(<span class="hljs-string">"%>"</span>).join(<span class="hljs-string">"p.push('"</span>)
          .split(<span class="hljs-string">"\r"</span>).join(<span class="hljs-string">"\\'"</span>)
      + <span class="hljs-string">"');&#125;return p.join('');"</span>);
     
    <span class="hljs-comment">// Provide some basic currying to the user</span>
    <span class="hljs-keyword">return</span> data ? fn( data ) : fn;
  &#125;;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">基本原理：</h3>
<ol>
<li>使用属性检查来进行缓存</li>
<li>采用正则替换标签（赋值标签，js语句标签）</li>
<li>使用with设置代码在对象中的作用域，主要是提升了编程体验，(当然也可以用apply,call,bind等修改函数作用域，然后通过this.prop来编写，但是体验上差一些)</li>
<li>动态构建执行函数</li>
<li>通过判断决定返回结果类型</li>
</ol>
<p>关于 1，3，5没有太多需要讲的，关于5，如果执行时不传入data参数，返回的执行函数，可以延迟使用，到处使用。</p>
<h3 data-id="heading-4">print</h3>
<p>调试的日志输出。</p>
<p>重点在于2和4，在这之前，先看看print，这个print申请在函数顶部，就表示在js语句的时候是可以调用呢，怎么调用呢，看看示例，至于作用么，当然是debug啊</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/html"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"item_tmpl"</span>></span><span class="javascript">         
        <% <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++ ) &#123; %>    
            <% <span class="hljs-keyword">if</span>( i%<span class="hljs-number">2</span> == <span class="hljs-number">1</span>) &#123;%>
                <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span><%=items[i].id%>:<%=items[i].name%><span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
            <% &#125; %> 
        <% &#125; %>
        <% print(<span class="hljs-string">'数组长度'</span> + items.length ); %>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">'background:<%=color%>'</span>></span><%=id%><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

      </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很简单：  <% print('数组长度' + items.length ); %><br>
原理也很简单，数组p里面添加一条数据</p>
<h3 data-id="heading-5">正则替换</h3>
<p>为了方便debug和备注，我调整一下原理结构</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> cache = &#123;&#125;;

    <span class="hljs-built_in">this</span>.tmpl = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tmpl</span>(<span class="hljs-params">str, data</span>) </span>&#123;
        <span class="hljs-comment">// Figure out if we're getting a template, or if we need to</span>
        <span class="hljs-comment">// load the template - and be sure to cache the result.</span>
        <span class="hljs-keyword">var</span> fn = !<span class="hljs-regexp">/\W/</span>.test(str) ?
            cache[str] = cache[str] ||
            tmpl(<span class="hljs-built_in">document</span>.getElementById(str).innerHTML) :

            <span class="hljs-comment">// Generate a reusable function that will serve as a template</span>
            <span class="hljs-comment">// generator (and which will be cached).</span>
            <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">"obj"</span>,
                <span class="hljs-string">"var p=[],print=function()&#123;p.push.apply(p,arguments);&#125;;"</span> +

                <span class="hljs-comment">// Introduce the data as local variables using with()&#123;&#125;</span>
                <span class="hljs-string">"with(obj)&#123;p.push('"</span> +

                <span class="hljs-comment">// Convert the template into pure JavaScript</span>
                getStr(str)
                + <span class="hljs-string">"');&#125;return p.join('');"</span>);

        <span class="hljs-comment">// Provide some basic currying to the user</span>
        <span class="hljs-keyword">return</span> data ? fn(data) : fn;
    &#125;;


    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getStr</span>(<span class="hljs-params">str</span>)</span>&#123;
         <span class="hljs-comment">// 删除回车，制表，换行</span>
        str = str .replace(<span class="hljs-regexp">/[\r\t\n]/g</span>, <span class="hljs-string">" "</span>);   
        <span class="hljs-comment">// 替换 <% 为 \t制表符，两种情况（赋值和js代码）</span>
        <span class="hljs-comment">// 赋值： 例如 <div id="<%=id%>">  ==>  <div id="\t=id%>"></span>
        <span class="hljs-comment">// js代码：例如 <% for ( var i = 0; i < items.length; i++ ) &#123; %>  ==>  \t for ( var i = 0; i < items.length; i++ ) &#123; %></span>
        str = str.split(<span class="hljs-string">"<%"</span>).join(<span class="hljs-string">"\t"</span>); 
        <span class="hljs-comment">// 替换'为\r ，最后一步会重新替换回来 </span>
        <span class="hljs-comment">// 节点属性操作赋值使用单引号，如果不替换 ,''>' 是会报错的</span>
        <span class="hljs-comment">// <div style='background:<%=color%>'><%=id%></div>   ==> p.push(' <div style='background:',color,''>',id,'</div>        ');            </span>
        str = str.replace(<span class="hljs-regexp">/((^|%>)[^\t]*)'/g</span>, <span class="hljs-string">"$1\r"</span>);
        <span class="hljs-comment">// 赋值解析：赋值后部分，拆分为三项，结合with，id就会成为实际的值，然后一直被push  <div id="\t=id%>"> ==>    <div id=" ,id, "></span>
        <span class="hljs-comment">// 这里会消费掉 <%=xxx%>，</span>
        <span class="hljs-comment">// 那么剩下的 %>必然是js语句结尾的, \t必然是js语句的开头</span>
        str = str.replace(<span class="hljs-regexp">/\t=(.*?)%>/g</span>, <span class="hljs-string">"',$1,'"</span>);   
        <span class="hljs-comment">//js语句开始符号替换： 经过上一步后，还剩余的\t，是js语句的，这里就用 ');来结束 ，js语句会单开p.push, </span>
        str = str.split(<span class="hljs-string">"\t"</span>).join(<span class="hljs-string">"');"</span>);        
        <span class="hljs-comment">// js语句结尾符号替换： %> 替换为 p.push, 这里把js语句内生成的字符串或者变量再push一次</span>
        str = str.split(<span class="hljs-string">"%>"</span>).join(<span class="hljs-string">"p.push('"</span>);
        <span class="hljs-comment">// 替换回车为\' ， 恢复str.replace(/((^|%>)[^\t]*)'/g, "$1\r") 去掉的'  </span>
        str = str.split(<span class="hljs-string">"\r"</span>).join(<span class="hljs-string">"\\'"</span>);  
        
        <span class="hljs-keyword">return</span> str;
    &#125;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面很有意思的是，先完全替换了\r\t，然后再用\r\t作为占位符。
\t作为<%的占位符，\r作为特定条件下'的占位符。</p>
<h3 data-id="heading-6">逐步分析</h3>
<p>我们接下来按照正则替换一步异步来分析</p>
<h4 data-id="heading-7">模板源码</h4>
<pre><code class="hljs language-js copyable" lang="js">    <% <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++ ) &#123; %>    
        <% <span class="hljs-keyword">if</span>( i%<span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;%>
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span><%=items[i].id%>:<%=items[i].name%><span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
        <% &#125; %> 
    <% &#125; %>
    <% print(<span class="hljs-string">'数组长度'</span> + items.length ); %>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">'background:<%=color%>'</span>></span><%=id%><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">第零步:等于源码,只是把\n显示出来</h4>
<pre><code class="hljs language-js copyable" lang="js">         \n
    <% <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++ ) &#123; %>    \n
        <% <span class="hljs-keyword">if</span>( i%<span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;%>\n
            <li><%=items[i].id%>:<%=items[i].name%></li>\n            
        <% &#125; %> \n
    <% &#125; %>\n
    <% print(<span class="hljs-string">'数组长度'</span> + items.length ); %>\n
    <div style=<span class="hljs-string">'background:<%=color%>'</span>><%=id%></div>\n   
 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">第一步: replace(/[\r\t\n]/g, " ")</h4>
<p>去掉回车，换行，制表</p>
<pre><code class="hljs language-js copyable" lang="js">    <% <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++ ) &#123; %>                 
        <% <span class="hljs-keyword">if</span>( i%<span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;%>                 
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span><%=items[i].id%>:<%=items[i].name%><span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>             
        <% &#125; %>          
    <% &#125; %>         
    <% print(<span class="hljs-string">'数组长度'</span> + items.length ); %>         
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">'background:<%=color%>'</span>></span><%=id%><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>  
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">第二步: split("<%").join("\t")</h4>
<p><%替换为\t</p>
<pre><code class="hljs language-js copyable" lang="js">    \t <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++ ) &#123; %>                 
        \t <span class="hljs-keyword">if</span>( i%<span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;%>                 
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>\t=items[i].id%>:\t=items[i].name%><span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>             
        \t &#125; %>          
    \t &#125; %>         
    \t print(<span class="hljs-string">'数组长度'</span> + items.length ); %>         
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">'background:\t=color%>'</span>></span>\t=id%><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">第三步: replace(/((^|%>)[^\t]*)'/g, "$1\r")</h4>
<p>替换需要保留的'为\r, 主要是节点属性操作</p>
<pre><code class="hljs language-js copyable" lang="js">    \t <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++ ) &#123; %>                 
        \t <span class="hljs-keyword">if</span>( i%<span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;%>                 
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>\t=items[i].id%>:\t=items[i].name%><span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>             
        \t &#125; %>          
    \t &#125; %>         
    \t print(<span class="hljs-string">'数组长度'</span> + items.length ); %>         
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">\rbackground:\t</span>=<span class="hljs-string">color%</span>></span>\r>\t=id%><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">第四步: replace(/\t=(.*?)%>/g, "',$1,'")</h4>
<p>赋值部分替换，',$1,',实际是把赋值部分独立出来，那么push到这里的时候，就会进行运算</p>
<pre><code class="hljs language-js copyable" lang="js">    \t <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++ ) &#123; %>                 
        \t <span class="hljs-keyword">if</span>( i%<span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;%>                 
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>',items[i].id,':',items[i].name,'<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>             
        \t &#125; %>          
    \t &#125; %>         
    \t print(<span class="hljs-string">'数组长度'</span> + items.length ); %>         
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">\rbackground:</span>',<span class="hljs-attr">color</span>,'\<span class="hljs-attr">r</span>></span>',id,'<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>  
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">第五步: split("\t").join("');")</h4>
<p>剩下的\t，代表了js语句开始部分， js语句\t替换为'); ，正是push的结束部分，正好完成push语句</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-string">'); for ( var i = 0; i < items.length; i++ ) &#123; %>                 
        '</span>); <span class="hljs-keyword">if</span>( i%<span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;%>                 
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>',items[i].id,':',items[i].name,'<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>              
        <span class="hljs-string">');&#125; %>          
    '</span>); &#125; %>         
    <span class="hljs-string">'); print('</span>数组长度<span class="hljs-string">' + items.length ); %>         
    <div style=\rbackground:'</span>,color,<span class="hljs-string">'\r>'</span>,id,<span class="hljs-string">'</div>    
 
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">第六步: split("%>").join("p.push('");</h4>
<p>剩下的%>体表了js语句的结束，替换为p.push('"，开启新的环节</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-string">'); for ( var i = 0; i < items.length; i++ ) &#123; p.push('</span>                 
        <span class="hljs-string">'); if( i%2 == 0) &#123;p.push('</span>                 
            <li><span class="hljs-string">',items[i].id,'</span>:<span class="hljs-string">',items[i].name,'</span></li>             
        <span class="hljs-string">'); &#125; p.push('</span>          
    <span class="hljs-string">'); &#125; p.push('</span>         
    <span class="hljs-string">'); print('</span>数组长度<span class="hljs-string">' + items.length ); p.push('</span>         
    <div style=\rbackground:<span class="hljs-string">',color,'</span>\r><span class="hljs-string">',id,'</span></div>  
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">第七部： split("\r").join("\'")</h4>
<p>替换\r为' ， 恢复str.replace(/((^|%>)[^\t]*)'/g, "$1\r") 去掉的'</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-string">'); for ( var i = 0; i < items.length; i++ ) &#123; p.push('</span>
        <span class="hljs-string">'); if( i%2 == 0) &#123;p.push('</span>                 
            <li><span class="hljs-string">',items[i].id,'</span>:<span class="hljs-string">',items[i].name,'</span></li>             
        <span class="hljs-string">'); &#125; p.push('</span>          
    <span class="hljs-string">'); &#125; p.push('</span>         
    <span class="hljs-string">'); print('</span>数组长度<span class="hljs-string">' + items.length ); p.push('</span>         
    <div style=\<span class="hljs-string">'background:'</span>,color,<span class="hljs-string">'\'>'</span>,id,<span class="hljs-string">'</div>    
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">加上头尾</h4>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">var</span> p=[],print=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;p.push.apply(p,<span class="hljs-built_in">arguments</span>);&#125;;<span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params">obj</span>)</span>&#123;p.push(<span class="hljs-string">'
    '</span>); <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++ ) &#123; p.push(<span class="hljs-string">'
        '</span>); <span class="hljs-keyword">if</span>( i%<span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;p.push(<span class="hljs-string">'                 
            <li>'</span>,items[i].id,<span class="hljs-string">':'</span>,items[i].name,<span class="hljs-string">'</li>             
        '</span>); &#125; p.push(<span class="hljs-string">'          
    '</span>); &#125; p.push(<span class="hljs-string">'         
    '</span>); print(<span class="hljs-string">'数组长度'</span> + items.length ); p.push(<span class="hljs-string">'         
    <div style=\'background:'</span>,color,<span class="hljs-string">'\'>'</span>,id,<span class="hljs-string">'</div>  
    '</span>);&#125;<span class="hljs-keyword">return</span> p.join(<span class="hljs-string">''</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后格式化一下</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">var</span> p = [], print = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; p.push.apply(p, <span class="hljs-built_in">arguments</span>); &#125;; <span class="hljs-keyword">with</span> (obj) &#123;
        p.push(<span class="hljs-string">'    '</span>); <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++) &#123;
            p.push(<span class="hljs-string">'        '</span>); <span class="hljs-keyword">if</span> (i % <span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;
                p.push(<span class="hljs-string">'            < li > '</span>, items[i].id, <span class="hljs-string">': '</span>, items[i].name, <span class="hljs-string">'</li >            '</span>);
            &#125;
            p.push(<span class="hljs-string">'      '</span>);
        &#125;
        p.push(<span class="hljs-string">'      '</span>);
        print(<span class="hljs-string">'数组长度'</span> + items.length); p.push(<span class="hljs-string">'                    < div style =\'background:'</span>, color, <span class="hljs-string">'\'>'</span>, id, <span class="hljs-string">'</div>      '</span>);
    &#125;
    <span class="hljs-keyword">return</span> p.join(<span class="hljs-string">''</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">split + join VS replace</h4>
<p>源码中你会发现，时而replace,时而split + join，大家都很清楚的可以看出
split + join达到的效果是和replace完全一致的。说到这里，大家肯定都很明白了，<strong>效率</strong><br>
我简单做了个实验，源码如下，<strong>自行替换str的值，然后贴到控制台执行</strong>，我测试的内容是打开百度，
查看源码，把所有源码赋值过来，然后执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> str = <span class="hljs-string">`
    blabla......................................
`</span> + <span class="hljs-built_in">Math</span>.random();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'str length:'</span> + str.length) 
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a count:'</span> + str.match(<span class="hljs-regexp">/a/g</span>).length)

<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'split-join-a'</span>)
str.split(<span class="hljs-string">'a'</span>).join(<span class="hljs-string">'_a_'</span>)
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'split-join-a'</span>)

<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'replace-a'</span>)
str.replace(<span class="hljs-regexp">/a/g</span>,<span class="hljs-string">'_a_'</span>)
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'replace-a'</span>)


<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'window count:'</span> + str.match(<span class="hljs-regexp">/window/g</span>).length)
<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'split-join-window'</span>)
str.split(<span class="hljs-string">'window'</span>).join(<span class="hljs-string">'_window_'</span>)
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'split-join-window'</span>)

<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'replace-window'</span>)
str.replace(<span class="hljs-regexp">/window/g</span>,<span class="hljs-string">'_window_'</span>)
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'replace-window'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果</p>
<pre><code class="hljs language-str copyable" lang="str">a count:4364
split-join-a: 4.521240234375ms
replace-a: 13.24609375ms
window count:29
split-join-window: 0.330078125ms
replace-window: 0.297119140625ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>11万个字符，<br>
当匹配项是4000多得时候，执行时间相差比较大 ，<br>
当匹配项是29的时候，知晓效率相差并不大，很多时候，replace比split+join还快<br>
<strong>注意注意</strong>,这里都是不带正则查找，建议就是匹配项多得时候，用split +join喽</p>
<h2 data-id="heading-18">能用否</h2>
<p>这个模板如此简单，能不能担任重任。这是基于字符串模板，还有基于dom的模板，还有混合型的。
字符串模板的缺点抛开安全和性能，就是渲染后和页面分离了，要想再操作，就需要自己再去定制了。
假如是仅仅是列表展现，是相当好的。</p>
<h2 data-id="heading-19">写在最后</h2>
<p>如果你觉得不错，你的一赞一评就是我前行的最大动力。</p>
<p>技术交流群请到 <a href="https://juejin.cn/pin/6994350401550024741" title="https://juejin.cn/pin/6994350401550024741" target="_blank">这里来</a>。
或者添加我的微信 dirge-cloud，一起学习。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fblog.csdn.net%2Fyczz%2Farticle%2Fdetails%2F49585381" target="_blank" rel="nofollow noopener noreferrer" title="http://blog.csdn.net/yczz/article/details/49585381" ref="nofollow noopener noreferrer">一个对前端模板技术的全面总结</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000010456158" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000010456158" ref="nofollow noopener noreferrer">JavaScript 进阶之深入理解数据双向绑定</a><br>
<a href="https://link.juejin.cn/?target=http%3A%2F%2Fblog.csdn.net%2Fwuchengzhi82%2Farticle%2Fdetails%2F8938122" target="_blank" rel="nofollow noopener noreferrer" title="http://blog.csdn.net/wuchengzhi82/article/details/8938122" ref="nofollow noopener noreferrer">模板引擎性能对比</a><br>
<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.cnblogs.com%2FdolphinX%2Fp%2F3489269.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.cnblogs.com/dolphinX/p/3489269.html" ref="nofollow noopener noreferrer">最简单的JavaScript模板引擎</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F32524504" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/32524504" ref="nofollow noopener noreferrer">有哪些好用的前端模板引擎？</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjohnresig.com%2Fblog%2Fjavascript-micro-templating%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://johnresig.com/blog/javascript-micro-templating/" ref="nofollow noopener noreferrer">JavaScript Micro-Templating</a></p>
</blockquote></div>  
</div>
            