
---
title: '.Net 设计模式进阶之路——代理模式_Proxy_'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce1096e009a41b591eea9f265c8cc3c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 06:07:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce1096e009a41b591eea9f265c8cc3c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第9天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 01.代理模式</h1>
<p><strong>意图：</strong> 把用户无法访问的对象代理出去，使得你可以间接访问对象。</p>
<p>形象的说：就如同给你的浏览器增加加个代理，然后，你就可以翻越长江长城，直接看到外面的世界了。</p>
<p><strong>友好提醒：vpn有罪！</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce1096e009a41b591eea9f265c8cc3c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>问题领域：</strong> 跳过障碍，加点东东。</p>
<ul>
<li>封装三方类库，并加点东东，</li>
<li>增加保护控制，</li>
<li>过滤请求，</li>
<li>为了资源、链接保护，封装原生类</li>
<li>产品仅提供接口，而非具体的类</li>
</ul>
<p><strong>解决方案</strong>： 我们使用UML图来描述它。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a00f43867fc4ab59bddf3f61f28239e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Proxy类有个BehindClass的实例成员，因此其可以直接访问BehindClass类中的所有公开方法，通过包装这些方法形成可被其他类调用的接口。</p>
<p>Client就是一个使用者，其内部可以实例化 Proxy类，并调用方法Request达到和调用 BehindClass的Request一样的效果，当然在Proxy类中，可以增加额外的权限安全判断，或引用计数等，以达到对BehindClass方法调用的控制。</p>
<p><strong>效果：</strong></p>
<ul>
<li>好处：</li>
</ul>
<ol>
<li>隐藏BehindClass的直接调用；</li>
<li>开放对BehindClass的功能调用；</li>
<li>可以方便的增加权限、引用计数等相关的控制；</li>
<li>可以延迟加载重量级的资源；</li>
</ol>
<ul>
<li>限定:</li>
</ul>
<ol>
<li>如果BehindClass类接口众多，对Proxy来说，需要敲更多的类似代码。</li>
</ol>
<h1 data-id="heading-1">🎏 02. dotnet core 源码赏析</h1>
<p>在 <code>aspnet Core</code>源代码内有一个动态客户端的代理`DynamicClientProxy，采用了代理模式。</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">internal</span> <span class="hljs-keyword">class</span> <span class="hljs-title">DynamicClientProxy</span> : <span class="hljs-title">DynamicObject</span>
    &#123;
        <span class="hljs-keyword">private</span> <span class="hljs-keyword">readonly</span> IClientProxy _clientProxy;

        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">DynamicClientProxy</span>(<span class="hljs-params">IClientProxy clientProxy</span>)</span>
        &#123;
            _clientProxy = clientProxy;
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> <span class="hljs-built_in">bool</span> <span class="hljs-title">TryInvokeMember</span>(<span class="hljs-params">InvokeMemberBinder binder, <span class="hljs-built_in">object</span>?[]? args, <span class="hljs-keyword">out</span> <span class="hljs-built_in">object</span>? result</span>)</span>
        &#123;
            result = _clientProxy.SendCoreAsync(binder.Name, args!);
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代理模式超级简单吧，几乎不做什么事情，直接转发请求即可。</p>
<p>这里TryInvokeMember方法就是直接调用_clientProxy的SendCoreAsync方法完成对真实对象的方法调用代理。</p>
<h1 data-id="heading-2">🎏 03. dotnet 代理类实现</h1>
<p>这是一个例子，我们来实现一个抽象工厂，接口定义如下：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">internal</span> <span class="hljs-keyword">class</span> <span class="hljs-title">BehindResource</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">PerformRWOperations</span>(<span class="hljs-params"></span>)</span>

    &#123;

    Console.WriteLine(<span class="hljs-string">"Performing Read Write operation on the Shared Folder"</span>);

    &#125;
&#125;
<span class="hljs-keyword">class</span> <span class="hljs-title">ResourceProxy</span> 
    &#123;
        <span class="hljs-keyword">private</span> BehindResource folder;
        <span class="hljs-keyword">private</span> Employee employee;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">ResourceProxy</span>(<span class="hljs-params">Employee emp</span>)</span>
        &#123;
            employee = emp;
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">PerformRWOperations</span>(<span class="hljs-params"></span>)</span>
        &#123;
            <span class="hljs-keyword">if</span> (employee.Role.ToUpper() == <span class="hljs-string">"CEO"</span> || employee.Role.ToUpper() ==<span class="hljs-string">"MANAGER"</span>)
            &#123;
                folder = <span class="hljs-keyword">new</span> BehindResource();
                Console.WriteLine(<span class="hljs-string">"Shared Folder Proxy makes call to the RealFolder 'PerformRWOperations method'"</span>);
                folder.PerformRWOperations();
            &#125;
            <span class="hljs-keyword">else</span>
            &#123;
                Console.WriteLine(<span class="hljs-string">"Shared Folder proxy says 'You don't have permission to access this folder'"</span>);
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里对能访问资源的雇员进行了限制，只有符合条件的雇员才可以访问到后台资源，其他雇员我们不允许它访问资源。</p>
<p>调用方，可以按照下列方式直接使用。</p>
<pre><code class="copyable">Console.WriteLine("Client passing employee with Role Developer to folderproxy");

Employee emp1 = new Employee("Anurag", "Anurag123", "Developer");

ResourceProxy proxy1 = new ResourceProxy(emp1);

proxy1.PerformRWOperations();

Console.WriteLine();

Console.WriteLine("Client passing employee with Role Manager to proxy");

<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，通过上述的代理类，我们为后台资源增加了安全访问权限，对于客户端来说，它无法直接访问后后台资源，它只能通过我们提供的代理类访问后台资源，这样我们可以轻松控制资源了。</p>
<p>有类似需求的，均可以按照代理模式来解决。</p>
<h1 data-id="heading-3">🎏 04. 小结</h1>
<p>如果我们有添加对现有对象的安全访问、简化复杂对象的 API、为远程资源提供接口、在不更改现有类代码的情况下向现有类添加线程安全功能等类似的业务设计时，可以考虑是否可以利用设计模式中的代码模式了。</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            