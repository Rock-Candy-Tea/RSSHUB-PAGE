
---
title: '学习React特征（四） - React Form 单向数据流'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e7c705119194d7398bda43689b5273d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 22:14:20 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e7c705119194d7398bda43689b5273d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:var(--cyanosis-base-color);transition:color .35s;--cyanosis-base-color:#353535;--cyanosis-title-color:#005bb7;--cyanosis-strong-color:#2196f3;--cyanosis-em-color:#4fc3f7;--cyanosis-del-color:#ccc;--cyanosis-link-color:#3da8f5;--cyanosis-linkh-color:#007fff;--cyanosis-border-color:#bedcff;--cyanosis-border-color-2:#ececec;--cyanosis-bg-color:#fff;--cyanosis-blockquote-color:#8c8c8c;--cyanosis-blockquote-bg-color:#f0fdff;--cyanosis-code-color:#c2185b;--cyanosis-code-bg-color:#fff4f4;--cyanosis-code-pre-color:#f8f8f8;--cyanosis-table-border-color:#c3e0fd;--cyanosis-table-th-color:#dff0ff;--cyanosis-table-tht-color:#005bb7;--cyanosis-table-tr-nc-color:#f7fbff;--cyanosis-table-trh-color:#e0edf7;--cyanosis-slct-title-color:#005bb7;--cyanosis-slct-titlebg-color:rgba(175,207,247,0.25);--cyanosis-slct-text-color:#c80000;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#e8ebec;--cyanosis-slct-codebg-color:#ffeaeb;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body.__dark&#123;--cyanosis-base-color:#cacaca;--cyanosis-title-color:#ddd;--cyanosis-strong-color:#fe9900;--cyanosis-em-color:#ffd28e;--cyanosis-del-color:#ccc;--cyanosis-link-color:#ffb648;--cyanosis-linkh-color:#fe9900;--cyanosis-border-color:#ffe3ba;--cyanosis-border-color-2:#ffcb7b;--cyanosis-bg-color:#2f2f2f;--cyanosis-blockquote-color:#c7c7c7;--cyanosis-blockquote-bg-color:rgba(255,199,116,0.1);--cyanosis-code-color:#000;--cyanosis-code-bg-color:#ffcb7b;--cyanosis-code-pre-color:rgba(255,227,185,0.5);--cyanosis-table-border-color:#fe9900;--cyanosis-table-th-color:#ffb648;--cyanosis-table-tht-color:#000;--cyanosis-table-tr-nc-color:#6d5736;--cyanosis-table-trh-color:#947443;--cyanosis-slct-title-color:#000;--cyanosis-slct-titlebg-color:#fe9900;--cyanosis-slct-text-color:#00c888;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#000;--cyanosis-slct-codebg-color:#ffcb7b;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);transition:color .35s&#125;.markdown-body h2&#123;position:relative;padding-left:10px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid var(--cyanosis-border-color-2)&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-14px&#125;.markdown-body h2:after&#123;content:"」";position:relative;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:var(--cyanosis-strong-color)&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,var(--cyanosis-link-color),rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),var(--cyanosis-link-color));border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background-color:var(--cyanosis-bg-color);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center;transition:background-color .5s&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:var(--cyanosis-code-color);word-break:break-word;overflow-x:auto;background-color:var(--cyanosis-code-bg-color);border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:var(--cyanosis-code-pre-color)&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:var(--cyanosis-border-color)&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:var(--cyanosis-strong-color);border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:var(--cyanosis-link-color);border-bottom:1px solid var(--cyanosis-border-color)&#125;.markdown-body a:hover&#123;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:var(--cyanosis-linkh-color)&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid var(--cyanosis-border-color);transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid var(--cyanosis-table-border-color);border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:var(--cyanosis-table-tr-nc-color)&#125;.markdown-body table tr:hover&#123;background-color:var(--cyanosis-table-trh-color)&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid var(--cyanosis-table-border-color)&#125;.markdown-body table th&#123;color:var(--cyanosis-table-tht-color);background-color:var(--cyanosis-table-th-color)&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:var(--cyanosis-blockquote-color);border-left:4px solid var(--cyanosis-strong-color);background-color:var(--cyanosis-blockquote-bg-color);padding:1px 20px;margin:22px 0;transition:color .35s&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:var(--cyanosis-strong-color)&#125;.markdown-body em,.markdown-body i&#123;color:var(--cyanosis-em-color)&#125;.markdown-body del&#123;color:var(--cyanosis-del-color)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:var(--cyanosis-title-color);font-size:20px;font-weight:bolder;border-bottom:1px solid var(--cyanosis-border-color);cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:var(--cyanosis-blockquote-bg-color);border:2px dashed var(--cyanosis-strong-color)&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:var(--cyanosis-slct-title-color);background-color:var(--cyanosis-slct-titlebg-color)&#125;.markdown-body ol li::selection,.markdown-body p::selection,.markdown-body ul li::selection&#123;color:var(--cyanosis-slct-text-color);background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body del::selection&#123;color:var(--cyanosis-slct-del-color);background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body table thead th::selection&#123;background-color:transparent&#125;.markdown-body table tbody td::selection&#123;background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body code::selection&#123;background-color:var(--cyanosis-slct-codebg-color)&#125;.markdown-body pre>code::selection&#123;background-color:var(--cyanosis-slct-prebg-color)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与[新人创作礼]活动, 一起开启掘金创作之路。
我报名参加金石计划一期挑战——瓜分10万奖池，这是我的第一篇文章，点击查看活动详情。</p>
<p>今天将之前的内容做个系统整理，结合 React Form 案例， 来了解下为何React推荐单向数据流，如果采用双向管理，可能的问题
(关于React Form案例，可参考相关文章 - 学习React的特征（二） - React Form <a href="https://juejin.cn/post/7143478192827793445%EF%BC%89" target="_blank" title="https://juejin.cn/post/7143478192827793445%EF%BC%89">juejin.cn/post/714347…</a></p>
<h2 data-id="heading-0">集中状态管理</h2>
<p>首先来看之前的React Form， 若采用单向数据流</p>
<pre><code class="hljs language-ini copyable" lang="ini">import * as React from 'react'<span class="hljs-comment">;</span>

const <span class="hljs-attr">Useremail</span> = props => <input type=<span class="hljs-string">"email"</span> &#123;...props&#125; />
const <span class="hljs-attr">Userpassword</span> = props => <input type=<span class="hljs-string">"password"</span> &#123;...props&#125; />
const <span class="hljs-attr">SubmitButton</span> = props => <button type=<span class="hljs-string">"submit"</span> &#123;...props&#125; />

const <span class="hljs-attr">LoginForm</span> = () => &#123;
  // LoginForm状态变化 => Useremail/Userpassword组件
  const <span class="hljs-section">[email, setEmail]</span> = React.useState('')<span class="hljs-comment">;</span>
  const <span class="hljs-section">[password, setPassword]</span> = React.useState('')<span class="hljs-comment">;</span>

  const <span class="hljs-attr">handleEmail</span> = (e) => &#123;
    setEmail(e.target.value)<span class="hljs-comment">;</span>
  &#125;<span class="hljs-comment">;</span>

  const <span class="hljs-attr">handlePassword</span> = (e) => &#123;
    setPassword(e.target.value)<span class="hljs-comment">;</span>
  &#125;<span class="hljs-comment">;</span>

  const <span class="hljs-attr">handleSubmit</span> = (e) => &#123;
    e.preventDefault()<span class="hljs-comment">;</span>

    alert(email + ' ' + password)<span class="hljs-comment">;</span>
  &#125;<span class="hljs-comment">;</span>

  return (
    <form <span class="hljs-attr">onSubmit</span>=&#123;handleSubmit&#125;>
      <div>
        <label <span class="hljs-attr">htmlFor</span>=<span class="hljs-string">"email"</span>>Email</label>
        <Useremail
          <span class="hljs-attr">id</span>=<span class="hljs-string">"email"</span>
          <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
          <span class="hljs-attr">value</span>=&#123;email&#125;
          <span class="hljs-attr">onChange</span>=&#123;handleEmail&#125;
        />
      </div>
      <div>
        <label <span class="hljs-attr">htmlFor</span>=<span class="hljs-string">"password"</span>>Password</label>
        <Userpassword
          <span class="hljs-attr">id</span>=<span class="hljs-string">"password"</span>
          <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span>
          <span class="hljs-attr">value</span>=&#123;password&#125;
          <span class="hljs-attr">onChange</span>=&#123;handlePassword&#125;
        />
      </div>
      <SubmitButton <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span>>Submit</SubmitButton>
    </form>
  )<span class="hljs-comment">;</span>
&#125;<span class="hljs-comment">;</span>

export &#123; LoginForm &#125;<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到， 每次<code>Useremail</code> or <code>Password</code> 输入发生改变时，<code>LoginForm</code>中的<code>email</code>与<code>password</code>状态动态产生改变</p>
<h2 data-id="heading-1">双向数据流</h2>
<pre><code class="hljs language-ini copyable" lang="ini">import * as React from 'react'<span class="hljs-comment">;</span>

// Useremail/Userpassword组件状态变化 => LoginForm父组件
const <span class="hljs-attr">Useremail</span> = (&#123;updateUseremail, ...props&#125;) =>
  <input <span class="hljs-attr">type</span>=<span class="hljs-string">"email"</span> 
         <span class="hljs-attr">onChange</span>=&#123;e => updateUseremail(e.target.value)&#125;
         &#123;...props&#125; />
const <span class="hljs-attr">Userpassword</span> = (&#123;updateUserpassword, ...props&#125;) => 
  <input <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> 
         <span class="hljs-attr">onChange</span>=&#123;e => updateUserpassword(e.target.value)&#125;
         &#123;...props&#125; />
const <span class="hljs-attr">SubmitButton</span> = props => <button type=<span class="hljs-string">"submit"</span> &#123;...props&#125; />

const <span class="hljs-attr">LoginForm</span> = () => &#123;
  // LoginForm状态变化 => Useremail/Userpassword组件
  const <span class="hljs-section">[email, setEmail]</span> = React.useState('')<span class="hljs-comment">;</span>
  const <span class="hljs-section">[password, setPassword]</span> = React.useState('')<span class="hljs-comment">;</span>

  const <span class="hljs-attr">handleSubmit</span> = (e) => &#123;
    e.preventDefault()<span class="hljs-comment">;</span>

    alert(email + ' ' + password)<span class="hljs-comment">;</span>
  &#125;<span class="hljs-comment">;</span>

  return (
    <form <span class="hljs-attr">onSubmit</span>=&#123;handleSubmit&#125;>
      <div>
        <label <span class="hljs-attr">htmlFor</span>=<span class="hljs-string">"email"</span>>Email</label>
        <Useremail
          <span class="hljs-attr">id</span>=<span class="hljs-string">"email"</span>
          <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
          <span class="hljs-attr">value</span>=&#123;email&#125;
          <span class="hljs-attr">updateUseremail</span>=&#123;setEmail&#125;
        />
      </div>
      <div>
        <label <span class="hljs-attr">htmlFor</span>=<span class="hljs-string">"password"</span>>Password</label>
        <Userpassword
          <span class="hljs-attr">id</span>=<span class="hljs-string">"password"</span>
          <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span>
          <span class="hljs-attr">value</span>=&#123;password&#125;
          <span class="hljs-attr">updateUserpassword</span>=&#123;setPassword&#125;
        />
      </div>
      <SubmitButton <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span>>Submit</SubmitButton>
    </form>
  )<span class="hljs-comment">;</span>
&#125;<span class="hljs-comment">;</span>

export &#123; LoginForm &#125;<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际执行这两个程序，得到的结果是一致，看起来两者没有什么区别</p>
<h2 data-id="heading-2">那为何不选择双向数据流</h2>
<ul>
<li><strong>代码维护</strong></li>
</ul>
<p>以上代码可以发现，一旦LoginForm发生问题，双向数据流需要在多个子组件和父组件中同时寻找状态异常的原因，当程序逐渐趋于复杂化，后期维护会变得异常困难</p>
<ul>
<li><strong>组件复用</strong></li>
</ul>
<p>每次用户状态需求发生新的变化，每个子组件都要相应调整，造成组件在实际使用中难以复用</p>
<ul>
<li><strong>应用升级</strong></li>
</ul>
<p>另外，当程序需要做整体升级，因为状态分散在各个组件，将会导致难以实行</p>
<h2 data-id="heading-3">小结</h2>
<p>组件设计成响应式，从长远看，更符合React推荐的设计模式</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e7c705119194d7398bda43689b5273d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="example.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            