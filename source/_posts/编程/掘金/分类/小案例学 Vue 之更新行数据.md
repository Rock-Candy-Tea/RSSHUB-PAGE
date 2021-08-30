
---
title: '小案例学 Vue 之更新行数据'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/730714672fb34441bc33541e2c7e52a3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 01:45:29 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/730714672fb34441bc33541e2c7e52a3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<blockquote>
<p><strong>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>。恰逢掘金<code>八月更文挑战</code>，通过前几天更新的 <a href="https://juejin.cn/post/7000398131057655822" target="_blank" title="https://juejin.cn/post/7000398131057655822">小案例理解何为 Vue 组件、插槽 (juejin.cn)</a> 博文，想必大家对与 <code>component</code> 和 <code>slot</code> 有一定的了解了，今天给大伙儿分享的是通过点击列表栏功能按钮修改行数据，不仅用到了组件和插槽还结合了我这篇 <code>Blog</code> <a href="https://juejin.cn/post/6999655130597589028" target="_blank" title="https://juejin.cn/post/6999655130597589028">Vue 实现用户注册，前端正则校验以及密码强度实时显示 (juejin.cn)</a>，希望通过这个小案例帮助到正在学习 Vue 的小伙伴。加油，共勉！</p>
</blockquote>
<h2 data-id="heading-1">页面效果展示</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/730714672fb34441bc33541e2c7e52a3~tplv-k3u1fbpfcp-watermark.image" alt="动画.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">需求分析</h2>
<ol>
<li>
<p>首先，进入用户信息管理列表，就获取用户注册的所有信息数据，并通过数据表格动态渲染出来，每一个用户独占一行，并且根据用户 <code>id</code> 号给定<code>固定的序号</code>。</p>
</li>
<li>
<p>其次，表格的最后一列作为操作列，通过按下修改按钮，隐藏数据表格，将该行数据填充到可修改表单上，自动计算年龄以及渲染密码强度等级，此时，用户可以根据需要对表单中的原始数据进行修改了，修改完成后，点击确认修改完成修改操作，在成功完成修改行数据之前，必须得通过表单验证，否则提交不成功！</p>
</li>
<li>
<p>最后，可通过确认修改完成对行数据的一次更新，重新进入到用户信息管理列表，就能看到已经被修改的用户信息数据了；如若中途修改过程中不想再继续进行修改操作了，可以点击返回按钮，重回管理列表页面，再次确认修改目标，进行下一次修改。</p>
</li>
</ol>
<h2 data-id="heading-3">代码实现</h2>
<h3 data-id="heading-4">复用部分</h3>
<p>用户信息管理列表如何实现不再赘述，要想获取具体代码点击 <a href="https://juejin.cn/post/7000398131057655822" target="_blank" title="https://juejin.cn/post/7000398131057655822">这里</a>。</p>
<p>更新数据表单代码，具体可翻阅我以往的博文，可照搬 <a href="https://juejin.cn/post/6999655130597589028" target="_blank" title="https://juejin.cn/post/6999655130597589028">传送门</a>。</p>
<p>唯一不同，都是在外层套一个 <code>div</code> 并通过 <code>v-if</code> 绑定一个变量 <code>showFlag</code>，用来判断是否显示所有可供修改的用户信息。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"updUserInfoTable"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!showFlag"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">table</span>></span> &#123;...&#125; <span class="hljs-tag"></<span class="hljs-name">table</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Vue 核心代码</h3>
<h4 data-id="heading-6">数据绑定部分</h4>
<pre><code class="hljs language-JS copyable" lang="JS">data: &#123;
    <span class="hljs-attr">showFlag</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">users</span>: [],
    <span class="hljs-attr">targetUser</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>showFlag</code> => <em>是否显示所有可供修改的用户信息</em></li>
