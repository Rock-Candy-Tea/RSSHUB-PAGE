
---
title: '手把手教你用koa写项目接口'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6877948974b84e058de5ef6e926ee43f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 23:35:17 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6877948974b84e058de5ef6e926ee43f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0"><a href="https://juejin.cn/post/6998346793574465549" target="_blank" title="https://juejin.cn/post/6998346793574465549">前一篇</a>我们封装了验证权限工具，发表动态（增删改查）</h4>
<h3 data-id="heading-1">今天我们做评论和回复评论功能</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
评论 --> 验证登录 --> 获取要评论动态的id,用户id --> 发表评论 --> 获取当前文章下面的评论的id,然后进行评论
</code></pre>
<h3 data-id="heading-2">创建对应的表<code>comment</code></h3>
<pre><code class="hljs language-mysql copyable" lang="mysql"><span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> <span class="hljs-keyword">IF</span> <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">EXISTS</span> <span class="hljs-string">`comment`</span>(
<span class="hljs-keyword">id</span> <span class="hljs-built_in">INT</span> PRIMARY <span class="hljs-keyword">KEY</span> AUTO_INCREMENT,
<span class="hljs-keyword">content</span> <span class="hljs-built_in">VARCHAR</span>(<span class="hljs-number">1000</span>) <span class="hljs-keyword">NOT</span> <span class="hljs-literal">NULL</span>,
moment_id <span class="hljs-built_in">INT</span> <span class="hljs-keyword">NOT</span> <span class="hljs-literal">NULL</span>,   //文章<span class="hljs-keyword">id</span>
user_id <span class="hljs-built_in">INT</span> <span class="hljs-keyword">NOT</span> <span class="hljs-literal">NULL</span>,     //用户<span class="hljs-keyword">id</span>
comment_id <span class="hljs-built_in">INT</span> <span class="hljs-keyword">DEFAULT</span> <span class="hljs-literal">NULL</span>,  //回复的<span class="hljs-keyword">id</span>
createAt <span class="hljs-built_in">TIMESTAMP</span> <span class="hljs-keyword">DEFAULT</span> <span class="hljs-keyword">CURRENT_TIMESTAMP</span>,
updateAt <span class="hljs-built_in">TIMESTAMP</span> <span class="hljs-keyword">DEFAULT</span> <span class="hljs-keyword">CURRENT_TIMESTAMP</span> <span class="hljs-keyword">ON</span> <span class="hljs-keyword">UPDATE</span> <span class="hljs-keyword">CURRENT_TIMESTAMP</span>,

<span class="hljs-keyword">FOREIGN</span> <span class="hljs-keyword">KEY</span>(moment_id) <span class="hljs-keyword">REFERENCES</span> moment(<span class="hljs-keyword">id</span>) <span class="hljs-keyword">ON</span> <span class="hljs-keyword">DELETE</span> <span class="hljs-keyword">CASCADE</span> <span class="hljs-keyword">ON</span> <span class="hljs-keyword">UPDATE</span> <span class="hljs-keyword">CASCADE</span>,
<span class="hljs-keyword">FOREIGN</span> <span class="hljs-keyword">KEY</span>(user_id) <span class="hljs-keyword">REFERENCES</span> <span class="hljs-keyword">user</span>(<span class="hljs-keyword">id</span>) <span class="hljs-keyword">ON</span> <span class="hljs-keyword">DELETE</span> <span class="hljs-keyword">CASCADE</span> <span class="hljs-keyword">ON</span> <span class="hljs-keyword">UPDATE</span> <span class="hljs-keyword">CASCADE</span>,
<span class="hljs-keyword">FOREIGN</span> <span class="hljs-keyword">KEY</span>(comment_id) <span class="hljs-keyword">REFERENCES</span> <span class="hljs-keyword">comment</span>(<span class="hljs-keyword">id</span>) <span class="hljs-keyword">ON</span> <span class="hljs-keyword">DELETE</span> <span class="hljs-keyword">CASCADE</span> <span class="hljs-keyword">ON</span> <span class="hljs-keyword">UPDATE</span> <span class="hljs-keyword">CASCADE</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">发表评论</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa-router"</span>);

