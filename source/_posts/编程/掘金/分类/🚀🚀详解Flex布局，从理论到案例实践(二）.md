
---
title: '🚀🚀详解Flex布局，从理论到案例实践(二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a6e34384fb4a3e8e5e713559e05cc7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 00:22:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a6e34384fb4a3e8e5e713559e05cc7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a6e34384fb4a3e8e5e713559e05cc7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" title="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<hr>
<h4 data-id="heading-0">前言</h4>
<blockquote>
<p>上一篇说到了容器属性，本文就接着来讲项目属性。<a href="https://juejin.cn/post/6979612188000387109" target="_blank" title="https://juejin.cn/post/6979612188000387109">上一篇传送门</a></p>
<p>如何理解容器属性和项目属性？容器属性是加在容器上的，那么项目属性呢，就是写在项目上的，就好比容器属性给ul，项目属性给li。ul这个容器里面放了很多li项目。我是这么来理解的。</p>
</blockquote>
<hr>
<p>好了，言归正传，xdm准备好了么？</p>
<hr>
<h4 data-id="heading-1">项目属性</h4>
<hr>
<h5 data-id="heading-2"><strong>order</strong></h5>
<p>取值：<code>默认0</code>，用于决定<code>项目排列顺序</code>，<code>数值越小，项目排列越靠前</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcf8e625d0ae44d3abca927eb07e0f4e~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h5 data-id="heading-3"><strong>flex-grow</strong></h5>
<p>取值：<code>默认0</code>，用于决定项目在有剩余空间的情况下<code>是否放大，默认不放大</code>；注意，即便设置了固定宽度，也会放大。</p>
<p>假设默认三个项目中前两个个项目都是0，最后一个是1，最后的项目会沾满剩余所有空间。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c24c74e945342c1bc4075a7784528d1~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假设只有第一个项目默认为0，后面两个项目flex-grow均为1，那么后两个项目平分剩余空间。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d653ce6fc8a40b18622f691c59ab2b7~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假设第一个项目默认为0，第二个项目为flex-grow:2，最后一个项目为1，则第二个项目在放大时所占空间是最后项目的两倍。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f8bcfa07e054132b963372ec381d65c~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h5 data-id="heading-4"><strong>flex-shrink</strong></h5>
<p>取值：默认1，用于决定项目在空间不足时<code>是否缩小</code>，<code>默认项目都是1</code>，即空间不足时大家一起<code>等比缩小</code>；注意，即便设置了固定宽度，也会缩小。</p>
<p>但如果某个项目flex-shrink设置为0，则即便空间不够，自身也不缩小。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/185ec0a465df4b14a48a8f69ad09a09e~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中第二个项目flex-shrink为0，所以自身不会缩小。</p>
<hr>
<h5 data-id="heading-5"><strong>flex-basis</strong></h5>
<p>取值：<code>默认auto，用于设置项目宽度</code>，默认auto时，项目会保持默认宽度，或者以width为自身的宽度，但如果设置了<code>flex-basis，权重会比width属性高</code>，因此会覆盖widtn属性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce2d6a841b144aa5b4b0fb1b0327b00f~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中先设置了flex-basis属性，后设置了width属性，但宽度依旧以flex-basis属性为准。</p>
<hr>
<h5 data-id="heading-6"><strong>flex</strong></h5>
<p>取值：<code>默认0 1 auto</code>，flex属性是flex-grow，flex-shrink与flex-basis三个属性的<code>简写，</code> <code>用于定义项目放大，缩小与宽度</code>。</p>
<p>这个属性还有几个快捷键值，面试问flex时，基本必问。</p>
<ul>
<li>flex: auto (1 1 auto)</li>
<li>flex: none (0 0 auto)</li>
<li>flex: 1 (1 1 0%)</li>
<li>flex: 0 (0 1 0%)</li>
</ul>
<p><code>分别是auto(1 1 auto)等分放大缩小</code>，与<code>none(0 0 auto)不放大不缩小</code>。</p>
<blockquote>
<p>面试官：给我说说 flex:auto和flex:1的区别？</p>
<p>我：....</p>
</blockquote>
<p>分析：两者本质其实是flex-basis属性为 0% 和auto的区别,auto为默认值即为子元素的大小，那么存在多余空间时，flex为1，width将会被忽略；flex为auto时，width的设置将是有效的。 这是一个很经典的问题，还有面试题也是由这个分化而来，大家有兴趣，可以自己去研究研究。</p>
<hr>
<h5 data-id="heading-7"><strong>align-self</strong></h5>
<p><code>取值：auto(默认)</code>| flex-start | flex-end | center | baseline | stretch，表示<code>继承父容器的align-items属性</code>。如果没父元素，则默认stretch。</p>
<p>用于让个别项目拥有与其它项目不同的对齐方式，各值的表现与父容器的align-items属性完全一致。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01c5e1ffdb1f448a9ac96cbdc9655631~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h4 data-id="heading-8">小结</h4>
<p>到这里，flex布局的属性也就基本上介绍完毕了，自己也跟着老老实实的实操一遍。实操真的很重要，自己不是大佬，没办法看过一遍就能记住还能举一反三，我是菜鸡实锤了，只能老老实实多练习。 最后附上总结图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c520df3b7ee45a98c61461188afda71~tplv-k3u1fbpfcp-zoom-1.image" alt="table1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fedfe19a21d48249f5c0d490580bab7~tplv-k3u1fbpfcp-zoom-1.image" alt="table2.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            