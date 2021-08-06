
---
title: '图解算法 _ LeetCode第 70 题爬楼梯问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b27eb76ab9d64f509df478e198bca64d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 15:50:18 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b27eb76ab9d64f509df478e198bca64d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近开始努力研究算法，遇到这个很有意思的题目，因为从中复习到斐波那契数列，又通过某篇资料，查到中科院官网，看了很多科普文章。深挖下去能看到很多东西。</p>
<p>本着热爱分享的初衷，整理本文与大家分享，题目本身没啥难度，欢迎一起交流，算法大佬求不喷，多谢。</p>
<p>进入主题。</p>
<hr>
<p>本题为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fclimbing-stairs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/climbing-stairs/" ref="nofollow noopener noreferrer">LeetCode第70题爬楼梯</a>，题目如下：</p>
<p>假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>
<p><strong>大家可以先想想</strong>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b27eb76ab9d64f509df478e198bca64d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="cover.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">流程分析</h2>
<p>本题中，可以每次可以走 1 级，也可以一次走 2 级，因此我们会有 3 种走法：</p>
<ul>
<li>全程任意走，如全部 1 级走；</li>
<li>前面任意走，最后一步只走 1 级；</li>
<li>前面任意走，最后一步只走 2 级；</li>
</ul>
<p>我画了几张图方便大家理解，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf5f70be6e0b4b4282e769d900a4636b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一种走法就不做详细介绍。</p>
<p>第二种走法，倒数第二步的走法如下，有 1 步和 2 步两种方式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f215d29ff724fb0bd049819addd6c51~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第三种走法，倒数第二步的走法如下，也有 1 步和 2 步两种方式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc4c7b66447549af84d7cc60fad99206~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面这个过程描述的是，从最后一层开始往下的每一层的走法。</p>
<p>在最后一步时，有 1 步和 2 步两种方式，可以理解为只能 1 步或者 2 步到达最后一层。</p>
<ul>
<li>当最后一步为 1 步时，即从 n-1 层开始；</li>
<li>当最后一步为 2 步时，即从 n-2 层开始；</li>
</ul>
<p>再理解一下这个过程，就是第 n 层的走法数量是第 n-1 层和第 n-2 层走法数量之和。</p>
<p>如果还不太理解，可以再看看前面的图。</p>
<h2 data-id="heading-1">归纳法分析</h2>
<p>当然，遇事不决，归纳法走起，我们可以列举几种情况进行分析：</p>








































