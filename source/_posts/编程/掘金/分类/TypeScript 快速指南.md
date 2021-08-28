
---
title: 'TypeScript 快速指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af23516214a5455aa77fc9c9bc2441cb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 02:53:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af23516214a5455aa77fc9c9bc2441cb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第25天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<hr>
<h2 data-id="heading-0">一、为什么要用TypeScript</h2>
<p><code>TypeScript</code>可以让我们开发中避免一些<code>类型</code>或者<code>一些不是我们预期希望的代码结果</code>错误。xxx is not defined 我们都知道<code>JavaScript</code>错误是在运行中才抛出的，但是<code>TypeScript</code>错误直接是在编辑器里告知我们的，这极大的提升了开发效率，也不用花大量的时间去写单测，同时也避免了大量的时间排查<code>Bug</code>。</p>
<h2 data-id="heading-1">二、TypeScript优缺点</h2>
<h3 data-id="heading-2">优点</h3>
<ul>
<li>一般我们在前后端联调时，都要去看接口文档上的字段类型，而<code>TypeScript</code>会自动帮我们识别当前的类型。节省了我们去看<code>文档</code>或者<code>network</code>时间。这叫做类型推导(待会我们会讲到)</li>
<li>友好地在编辑器里提示错误，避免代码在运行时类型隐式转换踩坑。</li>
</ul>
<h3 data-id="heading-3">缺点</h3>
<ul>
<li>有一定的学习成本，<code>TypeScript</code>中有几种类型概念，<code>interface接口</code>、<code>class类</code>、<code>enum枚举</code>、<code>generics泛型</code>等这些需要我们花时间学习。</li>
<li>可能和一些插件库结合的不是很完美</li>
</ul>
<h2 data-id="heading-4">三、TypeScript运行流程及JavaScript代码运行流程</h2>
<p><strong>1. JavaScript运行流程如下，依赖NodeJs环境和浏览器环境</strong></p>
<ul>
<li>将<code>JavaScript</code>代码转换为<code>JavaScript-AST</code></li>
<li>将<code>AST</code>代码转换为字节码</li>
<li>运算时计算字节码</li>
</ul>
<p><strong>2. TypeScript运行流程，以下操作均为TSC操作，三步执行完继续同上操作，让浏览器解析</strong></p>
<ul>
<li>将<code>TypeScript</code>代码编译为 <code>TypeScript-AST</code></li>
<li>检查<code>AST</code>代码上类型检查</li>
<li>类型检查后，编译为<code>JavaScript</code>代码</li>
<li><code>JavaScript</code>代码转换为<code>JavaScript-AST</code></li>
<li>将<code>AST</code>代码转换为字节码</li>
<li>运算时计算字节码</li>
</ul>
<h2 data-id="heading-5">四、TypeScript和JavaScript区别</h2>
<p>只有搞懂了二者的区别，我们才可以更好的理解<code>TypeScript</code></p>






























<table><thead><tr><th>类型系统特性</th><th>JavaScript</th><th>TypeScript</th></tr></thead><tbody><tr><td>类型是如何绑定？</td><td>动态</td><td>静态</td></tr><tr><td>是否存在类型隐式转换？</td><td>是</td><td>否</td></tr><tr><td>何时检查类型？</td><td>运行时</td><td>编译时</td></tr><tr><td>何时报告错误</td><td>运行时</td><td>编译时</td></tr></tbody></table>
<h3 data-id="heading-6">1.类型转换</h3>
<p><strong>JavaScript</strong></p>
<p>比如在<code>JavaScript</code>中<code>1 + true</code>这样一个代码片段，<code>JavaScript</code>存在隐式转换，这时<code>true</code>会变成<code>number</code>类型<code>number(true)</code>和1相加。</p>
<p><strong>TypeScript</strong></p>
<p>在<code>TypeScript</code>中，<code>1+true</code>这样的代码会在<code>TypeScript</code>中报错，提示<code>number</code>类型不能和<code>boolean</code>类型进行运算。</p>
<h3 data-id="heading-7">2.何时检查类型</h3>
<p><strong>JavaScript</strong></p>
<p>在<code>JavaScript</code>中只有在程序运行时才能检查类型。类型也会存在隐式转换，很坑。</p>
<p><strong>TypeScript</strong></p>
<p>在<code>TypeScript</code>中，在编译时就会检查类型，如果和预期的类型不符合直接会在编辑器里报错、爆红</p>
<h3 data-id="heading-8">3.何时报告错误</h3>
<p><strong>JavaScript</strong></p>
<p>在<code>JavaScript</code>只有在程序执行时才能抛出异常，<code>JavaScript</code>存在隐式转换，等我们程序执行时才能真正的知道代码类型是否是预期的类型，代码是不是有效。</p>
<p><strong>TypeScript</strong></p>
<p>在<code>TypeScript中</code>，当你在编辑器写代码时，如有错误则会直接抛出异常，极大得提高了效率，也是方便。</p>
<h2 data-id="heading-9">TypeScript 的两种模式</h2>
<h3 data-id="heading-10">1.显式注解类型</h3>
<p>举个栗子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> name: string = <span class="hljs-string">"前端掘金人"</span>;

<span class="hljs-keyword">let</span> age: number = <span class="hljs-number">38</span>;

