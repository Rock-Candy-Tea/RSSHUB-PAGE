
---
title: 'console也能玩出新花样，效果nice！！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e334dbc7f11144d2a5fc5c29cb2a0f12~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 19:27:43 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e334dbc7f11144d2a5fc5c29cb2a0f12~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<p>相信大部分朋友在使用console的基本只是使用其中的<code>log</code>方法吧，本文将介绍其中更有趣的玩法</p>
</blockquote>
<h2 data-id="heading-0">获取代码块运行时间</h2>
<p>日常中开发需要优化代码块，那么怎么知道优化的空间有多大呢，这时候如果能准确记录代码块运行时间那就有优劣之分了，来，让我们看看代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.time(<span class="hljs-string">"执行时间"</span>);
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
  <span class="hljs-comment">// 执行相关代码</span>
  count++;
&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"执行时间"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e334dbc7f11144d2a5fc5c29cb2a0f12~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807104116533.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">个性打印</h2>
<p>使用<code>%c</code>格式化打印，能给被打印内容添加自定义css样式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">`%c 这是自定义打印 内容 `</span>, <span class="hljs-string">"background:#286fb9;color:white;"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2afcd0d46e044742a8d2b37f7d703307~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807102802512.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">清空控制台</h2>
<p>有时候我们会遇到多人合作的场景，李磊开发A模块，小明开发B模块，阿银开发子模块C。由于处于开发阶段，李磊，小明，阿银都分别打印了很多条（每人5条）控制台信息进行调试，这时候代码合并后再继续开发。噢天，满屏的信息打印出来，自己不想去删除别人的代码，又要从满屏的打印记录中查找自己所需要的信息，简直崩溃，好在阿银学会了<code>console.clear()</code>方法，在自己开发模块的开头位置使用一下<code>clear</code>方法，即可舒舒服服的继续开发</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">"李磊信息：这是第一条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"李磊信息：这是第二条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"李磊信息：这是第三条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"李磊信息：这是第四条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"李磊信息：这是第五条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"小明信息：这是第一条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"小明信息：这是第二条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"小明信息：这是第三条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"小明信息：这是第四条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"小明信息：这是第五条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.clear();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"阿银信息：这是第一条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"阿银信息：这是第二条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"阿银信息：这是第三条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"阿银信息：这是第四条emmmmmmmmm......................"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"阿银信息：这是第五条emmmmmmmmm......................"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p>​清空前：</p>
<h2 data-id="heading-3"><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dff164d21c0b47eca5d4f1c7a5442ca2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807105205632.png" loading="lazy" referrerpolicy="no-referrer"></h2>
<p>​清空后：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5809811a29f74a2d98f6f8aa7941e6e0~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807105315320.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">常用输出内容</h2>
<p>这一块主要根据不同的指令输出不同的样式类型，让人联想起elementUI中的<code>$message</code>组件，和它类似，有<strong>error|warn|info</strong>，</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.error(<span class="hljs-string">"这是一条错误"</span>);
<span class="hljs-built_in">console</span>.warn(<span class="hljs-string">"这是一个警告"</span>);
<span class="hljs-built_in">console</span>.info(<span class="hljs-string">"这是一条信息"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"这是一条日志"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p>​chrome：<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5787dc352dcd4faa895947fdab36844e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807110529380.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​    火狐：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec244dcdd0714bda9e1d3b92cc09b2af~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807110625825.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​ 对于info打印有一点区别，火狐的前面有个icon，个人比较喜欢火狐的这种展示。反观chrome，info和log没什么区别。</p>
<h2 data-id="heading-5">输出信息分组</h2>
<p>顾名思义：可以将多个输出合并到一个组下面，也就是分类的意思</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.group(<span class="hljs-string">"用户数据"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"数据A： 1"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"数据B： 2"</span>);
<span class="hljs-built_in">console</span>.groupEnd();<span class="hljs-comment">// 切记，如果不想让后面的打印也加入分组，要手动调用 groupEnd 方法，声明分组结束</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"a"</span>, a);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/962a420ad6c04e4f95fe6f371611b375~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807111409407.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ac3b1b4e85046839f2939fb715860b7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807111428613.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">本章小结</h2>
<p>关于console的多种打印基本使用，总结就到这了，代码没什么难度，平常多多使用即可玩出不一样的控制台~~~</p></div>  
</div>
            