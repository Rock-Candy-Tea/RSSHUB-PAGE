
---
title: 'koa接口，项目结尾'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06d5205fff044a18949fb3d662a6d8e1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 17:43:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06d5205fff044a18949fb3d662a6d8e1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0"><a href="https://juejin.cn/post/6998781892849991717" target="_blank" title="https://juejin.cn/post/6998781892849991717">上一篇文章</a>完成了评论，回复评论，查询评论，删除评论</h4>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 完成创建标签，</li>
<li class="task-list-item"><input type="checkbox" disabled> 给动态分配标签</li>
<li class="task-list-item"><input type="checkbox" disabled> 上传用户头像</li>
<li class="task-list-item"><input type="checkbox" disabled> 上传动态配图</li>
</ul>
<h3 data-id="heading-1">创建标签表，用于多表查询</h3>
<pre><code class="hljs language-mysql copyable" lang="mysql"><span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> <span class="hljs-keyword">IF</span> <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">EXISTS</span> <span class="hljs-string">`label`</span>(
<span class="hljs-keyword">id</span> <span class="hljs-built_in">INT</span> PRIMARY <span class="hljs-keyword">KEY</span> AUTO_INCREMENT,
<span class="hljs-keyword">name</span> <span class="hljs-built_in">VARCHAR</span>(<span class="hljs-number">10</span>) <span class="hljs-keyword">NOT</span> <span class="hljs-literal">NULL</span> <span class="hljs-keyword">UNIQUE</span>,
createAt <span class="hljs-built_in">TIMESTAMP</span> <span class="hljs-keyword">DEFAULT</span> <span class="hljs-keyword">CURRENT_TIMESTAMP</span>,
updateAt <span class="hljs-built_in">TIMESTAMP</span> <span class="hljs-keyword">DEFAULT</span> <span class="hljs-keyword">CURRENT_TIMESTAMP</span> <span class="hljs-keyword">ON</span> <span class="hljs-keyword">UPDATE</span> <span class="hljs-keyword">CURRENT_TIMESTAMP</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">完成创建标签</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//label.router.js</span>

<span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-router'</span>)

<span class="hljs-keyword">const</span> labelRouter = <span class="hljs-keyword">new</span> Router(&#123;<span class="hljs-attr">prefix</span>: <span class="hljs-string">"/label"</span>&#125;)

<span class="hljs-keyword">const</span> &#123;
    verifyAuth    <span class="hljs-comment">//验证用户登录</span>
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../middleware/auth.middleware'</span>)

<span class="hljs-keyword">const</span> &#123;
    create
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../controller/label.controller'</span>)

labelRouter.post(<span class="hljs-string">'/'</span>, verifyAuth, create)

<span class="hljs-built_in">module</span>.exports = labelRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">处理数据</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//label.controller.js</span>

<span class="hljs-keyword">const</span> service = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../service/label.service.js'</span>)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">labelController</span> </span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;name&#125; = ctx.request.body

        <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> service.create(name)

        ctx.body = result
    &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> labelController()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">添加到数据库</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//label.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LabelService</span> </span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">name</span>)</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`INSERT INTO label (name) VALUES (?)`</span>;
    
          <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [name]);
    
          <span class="hljs-keyword">return</span> result;
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-built_in">console</span>.log(error);
        &#125;
      &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> LabelService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">测试</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06d5205fff044a18949fb3d662a6d8e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">给动态分配标签</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//moment.router.js</span>

<span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-router'</span>)