<span class="hljs-keyword">let</span> hobby: string[] = [<span class="hljs-string">"write code"</span>, <span class="hljs-string">"玩游戏"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显式注解类型就是，声明变量时定义上类型（官方话语就是<strong>声明时带上注解</strong>），让我们一看就明白，哦~，这个<code>name</code>是一个<code>string</code>类型。</p>
<h3 data-id="heading-11">2.推导类型</h3>
<p>举个栗子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> name = <span class="hljs-string">"前端掘金人"</span>; <span class="hljs-comment">// 是一个string类型</span>

<span class="hljs-keyword">let</span> age = <span class="hljs-number">38</span>;  <span class="hljs-comment">// 是一个number类型</span>

<span class="hljs-keyword">let</span> hobby = [<span class="hljs-string">"write code"</span>, <span class="hljs-string">"玩游戏"</span>] <span class="hljs-comment">// 是一个string数组类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>推导类型就是去掉显示注解，系统自动会识别当前值是一个什么类型的。</p>
<h2 data-id="heading-12">六、安装TypeScript && 运行</h2>
<h3 data-id="heading-13">typescript</h3>
<p>全局安装<code>typescript</code>环境。</p>
<pre><code class="hljs language-js copyable" lang="js">npm i -g typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可是这只是安装了<code>typescript</code>，那我们怎么运行<code>.ts</code>文件呢，安装完<code>typescript</code>我们就可以执行<code>tsc</code>命令。</p>
<p>如：我们的文件叫做<code>index.ts</code>，直接在命令行执行<code>tsc index.ts</code>即可。然后就可以看到在目录下编译出来一个<code>index.js</code>，这就是<code>tsc</code>编译完的结果。</p>
<p><strong>index.ts</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> userName: string = <span class="hljs-string">"前端掘金人"</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行<code>tsc index.ts</code>，你可以看见在<code>index.ts</code>的同级下又生成一个<code>index.js</code>，如下就是编译的结果文件<code>index.js</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> userName = <span class="hljs-string">"前端掘金人"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们知道了运行<code>tsc</code>命令就可以编译生成一个文件，有的小伙伴觉得这样太麻烦了，每次运行只是编译出来一个文件还不是运行，还得用<code>node index.js</code>才可以运行。不急我们接着往下看</p>
<h3 data-id="heading-14">ts-node</h3>
<p>我们来看一下这个插件<code>ts-node</code>，这个插件可以直接运行<code>.ts</code>文件，并且也不会编译出来<code>.js</code>文件。</p>
<pre><code class="hljs language-js copyable" lang="js">npm i ts-node

<span class="hljs-comment">// 运行 ts-node index.ts</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>讲到这里我们了解了<strong>为什么要用TypeScript</strong>和它的<strong>优缺点</strong>以及它的<strong>运行工作方式</strong>。</p>
<p>那么接下来就是<code>TypeScript</code>的基础知识重点来了~</p>
<h2 data-id="heading-15">七、基础知识</h2>
<h3 data-id="heading-16">1. 基础静态类型</h3>
<p>在<code>TypeScript</code>中基础类型跟我们<code>JavScript</code>中基础类型是一样的。只是有各别是<code>Ts</code>里面新出的。</p>
<h4 data-id="heading-17">1. number</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count: number = <span class="hljs-number">18</span>; <span class="hljs-comment">// 显示注解一个number类型</span>

<span class="hljs-keyword">const</span> count1 = <span class="hljs-number">18</span>; <span class="hljs-comment">// 不显示注解，ts会自动推导出来类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">2. string</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> str: string = <span class="hljs-string">"前端掘金人"</span>; <span class="hljs-comment">// 显示注解一个string类型</span>

<span class="hljs-keyword">const</span> str1 = <span class="hljs-string">"蛙人"</span>; <span class="hljs-comment">// 不显示注解，ts会自动推导出来类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">3. boolean</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> status: string = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 显示注解一个string类型</span>

<span class="hljs-keyword">const</span> status1 = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 不显示注解，ts会自动推导出来类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">4. null</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> value: <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;

<span class="hljs-keyword">const</span> value: <span class="hljs-literal">null</span> = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 这一点null类型可以赋值undefined跟在 js中是一样的，null == undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">5. undefined</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> value: <span class="hljs-literal">undefined</span> = <span class="hljs-literal">undefined</span>;

<span class="hljs-keyword">const</span> value: <span class="hljs-literal">undefined</span> = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 这一点null类型可以赋值undefined跟在 js中是一样的，null == undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">6. void</h4>
<p>估计到这有一些小伙伴可能对<code>void</code>这个比较陌生，以为只有<code>TypeScript</code>才有的。其实不是哈，在我们<code>JavaScript</code>就已经存在<code>void</code>关键字啦，它的意思就是无效的，有的小伙伴可能看见过早些项目里面<code><a href="javascript: void(0)"></code>这是控制<code>a</code>标签的跳转默认行为。你不管怎么执行<code>void</code>方法它都是返回<code>undefined</code></p>
<p>那么在我们<code>TypeScript</code>中<code>void</code>类型是什么呢。它也是代表无效的，一般只用在<strong>函数</strong>上，告诉别人这个<strong>函数</strong>没有返回值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;&#125; <span class="hljs-comment">// 正确</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testFn</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>; <span class="hljs-comment">// 报错，不接受返回值存在</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>&#125; <span class="hljs-comment">// 显示返回undefined类型，也是可以的</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn2</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>&#125; <span class="hljs-comment">// 显示返回null类型也可以，因为 null == undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">7. never</h4>
<p><code>never</code><strong>一个永远不会有值的类型</strong>或者也可以说<strong>一个永远也执行不完的类型</strong>，代表用于不会有值，<code>undefined</code>、<code>null</code>也算做是值。一般这个类型就不会用到，也不用。大家知道这个类型就行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test: never = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 错误</span>
<span class="hljs-keyword">const</span> test1: never = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 错误</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123; <span class="hljs-comment">// 正确，因为死循环了，一直执行不完</span>
    <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>) &#123;&#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123; <span class="hljs-comment">// 正确，因为递归，永远没有出口</span>
    Person()
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123; <span class="hljs-comment">// 正确 代码报错了，执行不下去</span>
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">8. any</h4>
<p><code>any</code>这个类型代表<strong>任何的</strong>、<strong>任意的</strong>。希望大家在项目中，不要大片定义<code>any</code>类型。虽然它真的好使，那这样我们写<code>TypeScript</code>就没有任何意义了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> value: any = <span class="hljs-string">""</span>; <span class="hljs-comment">// 正确</span>
value = <span class="hljs-literal">null</span> <span class="hljs-comment">// 正确</span>
value = &#123;&#125; <span class="hljs-comment">// 正确</span>
value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 正确</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">9. unknown</h4>
<p><code>unknown</code>类型是我们<code>TypeScript</code>中第二个<code>any</code>类型，也是接受任意的类型的值。它的英文翻译过来就是<strong>未知的</strong>，我们来看一下栗子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> value: unknown = <span class="hljs-string">""</span>  
value = <span class="hljs-number">1</span>;
value = <span class="hljs-string">"fdsfs"</span>
value = <span class="hljs-literal">null</span>
value = &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那现在肯定有小伙伴疑惑，诶，那它<code>unknown</code>相当于是<code>any</code>类型，那二者的区别是什么。我们来看一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> valueAny: any = <span class="hljs-string">""</span>;
<span class="hljs-keyword">let</span> valueUnknown: unknown = <span class="hljs-string">""</span>;