<span class="hljs-keyword">const</span> commnetRouter = <span class="hljs-keyword">new</span> Router(&#123; <span class="hljs-attr">prefix</span>: <span class="hljs-string">"/commnet"</span> &#125;);

<span class="hljs-keyword">const</span> &#123; 
    verifyAuth,       <span class="hljs-comment">//判断是否登录</span>
    verifyPermission  <span class="hljs-comment">//验证权限</span>
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../middleware/auth.middleware"</span>);

<span class="hljs-keyword">const</span> &#123;
    create
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../controller/comment.controller.js"</span>);

commnetRouter.post(<span class="hljs-string">"/"</span>, verifyAuth(comment), create);    <span class="hljs-comment">//发表评论</span>

<span class="hljs-built_in">module</span>.exports = commnetRouter;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">要获取到评论的内容，用户的id，评论动态的id</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.controller.js</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentController</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; momentId, content &#125; = ctx.request.body;
    <span class="hljs-keyword">const</span> &#123; id &#125; = ctx.user;

    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> service.create(momentId, content, id);

    ctx.body = result;
  &#125;
  
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentController();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">将获取到评论的内容，用户的id，评论动态的id，传入到数据库中</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentService</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">commentId, content, userId</span>)</span> &#123;
    <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`INSERT INTO comment (content, moment_id, user_id) VALUES (?, ?, ?)`</span>;

    <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [
      content,
      commentId,
      userId,
    ]);

    <span class="hljs-keyword">return</span> result;
  &#125;

&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">测试</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6877948974b84e058de5ef6e926ee43f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">获取评论</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa-router"</span>);

<span class="hljs-keyword">const</span> commnetRouter = <span class="hljs-keyword">new</span> Router(&#123; <span class="hljs-attr">prefix</span>: <span class="hljs-string">"/commnet"</span> &#125;);

<span class="hljs-keyword">const</span> &#123;
    list
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../controller/comment.controller.js"</span>);

commentRouter.get(<span class="hljs-string">"/"</span>, list)    <span class="hljs-comment">//获取评论</span>

<span class="hljs-built_in">module</span>.exports = commnetRouter;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">要获取文章的id</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.controller.js</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentController</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">list</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; commentId &#125; = ctx.query;
    
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> service.getCommentsByMomentId(commentId);

    ctx.body = result;
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentController();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">将获取到文章id，传入到数据库，进行查询</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentService</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getCommentsByMomentId</span>(<span class="hljs-params">commentId</span>)</span> &#123;
    <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`
    SELECT 
      m.id, m.content, m.comment_id commentId, m.createAt createTime,
      JSON_OBJECT('id', u.id, 'name', u.name) user
    FROM comment m
    LEFT JOIN user u ON u.id = m.user_id   //这里要连接用户表，查询是那些用户发表了评论
    WHERE moment_id = ?
    `</span>;

    <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [commentId]);

    <span class="hljs-keyword">return</span> result;
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">测试</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df50e1b23eeb4d43aeda574dee1bc016~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">回复评论</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa-router"</span>);

<span class="hljs-keyword">const</span> commnetRouter = <span class="hljs-keyword">new</span> Router(&#123; <span class="hljs-attr">prefix</span>: <span class="hljs-string">"/commnet"</span> &#125;);

<span class="hljs-keyword">const</span> &#123; 
    verifyAuth,       <span class="hljs-comment">//判断是否登录</span>
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../middleware/auth.middleware"</span>);

<span class="hljs-keyword">const</span> &#123;
    reply
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../controller/comment.controller.js"</span>);

commentRouter.post(<span class="hljs-string">'/:commentId/reply'</span>, verifyAuth, reply)    <span class="hljs-comment">//回复评论</span>

<span class="hljs-built_in">module</span>.exports = commnetRouter;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">获取评论文章id,用户id,回复评论内容,要回复的评论的id</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.controller.js</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentController</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">reply</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; momentId, content &#125; = ctx.request.body;
    <span class="hljs-keyword">const</span> &#123; commentId &#125; = ctx.params;
    <span class="hljs-keyword">const</span> &#123; id &#125; = ctx.user;

    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> service.reply(momentId, content, id, commentId);

    ctx.body = result;
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentController();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">将获取评论文章id,用户id,回复评论内容,要回复的评论的id，传入到数据库，进行查询</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentService</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">reply</span>(<span class="hljs-params">momentId, content, userId, commentId</span>)</span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`
      INSERT INTO comment (content, moment_id, user_id, comment_id) VALUES (?, ?, ?, ?)
      `</span>;

      <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [content,commentId,userId,momentId]);

      <span class="hljs-keyword">return</span> result;
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">console</span>.log(error);
    &#125;
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">测试</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd18704b58d7401ab1d0b083f320f7fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">修改评论</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa-router"</span>);