<li><code>users</code> => <em>存放用户信息的数组</em></li>
<li><code>targetUser</code> => <em>要修改的目标用户对象</em></li>
</ul>
<h4 data-id="heading-7">方法定义部分</h4>
<pre><code class="hljs language-JS copyable" lang="JS">showTargetUserInfo: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">index</span>) </span>&#123;
    <span class="hljs-comment">// 开始更新用户信息</span>
    <span class="hljs-built_in">this</span>.showFlag = <span class="hljs-literal">false</span>;
    <span class="hljs-comment">// 当前序号</span>
    <span class="hljs-keyword">var</span> num = index.valueOf();
    <span class="hljs-built_in">this</span>.targetUser = <span class="hljs-built_in">this</span>.users[num];
    <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.msg = <span class="hljs-literal">null</span>;
        <span class="hljs-comment">// 显示修改前密码安全强度</span>
        <span class="hljs-built_in">this</span>.strengthShow();
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>showTargetUserInfo()</code> 方法用于显示指定行用户信息，由于表单绑定到了 targetUser 对象属性，被赋值之后，立马显示对应属性名的属性值，完成修改表单的赋值。</p>
<p><strong>注意：</strong></p>
<ol>
<li><code>v-if</code> 切换需要等待页面的重新渲染 <code>DOM</code> 对象，否则密码安全强度效果无法正常显示，根本原因在于 <strong>vue 中的 DOM 渲染是异步的</strong>。</li>
<li>使用 <code>this.$nextTick</code> 将回调延迟到下次 <code>DOM</code> 更新循环之后执行，此时，这个问题就迎刃而解了。</li>
</ol>
<pre><code class="hljs language-JS copyable" lang="JS">checkModify: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> emptyKey = isEmptyModify();
    <span class="hljs-keyword">switch</span> (emptyKey) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'username'</span>:
            msgForUser(<span class="hljs-string">'用户名不能修改为空！'</span>, emptyKey);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'name'</span>:
            msgForUser(<span class="hljs-string">'姓名不能修改为空！'</span>, emptyKey);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'birthday'</span>:
            msgForUser(<span class="hljs-string">'出生年月不能修改为空！'</span>, emptyKey);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'mobile'</span>:
            msgForUser(<span class="hljs-string">'手机号码不能修改为空！'</span>, emptyKey);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'password'</span>:
            msgForUser(<span class="hljs-string">'密码不能修改为空！'</span>, emptyKey);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">default</span>:
            <span class="hljs-comment">// 非空验证判断完毕，对电话号码的格式的正则验证</span>
            <span class="hljs-keyword">if</span> (!(<span class="hljs-regexp">/^1([345789])\d&#123;9&#125;$/</span>.test(<span class="hljs-built_in">this</span>.targetUser.mobile))) &#123;
                <span class="hljs-built_in">this</span>.msg = <span class="hljs-string">'手机号码格式有误！'</span>;
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.targetUser.password.length < <span class="hljs-number">6</span> || <span class="hljs-built_in">this</span>.targetUser.password.length > <span class="hljs-number">16</span>) &#123;
                <span class="hljs-built_in">this</span>.msg = <span class="hljs-string">'密码长度必须在6-16位之间！'</span>
            &#125; <span class="hljs-keyword">else</span> &#123; 
                <span class="hljs-keyword">const</span> updatedUser = <span class="hljs-built_in">this</span>.targetUser;
                $.ajax(&#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-string">'POST'</span>,
                    <span class="hljs-attr">url</span>: <span class="hljs-string">'/user/updateUserInfo'</span>,
                    <span class="hljs-attr">data</span>: updatedUser,
                    <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
                        handleUpdatedMsg(data);
                    &#125;,
                    <span class="hljs-attr">error</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
                        alert(error);
                    &#125;
                &#125;);
            &#125;
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>isEmptyModify()</code> 方法判断表单是否为修改为空，是则返回对应的 <code>key</code>，结合 <code>checkModify()</code> 方法用于校验修改表单中的数据，验证不通过，根据键拿到对应表单对象，聚焦然后提醒用户修改更改内容。</p>
<p>验证通过之后，将更新用户信息请求到后端，完成更新操作。</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isEmptyModify</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> entries = <span class="hljs-built_in">Object</span>.entries(vm.targetUser);
    <span class="hljs-keyword">var</span> key = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [k, v] <span class="hljs-keyword">of</span> entries) &#123;
        <span class="hljs-keyword">if</span> (v === <span class="hljs-literal">null</span>) &#123;
            key = k;
            <span class="hljs-keyword">break</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">if</span> ((v.toString()).match(<span class="hljs-regexp">/^[ ]*$/</span>)) &#123;
                key = k;
                <span class="hljs-keyword">break</span>;
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> key;
&#125;
<span class="hljs-comment">// 进行表单判断，验证用户输入</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">msgForUser</span>(<span class="hljs-params">text, id</span>) </span>&#123;
    vm.msg = text;
    <span class="hljs-keyword">const</span> obj = $(<span class="hljs-string">`#<span class="hljs-subst">$&#123;id&#125;</span>`</span>);
    obj.focus();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成修改操作后，返回修改结果信息，通过 <code>vm.msg</code> 赋值显示该信息，在 <code>750 毫秒</code> 后返回到用户信息管理列表吗，这里仅需将 <code>vm.showFlag</code> 重置为 <code>true</code> 即可。</p>
<p>到此，这个小案例就完成实现啦！是不是很简单呢？总的来说，这个案例基于我前面两篇文章而成，如果存在不懂之处，那么就要好好看看我前文提到的两篇博文哦~</p>
<h2 data-id="heading-8">结尾</h2>
<blockquote>
<p>撰文不易，欢迎大家点赞、评论，你的关注、点赞是我坚持的不懈动力，感谢大家能够看到这里！Peace & Love。</p>
</blockquote></div>  
</div>
            