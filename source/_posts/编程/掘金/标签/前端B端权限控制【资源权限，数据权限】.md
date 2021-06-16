
---
title: '前端B端权限控制【资源权限，数据权限】'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d10f504df749426eb8166090edd0379e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 21:01:42 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d10f504df749426eb8166090edd0379e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与更文挑战的第4天，活动详情查看</strong>： <a href="https://juejin.cn/post/6967194882926444557" target="_blank"><strong>更文挑战</strong></a></p>
<p>后台管理平台内部权限大部分涉及到到两种方式：
资源权限  & 数据权限</p>
<p><strong>说明：下面的代码是react + ant design pro的例子。</strong></p>
<h1 data-id="heading-0">1. 基本介绍</h1>
<ul>
<li>资源权限：菜单导航栏 & 页面 & 按钮 资源可见权限。</li>
<li>数据权限：对于页面上的数据操作，同一个人同一个页面不同的数据可能存在不同的数据操作权限。</li>
</ul>
<p><strong>权限纬度</strong></p>
<ul>
<li>角色纬度：大部分的情况为：用户 => 角色 => 权限</li>
<li>用户纬度：用户 => 权限</li>
</ul>
<p><strong>表现形式</strong></p>
<ul>
<li>基础表现形式还是树结构的展现形式，因为对应的<strong>菜单-页面-按钮</strong>是一个树的从主干到节点的数据流向。</li>
</ul>
<br>
<h1 data-id="heading-1">2. 权限数据录入与展示</h1>
<p>采用<strong>树结构</strong>进行处理。唯一需要处理的是<strong>父子节点的联动关系</strong>处理。这里因为不同的公司或者系统可能对于这部分的数据录入方式不同，所以久不贴图了。</p>
<br>
<h1 data-id="heading-2">3.用户资源权限流程图</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d10f504df749426eb8166090edd0379e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<h1 data-id="heading-3">4 前端权限控制</h1>
<p>前端控制权限也是分为两部分，菜单页面 与 按钮。因为前端权限控制的实现，会因为后台接口形式有所影响，但是大体方向是相同。还是会分为这两块内容。<strong>这里对于权限是使用多接口查询权限，初始登录查询页面权限，点击业务页面，查询对应业务页面的资源code。</strong>
<br>
<br></p>
<h2 data-id="heading-4">4.1 菜单权限</h2>
<p>菜单权限控制需要了解两个概念：</p>
<ul>
<li>一个是可见的菜单页面          ： 左侧dom节点</li>
<li>一个是可访问的菜单页面       ： 系统当中路由这一块</li>
</ul>
<p>这里说的意思是：<strong>我们所说的菜单权限控制，大多只是停留在菜单是否可见，但是系统路由的页面可见和页面上的菜单是否可见是两回事情。假设系统路由/path1可见，尽管页面上的没有/path1对应的菜单显示。我们直接在浏览器输入对应的path1，还是可以访问到对应的页面。这是因为系统路由那一块其实我们是没有去处理的。</strong>
<strong>​</strong></p>
<p>了解了这个之后，我们需要做菜单页面权限的时候就需要去考虑两块，并且是对应的。
<br>
<br></p>
<h3 data-id="heading-5">4.1.1 路由权限 【<a href="https://github.com/rodchen-king/ant-design-pro-v2/commit/0e7895c56e4962d75ab8ccf4637cefca3f5f71b6#diff-a7acc04e8fb20252554c588f7b7a8564" target="_blank" rel="nofollow noopener noreferrer">代码地址</a>  <a href="https://github.com/rodchen-king/ant-design-pro-v2/commits/permission-branch" target="_blank" rel="nofollow noopener noreferrer">demo地址</a>】</h3>
<p>这里是有两种做法：</p>
<ul>
<li>第一种，控制路由的配置，当然不是路由配置文件里去配置。而是生效的路由配置里去做。</li>
<li>第二种，完全不做这里的路由控制，而是在路由跳转到没有权限的页面，写逻辑校验是否有当前的权限，然后手动跳转到403页面。</li>
</ul>
<p>这里还是先用第一种做法来做：因为这里用第一种做了之后，菜单可见权限自动适配好了。会省去我们很多事情。</p>
<p><strong>a. 路由文件，定义菜单页面权限。并且将exception以及404的路由添加notInAut标志，这个标志说明：这两个路由不走权限校验。同理的还有 /user。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> [
  <span class="hljs-comment">// user</span>
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-string">'../layouts/UserLayout'</span>,
    <span class="hljs-attr">routes</span>: [
      &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>, <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/user/login'</span> &#125;,
      &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/login'</span>, <span class="hljs-attr">component</span>: <span class="hljs-string">'./User/Login'</span> &#125;,
      &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/register'</span>, <span class="hljs-attr">component</span>: <span class="hljs-string">'./User/Register'</span> &#125;,
      &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/register-result'</span>, <span class="hljs-attr">component</span>: <span class="hljs-string">'./User/RegisterResult'</span> &#125;,
    ],
  &#125;,
  <span class="hljs-comment">// app</span>
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-string">'../layouts/BasicLayout'</span>,
    <span class="hljs-attr">Routes</span>: [<span class="hljs-string">'src/pages/Authorized'</span>],
    <span class="hljs-attr">authority</span>: [<span class="hljs-string">'admin'</span>, <span class="hljs-string">'user'</span>],
    <span class="hljs-attr">routes</span>: [
      <span class="hljs-comment">// dashboard</span>
      &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/list/table-list'</span> &#125;,
      <span class="hljs-comment">// forms</span>
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/form'</span>,
        <span class="hljs-attr">icon</span>: <span class="hljs-string">'form'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'form'</span>,
        <span class="hljs-attr">code</span>: <span class="hljs-string">'form_menu'</span>,
        <span class="hljs-attr">routes</span>: [
          &#123;
            <span class="hljs-attr">path</span>: <span class="hljs-string">'/form/basic-form'</span>,
            <span class="hljs-attr">code</span>: <span class="hljs-string">'form_basicForm_page'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'basicform'</span>,
            <span class="hljs-attr">component</span>: <span class="hljs-string">'./Forms/BasicForm'</span>,
          &#125;,
        ],
      &#125;,
      <span class="hljs-comment">// list</span>
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/list'</span>,
        <span class="hljs-attr">icon</span>: <span class="hljs-string">'table'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'list'</span>,
        <span class="hljs-attr">code</span>: <span class="hljs-string">'list_menu'</span>,
        <span class="hljs-attr">routes</span>: [
          &#123;
            <span class="hljs-attr">path</span>: <span class="hljs-string">'/list/table-list'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'searchtable'</span>,
            <span class="hljs-attr">code</span>: <span class="hljs-string">'list_tableList_page'</span>,
            <span class="hljs-attr">component</span>: <span class="hljs-string">'./List/TableList'</span>,
          &#125;,
        ],
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/profile'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'profile'</span>,
        <span class="hljs-attr">icon</span>: <span class="hljs-string">'profile'</span>,
        <span class="hljs-attr">code</span>: <span class="hljs-string">'profile_menu'</span>,
        <span class="hljs-attr">routes</span>: [
          <span class="hljs-comment">// profile</span>
          &#123;
            <span class="hljs-attr">path</span>: <span class="hljs-string">'/profile/basic'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'basic'</span>,
            <span class="hljs-attr">code</span>: <span class="hljs-string">'profile_basic_page'</span>,
            <span class="hljs-attr">component</span>: <span class="hljs-string">'./Profile/BasicProfile'</span>,
          &#125;,
          &#123;
            <span class="hljs-attr">path</span>: <span class="hljs-string">'/profile/advanced'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'advanced'</span>,
            <span class="hljs-attr">code</span>: <span class="hljs-string">'profile_advanced_page'</span>,
            <span class="hljs-attr">authority</span>: [<span class="hljs-string">'admin'</span>],
            <span class="hljs-attr">component</span>: <span class="hljs-string">'./Profile/AdvancedProfile'</span>,
          &#125;,
        ],
      &#125;,
      &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'exception'</span>,
        <span class="hljs-attr">icon</span>: <span class="hljs-string">'warning'</span>,
        <span class="hljs-attr">notInAut</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">hideInMenu</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/exception'</span>,
        <span class="hljs-attr">routes</span>: [
          <span class="hljs-comment">// exception</span>
          &#123;
            <span class="hljs-attr">path</span>: <span class="hljs-string">'/exception/403'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'not-permission'</span>,
            <span class="hljs-attr">component</span>: <span class="hljs-string">'./Exception/403'</span>,
          &#125;,
          &#123;
            <span class="hljs-attr">path</span>: <span class="hljs-string">'/exception/404'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'not-find'</span>,
            <span class="hljs-attr">component</span>: <span class="hljs-string">'./Exception/404'</span>,
          &#125;,
          &#123;
            <span class="hljs-attr">path</span>: <span class="hljs-string">'/exception/500'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'server-error'</span>,
            <span class="hljs-attr">component</span>: <span class="hljs-string">'./Exception/500'</span>,
          &#125;,
          &#123;
            <span class="hljs-attr">path</span>: <span class="hljs-string">'/exception/trigger'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'trigger'</span>,
            <span class="hljs-attr">hideInMenu</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">component</span>: <span class="hljs-string">'./Exception/TriggerException'</span>,
          &#125;,
        ],
      &#125;,
      &#123;
        <span class="hljs-attr">notInAut</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-string">'404'</span>,
      &#125;,
    ],
  &#125;,
];

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>b. 修改app.js 文件，加载路由</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> dva = &#123;
  <span class="hljs-attr">config</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">onError</span>(<span class="hljs-params">err</span>)</span> &#123;
      err.preventDefault();
    &#125;,
  &#125;,
