
---
title: '🍬 为什么 CSS 动画比 JavaScript 高效？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54110664c3694f2abc169e9ecebe9b3c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 02:04:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54110664c3694f2abc169e9ecebe9b3c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「话题写作」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力</a>。</p>
<blockquote>
<p>📢 大家好，我是小丞同学，一名准大二的前端爱好者</p>
<p>📢 这篇文章将<strong>欢快的</strong>带你了解一下 CSS 和 JS 动画的差别</p>
<p>📢 <strong>愿你忠于自己，热爱生活</strong></p>
</blockquote>
<h2 data-id="heading-0">引言</h2>
<p>讲到动画，当然是非常有意思的啦，你可以往上滑一下，看看上面的封面图，是不是相当的炫酷，以为我是代码写出来的吗？</p>
<p>那当然不可能啊，我这么摸鱼，怎么会为了个封面图上号呢</p>
<p>废话不多说，其实上面的动图用代码实现也不会很困难，这个图是用 canva 做出来的。</p>
<p>本文主要讲以下这些内容</p>
<ol>
<li>浏览器渲染流程</li>
<li>回流和重绘</li>
<li>CSS 动画</li>
<li>JS 动画</li>
<li>两者对比</li>
</ol>
<h2 data-id="heading-1">🍉 1. 浏览器的渲染流程</h2>
<p>渲染流程主要有4个步骤</p>
<ol>
<li>解析 HTML 生成DOM 树</li>
<li>解析 CSS 样式生成 CSSOM 树，CSSOM 树与 DOM 树结合生成 Render tree</li>
<li>布局 Render Tree 对每个节点进行布局处理，确定在屏幕上的位置</li>
<li>绘制 Render Tree，遍历渲染树将每个节点绘制出来</li>
</ol>
<p>为了优化用户体验，渲染引擎不会等到 HTML 解析完才创建布局渲染树</p>
<h3 data-id="heading-2"><strong>生成 DOM 树</strong></h3>
<p>DOM 树的构建是一个深度遍历过程，也就是说只有在所有子节点都构建好后才会去构建当前节点的下一个兄弟节点</p>
<h3 data-id="heading-3"><strong>生成 Render 树</strong></h3>
<p>生成 DOM 树的同时会生成 CSSOM 树，根据 CSSOM 和 DOM 树构建 Render Tree，渲染树包括颜色，尺寸等显示属性的矩形</p>
<h3 data-id="heading-4"><strong>DOM 树和 Render 树</strong></h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54110664c3694f2abc169e9ecebe9b3c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210822213018363" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">🍋 2. 回流和重绘</h2>
<p>CSS 中至关重要的概念</p>
<h3 data-id="heading-6">回流</h3>
<p>回流也叫<strong>重排</strong>，指<strong>几何属性</strong>需要改变的渲染。</p>
<p>每一次的回流都会将网页内容<strong>重新渲染</strong>，只是我们人眼感觉不到有任何变化，但是它确实是会清空页面的，再从页面的左上角的第一个像素点从左到右从上到下这样一点一点渲染，每次回流都会是这样的过程，只是感觉不到而已</p>
<blockquote>
<p>渲染树的节点发生改变，影响了该节点的几何属性，导致该节点位置发生变化，此时就会触发浏览器回流并重新生成渲染树。</p>
</blockquote>
<p>常见的几何属性：布局，尺寸这些可以用尺子量出来的属性</p>
<ul>
<li>display、float、grid</li>
<li>width、padding</li>
</ul>
<p>等</p>
<h3 data-id="heading-7">重绘</h3>
<p>重绘指更改<strong>外观属性</strong>而不影响<strong>集合属性</strong>的渲染，类似于颜色这些。相比于回流，重绘的作用不会那么强烈。</p>
<p>渲染树的节点发生改变，但不影响该节点的集合属性，回流对浏览器性能的消耗是远大于重绘的。并且回流就必然带来重绘，重绘不一定需要回流</p>
<p><strong>外观属性</strong></p>
<ul>
<li>clip，background</li>
<li>text</li>
</ul>
<p>等</p>
<p>在介绍完这些知识后我们来聊聊 CSS 动画</p>
<h2 data-id="heading-8">🍍 3. CSS3 动画</h2>
<p>这里我们只谈论 CSS3 的动画</p>
<p>CSS3 动画也被称为补间动画，原因是只需要添加关键帧的位置，其他的未定义的帧会被自动生成</p>
<p>因为我们只设置了几个关键帧的位置，所以在进行动画控制的时候比较困难，不能再半路暂停动画，或者在动画过程中添加一些其他操作，都不大容易</p>
<p>但是 CSS 动画也有很多的好处</p>
<ul>
<li>浏览器可以对动画进行优化</li>
<li>帧速不好的浏览器，CSS3 可以自然降级兼容</li>
<li>代码简单，调优方向固定</li>
</ul>
<h2 data-id="heading-9">🍎 4. JS 动画</h2>
<p>首先，JS 动画是逐帧动画，在时间帧上绘制内容，一帧一帧的，所以他的可再造性很高，几乎可以完成任何你想要的动画形式。但是由于逐帧动画的内容不一样，会增加制作的负担，占用比较大的资源空间。</p>
<p>但是它也有很多的优势</p>
<ul>
<li>细腻的动画</li>
<li>可控性高</li>
<li>炫酷高级的动画</li>
</ul>
<h2 data-id="heading-10">💯 5. CSS 动画与 JS 动画对比</h2>
<p>前面关于 CSS 动画和 JS 动画，都是一些概念性比较强的东西，不看也罢</p>
<p>说了这么多，到底为什么CSS动画要<strong>更高效</strong>呢？</p>
<h3 data-id="heading-11"><strong>第一点</strong></h3>
<p>从实现动画的复杂度来看，CSS 动画大多数都是补间动画，而 JS 动画是逐帧动画。当然这里我们不谈论实现的效果</p>
<h3 data-id="heading-12"><strong>第二点</strong></h3>
<p>编码的高效，采用 JS 去实现的动画，无论多简单的动画，都需要去控制整个过程，当然你可能会说可以采用一些库来解决这些问题，但是这些库的实际运行可能要比原生实现的效率要低的多</p>
<h3 data-id="heading-13"><strong>第三点</strong></h3>
<p>性能的高效，在我们前面讲到了回流和重绘，如果我们要操作一个元素向右移动，我们可能需要控制 <code>dom.style.left</code> 属性，每次来<strong>改变元素的位置</strong>，而结合我们所说的，<strong>几何属性</strong>的改变必然会引起<strong>回流</strong>，回流必然引起重绘，可想而知如果我们采用 JS 来实现动画，这个代价有多大，这会造成浏览器在不断的计算页面，从而导致浏览器内存堆积。同时由于 JavaScript 运行在浏览器的主线程中，主线程中还有其他的重要任务在运行，因而可能会受到干扰导致<strong>线程阻塞</strong>，从而<strong>丢帧</strong></p>
<p>而 CSS 的动画是运行在合成线程中的，不会阻塞主线程，并且在合成线程中完成的动作不会触发回流和重绘</p>
<p>当然还有一个重要的点：JS 动画运行在 CPU，而 CSS 动画运行在 GPU</p>
<p>总的来说， CSS动画的渲染成本小，并且它的执行效率高于 JavaScript 动画</p>
<hr>
<p>那我们什么时候使用 CSS 动画，什么时候使用 JS 动画呢？</p>
<p>我个人觉得</p>
<p><strong>只要能用 CSS 实现的动画，就不要采用 JS 去实现</strong>，可以多采用 CSS 预处理器去做更多复杂的动画，就像我之前用 SCSS 做的流星雨动画一样</p>
<p>如果动画相较复杂，我们可以采用 <code>JS + canvas</code> 去尝试，能不能实现</p>
<p>最后再考虑纯 JS 实现</p>
<hr>
<p>这篇文章可能还有很多值得探讨的地方，大佬们有什么看法或者不一样的见解可以一起交流以下~</p>
<blockquote>
<p>非常感谢您的阅读，欢迎提出你的意见，有什么问题欢迎指出，谢谢！🎈</p>
</blockquote></div>  
</div>
            