valueAny = <span class="hljs-string">"蛙人"</span>;
valueUnknown = <span class="hljs-string">"前端掘金人"</span>

<span class="hljs-keyword">let</span> status: <span class="hljs-literal">null</span> = <span class="hljs-literal">false</span>;
status = valueAny; <span class="hljs-comment">// 正确</span>
status = valueUnknown <span class="hljs-comment">// 报错，不能将unknown类型分配给null类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来看一下上面的，为什么<code>any</code>类型就能被赋值成功，而<code>unknown</code>类型不行呢，从它俩的意义来上看，还是有点区别的，<code>any</code>任何的，任意的、<code>unknown</code>未知的。所以你给<code>unknown</code>类型赋值任何类型都没关系，因为它本来就是未知类型嘛。但是你如果把它的<code>unknown</code>类型去被赋值一个<code>null</code>类型，这时人家<code>null</code>这边不干了，我不接受<code>unknown</code>类型。</p>
<p>说白了一句话，别人不接受<code>unknown</code>类型，而<code>unknown</code>类型接受别人，哈哈哈哈。</p>
<h3 data-id="heading-26">2. 对象静态类型</h3>
<p>说起对象类型，我们肯定都能想到对象包含<code>&#123;&#125;</code>、<code>数组</code>、<code>类</code>、<code>函数</code></p>
<h4 data-id="heading-27">1. object && &#123;&#125;</h4>
<p>其实这俩意思一样，<code>&#123;&#125;</code>、<code>object</code>表示非原始类型，也就是除<code>number</code>，<code>string</code>，<code>boolean</code>，<code>symbol</code>，<code>null</code>或<code>undefined</code>之外的类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> list: object = &#123;&#125; <span class="hljs-comment">// 空对象</span>

<span class="hljs-keyword">const</span> list1: object = <span class="hljs-literal">null</span>; <span class="hljs-comment">// null对象</span>

<span class="hljs-keyword">const</span> list: object = [] <span class="hljs-comment">// 数组对象</span>

<span class="hljs-keyword">const</span> list: &#123;&#125; = &#123;&#125;
list.name = <span class="hljs-number">1</span> <span class="hljs-comment">// 报错 不可更改里面的字段，但是可以读取</span>
list.toString()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">2. 数组</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> list: [] = []; <span class="hljs-comment">// 定义一个数组类型</span>

<span class="hljs-keyword">const</span> list1: number[] = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>] <span class="hljs-comment">// 定义一个数组，里面值必须是number</span>

<span class="hljs-keyword">const</span> list2: object[] = [<span class="hljs-literal">null</span>, &#123;&#125;, []] <span class="hljs-comment">// 定义一个数组里面必须是对象类型的</span>

<span class="hljs-keyword">const</span> list3: <span class="hljs-built_in">Array</span><number> = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>] <span class="hljs-comment">// 泛型定义数组必须是number类型，泛型我们待会讲到</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">3. 类</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClassPerson</span> </span>= &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>
&#125;