<table><thead><tr><th align="center">台阶层数</th><th align="center">走法数量</th><th align="center">走法</th></tr></thead><tbody><tr><td align="center"><strong>1</strong></td><td align="center">1</td><td align="center">1</td></tr><tr><td align="center"><strong>2</strong></td><td align="center">2</td><td align="center">11、2</td></tr><tr><td align="center"><strong>3</strong></td><td align="center">3</td><td align="center">111、12、21</td></tr><tr><td align="center"><strong>4</strong></td><td align="center">5</td><td align="center">1111、112、121、211、22</td></tr><tr><td align="center"><strong>5</strong></td><td align="center">8</td><td align="center">11111、1112、1121、1211、2111、221、212、122</td></tr><tr><td align="center"><strong>...</strong></td><td align="center">...</td><td align="center">...</td></tr></tbody></table>
<p>可以发现有个简单的规律，当台阶层数为 n 层，它的走法数量就有 n-1 层的走法数量加上 n-2 层的走法数量。</p>
<p>记做：<code>f(n)=f(n-1)+f(n-2)</code>。</p>
<p>第 1 层固定 1 种走法；
第 2 层固定 2 种走法；
...
第 5 层走法的数量等于第 4 层加上第 5 层走法数量。</p>
<p>理解清楚整个流程规律以后，我们就可以编码就简单多了：</p>
<h2 data-id="heading-2">解法1：循环累加计算</h2>
<p>通过简单的循环累加就能得到结果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> climbStairs = <span class="hljs-function">(<span class="hljs-params">n = <span class="hljs-number">1</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span>(n <= <span class="hljs-number">2</span>) <span class="hljs-keyword">return</span> n;
    <span class="hljs-keyword">let</span> res = <span class="hljs-number">0</span>, n1 = <span class="hljs-number">1</span>, n2 = <span class="hljs-number">2</span>; <span class="hljs-comment">// n1 表示前 2 项，n2 表示前 1 项</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">3</span>; i<= n; i++)&#123;  <span class="hljs-comment">// 前两项值固定，因此从第 3 项开始循环</span>
        res = n1 + n2;
        n1 = n2;
        n2 = res;
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试下第 6 层的走法数量：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">climbStairs(<span class="hljs-number">6</span>); <span class="hljs-comment">// 13</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">解法2：递归计算</h2>
<p>按照 <code>f(n)=f(n-1)+f(n-2)</code>，这个方法更加简单：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> climbStairs = <span class="hljs-function">(<span class="hljs-params">n = <span class="hljs-number">1</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span>(n <= <span class="hljs-number">2</span>) <span class="hljs-keyword">return</span> n;
    <span class="hljs-keyword">return</span> climbStairs(n-<span class="hljs-number">1</span>) + climbStairs(n-<span class="hljs-number">2</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试下第 6 层的走法数量：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">climbStairs(<span class="hljs-number">6</span>); <span class="hljs-comment">// 13</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法比较简洁易懂，但递归比较费时，容易出现 LeetCode 超出时间限制的提示。</p>
<h2 data-id="heading-4">解法3：利用数组特性</h2>
<p>利用 <code>f(n)=f(n-1)+f(n-2)</code> 这个规律，先预设好前 2 项，再开始循环，最后返回数组最后一项即可：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> climbStairs = <span class="hljs-function"><span class="hljs-params">n</span> =></span> &#123;
    <span class="hljs-keyword">let</span> result = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>; i < n; i++) &#123;
        result.push(result[i-<span class="hljs-number">1</span>] + result[i-<span class="hljs-number">2</span>]);
    &#125;
    <span class="hljs-keyword">return</span> result[n-<span class="hljs-number">1</span>];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">解法4：利用 JavaScript ES6 新特性</h2>
<p>利用数组结构赋值操作： <code>[a, b] = [c, d]</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> climbStairs = <span class="hljs-function"><span class="hljs-params">n</span> =></span> &#123;
    <span class="hljs-keyword">let</span> a = b = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; i++) &#123;
        [a, b] = [b, a + b];
    &#125;
    <span class="hljs-keyword">return</span> a;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，大家还有其他解法，欢迎一起讨论~</p>
<h2 data-id="heading-6">拓展知识：每次可以走 1 步、2 步、3 步</h2>
<p>这里多增加了一次可以走 3 步，这时候最后一步会有以下情况：</p>
<ul>
<li>当最后一步为 1 步时，即从 n-1 层开始；</li>
<li>当最后一步为 2 步时，即从 n-2 层开始；</li>
<li>当最后一步为 3 步时，即从 n-3 层开始；</li>
</ul>
<p>改造一下前面解法，还是一样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> climbStairs = <span class="hljs-function">(<span class="hljs-params">n = <span class="hljs-number">1</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span>(n <= <span class="hljs-number">2</span>) <span class="hljs-keyword">return</span> n;
  <span class="hljs-keyword">if</span>(n == <span class="hljs-number">3</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">4</span>;
    <span class="hljs-keyword">return</span> climbStairs(n-<span class="hljs-number">1</span>) + climbStairs(n-<span class="hljs-number">2</span>) + climbStairs(n-<span class="hljs-number">3</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试下第 6 层的走法数量：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">climbStairs(<span class="hljs-number">6</span>); <span class="hljs-comment">// 24</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">拓展知识：斐波那契数列</h2>
<p>这一题主要考察的内容类似<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%2596%2590%25E6%25B3%25A2%25E9%2582%25A3%25E5%25A5%2591%25E6%2595%25B0%25E5%2588%2597%2F99145%3Ffr%3Daladdin" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97/99145?fr=aladdin" ref="nofollow noopener noreferrer">斐波那契数列（Fibonacci sequence）</a>的计算，如果你还不清楚什么是斐波那契数列，这边先简单介绍一下，另外推荐<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1is411E7df%3Ffrom%3Dsearch%26seid%3D8645707287599730898" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1is411E7df?from=search&seid=8645707287599730898" ref="nofollow noopener noreferrer">李永乐老师讲解的斐波那契的课</a>。</p>
<p>最早是有由数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入的，数列大致如：0、1、1、2、3、5、8、13、21、34、....。
认真观察，我们可以发现一个规律：<strong>从第 3 项开始，每一项的值都等于前两项之和</strong>。</p>
<p>在自然界中，存在着许许多多的斐波那契数列的排列方式，比如一棵普通的树，它的树枝生长情况就像下面这样：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f77f7fbf76fa4d829027a12bb34856b9~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片来源网络）</p>
<p>可以看到每一层枝干的数量为 1、2、3、5、8、...排列下去。当然还有很多其他的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd142236adc64ca790b0741547a0e8e8~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（自然界中各种各样的裴波那契螺旋，图片来源于网络）</p>
<p>根据斐波那契数列的规律，得到这样的公式 <code>f(n)=f(n-1)+f(n-2)</code> 。跟我们前面列的差不多。</p>
<h2 data-id="heading-8">总结</h2>
<p>这道题本身难度不大，但是如果没有理清流程和规律，很容易掉坑，写多余的代码。本文只列举四个简单实现方法，如果大家有其他实现方式，欢迎一起讨论~哈哈。</p></div>  
</div>
            