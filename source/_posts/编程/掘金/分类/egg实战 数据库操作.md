
---
title: 'egg实战 数据库操作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c373337c8794667bc8914ae1790ad0d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 23:57:08 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c373337c8794667bc8914ae1790ad0d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先写个简单的增删改查，在service中创建个user.js文件，添加查询信息和插入信息的代码</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c373337c8794667bc8914ae1790ad0d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>调用queryUserName方法时返回了个空对象，ok没问题</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/451a144a2879440f885b850c48df707f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>调用 insertUser方法时报错了，提示是没有jacktest.user这个表，ok，那我们新建个表，百度一番之后,发现是需要先在mysql中建一个表</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">create</span> <span class="hljs-keyword">table</span> users(
  user_id <span class="hljs-type">int</span>(<span class="hljs-number">10</span>) unsigned <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">NULL</span> auto_increment,
  username <span class="hljs-type">varchar</span>(<span class="hljs-number">30</span>),
  password <span class="hljs-type">varchar</span>(<span class="hljs-number">30</span>),
  created_at <span class="hljs-type">timestamp</span>,
  <span class="hljs-keyword">primary</span> key (user_id)
)engine<span class="hljs-operator">=</span>InnoDB AUTO_INCREMENT<span class="hljs-operator">=</span><span class="hljs-number">1</span> comment <span class="hljs-string">'用户表'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们再运行代码，成功。
然后对代码进行简单的修改，登录注册的逻辑就通了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 登录逻辑</span>
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">login</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> body = <span class="hljs-built_in">this</span>.ctx.request.body;
    <span class="hljs-keyword">const</span> &#123; username, password &#125; = body;
    <span class="hljs-keyword">const</span> &#123; user &#125; = <span class="hljs-built_in">this</span>.ctx.service;
    <span class="hljs-keyword">let</span> postBody = &#123;
      <span class="hljs-attr">code</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">msg</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">data</span>: &#123;&#125;,
    &#125;;
    <span class="hljs-comment">// 先判断是否已存在</span>
    <span class="hljs-keyword">const</span> userData = <span class="hljs-keyword">await</span> user.queryUserName(username);
    <span class="hljs-keyword">if</span> (userData && <span class="hljs-built_in">Object</span>.keys(userData).length) &#123; <span class="hljs-comment">// 已存在</span>
      <span class="hljs-keyword">if</span> (password === userData.password) &#123;
        postBody = &#123;
          ...postBody,
          <span class="hljs-attr">code</span>: <span class="hljs-number">1</span>,
          <span class="hljs-attr">msg</span>: <span class="hljs-string">'登录成功'</span>,
          <span class="hljs-attr">data</span>: &#123; userData &#125;,
        &#125;;
        <span class="hljs-built_in">this</span>.ctx.cookies.set(<span class="hljs-string">'token'</span>, userData.user_id);
      &#125; <span class="hljs-keyword">else</span> &#123;
        postBody.msg = <span class="hljs-string">'账号或密码错误'</span>;
        postBody.code = <span class="hljs-number">0</span>;
      &#125;
      <span class="hljs-comment">// 判断密码是否正确</span>
      <span class="hljs-built_in">this</span>.ctx.body = postBody;
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-built_in">this</span>.ctx.body = &#123;
      ...postBody,
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'用户不存在'</span>,
    &#125;;
  &#125;
  <span class="hljs-comment">// 注册逻辑</span>
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">register</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> body = <span class="hljs-built_in">this</span>.ctx.request.body;
    <span class="hljs-keyword">const</span> &#123; username, password &#125; = body;
    <span class="hljs-keyword">const</span> &#123; user &#125; = <span class="hljs-built_in">this</span>.ctx.service;
    <span class="hljs-keyword">const</span> postBody = &#123;
      <span class="hljs-attr">code</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">msg</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">data</span>: &#123;&#125;,
    &#125;;
    <span class="hljs-comment">// 先判断是否已存在</span>
    <span class="hljs-keyword">const</span> userIsExists = <span class="hljs-keyword">await</span> user.queryUserName(username);
    <span class="hljs-keyword">if</span> (userIsExists && <span class="hljs-built_in">Object</span>.keys(userIsExists).length) &#123; <span class="hljs-comment">// 已存在</span>
      <span class="hljs-built_in">this</span>.ctx.body = &#123;
        ...postBody,
        <span class="hljs-attr">msg</span>: <span class="hljs-string">'用户已存在'</span>,
      &#125;;
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-comment">// 创建用户</span>
    <span class="hljs-keyword">const</span> newUser = <span class="hljs-keyword">await</span> user.insertUser(&#123; username, password &#125;);
    <span class="hljs-keyword">if</span> (newUser.affectedRows === <span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">const</span> userData = <span class="hljs-keyword">await</span> user.queryUserName(username);
      postBody.data = &#123;
        userData,
      &#125;;
    &#125;

    <span class="hljs-built_in">this</span>.ctx.body = &#123;
      ...postBody,
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'注册成功'</span>,
    &#125;;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            