<span class="hljs-keyword">const</span> person: ClassPerson = <span class="hljs-keyword">new</span> Person();
person.xxx = <span class="hljs-number">123</span>; <span class="hljs-comment">// 这行代码报错，因为当前类中不存在该xxx属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">4. 函数</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 函数</span>
<span class="hljs-keyword">const</span> fn: <span class="hljs-function">() =></span> string = <span class="hljs-function">() =></span> <span class="hljs-string">"前端掘金人"</span> <span class="hljs-comment">// 定义一个变量必须是函数类型的，返回值必须是string类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">3. 函数类型注解</h3>
<p>这里说一下函数显示注解和函数参数不会类型推导问题。</p>
<h4 data-id="heading-32">1. 函数返回类型为number</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">a, b</span>): <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
fn(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">2. 函数void</h4>
<p>显示注解为<code>void</code>类型，函数没有返回值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">3. 函数不会自动类型推导</h4>
<p>可以看到下面的函数类型，不会自动类型推导，我们实参虽然传入的1和2，但是形参方面是可以接受任意类型值的，所以系统也识别不出来你传递的什么，所以这里得需要我们显示定义注解类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testFnQ</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b
&#125;
testFnQ(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af23516214a5455aa77fc9c9bc2441cb~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>微信截图_20210824233905.png</p>
<p>我们来改造一下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testFnQ</span>(<span class="hljs-params">a:number, b:number</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b
&#125;
testFnQ(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f2988ccc2bb42ec99c5a0dff115c308~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们再来看一下参数对象显示注解类型，也是在<code>:</code>号后面赋值每个字段类型即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testFnQ</span>(<span class="hljs-params">obj : &#123;num: number&#125;</span>) </span>&#123;
    <span class="hljs-keyword">return</span> obj.num
&#125;
testFnQ(&#123;<span class="hljs-attr">num</span>: <span class="hljs-number">18</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">4. 元组Tuple</h3>
<p>元组用于表示一个已知数组的数量和类型的数组，定义数组中每一个值的类型，一般不经常使用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr: [string, number] = [<span class="hljs-string">"前端掘金人"</span>, <span class="hljs-number">1</span>]

<span class="hljs-keyword">const</span> arr: [string, string] = [<span class="hljs-string">"前端掘金人"</span>, <span class="hljs-number">1</span>] <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">5. 枚举Enum</h3>
<p><code>Enum</code>枚举类型，可以设置默认值，如果不设置则为索引。</p>
<pre><code class="hljs language-js copyable" lang="js">enum color &#123;
    RED,
    BLUE = <span class="hljs-string">"blue"</span>,
    GREEN = <span class="hljs-string">"green"</span>
&#125;

<span class="hljs-comment">// color["RED"] 0</span>
<span class="hljs-comment">// color["BLUE"] blue</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像上面的<code>color</code>中<code>RED没</code>有设置值，那么它的值则为<code>0</code>，如果<code>BLUE</code>也不设置的话那么它的值则是<code>1</code>，它们这里是递增。如果设置值则是返回设置的值</p>
<p><strong>注意这里还有一个问题，直接来上代码</strong></p>
<p>通过上面学习我们知道了<code>enum</code>可以递增值，也可以设置默认值。但是有一点得注意一下，<code>enum</code>没有<code>json</code>对象那样灵活，<code>enum</code>不能在任意字段上设置默认值。</p>
<p>比如下面栗子，<code>RED</code>没有设置值，然后<code>BLUE</code>设置了默认值，但是<code>GREEN</code>又没有设置，这时这个<code>GREEN</code>会报错。因为你第二个<code>BLUE</code>设置完默认值，第三又不设置，这时代码都不知道该咋递增了，所以报错。还有一种方案就是你给<code>BLUE</code>可以设置一个数字值，这时第三个<code>GREEN</code>不设置也会跟着递增，因为都是<code>number</code>类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 报错</span>
enum color &#123;
    RED,
    BLUE = <span class="hljs-string">"blue"</span>,
    GREEN
&#125;

<span class="hljs-comment">// good</span>
enum color &#123;
    RED,    <span class="hljs-comment">// 0</span>
    BLUE = <span class="hljs-number">4</span>,  <span class="hljs-comment">// 4</span>
    GREEN      <span class="hljs-comment">// 5</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如<code>enum</code>枚举类型还可以反差，通过<code>value</code>查<code>key</code>值。像我们<code>json</code>对象就是不支持这种写法的。</p>
<pre><code class="hljs language-js copyable" lang="js">enum color &#123;
    RED,    <span class="hljs-comment">// 0</span>
    BLUE = <span class="hljs-number">4</span>,  <span class="hljs-comment">// 4</span>
    GREEN      <span class="hljs-comment">// 5</span>
&#125;

<span class="hljs-built_in">console</span>.log(color[<span class="hljs-number">4</span>]) <span class="hljs-comment">// BLUE</span>
<span class="hljs-built_in">console</span>.log(color[<span class="hljs-number">0</span>]) <span class="hljs-comment">// RED</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">5. 接口Interface</h3>
<p>接口<code>interface</code>是什么，接口<code>interface</code>就是方便我们定义一处代码，多处复用。接口里面也存在一些修饰符。下面我们来认识一下它们吧。</p>
<h4 data-id="heading-38">1. 接口怎么复用</h4>
<p>比如在讲到这之前，我们不知道<code>接口</code>这东西，可能需要给对象定义一个类型的话，你可能会这样做。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> testObj: &#123; <span class="hljs-attr">name</span>: string, <span class="hljs-attr">age</span>: number &#125; = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;

<span class="hljs-keyword">const</span> testObj1: &#123; <span class="hljs-attr">name</span>: string, <span class="hljs-attr">age</span>: number &#125; = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"蛙人"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们用接口来改造一下。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Types &#123;
    <span class="hljs-attr">name</span>: string, 
    <span class="hljs-attr">age</span>: number
&#125;

<span class="hljs-keyword">const</span> testObj: Types = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;

<span class="hljs-keyword">const</span> testObj1: Types = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"蛙人"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到使用<code>interface</code>关键字定义一个接口，然后赋值给这两个变量，实现复用。</p>
<h4 data-id="heading-39">2. readonly修饰符</h4>
<p><code>readonly</code>类型，只可读状态，不可更改。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Types &#123;
    readonly name: string, 
    readonly age: number
&#125;

<span class="hljs-keyword">const</span> testObj: Types = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;

<span class="hljs-keyword">const</span> testObj1: Types = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"蛙人"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;

testObj.name = <span class="hljs-string">"张三"</span> <span class="hljs-comment">// 无法更改name属性，因为它是只读属性</span>
testObj1.name = <span class="hljs-string">"李四"</span> <span class="hljs-comment">// 无法更改name属性，因为它是只读属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-40">3. ?可选修饰符</h4>
<p>可选修饰符以<code>?</code>定义，为什么需要可选修饰符呢，因为如果我们不写<code>可选修饰符</code>，那<code>interface</code>里面的属性都是必填的。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Types &#123;
    readonly name: string, 
    readonly age: number,
    sex?: string
&#125;

<span class="hljs-keyword">const</span> testObj: Types = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-41">4. extends继承</h4>
<p>我们的<code>interface</code>也是可以继承的，跟<strong>ES6</strong><code>Class</code>类一样，使用<code>extends</code>关键字。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Types &#123;
    readonly name: string, 
    readonly age: number,
    sex?: string
&#125;

interface ChildrenType <span class="hljs-keyword">extends</span> Types &#123; 
    <span class="hljs-comment">// 这ChildrenType接口就已经继承了父级Types接口</span>
    <span class="hljs-attr">hobby</span>: []
&#125;
    
<span class="hljs-keyword">const</span> testObj: ChildrenType = &#123; 
    <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>, 
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>， 
    <span class="hljs-attr">hobby</span>: [<span class="hljs-string">"code"</span>, <span class="hljs-string">"羽毛球"</span>] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-42">5. propName扩展</h4>
<p>interface里面这个功能就很强大，它可以写入不在interface里面的属性。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Types &#123;
    readonly name: string, 
    readonly age: number,
    sex?: string,
&#125;

<span class="hljs-keyword">const</span> testObj: Types = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">19</span>, <span class="hljs-attr">hobby</span>: [] &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个<code>testObj</code>这行代码会爆红，因为<code>hobby</code>属性不存在<code>interface</code>接口中，那么我们不存在的接口中的，还不让人家写了？。这时候可以使用<strong>自定义</strong>就是上面的<code>propName</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Types &#123;
    readonly name: string, 
    readonly age: number,
    sex?: string,
    [propName: string]: any <span class="hljs-comment">// propName字段必须是 string类型 or number类型。 值是any类型，也就是任意的</span>
&#125;

<span class="hljs-keyword">const</span> testObj: Types = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">19</span>, <span class="hljs-attr">hobby</span>: [] &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在运行上面代码，就可以看到不爆红了~</p>
<h3 data-id="heading-43">6. Type</h3>
<p>我们再来看一下<code>Type</code>，这个是声明类型别名使的，别名类型只能定义是：<code>基础静态类型</code>、<code>对象静态类型</code>、<code>元组</code>、<code>联合类型</code>。</p>
<blockquote>
<p>注意：type别名不可以定义interface</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">type Types = string;

type TypeUnite = string | number

<span class="hljs-keyword">const</span> name: typeUnite = <span class="hljs-string">"前端掘金人"</span>
<span class="hljs-keyword">const</span> age: typeUnite = <span class="hljs-number">18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-44">1. 那么type类型别名和interface接口有什么区别呢</h4>
<h5 data-id="heading-45">1. type不支持interface声明</h5>
<pre><code class="hljs language-js copyable" lang="js">type Types = number
type Types = string <span class="hljs-comment">// 报错， 类型别名type不允许出现重复名字</span>

interface Types1 &#123;
    <span class="hljs-attr">name</span>: string
&#125;

interface Types1 &#123;
    <span class="hljs-attr">age</span>: number
&#125;

<span class="hljs-comment">// interface接口可以出现重复类型名称，如果重复出现则是，合并起来也就是变成 &#123; name：string, age: number &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个<code>Types</code>类型别名type不允许出现重复名字，interface接口可以出现重复类型名称，如果重复出现则是，合并起来也就是变 <code>&#123; name：string, age: number &#125;</code></p>
<p><strong>再来看一下interface另一种情况</strong></p>
<pre><code class="hljs language-js copyable" lang="js">interface Types1 &#123;
    <span class="hljs-attr">name</span>: string
&#125;

interface Types1 &#123;
    <span class="hljs-attr">name</span>: number
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到上面两个同名称的<code>interface</code>接口，里面的属性也是同名称，但是类型不一样。这第二个的<code>Types1</code>就会爆红，提示：<strong>后续声明的接口，必须跟前面声明的同名属性类型必须保持一致</strong>，把后续声明的<code>name</code>它类型换成<code>string</code>即可。</p>
<h5 data-id="heading-46">2. type支持表达式 interface不支持</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count: number = <span class="hljs-number">123</span>
type testType = <span class="hljs-keyword">typeof</span> count

<span class="hljs-keyword">const</span> count: number = <span class="hljs-number">123</span>

interface testType &#123;
    [name: <span class="hljs-keyword">typeof</span> count]: any <span class="hljs-comment">// 报错</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到上面<code>type</code>支持表达式，而<code>interface</code>不支持</p>
<h5 data-id="heading-47">3. type 支持类型映射，interface不支持</h5>
<pre><code class="hljs language-js copyable" lang="js">type keys = <span class="hljs-string">"name"</span> | <span class="hljs-string">"age"</span>  
type KeysObj = &#123;
    [propName <span class="hljs-keyword">in</span> keys]: string
&#125;

<span class="hljs-keyword">const</span> PersonObj: KeysObj = &#123; <span class="hljs-comment">// 正常运行</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">"蛙人"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-string">"18"</span>
&#125; 

interface testType &#123;
    [propName <span class="hljs-keyword">in</span> keys]: string <span class="hljs-comment">// 报错</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-48">7. 联合类型</h3>
<p><code>联合类型</code>用<code>|</code>表示，说白了就是满足其中的一个<code>类型</code>就可以。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> statusTest: string | number = <span class="hljs-string">"前端掘金人"</span>

<span class="hljs-keyword">const</span> flag: boolean | number = <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看一下栗子。我们用函数参数使用<strong>联合类型</strong>看看会发生什么</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testStatusFn</span>(<span class="hljs-params">params: number | string</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(params.toFixed()) <span class="hljs-comment">// 报错</span>
&#125;

testStatusFn(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们说过了，函数参数类型不能类型自动推导，更何况现在用上<strong>联合类型</strong>，系统更懵逼了，不能识别当前实参的类型。所以访问当前类型上的方法报错。</p>
<p>接下来带大家看一些<code>类型保护</code>，听着挺高级，其实这些大家都见过。</p>
<h4 data-id="heading-49">1. typeof</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testStatusFn</span>(<span class="hljs-params">params: number | string</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(params.toFixed()) <span class="hljs-comment">// 报错</span>
&#125;
testStatusFn(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>改造后</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 正常</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testStatusFn</span>(<span class="hljs-params">params: string | number</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> params == <span class="hljs-string">"string"</span>) &#123;
        <span class="hljs-built_in">console</span>.log(params.split)
    &#125;

    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> params == <span class="hljs-string">"number"</span>) &#123;
        <span class="hljs-built_in">console</span>.log(params.toFixed)
    &#125;
&#125;

testStatusFn(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-50">2. in</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 报错</span>
interface frontEnd &#123;
    <span class="hljs-attr">name</span>: string
&#125;

interface backEnd &#123;
    <span class="hljs-attr">age</span>: string
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testStatusFn</span>(<span class="hljs-params">params: frontEnd | backEnd</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(params.name)
&#125;

testStatusFn(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"蛙人"</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>改造后</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 正常</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testStatusFn</span>(<span class="hljs-params">params: frontEnd | backEnd</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-string">"name"</span> <span class="hljs-keyword">in</span> params) &#123;
        <span class="hljs-built_in">console</span>.log(params.name)
    &#125;

    <span class="hljs-keyword">if</span> (<span class="hljs-string">"age"</span> <span class="hljs-keyword">in</span> params) &#123;
        <span class="hljs-built_in">console</span>.log(params.age)
    &#125;
&#125;

testStatusFn(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"蛙人"</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-51">3. as 断言</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 报错</span>
interface frontEnd &#123;
    <span class="hljs-attr">name</span>: string
&#125;

interface backEnd &#123;
    <span class="hljs-attr">age</span>: string
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testStatusFn</span>(<span class="hljs-params">params: frontEnd | backEnd</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(params.name)
&#125;

testStatusFn(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"蛙人"</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>改造后</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 正常</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testStatusFn</span>(<span class="hljs-params">params: frontEnd | backEnd</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-string">"name"</span> <span class="hljs-keyword">in</span> params) &#123;
        <span class="hljs-keyword">const</span> res = (params <span class="hljs-keyword">as</span> frontEnd).name
        <span class="hljs-built_in">console</span>.log(res)
    &#125;
    
    
    <span class="hljs-keyword">if</span> (<span class="hljs-string">"age"</span> <span class="hljs-keyword">in</span> params) &#123;
        <span class="hljs-keyword">const</span> res = (params <span class="hljs-keyword">as</span> backEnd).age
        <span class="hljs-built_in">console</span>.log(res)
    &#125;
&#125;

testStatusFn(&#123;<span class="hljs-attr">age</span>: <span class="hljs-number">118</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-52">8. 交叉类型</h3>
<p><code>交叉类型</code>就是跟联合类型相反，它用<code>&</code>表示，<code>交叉类型</code>就是两个类型必须存在。这里还用上面的<strong>联合类型</strong>的栗子来看下。</p>
<pre><code class="hljs language-js copyable" lang="js">interface frontEnd &#123;
    <span class="hljs-attr">name</span>: string
&#125;

interface backEnd &#123;
    <span class="hljs-attr">age</span>: number
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testStatusFn</span>(<span class="hljs-params">params: frontEnd & backEnd</span>) </span>&#123;&#125;

testStatusFn(&#123;<span class="hljs-attr">age</span>: <span class="hljs-number">118</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们可以看到实参必须传入两个**接口(interface)**全部的属性值才可以。<strong>联合类型</strong>是传入其中类型就可以。</p>
<p><strong>注意：我们的接口interface出现同名属性</strong></p>
<pre><code class="hljs language-js copyable" lang="js">interface frontEnd &#123;
    <span class="hljs-attr">name</span>: string
&#125;

interface backEnd &#123;
    <span class="hljs-attr">name</span>: number
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testStatusFn</span>(<span class="hljs-params">params: frontEnd & backEnd</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(params)
&#125;

testStatusFn(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"前端"</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们两个接口类型中都出现了同名属性，但是类型不一样，这时类型就会变为<code>never</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adeb8195f3a74209adcbc504190455ac~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-53">9. 泛型</h3>
<p>泛型是<code>TypeScript</code>中最难理解的了，这里我尽量用通俗易懂的方式讲明白。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">a: string | number, b: string | number</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a, b)
&#125;
test(<span class="hljs-number">1</span>, <span class="hljs-string">"前端掘金人"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如上面栗子，函数参数<code>注解类型</code>定义<code>string</code>和<code>number</code>，调用函数实参传入也没什么问题，但是有个需求，就是实参我们<strong>必须传入同样的类型</strong>（传入两个<code>number</code>类型）。虽然上面这种<strong>联合类型</strong>也可以实现，但是如果我们要在加一个<code>boolean</code>类型，那么<strong>联合类型</strong>还得在追加一个<code>boolean</code>，那这样代码太冗余了。</p>
<p>这时就需要用到<strong>泛型</strong>了，<strong>泛型</strong>是专门针对不确定的类型使用，并且灵活。泛型的使用大部分都是使用<code><T></code>，当然也可以随便使用，如：<code><Test></code>、<code><Custom></code>都可以。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span><<span class="hljs-title">T</span>>(<span class="hljs-params">a: T, b: T</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a, b)
&#125;
test<number>(<span class="hljs-number">1</span>, <span class="hljs-string">"前端掘金人"</span>) <span class="hljs-comment">// 调用后面跟着尖括号这就是泛型的类型，这时报错，因为在调用的使用类型是number，所以只能传入相同类型的</span>

test<boolean>(<span class="hljs-literal">true</span>, <span class="hljs-literal">false</span>) 

test<string>(<span class="hljs-string">"前端掘金人"</span>, <span class="hljs-string">"蛙人"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这使用<strong>泛型</strong>就解决了我们刚才说的传入同一个类型参数问题，但是<strong>泛型</strong>也可以使用不同的参数，可以把调用类型定义为<code><any></code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span><<span class="hljs-title">T</span>>(<span class="hljs-params">a: T, b: T</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a, b)
&#125;

test<any>(<span class="hljs-number">1</span>, <span class="hljs-string">"前端掘金人"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是上面这种又有一种问题，它可以传入对象，但是如果我们只希望传入<code>number</code>类型和<code>string</code>类型。那么我们<strong>泛型</strong>也给我们提供了**<code>约束</code><strong>类型。<strong>泛型</strong>使用<code>extends</code>进行了</strong>类型约束**，只能选择<code>string</code>、<code>number</code>类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">number</span> | <span class="hljs-title">string</span>, <span class="hljs-title">Y</span> <span class="hljs-title">extends</span> <span class="hljs-title">number</span> | <span class="hljs-title">string</span>>(<span class="hljs-params">a: T, b: Y</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a, b)
&#125;

test<number, string>(<span class="hljs-number">18</span>, <span class="hljs-string">"前端掘金人"</span>)

test<string, number>(<span class="hljs-string">"前端掘金人"</span>, <span class="hljs-number">18</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时，传入泛型时使用<code>，</code>逗号分隔，来定义每一个类型希望是什么。记住，只有我们不确定的类型，可以使用泛型。</p>
<h3 data-id="heading-54">10. 模块</h3>
<p><code>TypeScript</code>也支持<code>import</code>和<code>export</code>这里大多数小伙伴都知道，这里都不多讲啦。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导入</span>

<span class="hljs-keyword">import</span> xxx, &#123; xxx &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./xxx"</span>

<span class="hljs-comment">// 导出</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> name = <span class="hljs-string">"前端掘金人"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如有不明白的小伙伴，可以看我以前文章 聊聊什么是CommonJs和Es Module及它们的区别[1]</p>
<h3 data-id="heading-55">11. Class类</h3>
<blockquote>
<p>以下这三个修饰符是在<code>TypeScript</code>类中才能使用，在<code>JavaScript</code>类中是不支持的。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb99e07ec49349019b6a72df54513666~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>报错.png</p>
<h4 data-id="heading-56">1. public</h4>
<p><code>public</code>为<code>类</code>的公共属性，就是不管在<code>类</code>的内部还是外部，都可以访问该<code>类</code>中<strong>属性</strong>及<strong>方法</strong>。默认定义的<strong>属性</strong>及<strong>方法</strong>都是<code>public</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
 name = <span class="hljs-string">"前端掘金人"</span>;
 public age = <span class="hljs-number">18</span>;
&#125;
<span class="hljs-keyword">const</span> res = <span class="hljs-keyword">new</span> Person();
<span class="hljs-built_in">console</span>.log(res.name, res.age) <span class="hljs-comment">// 前端掘金人 18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面可以看到打印结果都能显示出来，<code>name</code>属性没有定义<code>public</code>公共属性，所以<code>类</code>里面定义的<strong>属性</strong>及<strong>方法</strong>默认都是<code>public</code>定义。</p>
<h4 data-id="heading-57">2. private</h4>
<p><code>private</code>为<code>类</code>的私有属性，只有在当前<code>类</code>里面才能访问，当前<code>类</code>就是<code>&#123;&#125;</code>里面区域内。在<code>&#123;&#125;</code>外面是不能访问<code>private</code>定义的<strong>属性</strong>及<strong>方法</strong>的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
 private name = <span class="hljs-string">"前端掘金人"</span>;
 private age = <span class="hljs-number">18</span>;
&#125;
<span class="hljs-keyword">const</span> res = <span class="hljs-keyword">new</span> Person();
<span class="hljs-built_in">console</span>.log(res.name, res.age) <span class="hljs-comment">// 这俩行会爆红，当前属性为私有属性，只能在类内部访问</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Scholl</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.username + <span class="hljs-string">","</span> + <span class="hljs-built_in">this</span>.age
    &#125;
&#125;
<span class="hljs-keyword">const</span> temp = <span class="hljs-keyword">new</span> Scholl()
<span class="hljs-built_in">console</span>.log(temp.getData()) <span class="hljs-comment">// 爆红~，虽然继承了Person类，但是private定义是只能在当前类访问，子类也不能访问。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-58">3. protected</h4>
<p><code>protected</code>为<code>类</code>的保护属性，只有在<strong>当前类</strong>和<strong>子类</strong>可以访问。也就是说用<code>protected</code>属性定义的<strong>子类</strong>也可以访问。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    protected username = <span class="hljs-string">"前端掘金人"</span>;
    protected age = <span class="hljs-number">18</span>;
&#125;
<span class="hljs-keyword">const</span> res = <span class="hljs-keyword">new</span> Person();
<span class="hljs-built_in">console</span>.log(res.name, res.age) <span class="hljs-comment">// 这俩行会爆红，当前属性为私有属性，只能在类内部访问</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Scholl</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">getData</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.username + <span class="hljs-string">","</span> + <span class="hljs-built_in">this</span>.age
    &#125;
&#125;
<span class="hljs-keyword">const</span> temp = <span class="hljs-keyword">new</span> Scholl()
<span class="hljs-built_in">console</span>.log(temp.getData()) <span class="hljs-comment">// 前端掘金人，18。可以正常访问父类的属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-59">4. implements</h4>
<p><code>implements</code>关键字只能在<code>class</code>中使用，顾名思义，实现一个新的类，从父级或者从接口实现所有的属性和方法，如果在<code>PersonAll</code>类里面不写进去接口里面已有的属性和方法则会报错。</p>
<pre><code class="hljs language-js copyable" lang="js">interface frontEnd &#123;
    <span class="hljs-attr">name</span>: string,
    <span class="hljs-attr">fn</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PersonAll</span> <span class="hljs-title">implements</span> <span class="hljs-title">frontEnd</span> </span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>;
    
    <span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span> &#123;
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-60">5. 抽象类</h4>
<p>抽象类使用<code>abstract</code>关键字定义。<code>abstract</code>抽象方法不能实例化，如果，抽象类里面方法是抽象的，那么本身的类也必须是抽象的，抽象方法不能写函数体。父类里面有抽象方法，那么子类也必须要重新该方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 抽象类</span>
abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Boss</span> </span>&#123;
    name = <span class="hljs-string">"秦"</span>;
    <span class="hljs-function"><span class="hljs-title">call</span>(<span class="hljs-params"></span>)</span> &#123;&#125; <span class="hljs-comment">// 抽象方法不能写函数体</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Boss</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">call</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"A"</span>)
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Boss</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">call</span>(<span class="hljs-params"></span>)</span> &#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"B"</span>)
    &#125;
&#125;

<span class="hljs-keyword">new</span> A().call()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该抽象类使用场景，比如<code>A</code>需求或者<code>B</code>需求正好需要一个公共属性，然后本身还有一些自己的逻辑，就可以使用抽象类，抽象类只能在<code>TypeScript</code>中使用。</p>
<h3 data-id="heading-61">12. 命名空间namespace</h3>
<p>我们学到现在可以看到，不知道小伙伴们发现没有，项目中文件是不是不能有重复的变量(不管你是不是一样的文件还是其它文件)，否则就直接爆红了。命名空间一个最明确的目的就是解决重名问题。</p>
<p>命名空间使用<code>namespace</code>关键字来定义，来看栗子吧。</p>
<p><strong>index.ts</strong></p>
<pre><code class="hljs language-js copyable" lang="js">namespace SomeNameSpaceName &#123; 
    <span class="hljs-keyword">const</span> q = &#123;&#125;

    <span class="hljs-keyword">export</span> interface obj &#123;
        <span class="hljs-attr">name</span>: string
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这样，就定义好了一个命名空间，可以看到变量<code>q</code>没有写<code>export</code>关键字，这证明它是内部的变量，就算别的<code>.ts</code>文件引用它，它也不会暴露出去。而<code>interface</code>这个<code>obj</code>接口是可以被全局访问的。</p>
<p><strong>我们在别的页面访问当前命名空间</strong></p>
<h4 data-id="heading-62">1. reference引入</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/// <reference path="./index.ts" /></span>
namespace SomeNameSpaceName &#123; 
 <span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">person</span> <span class="hljs-title">implements</span> <span class="hljs-title">obj</span> </span>&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-63">2. import</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface valueData &#123;
     <span class="hljs-attr">name</span>: string
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; valueData &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./xxx.ts"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时使用命名空间之后完全可以解决不同文件重名爆红问题。</p>
<h3 data-id="heading-64">13. tsConfig.json</h3>
<p>这个<code>tsconfig</code>文件，是我们编译ts文件，如何将<code>ts</code>文件编译成我们的<code>js</code>文件。<code>tsc -init</code>这个命令会生成该文件出来哈。执行完该命令，我们可以看到根目录下会生成一个<code>tsconfig.json</code>文件，里面有一堆属性。</p>
<p>那么我们怎么将<code>ts</code>文件编译成<code>js</code>文件呢，直接执行<code>tsc</code>命令可以将根目录下所有的<code>.ts</code>文件全部编译成<code>.js</code>文件输出到项目下。</p>
<p>更多配置文档，请参考官网[2]</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-comment">// include: ["*.ts"] // 执行目录下所有的ts文件转换成js文件</span>
    <span class="hljs-comment">// include: ["index.ts"] // 只将项目下index.ts文件转换为js文件</span>
    <span class="hljs-comment">// files: ["index.ts"] // 跟include一样，只执行当前数组值里面的文件,当前files必须写相对路径</span>
    <span class="hljs-comment">// exclude: ["index.ts"] // exclude就是除了index.ts不执行，其它都执行</span>
    
    <span class="hljs-attr">compilerOptions</span>: &#123;
        <span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 去掉编译完js文件的注释</span>
        <span class="hljs-attr">outDir</span>: <span class="hljs-string">"./build"</span>, <span class="hljs-comment">// 最终输出的js文件目录</span>
        <span class="hljs-attr">rootDir</span>: <span class="hljs-string">"./src"</span>, <span class="hljs-comment">// ts入口文件查找</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-65">八、实用类型</h2>
<p>最后来说一下实用类型，<code>TypeScript</code>标准库自带了一些实用类型。这些实用类都是方便接口<code>Interface</code>使用。这里只列举几个常用的，更多实用类型官网[3]</p>
<h3 data-id="heading-66">1. Exclude</h3>
<p>从一个类型中排除另一个类型，只能是<strong>联合类型</strong>，从<code>TypesTest</code>类型中排除<code>UtilityLast</code>类型。</p>
<p><strong>适用于：并集类型</strong></p>
<pre><code class="hljs language-js copyable" lang="js">interface UtilityFirst &#123;
    <span class="hljs-attr">name</span>: string
&#125;

interface UtilityLast &#123;
    <span class="hljs-attr">age</span>: number
&#125;

type TypesTest = UtilityFirst | UtilityLast;

<span class="hljs-keyword">const</span> ObjJson: Exclude<TypesTest, UtilityLast> = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-67">2. Extract</h3>
<p><code>Extract</code>正好跟上面那个相反，这是选择某一个可赋值的<strong>联合类型</strong>，从<code>TypesTest</code>类型中只选择<code>UtilityLast</code>类型。</p>
<p><strong>适用于：并集类型</strong></p>
<pre><code class="hljs language-js copyable" lang="js">interface UtilityFirst &#123;
    <span class="hljs-attr">name</span>: string
&#125;

interface UtilityLast &#123;
    <span class="hljs-attr">age</span>: number
&#125;

type TypesTest = UtilityFirst | UtilityLast;

<span class="hljs-keyword">const</span> ObjJson: Extract<TypesTest, UtilityLast> = &#123;
    <span class="hljs-attr">age</span>: <span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-68">3. Readonly</h3>
<p>把数组或对象的所有属性值转换为只读的。这里只演示一下对象栗子，数组同样的写法。</p>
<p><strong>适用于：对象、数组</strong></p>
<pre><code class="hljs language-js copyable" lang="js">interface UtilityFirst &#123;
    <span class="hljs-attr">name</span>: string
&#125;

<span class="hljs-keyword">const</span> ObjJson: Readonly<UtilityFirst> = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"前端掘金人"</span>
&#125;
ObjJson.name = <span class="hljs-string">"蛙人"</span> <span class="hljs-comment">// 报错 只读状态</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-69">4. Partial</h3>
<p>把对象的所有属性设置为选的。我们知道<code>interface</code>只要不设置<code>?</code>修饰符，那么对象都是必选的。这个实用类可以将属性全部转换为可选的。</p>
<p><strong>适用于：对象</strong></p>
<pre><code class="copyable">interface UtilityFirst &#123;
    name: string
&#125;

const ObjJson: Partial<UtilityFirst> = &#123;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-70">5. Pick</h3>
<p><code>Pick</code>选择对象类型中的部分<code>key</code>值，提取出来。第一个参数<code>目标值</code>，第二个参数<strong>联合</strong><code>key</code></p>
<p><strong>适用于：对象</strong></p>
<pre><code class="copyable">interface UtilityFirst &#123;
    name: string,
    age: number,
    hobby: []
&#125;

const ObjJson: Pick<UtilityFirst, "name" | "age"> = &#123;
    name: "前端掘金人",
    age: 18
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-71">6. Omit</h3>
<p><code>Omit</code>选择对象类型中的部分<code>key</code>值，过滤掉。第一个参数<code>目标值</code>，第二个参数<strong>联合</strong><code>key</code></p>
<p><strong>适用于：对象</strong></p>
<pre><code class="copyable">interface UtilityFirst &#123;
    name: string,
    age: number,
    hobby: string[]
&#125;

const ObjJson: Pick<UtilityFirst, "name" | "age"> = &#123;
    hobby: ["code", "羽毛球"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-72">7. Required</h3>
<p><code>Required</code>把对象所有可选属性转换成必选属性。</p>
<p><strong>适用于：对象</strong></p>
<pre><code class="copyable">interface UtilityFirst &#123;
    name?: string,
    age?: number,
    hobby?: string[]
&#125;

const ObjJson: Required<UtilityFirst> = &#123;
    name: "蛙人",
    age: 18,
    hobby: ["code"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-73">8. Record</h3>
<p>创建一个对象结果集，第一个参数则是<code>key</code>值，第二个参数则是<code>value</code>值。规定我们只能创建这里面字段值。</p>
<p><strong>适用于：对象</strong></p>
<pre><code class="copyable">type IndexList = 0 | 1 | 2

const ObjJson: Record<IndexList, "前端掘金人"> = &#123;
    0: "前端掘金人",
    1: "前端掘金人",
    2: "前端掘金人"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            