<span class="hljs-keyword">const</span> commnetRouter = <span class="hljs-keyword">new</span> Router(&#123; <span class="hljs-attr">prefix</span>: <span class="hljs-string">"/commnet"</span> &#125;);

<span class="hljs-keyword">const</span> &#123; 
    verifyAuth,       <span class="hljs-comment">//判断是否登录</span>
    verifyPermission  <span class="hljs-comment">//验证权限</span>
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../middleware/auth.middleware"</span>);

<span class="hljs-keyword">const</span> &#123;
    update
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../controller/comment.controller.js"</span>);

commentRouter.patch(<span class="hljs-string">'/:commentId'</span>,verifyAuth,verifyPermission(comment), update)    <span class="hljs-comment">//修改评论</span>

<span class="hljs-built_in">module</span>.exports = commnetRouter;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">获取修改内容，评论id</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.controller.js</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentController</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; commentId &#125; = ctx.params;
    <span class="hljs-keyword">const</span> &#123; content &#125; = ctx.request.body;

    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> service.update(commentId, content);

    ctx.body = result;
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentController();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">将数据传入到数据库，并修改</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentService</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">commentId, content</span>)</span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`UPDATE comment SET content = ? WHERE id = ?`</span>;
      <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [
        content,
        commentId,
      ]);

      <span class="hljs-keyword">return</span> result;
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      <span class="hljs-built_in">console</span>.log(err);
    &#125;
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">测试</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e3594fca0ca447fb8914c339cea3297~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">删除评论</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa-router"</span>);

<span class="hljs-keyword">const</span> commnetRouter = <span class="hljs-keyword">new</span> Router(&#123; <span class="hljs-attr">prefix</span>: <span class="hljs-string">"/commnet"</span> &#125;);

<span class="hljs-keyword">const</span> &#123; 
    verifyAuth,       <span class="hljs-comment">//判断是否登录</span>
    verifyPermission  <span class="hljs-comment">//验证权限</span>
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../middleware/auth.middleware"</span>);

<span class="hljs-keyword">const</span> &#123;
    remove
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../controller/comment.controller.js"</span>);

commentRouter.delete(<span class="hljs-string">"/:commentId"</span>,verifyAuth,verifyPermission, remove )    <span class="hljs-comment">//删除评论</span>

<span class="hljs-built_in">module</span>.exports = commnetRouter;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">获取要删除的评论id</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.controller.js</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentController</span> </span>&#123;
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; commentId &#125; = ctx.params;

    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> service.remove(commentId);

    ctx.body = result;
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentController();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">将数据传入到数据库，并修改</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//comment.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentService</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">commentId</span>)</span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`DELETE FROM comment WHERE id = ?`</span>
      <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [commentId])
      <span class="hljs-keyword">return</span> result

    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">console</span>.log(error);
    &#125;
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> CommentService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">测试</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd4f5f9130e1472ab46d494e320f190e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">写接口的的流程</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
创建路由 --> 验证中间件 --> 拿到数据进行处理 --> 传入数据库 --> 将结果返回给 --> 拿到最后的结果,然后返回给前端
</code></pre>
<h3 data-id="heading-24"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fhjx2004%2Fkoa" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/hjx2004/koa" ref="nofollow noopener noreferrer">项目地址</a></h3></div>  
</div>
            