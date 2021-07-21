
---
title: 'Vue 数据响应式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1078'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 01:15:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=1078'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">什么是响应式呢？</h3>
<ul>
<li>若一个物体对外界的刺激做出反应，它就是响应式。</li>
<li>Vue 的 data 就是响应式</li>
<li>const vm = new Vue(&#123;data:&#123;n:0&#125;&#125;)</li>
<li>如果修改 vm.n ，那么 UI 中的 n 就会响应</li>
<li>通过<code>Object.defineProperty</code>来实现数据响应式</li>
</ul>
<h4 data-id="heading-1"><code>getter</code> 和 <code>setter</code></h4>
<p>看看下面代码的不同</p>
<pre><code class="copyable">let obj1 = &#123;
  姓: "张",
  名: "三",
  age: 18,
&#125;;
//需求一，得到姓名
let obj1 = &#123;
  姓: "张",
  名: "三",
  姓名() &#123;
    return this.姓 + this.名;         
  &#125;,
  age: 18,
&#125;;
console.log("需求一:" + obj1.姓名());  //这里不一样
//需求二，姓名不要括号也能得出值
let obj2 = &#123;
  姓: "张",
  名: "三",
  get 姓名() &#123;                        //这里不一样
    return this.姓 + this.名;
  &#125;,
  age: 18,
&#125;;
console.log("需求一:" + obj1.姓名);   //这里不一样
//需求三，姓名可以被写
let obj3 = &#123;
  姓: "张",
  名: "三",
  get 姓名() &#123;
    return this.姓 + this.名;
  &#125;,
  set 姓名(xxx) &#123;
    this.姓 = xxx[0];
    this.名 = xxx.substring(1);
  &#125;,
  age: 18,
&#125;;
console.log(`需求三：姓 $&#123;obj3.姓&#125;，名 $&#123;obj3.名&#125;`);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">Object.defineProperty</h4>
<p>语法：<code>Object.defineProperty(obj,'n',&#123;...&#125;)</code></p>
<p>假如没有传 <code>n</code> ，就会出 <code>bug</code>，解决方法有两种</p>
<ul>
<li><code>Vue.set</code></li>
<li><code>this.$set</code></li>
</ul>
<p>定义完一个东西之后，还想再它身上加新的 <code>get</code> 和 <code>set</code> 只能通过 <code>Object.defineProperty</code></p>
<pre><code class="copyable">let _xxx = 0;
Object.defineProperty(obj, "xxx", &#123;
  get() &#123;
    return _xxx;
  &#125;,
  set(value) &#123;
    _xxx = value;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">代理和监听</h4>
<p><code>vm = new Vue(&#123;data: myData&#125;)</code></p>
<ul>
<li><code>vm</code>是<code>myData</code>的代理<code>(proxy)</code></li>
<li>会对<code>myData</code>的所有属性进行监控</li>
<li>为什么要监控，为了防止 <code>myData</code>的属性变了，<code>vm</code>不知道</li>
<li><code>vm</code>知道了又如何?</li>
<li>知道属性变了就可以调用<code>render(data)</code>，<code>UI=render(data)</code>就自动刷新了</li>
</ul>
<p>代理：不管对 <code>obj</code> 做什么，<code>obj</code> 就对 <code>data</code> 做什么，<code>obj</code>就是代理</p>
<p>监听，记录下原始的值，引入一个新的虚拟属性 <code>n</code></p>
<p>只要把 <code>myData</code> 传给了 <code>Vue</code>，<code>Vue</code> 马上进行了篡改</p>
<h4 data-id="heading-4">总结</h4>
<p>对象中新增的<code>key</code></p>
<ul>
<li><code>Vue</code>没有办法事先监听和代理</li>
<li>要使用<code>set</code>来新增<code>key</code>，更新<code>UI</code></li>
<li>最好提前把属性都写出来，不要新增<code>key</code></li>
<li>但数组做不到「不新增<code>key</code>」</li>
</ul>
<p>数组中新增的<code>key</code></p>
<ul>
<li>也可用<code>set</code>来新增<code>key</code>，且创建监听和代理，更新<code>UI</code></li>
<li>尤玉溪篡改了7个<code>API</code>方便我们对数组进行增删</li>
<li>这7个<code>API</code>会自动处理监听和代理，并更新U</li>
</ul>
<h4 data-id="heading-5">Vue 数组中的变异方法</h4>
<ul>
<li><code>push()</code></li>
<li><code>pop()</code></li>
<li><code>shift()</code></li>
<li><code>unshift()</code></li>
<li><code>splice()</code></li>
<li><code>sort()</code></li>
<li><code>reverse()</code></li>
</ul></div>  
</div>
            