<span class="hljs-keyword">const</span> momentRouter = <span class="hljs-keyword">new</span> Router(&#123;<span class="hljs-attr">prefix</span>: <span class="hljs-string">'/moment'</span>&#125;)

<span class="hljs-keyword">const</span> &#123;
    verifyAuth,
    verifyPermission
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../middleware/auth.middleware'</span>)

<span class="hljs-keyword">const</span> &#123;
    addLabels
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../controller/moment.controller'</span>)

<span class="hljs-keyword">const</span> &#123;
    verifyLabelExists
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../middleware/label.middleware'</span>)

momentRouter.post(<span class="hljs-string">"/:momentId/labels"</span>, verifyAuth, verifyPermission(<span class="hljs-string">"moment"</span>), verifyLabelExists, addLabels)

<span class="hljs-built_in">module</span>.exports = momentRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">判断用户传入的标签是否存在</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// label.middleware.js</span>

<span class="hljs-keyword">const</span> service = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../service/label.service'</span>)

<span class="hljs-keyword">const</span> verifyLabelExists = <span class="hljs-keyword">async</span> (ctx, next) => &#123;
    <span class="hljs-comment">// 取出要添加的标签</span>
    <span class="hljs-keyword">const</span> &#123;labels&#125; = ctx.request.body
    <span class="hljs-built_in">console</span>.log(labels);

    <span class="hljs-comment">// 判断标签是否存在</span>
    <span class="hljs-keyword">const</span> newLabels = []
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> name <span class="hljs-keyword">of</span> labels)&#123;
        <span class="hljs-keyword">const</span> labelResult = <span class="hljs-keyword">await</span> service.getLabelByName(name)
        <span class="hljs-keyword">const</span> label = &#123;name&#125;
        <span class="hljs-keyword">if</span>(!labelResult) &#123;
            <span class="hljs-comment">// 创建标签数据</span>
            <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> service.create(name)
            label.id = result.insertId
        &#125;<span class="hljs-keyword">else</span> &#123;
            label.id = labelResult.id
        &#125;
        newLabels.push(label)
    &#125;

    ctx.labels = newLabels
    <span class="hljs-keyword">await</span> next()
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
    verifyLabelExists
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">获取到标签和动态id，传入到数据库处理文件</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//moment.controller.js</span>

<span class="hljs-keyword">const</span> momentService = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../service/moment.service"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MomentController</span> </span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">addLabels</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
        <span class="hljs-comment">// 1.获取标签和动态id</span>
        <span class="hljs-keyword">const</span> &#123; labels &#125; = ctx;
        <span class="hljs-keyword">const</span> &#123; momentId &#125; = ctx.params;

        <span class="hljs-comment">// 2.添加所有的标签</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> label <span class="hljs-keyword">of</span> labels) &#123;
          <span class="hljs-comment">// 2.1.判断标签是否已经和动态有关系</span>
          <span class="hljs-keyword">const</span> isExist = <span class="hljs-keyword">await</span> momentService.hasLabel(momentId, label.id);
          <span class="hljs-keyword">if</span> (!isExist) &#123;
            <span class="hljs-keyword">await</span> momentService.addLabel(momentId, label.id);
          &#125;
        &#125;

        ctx.body = <span class="hljs-string">"给动态添加标签成功~"</span>;
      &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> MomentController();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">拿到数据，进行处理</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//moment.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MomentService</span> </span>&#123;
    
    <span class="hljs-comment">//判断该动态是否拥有此标签</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">hasLabel</span>(<span class="hljs-params">momentId, labelId</span>)</span> &#123;
        <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`
        SELECT * FROM moment_label WHERE moment_id = ? AND label_id = ?
        `</span>;
        <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [momentId, labelId]);
        <span class="hljs-keyword">return</span> result[<span class="hljs-number">0</span>] ? <span class="hljs-literal">true</span>: <span class="hljs-literal">false</span>;
      &#125;
    <span class="hljs-comment">//给动态添加标签</span>
      <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">addLabel</span>(<span class="hljs-params">momentId, labelId</span>)</span> &#123;
        <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`INSERT INTO moment_label (moment_id, label_id) VALUES (?, ?);`</span>;
        <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [momentId, labelId]);
        <span class="hljs-keyword">return</span> result;
      &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> MomentService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">上传头像</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//file.router.js</span>

<span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-router'</span>)

