
---
title: '前端基础面试6_3-DOM事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7d49ead52874d38b091cdde7a223876~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 02:22:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7d49ead52874d38b091cdde7a223876~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" title="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7d49ead52874d38b091cdde7a223876~tplv-k3u1fbpfcp-watermark.image" alt="33608.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">DOM事件类</h1>
<h2 data-id="heading-1">1：基本概念：DOM事件的级别</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02a94e0bfcd14b82bed13e1dea69563e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">2：DOM事件模型</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7b8db39208d482bb68c78248163081e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">3：DOM事件流</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/870c33bee7e84b6a94407eea7ed0d13c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">4：描述DOM事件捕获的具体流程</h2>
<p><strong>流程图示</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea93611693784abf8b4ba544cfb2b4af~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>代码</strong></p>
<pre><code class="copyable">   <style>
            * &#123;
                margin: 0;
                padding: 0;
            &#125;

            #margin &#123;
                width: 300px;
                height: 300px;
                background-color: red;
                color: black;
                text-align: center;
                line-height: 100px;
            &#125;
        </style>
        <section id="margin">
            目标元素
        </section>
        <script>
            var margin = document.getElementById('margin');
            window.addEventListener('click', function () &#123;
                console.log('window captrue');
            &#125;, true);
            // true捕获触发，false冒泡触发
            document.addEventListener('click', function () &#123;
                console.log('document captrue');
            &#125;, true);
            document.documentElement.addEventListener('click', function () &#123;
                console.log('html captrue');
            &#125;, true);
            document.body.addEventListener('click', function () &#123;
                console.log('body captrue');
            &#125;, true);
            margin.addEventListener('click', function () &#123;
                console.log('margin captrue');
            &#125;, true);
        </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>图解</strong>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/279b20a808534e538639a532fb0a03ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">5：Event对象的常见应用</h2>
<p>1：组织默认事件，如阻止a标签跳转</p>
<p>2：阻止冒泡</p>
<p>3：两个事件，在A事件上加这句话，会阻止B事件响应。类似于给A设置优先级大于B</p>
<p>4：当前绑定的事件</p>
<p>5：当前被点击元素</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6164a2df11684c9f82eb1d4f14da5813~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">6：自定义事件</h2>
<p>1：new Event('事件名')自定义事件</p>
<p>2：1中做不到传参，想传参可以用CustomEvent。后跟objeck指定参数
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0303bcd7b11a4841bd15bd58b9f2eab3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
案例</p>
<pre><code class="copyable"><style>
       <style>
            * &#123;
                margin: 0;
                padding: 0;
            &#125;

            #margin &#123;
                width: 300px;
                height: 300px;
                background-color: red;
                color: black;
                text-align: center;
                line-height: 100px;
            &#125;
        </style>
        <section id="margin">
            目标元素
        </section>
        <script>
            var margin = document.getElementById('margin');
            var sb = new Event('test');
            margin.addEventListener('test', function () &#123;
                console.log('test dispatch');
            &#125;)
            setTimeout(function () &#123;
                margin.dispatchEvent(sb)
                // 此处不是事件名，是事件对象
            &#125;, 2000)
        </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6fd2bb552f54f819d46cc553c6decbf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文总结了dom的一些东西，没有那么细。但能帮你把知识点联系起来。</p></div>  
</div>
            