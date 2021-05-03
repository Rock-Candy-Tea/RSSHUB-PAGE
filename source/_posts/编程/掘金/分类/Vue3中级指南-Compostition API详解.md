
---
title: 'Vue3中级指南-Compostition API详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8066'
author: 掘金
comments: false
date: Sun, 02 May 2021 23:24:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=8066'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Compostition API集合，解决Vue2组件开发问题</p>
<p>更好的TypeScript支持</p>
<p>新的Api支持</p>
<h3 data-id="heading-0">什么是reactive？</h3>
<ul>
<li>reactive是vue3中提供的实现响应式数据的方法</li>
<li>在vue2中响应式数据是通过defineProperty来实现的
<ul>
<li>因为有缺陷，在处理数组方面，所以vue3中响应式数据是通过ES6的Proxy来实现的</li>
</ul>
</li>
</ul>
<h3 data-id="heading-1">reactive注意点</h3>
<ul>
<li>reactive参数必须是对象(json/arr)</li>
<li>如果给reactive传递了其他对象
<ul>
<li>默认情况下修改对象，界面不会自动更新。</li>
<li>如果想更新，可以通过重新赋值的方式。</li>
</ul>
</li>
</ul>
<hr>
<h3 data-id="heading-2">什么是ref?</h3>
<ul>
<li>ref和reactive一样，也用用来实现响应式数据的方法</li>
<li>由于reactive必须传递一个对象，所有导致在企业开发中如果我们只想让某个变量实现响应式的时候会非常麻烦，所有vue3就给我们提供了ref方法，实现对简单之的监听</li>
</ul>
<h3 data-id="heading-3">ref本质</h3>
<ul>
<li>
<p>ref底层的本质还是reactive,系统会自动根据我们给ref传入的值将它转换成以下这样</p>
<pre><code class="hljs language-js copyable" lang="js">ref(xxx) => reactive(&#123;<span class="hljs-attr">value</span>:xxx&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">ref注意点</h3>
<ul>
<li>在vue中使用ref声明的变量在模版中不需要通过.value获取，因为在template模版中，vue会自动给我们添加.value</li>
<li>在js中使用ref的值或者更改ref的值必须通过.value获取和更改</li>
</ul>
<hr>
<h3 data-id="heading-5">递归监听</h3>
<ul>
<li>
<p>默认情况下，无论是通过ref还是reactive都是递归监听</p>
</li>
<li>
<p>递归监听存在的问题，如果数据量较大，非常消耗性能</p>
</li>
<li>
<p>非递归监听</p>
</li>
</ul>
<h4 data-id="heading-6">shallowReactive</h4>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> state = shallowReactive(&#123;
      <span class="hljs-attr">a</span>: <span class="hljs-string">"a"</span>,
      <span class="hljs-attr">b</span>: &#123;
        <span class="hljs-attr">c</span>: <span class="hljs-string">"c"</span>,
        <span class="hljs-attr">d</span>: &#123;
          <span class="hljs-attr">e</span>: <span class="hljs-string">"e"</span>
        &#125;
      &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：shallowReactive用于创建非递归监听的属性，只会监听第一层</strong></p>
<h4 data-id="heading-7">shallowRef</h4>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> state = shallowRef(&#123;
      <span class="hljs-attr">a</span>: <span class="hljs-string">"a"</span>,
      <span class="hljs-attr">b</span>: &#123;
        <span class="hljs-attr">c</span>: <span class="hljs-string">"c"</span>,
        <span class="hljs-attr">d</span>: &#123;
          <span class="hljs-attr">e</span>: <span class="hljs-string">"e"</span>
        &#125;
      &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：shallowRef监听的是.value的变化。并不是shallowReactive第一层的变化。</strong></p>
<h4 data-id="heading-8">triggerRef</h4>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> state = shallowRef(&#123;
      <span class="hljs-attr">a</span>: <span class="hljs-string">"a"</span>,
      <span class="hljs-attr">b</span>: &#123;
        <span class="hljs-attr">c</span>: <span class="hljs-string">"c"</span>,
        <span class="hljs-attr">d</span>: &#123;
          <span class="hljs-attr">e</span>: <span class="hljs-string">"e"</span>
        &#125;
      &#125;
    &#125;)
    
    <span class="hljs-comment">// 修改后页面并不会更新视图</span>
    state.b.d.e = <span class="hljs-string">"ee"</span>
    <span class="hljs-comment">// 主动触发视图更新</span>
    triggerRef(state)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>应用场景</p>
<p><code>一半情况下我们使用ref和reactive即可，只有在需要监听的数据量比较大的时候，我们才使用shallowRef/shallowReactive</code></p>
</li>
</ul>
<h3 data-id="heading-9">toRaw</h3>
<p>了解toRaw之前我们可以先看下以下的一个小列子来理解为啥需要用到toRaw</p>
<pre><code class="hljs language-js copyable" lang="js"><script lang=<span class="hljs-string">"ts"</span>>
<span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> data = &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"只会番茄炒蛋"</span>,
      <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
    &#125;;
    <span class="hljs-keyword">let</span> state = reactive(data);
    
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeAge</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// state.age += 1;</span>
      data.age += <span class="hljs-number">1</span>;
      <span class="hljs-built_in">console</span>.log(data);
      <span class="hljs-built_in">console</span>.log(state);
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      state,
      changeAge,
    &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们会发现，数据改变了但是视图并没有更新。这里我们明白的一点就是data和state是引用关系。state的本质是一个Proxy对象，在这个Proxy对象中引用了data</p>
<p>如果直接修改data,数据是改变的，但是无法触发页面的更新</p>
<p>只有通过包装之后的对象来修改，才会触发页面的更新</p>
<p>这个方法有啥作用场景就是， 当我们只想修改数据，但是不想视图发生变化时使用。因为ref和reactive数据类型的特点就是每次修改数据都会被追踪，都会更新ui界面。非常消耗性能。如果我们有一些操作不需要追踪和更新页面，那么这时候就可以通过toRaw方法拿到他的原始数据。这样就能够节省性能</p>
<p><strong>总结：toRaw方法从响应式数据获取原始数据</strong></p>
<p><strong>注意：当我们通过toRaw获取ref类型的原始数据时会发现获取不到</strong>。</p>
<p>ref本质：reactive</p>
<p>Ref(obj) => reactive(&#123;value: obj&#125;)</p>
<p>这也是为什么需要通过.value来获取ref创建的数据</p>
<p>总结：如果想要通过toRaw拿到ref类型的原始数据（创建时传入的那个数据）那么久必须明确告诉toRaw方法，要获取的时.value的值。因为经过Vue处理之后，.value中保存的才是当初的原始数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><script lang=<span class="hljs-string">"ts"</span>>
<span class="hljs-keyword">import</span> &#123; ref, toRaw &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> data = &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"只会番茄炒蛋"</span>,
      <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
    &#125;;
    <span class="hljs-keyword">let</span> state = ref(data);
    <span class="hljs-keyword">let</span> data2 = toRaw(state.value);
    <span class="hljs-built_in">console</span>.log(data2);

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeAge</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// state.age += 1;</span>
      data.age += <span class="hljs-number">1</span>;
      <span class="hljs-built_in">console</span>.log(data);
      <span class="hljs-built_in">console</span>.log(state);
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      state,
      changeAge,
    &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Markrow</h3>
<p>永远不会被追踪的数据，被markrow声明的变量永远不会被追踪，即使被reactive或者ref声明。修改数据也不会改变数据，更不会触发视图更新</p>
<h3 data-id="heading-11">ref和toRef的区别</h3>
<ul>
<li>ref 和toRef 修改响应式数据都会会影响以前的数据</li>
<li>ref 数据发生改变，界面就会自动更新</li>
<li>toRef数据发生改变，界面也不会自动更新</li>
</ul>
<hr>
<p><strong>toRef应用场景：如果想让响应式数据和以前的数据关联起来，并且更新响应式数据之后还不想更新UI，那么就可以使用。</strong></p>
<h3 data-id="heading-12">toRefs</h3>
<p>将响应式对象转换为普通对象，其中结果对象的每个 property 都是指向原始对象相应 property 的 <a href="https://v3.cn.vuejs.org/api/refs-api.html#ref" target="_blank" rel="nofollow noopener noreferrer"><code>ref</code></a>。</p>
<p>或者说将一个对象身上的所有属性变为响应式数据可以使用。
<strong>以上这些方法都是为了提升性能。主要用的多的还是ref和reactive</strong></p>
<h2 data-id="heading-13"><code>customRef</code></h2>
<p>创建一个自定义的 ref，并对其依赖项跟踪和更新触发进行显式控制。它需要一个工厂函数，该函数接收 <code>track</code> 和 <code>trigger</code> 函数作为参数，并且应该返回一个带有 <code>get</code> 和 <code>set</code> 的对象。</p>
<p>为什么要自定义ref我们下面再说。先说如何实现</p>
<pre><code class="hljs language-js copyable" lang="js"><script lang=<span class="hljs-string">"ts"</span>>
<span class="hljs-keyword">import</span> &#123; customRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myRef</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> customRef(<span class="hljs-function">(<span class="hljs-params">track, trigger</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// track()方法告诉vue这个数据是要被追踪的</span>
        track();
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"get"</span>, value);
        <span class="hljs-keyword">return</span> value;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        value = newValue;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"set"</span>, value);
        <span class="hljs-comment">// trigger()方法告诉vue更新视图</span>
        trigger();
      &#125;,
    &#125;;
  &#125;);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> state = myRef(<span class="hljs-number">18</span>);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">change</span>(<span class="hljs-params"></span>) </span>&#123;
      state.value = <span class="hljs-number">20</span>;
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      state,
      change,
    &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么要自定义ref</p>
<p>首先我们要知道一点的是setup函数只能是一个同步的函数，不能是一个异步的函数。至于为什么不能是一个异步的函数大家在setup前面加上async让后正常声明变量在页面中显示就知道原因了。</p>
<p>所以当我们在业务中需要发起ajax请求获取数据的时候，且想通过async await来获取数据就行不通了。</p>
<p>那么无法使用async await的时候就意味着我们的代码中可能会出现大量的回调函数。</p>
<p>那么我们还想按照以前同步代码的方式来书写 就可以考虑使用自定义ref。</p>
<pre><code class="hljs language-js copyable" lang="js"><script lang=<span class="hljs-string">"ts"</span>>
<span class="hljs-keyword">import</span> &#123; customRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myRef</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> customRef(<span class="hljs-function">(<span class="hljs-params">track, trigger</span>) =></span> &#123;
    fetch(value)
      .then(<span class="hljs-keyword">async</span> (res) => &#123;
        value = <span class="hljs-keyword">await</span> res.json();
        <span class="hljs-built_in">console</span>.log(value);
        trigger();
      &#125;)
      .catch(<span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(reason);
      &#125;);

    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// track()方法告诉vue这个数据是要被追踪的</span>
        track();
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"get"</span>, value);
        <span class="hljs-keyword">return</span> value;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        value = newValue;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"set"</span>, value);
        <span class="hljs-comment">// trigger()方法告诉vue更新视图</span>
        trigger();
      &#125;,
    &#125;;
  &#125;);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> state = myRef(<span class="hljs-string">"../public/data.json"</span>);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">change</span>(<span class="hljs-params"></span>) </span>&#123;
      state.value = <span class="hljs-number">20</span>;
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      state,
      change,
    &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">ref获取元素</h3>
<p>vue3和vue2不同， vue3并没有this.$属性的那些东西了。想要获取元素也很简单</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"box"</span>></span>我是box<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; onMounted, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> box = ref(<span class="hljs-literal">null</span>);
    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(box.value);
    &#125;);
    <span class="hljs-keyword">return</span> &#123;
      box,
    &#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里注意为什么打印的是box.value 和上面ref声明变量获取的原因一致。</p>
<p>为什么在onMounted中打印。这点生命周期和2是一致的。因为setup和created还有beforeC reated一样，这这期间dom还没有创建</p>
<h3 data-id="heading-15">readonly家族</h3>
<ul>
<li>readonly</li>
</ul>
<p>接受一个对象 (响应式或纯对象) 或 <a href="https://v3.cn.vuejs.org/api/refs-api.html#ref" target="_blank" rel="nofollow noopener noreferrer">ref</a> 并返回原始对象的只读代理。只读代理是深层的：任何被访问的嵌套 property 也是只读的。</p>
<p>用于创建一个只读属性，并且是递归只读</p>
<ul>
<li>shallowReadonly</li>
</ul>
<p>用于创建一个只读的数据，但是不是递归只读。只有第一层只读</p>
<ul>
<li>isReadonly</li>
</ul>
<p>用于判断属性是否是一个readonly返回布尔值</p>
<p><strong>这里大家可能会有疑问那么我直接使用const声明变量不就行了吗。 这里要注意。const通常用于声明常量，且通常是声明原始类型。但是如果声明引用类型。随便变量不可重新赋值。但是引用类型的属性的值是可以更改的。</strong></p>
<h3 data-id="heading-16">关于响应式数据本质上的理解</h3>
<ul>
<li>
<p>在vue2.x中是通过defineProperty来实现响应式数据的。但是有部分缺陷，例如数组的处理</p>
</li>
<li>
<p>在vue3.x中是通过Proxy来实现响应式数据的</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 简单实现</span>
<span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"番茄"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;
<span class="hljs-keyword">let</span> state = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(obj, key); <span class="hljs-comment">// &#123;name: '番茄', age: 18&#125; name</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, value</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(obj, key, value); <span class="hljs-comment">// &#123;name: '番茄', age: 18&#125; name 炒蛋</span>
        obj[key] = value
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"更新UI视图"</span>);
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
&#125;)

<span class="hljs-built_in">console</span>.log(state.name); <span class="hljs-comment">// 番茄</span>
state.name = <span class="hljs-string">"炒蛋"</span>
<span class="hljs-built_in">console</span>.log(state); <span class="hljs-comment">// Proxy &#123;name: '炒蛋', age: 18&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上述简单的列子。我们就可以在获取值和设置值的做很多事情了。</p>
<p><strong>注意点：set方法一定要给返回值告诉此次操作完成成功。因为在set操作中可能不止做一次修改例如数组</strong></p>
<h4 data-id="heading-17">proxy代理数组</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 简单实现</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="hljs-keyword">let</span> state = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(arr, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(obj, key); <span class="hljs-comment">// [1, 2, 3] 1</span>
        <span class="hljs-keyword">return</span> obj[key]
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, value</span>)</span> &#123;
        <span class="hljs-comment">/**
         *  [ 1, 2, 3 ] push
            [ 1, 2, 3 ] length
            [ 1, 2, 3 ] 3 4
            更新UI视图
            [ 1, 2, 3, 4 ] length 4
            更新UI视图
            [ 1, 2, 3, 4 ]
         */</span>
        <span class="hljs-built_in">console</span>.log(obj, key, value);
        obj[key] = value
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"更新UI视图"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
&#125;)

<span class="hljs-comment">// console.log(state[1]) // 2</span>
state.push(<span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(state);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上述代码我们会发现set方法中执行了两次。一次是[ 1, 2, 3 ] 3 4， 一次是[ 1, 2, 3, 4 ] length 4</p>
<p>set方法一定通过返回值告诉当前的操作是否成功。如果将上面的return ture注视掉就会报错</p>
<pre><code class="hljs language-js copyable" lang="js">state.push(<span class="hljs-number">4</span>)
      ^

<span class="hljs-built_in">TypeError</span>: <span class="hljs-string">'set'</span> on proxy: trap returned falsish <span class="hljs-keyword">for</span> property <span class="hljs-string">'3'</span>
    at <span class="hljs-built_in">Proxy</span>.push (<anonymous>)
    at <span class="hljs-built_in">Object</span>.<anonymous> (<span class="hljs-regexp">/Users/</span>cctvabu/vite-vue3-project/proxy.js:<span class="hljs-number">26</span>:<span class="hljs-number">7</span>)
    at Module._compile (internal/modules/cjs/loader.js:<span class="hljs-number">1063</span>:<span class="hljs-number">30</span>)
    at <span class="hljs-built_in">Object</span>.Module._extensions..js (internal/modules/cjs/loader.js:<span class="hljs-number">1092</span>:<span class="hljs-number">10</span>)
    at Module.load (internal/modules/cjs/loader.js:<span class="hljs-number">928</span>:<span class="hljs-number">32</span>)
    at <span class="hljs-built_in">Function</span>.Module._load (internal/modules/cjs/loader.js:<span class="hljs-number">769</span>:<span class="hljs-number">14</span>)
    at <span class="hljs-built_in">Function</span>.executeUserEntryPoint [<span class="hljs-keyword">as</span> runMain] (internal/modules/run_main.js:<span class="hljs-number">72</span>:<span class="hljs-number">12</span>)
    at internal/main/run_main_module.js:<span class="hljs-number">17</span>:<span class="hljs-number">47</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>所以注意在set方法中一定要通过返回值告诉当前操作是否成功</strong></p>
<hr>
<p>以上呢就是我学习了解到的部分api知识。后续还在学习和补充中。当然有不对的地方请评论指出，我查阅资料修改。</p>
<h4 data-id="heading-18">找工作</h4>
<p>本人最近准备跳槽找工作。有介绍工作的可以联系我哈～</p></div>  
</div>
            