<span class="hljs-keyword">const</span> filRouter = <span class="hljs-keyword">new</span> Router(&#123;<span class="hljs-attr">prefix</span>: <span class="hljs-string">'/upload'</span>&#125;)

<span class="hljs-keyword">const</span> &#123;
    verifyAuth  <span class="hljs-comment">//验证登录</span>
&#125; =<span class="hljs-built_in">require</span>(<span class="hljs-string">'../middleware/auth.middleware'</span>)

<span class="hljs-keyword">const</span> &#123;
    avatarHandler
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../middleware/file.middleware'</span>)

<span class="hljs-keyword">const</span> &#123;
    saveAvatarInfo
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../controller/file.controller'</span>)

<span class="hljs-comment">//上传头像</span>
filRouter.post(<span class="hljs-string">'/avatar'</span>, verifyAuth, avatarHandler, saveAvatarInfo)

<span class="hljs-built_in">module</span>.exports = filRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">实现<code>avatarHandler</code>中间件 <code>npm install koa-multer</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//file.middleware.js</span>

<span class="hljs-keyword">const</span> Multer = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa-multer"</span>);

<span class="hljs-keyword">const</span> avatarUpLoad = Multer(&#123;
  <span class="hljs-attr">dest</span>: <span class="hljs-string">"./uploads/avatar"</span>,   <span class="hljs-comment">//这个是将上传的图片保存到一个位置</span>
&#125;);

<span class="hljs-keyword">const</span> avatarHandler = avatarUpLoad.single(<span class="hljs-string">"avatar"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  avatarHandler
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">获取上传图片的信息，然后保存到数据库</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//file.controller.js</span>

<span class="hljs-keyword">const</span> fileService = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../service/file.service"</span>);
<span class="hljs-keyword">const</span> userService = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../service/user.service'</span>)
<span class="hljs-keyword">const</span> &#123;APP_HOST, APP_PORT&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../app/config'</span>)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FileController</span> </span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">saveAvatarInfo</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
        <span class="hljs-comment">// 获取图像信息</span>
        <span class="hljs-keyword">const</span> &#123; mimetype, filename, size &#125; = ctx.req.file;
        <span class="hljs-keyword">const</span> &#123; id &#125; = ctx.user;

        <span class="hljs-comment">// 将图像信息保持到数据库</span>
        <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> fileService.createAvatar(filename, mimetype, size, id);

        <span class="hljs-comment">// 将图片地址保存到user中</span>
        <span class="hljs-keyword">const</span> avatarUrl = <span class="hljs-string">`<span class="hljs-subst">$&#123;APP_HOST&#125;</span>:<span class="hljs-subst">$&#123;APP_PORT&#125;</span>/users/<span class="hljs-subst">$&#123;id&#125;</span>/avatar`</span>
        <span class="hljs-built_in">console</span>.log(avatarUrl);   <span class="hljs-comment">//http://localhost:8080/users/用户id/avatar</span>
        <span class="hljs-keyword">await</span> userService.updateAvatarUrlById(avatarUrl, id)

        <span class="hljs-comment">// 返回结果</span>
        ctx.body = <span class="hljs-string">"上传头像成功"</span>;
      &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> FileController();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">获取头像</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//user.router.js</span>

<span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-router'</span>)

<span class="hljs-keyword">const</span> userRouter = <span class="hljs-keyword">new</span> Router()

<span class="hljs-keyword">const</span> &#123;
    avatarInfo
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../controller/user.controller"</span>)

<span class="hljs-comment">// 获取头像</span>
userRouter.get(<span class="hljs-string">'/users/:userId/avatar'</span>, avatarInfo)

<span class="hljs-built_in">module</span>.exports = userRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">设置图像信息</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//user.controller.js</span>

<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)

<span class="hljs-keyword">const</span> userService = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../service/user.service"</span>);
<span class="hljs-keyword">const</span> fileService = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../service/file.service"</span>);
<span class="hljs-keyword">const</span> &#123; AVATAR_PATH &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../constants/file-path"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserController</span> </span>&#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">avatarInfo</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
    <span class="hljs-comment">// 获取userId</span>
    <span class="hljs-keyword">const</span> &#123; userId &#125; = ctx.params;
    <span class="hljs-comment">//查询头像</span>
    <span class="hljs-keyword">const</span> avatarInfo = <span class="hljs-keyword">await</span> fileService.getAvatarByUserId(userId);
    <span class="hljs-built_in">console</span>.log(avatarInfo); -->
                <span class="hljs-string">`BinaryRow &#123;
                  id: 1,
                  filename: '48b2d8e3740441294e57c91750f59e99',
                  mimetype: 'image/jpeg',
                  size: 98258,
                  user_id: 2,
                  createAt: 2021-08-17T08:11:53.000Z,
                  updateAt: 2021-08-17T08:11:53.000Z
                &#125;`</span>
 
    <span class="hljs-comment">// 提供图像信息</span>
    ctx.response.set(<span class="hljs-string">'content-type'</span>, avatarInfo.mimetype)  <span class="hljs-comment">//告诉浏览器，我们这个是图片</span>
    ctx.body = fs.createReadStream(<span class="hljs-string">`<span class="hljs-subst">$&#123;AVATAR_PATH&#125;</span>/<span class="hljs-subst">$&#123;avatarInfo.filename&#125;</span>`</span>);
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> UserController();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">查询头像</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//file.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FileService</span> </span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getAvatarByUserId</span>(<span class="hljs-params">userId</span>)</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">const</span> statemnet = <span class="hljs-string">`SELECT * FROM avatar WHERE user_id = ?`</span>;

          <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statemnet, [userId]);

          <span class="hljs-keyword">return</span> result[<span class="hljs-number">0</span>];
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-built_in">console</span>.log(error);
        &#125;
      &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> FileService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">上传动态配图</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//file.router.js</span>

<span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-router'</span>)

<span class="hljs-keyword">const</span> filRouter = <span class="hljs-keyword">new</span> Router(&#123;<span class="hljs-attr">prefix</span>: <span class="hljs-string">'/upload'</span>&#125;)

<span class="hljs-keyword">const</span> &#123;
    verifyAuth  <span class="hljs-comment">//验证登录</span>
&#125; =<span class="hljs-built_in">require</span>(<span class="hljs-string">'../middleware/auth.middleware'</span>)

<span class="hljs-keyword">const</span> &#123;
    pictureHandler
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../middleware/file.middleware'</span>)

<span class="hljs-keyword">const</span> &#123;
    savePictureInfo
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../controller/file.controller'</span>)

<span class="hljs-comment">//上传配图</span>
filRouter.post(<span class="hljs-string">'/picture'</span>, verifyAuth, pictureHandler, savePictureInfo)

<span class="hljs-built_in">module</span>.exports = filRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">获取上传图片</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//file.middleware.js</span>

<span class="hljs-keyword">const</span> Multer = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa-multer"</span>);

<span class="hljs-keyword">const</span> pictureUpload = Multer(&#123;
  <span class="hljs-attr">dest</span>: <span class="hljs-string">"./uploads/picture"</span>,
&#125;);

<span class="hljs-keyword">const</span> pictureHandler = pictureUpload.array(<span class="hljs-string">"picture"</span>, <span class="hljs-number">9</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  pictureHandler
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">设置图像信息</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> fileService = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../service/file.service"</span>)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FileController</span> </span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">savePictureInfo</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
        <span class="hljs-comment">// 获取信息</span>
        <span class="hljs-keyword">const</span> files = ctx.req.files
        <span class="hljs-keyword">const</span> &#123;id&#125; = ctx.user
        <span class="hljs-keyword">const</span> &#123;momentId&#125; = ctx.query

        <span class="hljs-comment">// 保存到数据库</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> file <span class="hljs-keyword">of</span> files) &#123;
          <span class="hljs-keyword">const</span> &#123;filename, mimetype, size&#125; = file

          <span class="hljs-keyword">await</span> fileService.createFile(filename, mimetype, size, id, momentId)
        &#125;

        ctx.body = <span class="hljs-string">"动态配图上传成功"</span>
      &#125;  
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> FileController();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">数据库处理动态配图</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//file.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FileService</span> </span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">createFile</span>(<span class="hljs-params">filename, mimetyep, size, userId, momentId</span>)</span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`INSERT INTO file (filename, mimetype, size, user_id, moment_id) VALUES (?, ?, ?, ?, ?)`</span>;

      <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [
        filename,
        mimetyep,
        size,
        userId,
        momentId,
      ]);

      <span class="hljs-keyword">return</span> result;
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">console</span>.log(error);
    &#125;
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> FileService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">获取动态配图</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//moment.router.js</span>

<span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-router'</span>)

<span class="hljs-keyword">const</span> momentRouter = <span class="hljs-keyword">new</span> Router(&#123;<span class="hljs-attr">prefix</span>: <span class="hljs-string">'/moment'</span>&#125;)

<span class="hljs-keyword">const</span> &#123;
    fileInfo
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../controller/moment.controller'</span>)

<span class="hljs-comment">//动态配图</span>
momentRouter.get(<span class="hljs-string">'/images/:filename'</span>, fileInfo)

<span class="hljs-built_in">module</span>.exports = momentRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

<span class="hljs-keyword">const</span> fileService = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../service/file.service"</span>);
<span class="hljs-keyword">const</span> momentService = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../service/moment.service"</span>);
<span class="hljs-keyword">const</span> &#123; PICTURE_PATH &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../constants/file-path"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MomentController</span> </span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">fileInfo</span>(<span class="hljs-params">ctx, next</span>)</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> &#123; filename &#125; = ctx.params;
          
          <span class="hljs-keyword">const</span> fileInfo = <span class="hljs-keyword">await</span> fileService.getFileByFilename(filename);
        
          ctx.response.set(<span class="hljs-string">"content-type"</span>, fileInfo.mimetype);
          
          ctx.body = fs.createReadStream(<span class="hljs-string">`./uploads/picture/<span class="hljs-subst">$&#123;filename&#125;</span>`</span>);
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-built_in">console</span>.log(error);
        &#125;
      &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> MomentController();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FileService</span> </span>&#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getFileByFilename</span>(<span class="hljs-params">filename</span>)</span> &#123;
         <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`SELECT * FROM file WHERE filename = ?`</span>

         <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [filename])

         <span class="hljs-keyword">return</span> result[<span class="hljs-number">0</span>];
      &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> FileService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">结尾，我们还需要去修改一下动态的查询，因为用户有了头像，要一起查询</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//moment.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MomentService</span> </span>&#123;
    <span class="hljs-comment">//这个的单条动态查询</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getMomentById</span>(<span class="hljs-params">id</span>)</span> &#123;
        <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`
        SELECT 
          m.id id, m.content content, m.createAt createTime, m.updateAt updateTime,
          JSON_OBJECT('id', u.id, 'name', u.name, 'avatarUrl', u.avatar_url) author,
          IF(COUNT(l.id),JSON_ARRAYAGG(
            JSON_OBJECT('id', l.id, 'name', l.name)
          ),NULL) labels,
          (SELECT IF(COUNT(c.id),JSON_ARRAYAGG(
            JSON_OBJECT('id', c.id, 'content', c.content, 'commentId', c.comment_id, 'createTime', c.createAt,
                        'user', JSON_OBJECT('id', cu.id, 'name', cu.name, 'avatarUrl', cu.avatar_url))
          ),NULL) FROM comment c LEFT JOIN user cu ON c.user_id = cu.id WHERE m.id = c.moment_id) comments,
          (SELECT JSON_ARRAYAGG(CONCAT('http://localhost:8080/moment/images/', file.filename)) 
          FROM file WHERE m.id = file.moment_id) images
        FROM moment m
        LEFT JOIN user u ON m.user_id = u.id
        LEFT JOIN moment_label ml ON m.id = ml.moment_id
        LEFT JOIN label l ON ml.label_id = l.id
        WHERE m.id = ?
        GROUP BY m.id; 
          `</span>;

        <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [id]);

        <span class="hljs-keyword">return</span> result[<span class="hljs-number">0</span>];
      &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> MomentService();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//moment.service.js</span>

<span class="hljs-keyword">const</span> connection = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../app/database"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MomentService</span> </span>&#123;
    <span class="hljs-comment">//这个的多条动态查询</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getMomentList</span>(<span class="hljs-params">offset, size</span>)</span> &#123;
    <span class="hljs-keyword">const</span> statement = <span class="hljs-string">`
    SELECT 
        m.id id, m.content content, m.createAt createTime, m.updateAt updateTime,
        JSON_OBJECT('id', u.id, 'name', u.name) author,
        (SELECT COUNT(*) FROM comment c WHERE c.moment_id = m.id) commentCount,
        (SELECT COUNT(*) FROM moment_label ml WHERE ml.moment_id = m.id) labelCount,
        (SELECT JSON_ARRAYAGG(CONCAT('http://localhost:8080/moment/images/', file.filename)) 
        FROM file WHERE m.id = file.moment_id) images
      FROM moment m
      LEFT JOIN user u ON m.user_id = u.id
      LIMIT ?, ?;
    `</span>;

    <span class="hljs-keyword">const</span> [result] = <span class="hljs-keyword">await</span> connection.execute(statement, [offset, size]);

    <span class="hljs-keyword">return</span> result;
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> MomentService();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fhjx2004%2Fkoa" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/hjx2004/koa" ref="nofollow noopener noreferrer">项目地址</a>，有兴趣的小伙伴可以去下载，自己尝试一下哦</h3></div>  
</div>
            