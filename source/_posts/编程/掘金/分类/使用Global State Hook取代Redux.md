
---
title: '使用Global State Hook取代Redux'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48d4d271f64f45709101776cfccb045b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 02:19:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48d4d271f64f45709101776cfccb045b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>从1年半前开始使用React Hook，看着大串大串的reducer方法，我在做项目的时候在想，redux这样的模式是否过于繁琐，比如说给管道写数据，非得调用一个dispatch方法，另外还要做一个reducer的数据合并方法，加上各种中间件容易整出一些头疼的代码。</p>
<h4 data-id="heading-0">Redux本质上是一种全局订阅模式</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48d4d271f64f45709101776cfccb045b~tplv-k3u1fbpfcp-watermark.image" alt="图.001.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图所示，redux提供了一个订阅管道，ComponentA / ComponentB / ComponentC 通过dispatch给redux写数据，reducer合并处理数据，保存到redux states，一旦数据改变订阅数据的组件做响应式更新。</p>
<p>react 16.8版本推出了hook写法，出现了useState的写法，我们能不能推出一种新的简化的写法取代Redux。</p>
<h4 data-id="heading-1">Global State 是不错的方案，国外有一些版本，我这里也给出我的版本。</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cf880340933441dae7a0c1067806228~tplv-k3u1fbpfcp-watermark.image" alt="图.002.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>就是这么简单的一段(^_^)</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// global-state.ts</span>
<span class="hljs-keyword">import</span> &#123; useEffect, useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">declare</span> <span class="hljs-keyword">const</span> process: <span class="hljs-built_in">any</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> GLOBAL_STATE = &#123;
  <span class="hljs-attr">DEBUG</span>: <span class="hljs-literal">false</span>
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> makeGlobalState = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">T</span> <span class="hljs-attr">extends</span> <span class="hljs-attr">unknown</span>></span>(initValue: T, name?: string, filter?: (val: T) => T) => &#123;
  const globalStates: any[] = [];
  let currentValue = initValue;

  return (): [T, (val: T) => void] => &#123;
    const [value, setValue] = useState(currentValue);
    if (!globalStates.includes(setValue)) &#123;
      globalStates.push(setValue);
    &#125;

    useEffect(
      () => () => &#123;
        if (process.env.NODE_ENV && process.env.NODE_ENV === 'development') &#123;
          globalStates.splice(globalStates.indexOf(setValue) - 1, 2);
        &#125; else &#123;
          globalStates.splice(globalStates.indexOf(setValue), 1);
        &#125;
      &#125;,
      []
    );

    const setAllStateValue = (value: T) => &#123;
      if (filter) &#123;
        value = filter(value);
      &#125;
      if (GLOBAL_STATE.DEBUG) &#123;
        console.log('SET ' + name, value);
      &#125;
      currentValue = value;
      globalStates.forEach((setVal) => &#123;
        setVal(value);
      &#125;);
    &#125;;
    return [value, setAllStateValue];
  &#125;;
&#125;;

</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>做法是给每个component的local state做一个收集器，把setState的方法收集起来，在每次调用这个global state的设置方法的时候，遍历执行所有的set state，达到给所有component刷新的目的。</p>
<ul>
<li>
<p>有添加就要有销毁，代码中的useEffect用于在component销毁时移除setState方法。这里要注意的是因为development模式下component渲染2次（会添加2次），所以这里需要做一些处理。</p>
</li>
<li>
<p>函数makeGlobalState还提供了一个filter功能，可以做类似reducer处理数据的功能，说得高大上一点就是可以定义一个中间件什么的....。第二个参数name则是用于debug打印。</p>
</li>
</ul>
<p>使用的时候，先要创建一份文件，去定义所有的global-state，给初始值。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// my-global-states.ts</span>
<span class="hljs-keyword">import</span> &#123; makeGlobalState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./global-state'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useCounter = makeGlobalState(<span class="hljs-number">1</span>, <span class="hljs-string">'Counter'</span>, <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> val > <span class="hljs-number">10</span> ? <span class="hljs-number">10</span> : val;
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useUserInfo = makeGlobalState(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'John'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">30</span> &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以在不同的component上使用了</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// CompA.tsx</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; useCounter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./my-global-states'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> CompA = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useCounter();
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
          setCount(count + 1);
        &#125;&#125;
      >
        加1
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;


<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// CompB.tsx</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; useCounter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./my-global-states'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> CompB = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useCounter();
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
          setCount(5);
        &#125;&#125;
      >
        设为5
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// App.tsx</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./App.css'</span>;
<span class="hljs-keyword">import</span> &#123; CompA &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./CompA'</span>;
<span class="hljs-keyword">import</span> &#123; CompB &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./CompB'</span>;
<span class="hljs-keyword">import</span> &#123; GLOBAL_STATE &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./global-state'</span>;
GLOBAL_STATE.DEBUG = <span class="hljs-literal">true</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">CompA</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">CompB</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果，任何一个使用了useCounter的组件调用了 setCounter 方法，其他的订阅了couter值的组件也一起刷新了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de02fd5e4de843e9b5e6694af7698341~tplv-k3u1fbpfcp-watermark.image" alt="Screen Shot 2021-05-08 at 17.56.22.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-2">Global State 使用起来会比Redux简单很多，非常推荐大家使用。</h5></div>  
</div>
            