&#125;;

<span class="hljs-keyword">let</span> authRoutes = <span class="hljs-literal">null</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ergodicRoutes</span>(<span class="hljs-params">routes, authKey, authority</span>) </span>&#123;
  routes.forEach(<span class="hljs-function"><span class="hljs-params">element</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (element.path === authKey) &#123;
      <span class="hljs-built_in">Object</span>.assign(element.authority, authority || []);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (element.routes) &#123;
      ergodicRoutes(element.routes, authKey, authority);
    &#125;
    <span class="hljs-keyword">return</span> element;
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">customerErgodicRoutes</span>(<span class="hljs-params">routes</span>) </span>&#123;
  <span class="hljs-keyword">const</span> menuAutArray = (<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'routerAutArray'</span>) || <span class="hljs-string">''</span>).split(<span class="hljs-string">','</span>);

  routes.forEach(<span class="hljs-function"><span class="hljs-params">element</span> =></span> &#123;
    <span class="hljs-comment">// 没有path的情况下不需要走逻辑检查</span>
    <span class="hljs-comment">// path 为 /user 不需要走逻辑检查</span>
    <span class="hljs-keyword">if</span> (element.path === <span class="hljs-string">'/user'</span> || !element.path) &#123;
      <span class="hljs-keyword">return</span> element;
    &#125;

    <span class="hljs-comment">// notInAut 为true的情况下不需要走逻辑检查</span>
    <span class="hljs-keyword">if</span> (!element.notInAut) &#123;
      <span class="hljs-keyword">if</span> (menuAutArray.indexOf(element.code) >= <span class="hljs-number">0</span> || element.path === <span class="hljs-string">'/'</span>) &#123;
        <span class="hljs-keyword">if</span> (element.routes) &#123;
          element.routes = customerErgodicRoutes(element.routes);

          element.routes = element.routes.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !item.isNeedDelete);
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        element.isNeedDelete = <span class="hljs-literal">true</span>;
      &#125;
    &#125;

    <span class="hljs-comment">/**
     * 后台接口返回子节点的情况，父节点需要溯源处理
     */</span>
    <span class="hljs-comment">// notInAut 为true的情况下不需要走逻辑检查</span>
    <span class="hljs-comment">// if (!element.notInAut) &#123;</span>
    <span class="hljs-comment">//   if (element.routes) &#123;</span>
    <span class="hljs-comment">//     // eslint-disable-next-line no-param-reassign</span>
    <span class="hljs-comment">//     element.routes = customerErgodicRoutes(element.routes);</span>

    <span class="hljs-comment">//     // eslint-disable-next-line no-param-reassign</span>
    <span class="hljs-comment">//     if (element.routes.filter(item => item.isNeedSave && !item.hideInMenu).length) &#123;</span>
    <span class="hljs-comment">//       // eslint-disable-next-line no-param-reassign</span>
    <span class="hljs-comment">//       element.routes = element.routes.filter(item => item.isNeedSave);</span>
    <span class="hljs-comment">//       if (element.routes.length) &#123;</span>
    <span class="hljs-comment">//         // eslint-disable-next-line no-param-reassign</span>
    <span class="hljs-comment">//         element.isNeedSave = true;</span>
    <span class="hljs-comment">//       &#125;</span>
    <span class="hljs-comment">//     &#125;</span>
    <span class="hljs-comment">//   &#125; else if (menuAutArray.indexOf(element.code) >= 0) &#123;</span>
    <span class="hljs-comment">//     // eslint-disable-next-line no-param-reassign</span>
    <span class="hljs-comment">//     element.isNeedSave = true;</span>
    <span class="hljs-comment">//   &#125;</span>
    <span class="hljs-comment">// &#125; else &#123;</span>
    <span class="hljs-comment">//   // eslint-disable-next-line no-param-reassign</span>
    <span class="hljs-comment">//   element.isNeedSave = true;</span>
    <span class="hljs-comment">// &#125;</span>

    <span class="hljs-keyword">return</span> element;
  &#125;);

  <span class="hljs-keyword">return</span> routes;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchRoutes</span>(<span class="hljs-params">routes</span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.keys(authRoutes).map(<span class="hljs-function"><span class="hljs-params">authKey</span> =></span>
    ergodicRoutes(routes, authKey, authRoutes[authKey].authority),
  );

  customerErgodicRoutes(routes);

  <span class="hljs-comment">/**
   * 后台接口返回子节点的情况，父节点需要溯源处理
   */</span>
  <span class="hljs-built_in">window</span>.g_routes = routes.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !item.isNeedDelete);

  <span class="hljs-comment">/**
   * 后台接口返回子节点的情况，父节点需要溯源处理
   */</span>
  <span class="hljs-comment">// window.g_routes = routes.filter(item => item.isNeedSave);</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">oldRender</span>) </span>&#123;
  authRoutes = <span class="hljs-string">''</span>;
  oldRender();
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>c. 修改login.js，获取路由当中的code便利获取到，进行查询权限</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; routerRedux &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'dva/router'</span>;
<span class="hljs-keyword">import</span> &#123; stringify &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;
<span class="hljs-keyword">import</span> &#123; fakeAccountLogin, getFakeCaptcha &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/services/api'</span>;
<span class="hljs-keyword">import</span> &#123; getAuthorityMenu &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/services/authority'</span>;
<span class="hljs-keyword">import</span> &#123; setAuthority &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/authority'</span>;
<span class="hljs-keyword">import</span> &#123; getPageQuery &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/utils'</span>;
<span class="hljs-keyword">import</span> &#123; reloadAuthorized &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/Authorized'</span>;
<span class="hljs-keyword">import</span> routes <span class="hljs-keyword">from</span> <span class="hljs-string">'../../config/router.config'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">namespace</span>: <span class="hljs-string">'login'</span>,

  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">status</span>: <span class="hljs-literal">undefined</span>,
  &#125;,

  <span class="hljs-attr">effects</span>: &#123;
    *<span class="hljs-function"><span class="hljs-title">login</span>(<span class="hljs-params">&#123; payload &#125;, &#123; call, put &#125;</span>)</span> &#123;
      <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">yield</span> call(fakeAccountLogin, payload);
      <span class="hljs-keyword">yield</span> put(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'changeLoginStatus'</span>,
        <span class="hljs-attr">payload</span>: response,
      &#125;);
      <span class="hljs-comment">// Login successfully</span>
      <span class="hljs-keyword">if</span> (response.status === <span class="hljs-string">'ok'</span>) &#123;
        <span class="hljs-comment">// 这里的数据通过接口返回菜单页面的权限是什么</span>

        <span class="hljs-keyword">const</span> codeArray = [];
        <span class="hljs-comment">// eslint-disable-next-line no-inner-declarations</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ergodicRoutes</span>(<span class="hljs-params">routesParam</span>) </span>&#123;
          routesParam.forEach(<span class="hljs-function"><span class="hljs-params">element</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (element.code) &#123;
              codeArray.push(element.code);
            &#125;
            <span class="hljs-keyword">if</span> (element.routes) &#123;
              ergodicRoutes(element.routes);
            &#125;
          &#125;);
        &#125;

        ergodicRoutes(routes);
        <span class="hljs-keyword">const</span> authMenuArray = <span class="hljs-keyword">yield</span> call(getAuthorityMenu, codeArray.join(<span class="hljs-string">','</span>));
        <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'routerAutArray'</span>, authMenuArray.join(<span class="hljs-string">','</span>));

        reloadAuthorized();
        <span class="hljs-keyword">const</span> urlParams = <span class="hljs-keyword">new</span> URL(<span class="hljs-built_in">window</span>.location.href);
        <span class="hljs-keyword">const</span> params = getPageQuery();
        <span class="hljs-keyword">let</span> &#123; redirect &#125; = params;
        <span class="hljs-keyword">if</span> (redirect) &#123;
          <span class="hljs-keyword">const</span> redirectUrlParams = <span class="hljs-keyword">new</span> URL(redirect);
          <span class="hljs-keyword">if</span> (redirectUrlParams.origin === urlParams.origin) &#123;
            redirect = redirect.substr(urlParams.origin.length);
            <span class="hljs-keyword">if</span> (redirect.match(<span class="hljs-regexp">/^\/.*#/</span>)) &#123;
              redirect = redirect.substr(redirect.indexOf(<span class="hljs-string">'#'</span>) + <span class="hljs-number">1</span>);
            &#125;
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">window</span>.location.href = redirect;
            <span class="hljs-keyword">return</span>;
          &#125;
        &#125;
        <span class="hljs-comment">// yield put(routerRedux.replace(redirect || '/'));</span>

        <span class="hljs-comment">// 这里之所以用页面跳转，因为路由的重新设置需要页面重新刷新才可以生效</span>
        <span class="hljs-built_in">window</span>.location.href = redirect || <span class="hljs-string">'/'</span>;
      &#125;
    &#125;,

    *<span class="hljs-function"><span class="hljs-title">getCaptcha</span>(<span class="hljs-params">&#123; payload &#125;, &#123; call &#125;</span>)</span> &#123;
      <span class="hljs-keyword">yield</span> call(getFakeCaptcha, payload);
    &#125;,

    *<span class="hljs-function"><span class="hljs-title">logout</span>(<span class="hljs-params">_, &#123; put &#125;</span>)</span> &#123;
      <span class="hljs-keyword">yield</span> put(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'changeLoginStatus'</span>,
        <span class="hljs-attr">payload</span>: &#123;
          <span class="hljs-attr">status</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">currentAuthority</span>: <span class="hljs-string">'guest'</span>,
        &#125;,
      &#125;);
      reloadAuthorized();
      <span class="hljs-keyword">yield</span> put(
        routerRedux.push(&#123;
          <span class="hljs-attr">pathname</span>: <span class="hljs-string">'/user/login'</span>,
          <span class="hljs-attr">search</span>: stringify(&#123;
            <span class="hljs-attr">redirect</span>: <span class="hljs-built_in">window</span>.location.href,
          &#125;),
        &#125;),
      );
    &#125;,
  &#125;,

  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">changeLoginStatus</span>(<span class="hljs-params">state, &#123; payload &#125;</span>)</span> &#123;
      setAuthority(payload.currentAuthority);
      <span class="hljs-keyword">return</span> &#123;
        ...state,
        <span class="hljs-attr">status</span>: payload.status,
        <span class="hljs-attr">type</span>: payload.type,
      &#125;;
    &#125;,
  &#125;,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>d. 添加service</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/request'</span>;

<span class="hljs-comment">// 查询菜单权限</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getAuthorityMenu</span>(<span class="hljs-params">codes</span>) </span>&#123;
  <span class="hljs-keyword">return</span> request(<span class="hljs-string">`/api/authority/menu?resCodes=<span class="hljs-subst">$&#123;codes&#125;</span>`</span>);
&#125;

<span class="hljs-comment">// 查询页面按钮权限</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getAuthority</span>(<span class="hljs-params">params</span>) </span>&#123;
  <span class="hljs-keyword">return</span> request(<span class="hljs-string">`/api/authority?codes=<span class="hljs-subst">$&#123;params&#125;</span>`</span>);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h3 data-id="heading-6">4.1.2 路由权限 菜单可见权限</h3>
<p>参照上面的方式，这里的菜单可见权限不用做其他的操作。</p>
<br>
<h2 data-id="heading-7">4.2  按钮权限 【<a href="https://github.com/rodchen-king/ant-design-pro-v2/commit/0e7895c56e4962d75ab8ccf4637cefca3f5f71b6#diff-a7acc04e8fb20252554c588f7b7a8564" target="_blank" rel="nofollow noopener noreferrer">代码地址</a>  <a href="https://github.com/rodchen-king/ant-design-pro-v2/commits/permission-branch" target="_blank" rel="nofollow noopener noreferrer">demo地址</a>】</h2>
<p>按钮权限上就涉及到两块，<strong>资源权限</strong>和<strong>数据权限</strong>。数据获取的方式不同，代码逻辑上会稍微有点不同。核心是业务组件内部的code，在加载的时候就自行累加，然后在页面加载完成的时候，发送请求。拿到数据之后，自行进行权限校验。尽量减少业务页面代码的复杂度。</p>
<p><strong>资源权限逻辑介绍：</strong></p>
<ol>
<li><strong>PageHeaderWrapper</strong>包含的业务页面存在按钮权限</li>
<li>按钮权限通过<strong>AuthorizedButton</strong>包含处理，需要添加code。但是业务页面因为是单独页面发送当前页面code集合去查询权限code，然后在<strong>AuthorizedButton</strong>进行权限逻辑判断。</li>
<li>所以<strong>AuthorizedButton</strong>的<strong>componentWillMount</strong>生命周期进行当前业务页面的code累加。累加完成之后，通过<strong>PageHeaderWrapper</strong>的<strong>componentDidMount</strong>生命周期函数发送权限请求，拿到权限code，通过公有globalAuthority model读取数据进行权限逻辑判断。</li>
<li>对于业务页面的调用参考readme进行使用。因为对于弹出框内部的code，在业务列表页面渲染的时候，组件还未加载，所以通过extencode提前将code累加起来进行查询权限。</li>
</ol>
<p><strong>数据权限介绍：</strong></p>
<ol>
<li>涉及数据权限，则直接将对应的数据规则放进<strong>AuthorizedButton</strong>内部进行判断，需要传入的数据则直接通过props传入即可。因为数据权限的规则不同，这里就没有举例子。</li>
<li>需要注意的逻辑是资源权限和数据权限是串行的，先判断资源权限，然后判断数据权限。</li>
</ol>
<br>
<p><strong>a. 添加公用authority model</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* eslint-disable no-unused-vars */</span>
<span class="hljs-comment">/* eslint-disable no-prototype-builtins */</span>
<span class="hljs-keyword">import</span> &#123; getAuthority &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/services/authority'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">namespace</span>: <span class="hljs-string">'globalAuthority'</span>,

  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">hasAuthorityCodeArray</span>: [], <span class="hljs-comment">// 获取当前具有权限的资源code</span>
    <span class="hljs-attr">pageCodeArray</span>: [], <span class="hljs-comment">// 用来存储当前页面存在的资源code</span>
  &#125;,

  <span class="hljs-attr">effects</span>: &#123;
    <span class="hljs-comment">/**
     * 获取当前页面的权限控制
     */</span>
    *<span class="hljs-function"><span class="hljs-title">getAuthorityForPage</span>(<span class="hljs-params">&#123; payload &#125;, &#123; put, call, select &#125;</span>)</span> &#123;
      <span class="hljs-comment">// 这里的资源code都是自己加载的</span>
      <span class="hljs-keyword">const</span> pageCodeArray = <span class="hljs-keyword">yield</span> select(<span class="hljs-function"><span class="hljs-params">state</span> =></span> state.globalAuthority.pageCodeArray);
      <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">yield</span> call(getAuthority, pageCodeArray);

      <span class="hljs-keyword">if</span> (pageCodeArray.length) &#123;
        <span class="hljs-keyword">yield</span> put(&#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">'save'</span>,
          <span class="hljs-attr">payload</span>: &#123;
            <span class="hljs-attr">hasAuthorityCodeArray</span>: response,
          &#125;,
        &#125;);
      &#125;
    &#125;,

    *<span class="hljs-function"><span class="hljs-title">plusCode</span>(<span class="hljs-params">&#123; payload &#125;, &#123; put, select &#125;</span>)</span> &#123;
      <span class="hljs-comment">// 组件累加当前页面的code，用来发送请求返回对应的权限code</span>
      <span class="hljs-keyword">const</span> &#123; codeArray = [] &#125; = payload;
      <span class="hljs-keyword">const</span> pageCodeArray = <span class="hljs-keyword">yield</span> select(<span class="hljs-function"><span class="hljs-params">state</span> =></span> state.globalAuthority.pageCodeArray);

      <span class="hljs-keyword">yield</span> put(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'save'</span>,
        <span class="hljs-attr">payload</span>: &#123;
          <span class="hljs-attr">pageCodeArray</span>: pageCodeArray.concat(codeArray),
        &#125;,
      &#125;);
    &#125;,

    <span class="hljs-comment">// eslint-disable-next-line no-unused-vars</span>
    *<span class="hljs-function"><span class="hljs-title">resetAuthorityForPage</span>(<span class="hljs-params">&#123; payload &#125;, &#123; put, call &#125;</span>)</span> &#123;
      <span class="hljs-keyword">yield</span> put(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'save'</span>,
        <span class="hljs-attr">payload</span>: &#123;
          <span class="hljs-attr">hasAuthorityCodeArray</span>: [],
          <span class="hljs-attr">pageCodeArray</span>: [],
        &#125;,
      &#125;);
    &#125;,
  &#125;,

  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">save</span>(<span class="hljs-params">state, &#123; payload &#125;</span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        ...state,
        ...payload,
      &#125;;
    &#125;,
  &#125;,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><strong>b. 修改PageHeaderWrapper文件【因为所有的业务页面都是这个组件的子节点】</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; PureComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; FormattedMessage &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'umi/locale'</span>;
<span class="hljs-keyword">import</span> Link <span class="hljs-keyword">from</span> <span class="hljs-string">'umi/link'</span>;
<span class="hljs-keyword">import</span> PageHeader <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/PageHeader'</span>;
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'dva'</span>;
<span class="hljs-keyword">import</span> MenuContext <span class="hljs-keyword">from</span> <span class="hljs-string">'@/layouts/MenuContext'</span>;
<span class="hljs-keyword">import</span> &#123; Spin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> GridContent <span class="hljs-keyword">from</span> <span class="hljs-string">'./GridContent'</span>;
<span class="hljs-keyword">import</span> styles <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.less'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PageHeaderWrapper</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; dispatch &#125; = <span class="hljs-built_in">this</span>.props;
    dispatch(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'globalAuthority/getAuthorityForPage'</span>, <span class="hljs-comment">// 发送请求获取当前页面的权限code</span>
    &#125;);
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; dispatch &#125; = <span class="hljs-built_in">this</span>.props;
    dispatch(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'globalAuthority/resetAuthorityForPage'</span>,
    &#125;);
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; children, contentWidth, wrapperClassName, top, loading, ...restProps &#125; = <span class="hljs-built_in">this</span>.props;

    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Spin</span> <span class="hljs-attr">spinning</span>=<span class="hljs-string">&#123;loading&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">margin:</span> '<span class="hljs-attr">-24px</span> <span class="hljs-attr">-24px</span> <span class="hljs-attr">0</span>' &#125;&#125; <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;wrapperClassName&#125;</span>></span>
          &#123;top&#125;
          <span class="hljs-tag"><<span class="hljs-name">MenuContext.Consumer</span>></span>
            &#123;value => (
              <span class="hljs-tag"><<span class="hljs-name">PageHeader</span>
                <span class="hljs-attr">wide</span>=<span class="hljs-string">&#123;contentWidth</span> === <span class="hljs-string">'Fixed'</span>&#125;
                <span class="hljs-attr">home</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">FormattedMessage</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"menu.home"</span> <span class="hljs-attr">defaultMessage</span>=<span class="hljs-string">"Home"</span> /></span>&#125;
                &#123;...value&#125;
                key="pageheader"
                &#123;...restProps&#125;
                linkElement=&#123;Link&#125;
                itemRender=&#123;item => &#123;
                  if (item.locale) &#123;
                    return <span class="hljs-tag"><<span class="hljs-name">FormattedMessage</span> <span class="hljs-attr">id</span>=<span class="hljs-string">&#123;item.locale&#125;</span> <span class="hljs-attr">defaultMessage</span>=<span class="hljs-string">&#123;item.title&#125;</span> /></span>;
                  &#125;
                  return item.title;
                &#125;&#125;
              />
            )&#125;
          <span class="hljs-tag"></<span class="hljs-name">MenuContext.Consumer</span>></span>
          &#123;children ? (
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.content&#125;</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">GridContent</span>></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">GridContent</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          ) : null&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Spin</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(<span class="hljs-function">(<span class="hljs-params">&#123; setting, globalAuthority, loading &#125;</span>) =></span> (&#123;
  <span class="hljs-attr">contentWidth</span>: setting.contentWidth,
  globalAuthority,
  <span class="hljs-attr">loading</span>: loading.models.globalAuthority,
&#125;))(PageHeaderWrapper);

<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><strong>c. 添加AuthorizedButton公共组件</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> PropTypes <span class="hljs-keyword">from</span> <span class="hljs-string">'prop-types'</span>;
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'dva'</span>;

@connect(<span class="hljs-function">(<span class="hljs-params">&#123; globalAuthority &#125;</span>) =></span> (&#123;
  globalAuthority,
&#125;))
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AuthorizedButton</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-keyword">static</span> contextTypes = &#123;
    <span class="hljs-attr">isMobile</span>: PropTypes.bool,
  &#125;;

  <span class="hljs-function"><span class="hljs-title">componentWillMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// extendcode 扩展表格中的code还没有出现的情况</span>
    <span class="hljs-keyword">const</span> &#123;
      dispatch,
      code,
      extendCode = [],
      <span class="hljs-attr">globalAuthority</span>: &#123; pageCodeArray &#125;,
    &#125; = <span class="hljs-built_in">this</span>.props;

    <span class="hljs-keyword">let</span> codeArray = [];

    <span class="hljs-keyword">if</span> (code) &#123;
      codeArray.push(code);
    &#125;

    <span class="hljs-keyword">if</span> (extendCode && extendCode.length) &#123;
      codeArray = codeArray.concat(extendCode);
    &#125;

    <span class="hljs-comment">// code已经存在，证明是页面数据渲染之后或者弹出框的按钮资源，不需要走dva了</span>
    <span class="hljs-keyword">if</span> (pageCodeArray.indexOf(code) >= <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;

    dispatch(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'globalAuthority/plusCode'</span>,
      <span class="hljs-attr">payload</span>: &#123;
        codeArray,
      &#125;,
    &#125;);
  &#125;

  checkAuthority = <span class="hljs-function"><span class="hljs-params">code</span> =></span> &#123;
    <span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">globalAuthority</span>: &#123; hasAuthorityCodeArray &#125;,
    &#125; = <span class="hljs-built_in">this</span>.props;

    <span class="hljs-keyword">return</span> hasAuthorityCodeArray.indexOf(code) >= <span class="hljs-number">0</span>; <span class="hljs-comment">// 资源权限</span>
  &#125;;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; children, code &#125; = <span class="hljs-built_in">this</span>.props;

    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> <span class="hljs-attr">this.checkAuthority</span>(<span class="hljs-attr">code</span>) ? '<span class="hljs-attr">inline</span>' <span class="hljs-attr">:</span> '<span class="hljs-attr">none</span>' &#125;&#125;></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> AuthorizedButton;

<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><strong>d. 添加AuthorizedButton readme文件</strong>
<br>
<a href="https://github.com/rodchen-king/ant-design-pro-v2/blob/permission-branch/src/components/AuthorizedButton/index.md" target="_blank" rel="nofollow noopener noreferrer">github.com/rodchen-kin…</a>
<br>
<br></p>
<h2 data-id="heading-8">4.3  按钮权限扩展-链接权限控制 【<a href="https://github.com/rodchen-king/ant-design-pro-v2/commit/02914330f17f11f3d6e8b7d5c1239702c6832337" target="_blank" rel="nofollow noopener noreferrer">代码地址</a>  <a href="https://github.com/rodchen-king/ant-design-pro-v2/commits/permission-branch" target="_blank" rel="nofollow noopener noreferrer">demo地址</a>】</h2>
<p>背景：页面上有需要控制跳转链接的权限，有权限则可以跳转，没有权限则不能跳转。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f07410670fe94313a5c0c6b3f569c538~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>a.公共model添加新的state：codeAuthorityObject</strong>
<br>
<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/097e301265494c8fbafd8efed7024cdb~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过redux-devtool，查看到codeAuthorityObject的状态值为：key:code值，value的值为true/false。
true代表，有权限，false代表无权限。主要用于开发人员自己做相关处理。<br><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d26733fe29134fe7b5d499635f544709~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>b.需要控制的按钮code，通过其他方式扩展进行code计算，发送请求获取权限</strong><br><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/832d4e43e8294794bfa52a2b5b527338~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>c.获取数据进行数据控制</strong><br><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0697bae8cde244859960f2ec87aefc47~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<h2 data-id="heading-9">4.4  按钮数据权限</h2>
<ul>
<li>demo分支：<a href="https://github.com/rodchen-king/ant-design-pro-v2/tree/permission-branch" target="_blank" rel="nofollow noopener noreferrer">github.com/rodchen-kin…</a></li>
<li>demo代码：<a href="https://github.com/rodchen-king/ant-design-pro-v2/commit/463514b0964c4c0187a503d315aa9f088e963f71" target="_blank" rel="nofollow noopener noreferrer">github.com/rodchen-kin…</a></li>
</ul>
<h3 data-id="heading-10">背景</h3>
<p>数据权限是对于业务组件内部表格组件的数据进行的数据操作权限。列表数据可能归属于不同的数据类型，所以具有不同的数据操作权限。对于批量操作则需要判断选择的数据是否都具有操作权限，然后显示是否可以批量操作，如果有一个没有操作权限，都不能进行操作。<br><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8a7f4cae6564a58a9bafc0c89170fd5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<br>
<br></p>
<h3 data-id="heading-11">总体思路</h3>
<p>场景：<br>比如在商品列表中，每条商品记录后面的“操作”一栏下用三个按钮：【编辑】、【上架/下架】、【删除】，而对于某一个用户，他可以查看所有的商品，但对于某些品牌他可以【上架/下架】但不能【编辑】，则前端需要控制到每一个商品后面的按钮的可用状态。<br><br>比如用户A对于某一条业务数据（id=1999）有编辑权限，则这条记录上的【编辑】按钮对他来说是可见的（前提是他首先要有【编辑】这个按钮的资源权限），但对于另一条记录（id=1899）是没有【编辑】权限，则这条记录上的【编辑】按钮对他来说是不可见的。
<br>
<br></p>
<h3 data-id="heading-12">按钮【actType】属性定义</h3>
<p>每个数据操作的按钮上加一个属性 “actType”代表这个按钮的动作类型（如：编辑、删除、审核等），这个属性是资权限的接口返回的，前端在调这个接口时将这个属性记录下来，或者保存到对应的控件中。所以前端可以不用关于这个属性的每个枚举值代表的是什么含义，只需根据接口的返回值赋值就好。
用兴趣的同学也可以参考一下actType取值如下：1 可读，2 编辑，3 可读+可写, 4 可收货，8 可发货，16 可配货， 32 可审核，64 可完结
<br>
<br></p>
<h3 data-id="heading-13">业务接口返回权限类型字段【permissionType】</h3>
<p>对于有权限控制的业务数据，列表接口或者详情接口都会返回一个“permissionType”的字段，这个字段代表当前用户对于这条业务数据的权限类型，如当 permissionType=2 代表这个用户对于这条数据有【编辑权限】，permisionType=4 代表这个用户对于这条业务数据有收货的权限，permisionType=6表示这个用户对于这条记录用编辑和发货的权限（6=2+4）
<br>
<br></p>
<h3 data-id="heading-14">怎么控制按钮的可用状态？</h3>
<p>现在列表上有三个按钮，【编辑】、【收货】、【完结】，它们对应的“actType”分别为2、4、64，某一条数据的permissionType=3，这时这三个按钮的状态怎么判断呢，permissionType=3 我们可以分解为 1+2，表示这个用户对于这条记录有“可读”+“编辑”权限，则这三个按钮中，只有【编辑】按钮是可用的。那么判断的公式为：</p>
<pre><code class="hljs language-js copyable" lang="js">((data[i].permissionType & obj.actType)==obj.actType)
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h3 data-id="heading-15">前端的js数据进行&判断</h3>
<p>需要进行数据转换</p>
<ul>
<li>data.toString(2): 将数据进行2进制转换成二进制字符串。</li>
<li>parseInt(permissionType,2) : 二进制字符串转换成二进制数据。</li>
</ul>
<br>
<h3 data-id="heading-16">代码修改</h3>
<p><strong>接口mock返回数据</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">response = [&#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-number">3</span>,
      <span class="hljs-string">"name"</span>: <span class="hljs-string">"创建活动-10001"</span>,
      <span class="hljs-string">"actType"</span>: <span class="hljs-number">0</span>,
      <span class="hljs-string">"code"</span>: <span class="hljs-string">"10001"</span>
    &#125;, &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-number">3</span>,
      <span class="hljs-string">"name"</span>: <span class="hljs-string">"编辑-10002"</span>,
      <span class="hljs-string">"actType"</span>: <span class="hljs-number">2</span>,
      <span class="hljs-string">"code"</span>: <span class="hljs-string">"10002"</span>
    &#125;, &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-number">3</span>,
      <span class="hljs-string">"name"</span>: <span class="hljs-string">"配置-10005"</span>,
      <span class="hljs-string">"actType"</span>: <span class="hljs-number">4</span>,
      <span class="hljs-string">"code"</span>: <span class="hljs-string">"10005"</span>
    &#125;, &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-number">3</span>,
      <span class="hljs-string">"name"</span>: <span class="hljs-string">"订阅警报-10006"</span>,
      <span class="hljs-string">"actType"</span>: <span class="hljs-number">8</span>,
      <span class="hljs-string">"code"</span>: <span class="hljs-string">"10006"</span>
    &#125;, &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-number">3</span>,
      <span class="hljs-string">"name"</span>: <span class="hljs-string">"查询详情-20001"</span>,
      <span class="hljs-string">"actType"</span>: <span class="hljs-number">16</span>,
      <span class="hljs-string">"code"</span>: <span class="hljs-string">"20001"</span>
    &#125;, &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-number">3</span>,
      <span class="hljs-string">"name"</span>: <span class="hljs-string">"批量操作-10007"</span>,
      <span class="hljs-string">"actType"</span>: <span class="hljs-number">32</span>,
      <span class="hljs-string">"code"</span>: <span class="hljs-string">"10007"</span>
    &#125;, &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-number">3</span>,
      <span class="hljs-string">"name"</span>: <span class="hljs-string">"更多操作-10008"</span>,
      <span class="hljs-string">"actType"</span>: <span class="hljs-number">64</span>,
      <span class="hljs-string">"code"</span>: <span class="hljs-string">"10008"</span>
    &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每一个返回的接口权限会将对应的actType一起返回。</p>
<p><strong>getAuthorityForPage代码修改</strong>
简单修改一下，因为之前返回的是code数组，现在返回的是对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-comment">/**
     * 获取当前页面的权限控制
     */</span>
    *<span class="hljs-function"><span class="hljs-title">getAuthorityForPage</span>(<span class="hljs-params">&#123; payload &#125;, &#123; put, call, select &#125;</span>)</span> &#123;
      <span class="hljs-comment">// 这里的资源code都是自己加载的</span>
      <span class="hljs-keyword">const</span> pageCodeArray = <span class="hljs-keyword">yield</span> select(<span class="hljs-function"><span class="hljs-params">state</span> =></span> state.globalAuthority.pageCodeArray);
      <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">yield</span> call(getAuthority, pageCodeArray);
      <span class="hljs-keyword">const</span> hasAuthorityCodeArray = response || [];
      <span class="hljs-keyword">const</span> codeAuthorityObject = &#123;&#125;;

      pageCodeArray.forEach(<span class="hljs-function">(<span class="hljs-params">value, index, array</span>) =></span> &#123;
        codeAuthorityObject[value] = hasAuthorityCodeArray.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.code).indexOf(value) >= <span class="hljs-number">0</span>;
      &#125;);

      <span class="hljs-comment">// debugger</span>
      <span class="hljs-keyword">yield</span> put(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'save'</span>,
        <span class="hljs-attr">payload</span>: &#123;
          hasAuthorityCodeArray,
          codeAuthorityObject,
        &#125;,
      &#125;);
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0eef8fd709446f69e0ddb06a470110d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>修改AuthorizedButton代码</strong>
增加数据权限判断</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* eslint-disable eqeqeq */</span>
<span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> PropTypes <span class="hljs-keyword">from</span> <span class="hljs-string">'prop-types'</span>;
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'dva'</span>;

@connect(<span class="hljs-function">(<span class="hljs-params">&#123; globalAuthority &#125;</span>) =></span> (&#123;
  globalAuthority,
&#125;))
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AuthorizedButton</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-keyword">static</span> contextTypes = &#123;
    <span class="hljs-attr">isMobile</span>: PropTypes.bool,
  &#125;;

  <span class="hljs-function"><span class="hljs-title">componentWillMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// extendcode 扩展表格中的code还没有出现的情况</span>
    <span class="hljs-keyword">const</span> &#123;
      dispatch,
      code,
      extendCode = [],
      <span class="hljs-attr">globalAuthority</span>: &#123; pageCodeArray &#125;,
    &#125; = <span class="hljs-built_in">this</span>.props;

    <span class="hljs-keyword">let</span> codeArray = [];

    <span class="hljs-keyword">if</span> (code) &#123;
      codeArray.push(code);
    &#125;

    <span class="hljs-keyword">if</span> (extendCode && extendCode.length) &#123;
      codeArray = codeArray.concat(extendCode);
    &#125;

    <span class="hljs-comment">// code已经存在，证明是页面数据渲染之后或者弹出框的按钮资源，不需要走dva了</span>
    <span class="hljs-keyword">if</span> (pageCodeArray.indexOf(code) >= <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;

    dispatch(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'globalAuthority/plusCode'</span>,
      <span class="hljs-attr">payload</span>: &#123;
        codeArray,
      &#125;,
    &#125;);
  &#125;

  checkAuthority = <span class="hljs-function"><span class="hljs-params">code</span> =></span> &#123;
    <span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">globalAuthority</span>: &#123; hasAuthorityCodeArray &#125;,
    &#125; = <span class="hljs-built_in">this</span>.props;

    <span class="hljs-keyword">return</span> hasAuthorityCodeArray.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.code).indexOf(code) >= <span class="hljs-number">0</span> && <span class="hljs-built_in">this</span>.checkDataAuthority(); <span class="hljs-comment">// 资源权限</span>
  &#125;;


  <span class="hljs-comment">/**
   * 检测数据权限
   */</span>
  checkDataAuthority = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">globalAuthority</span>: &#123; hasAuthorityCodeArray &#125;,
      code,                                         <span class="hljs-comment">// 当前按钮的code</span>
      actType,                                      <span class="hljs-comment">// 当前按钮的actType的值通过传递传入</span>
      recordPermissionType,                         <span class="hljs-comment">// 单条数据的数据操作权限总和</span>
      actTypeArray
    &#125; = <span class="hljs-built_in">this</span>.props;

    <span class="hljs-keyword">if</span> (recordPermissionType || actTypeArray) &#123;     <span class="hljs-comment">// 单条数据权限校验</span>
      <span class="hljs-keyword">const</span> tempCode = hasAuthorityCodeArray.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.code === code)
      <span class="hljs-keyword">let</span> tempActType = <span class="hljs-string">''</span>

      <span class="hljs-keyword">if</span> (actType) &#123;
        tempActType = actType
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (tempCode.length) &#123;
        tempActType = tempCode[<span class="hljs-number">0</span>].actType
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;                                <span class="hljs-comment">// 默认返回true</span>
      &#125;

      <span class="hljs-keyword">if</span> (actTypeArray) &#123;                           <span class="hljs-comment">// 批量操作</span>
        <span class="hljs-keyword">return</span> !actTypeArray.some(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !<span class="hljs-built_in">this</span>.checkPermissionType(item.toString(<span class="hljs-number">2</span>), tempActType.toString(<span class="hljs-number">2</span>)))
      &#125;

      <span class="hljs-comment">// 单条数据操作</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.checkPermissionType(recordPermissionType.toString(<span class="hljs-number">2</span>), tempActType.toString(<span class="hljs-number">2</span>))
    &#125; 

    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;                                    <span class="hljs-comment">// 如果字段没有值的情况下，证明不需要进行数据权限</span>
  &#125;

  <span class="hljs-comment">/**
   * 二进制检查当前当前数据是否具有当前权限
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>permissionType 
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">actType</span></span>
   */</span>
  checkPermissionType = <span class="hljs-function">(<span class="hljs-params">permissionType, actType</span>) =></span> 
     (<span class="hljs-built_in">parseInt</span>(permissionType,<span class="hljs-number">2</span>) & <span class="hljs-built_in">parseInt</span>(actType,<span class="hljs-number">2</span>)).toString(<span class="hljs-number">2</span>) == actType
  

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; children, code &#125; = <span class="hljs-built_in">this</span>.props;

    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> <span class="hljs-attr">this.checkAuthority</span>(<span class="hljs-attr">code</span>) ? '<span class="hljs-attr">inline</span>' <span class="hljs-attr">:</span> '<span class="hljs-attr">none</span>' &#125;&#125;></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> AuthorizedButton;

<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><strong>调用方式</strong>
<br><br>单条数据操作</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><AuthoriedButton code=<span class="hljs-string">"10005"</span> recordPermissionType=&#123;record.permissionType&#125;>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.handleUpdateModalVisible(true, record)&#125;>配置<span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>
</AuthoriedButton>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>批量操作</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <AuthoriedButton code=<span class="hljs-string">"10007"</span> actTypeArray=&#123;getNotDuplicateArrayById(selectedRows, <span class="hljs-string">'permissionType'</span>)&#125;>
     <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span>></span>批量操作<span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>
 </AuthoriedButton>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            