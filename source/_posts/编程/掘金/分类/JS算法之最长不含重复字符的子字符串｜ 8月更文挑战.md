
---
title: 'JS算法之最长不含重复字符的子字符串｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e064b7b72ebd445aa9865510683427a2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 07:41:10 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e064b7b72ebd445aa9865510683427a2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">最长不含重复字符的子字符串</h2>
<blockquote>
<p>剑指Offer 48.最长不含重复字符的子字符串</p>
<p>难度：中等</p>
<p>题目：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fproblems%2Fzui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/" ref="nofollow noopener noreferrer">leetcode-cn.com/problems/zu…</a></p>
</blockquote>
<p>请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。</p>
<p>示例1：</p>
<pre><code class="copyable"> 输入: "abcabcbb"
 输出: 3 
 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例2：</p>
<pre><code class="copyable"> 输入: "bbbbb"
 输出: 1
 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例3：</p>
<pre><code class="copyable"> 输入: "pwwkew"
 输出: 3
 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：s.length <= 40000</p>
<h2 data-id="heading-1">题解</h2>
<p>一个长度为N的字符串共有1+2+3+...N = (1/2)<em>N</em>(1+N)个子字符串，而判断子字符串是否有重复的复杂度为O(N)，因此暴力法的话复杂度为O(N^3)，显然这种方法AC不了。</p>
<p>首先，我们可以考虑使用动态规划来降低时间复杂度。</p>
<p>步骤：</p>
<ul>
<li>
<p>设dp[j]为以j结尾的“最长不重复子字符串”的长度。</p>
</li>
<li>
<p>固定右边界j，设字符s[j]左边距离最近且相等的字符为s[i]，以字符s[j - 1]结尾的子字符串sub[j - 1] ，其长度为dp[j - 1]，注意sub[j - 1]中字符不重复。在j的左侧寻找一个重复的字符s[i]，需要分两种情况：</p>
<ul>
<li><strong>索引i在字符串sub[j - 1]区间外</strong>，也就是sub[j-1]左边界的更左侧，则dp[j-1] < j - i，，由于sub[j - 1]中字符不重复，且当前最长，因此子字符串sub[j - 1]在后面接上s[j]即可，其长度dp[j] = dp[j - 1]。</li>
<li><strong>索引i在字符串sub[j - 1]区间内</strong>，则dp[j - 1] ≥ j - i，则sub[j]的左边界只能是i了，其长度dp[j] = j - i。</li>
</ul>
<p>这里举个例子，如<code>[abcdbaa]</code>，索引从0开始，当j=4时，sub[4] = “cbd”，长度dp[4] = 3；当j = 5时，s[0] = s[5]且s[0]在sub[4]之外，因此长度dp[5] = dp[4] + 1；当j = 6时，s[5]=s[6]且s[5]在sub[5]内，则dp[6] = j - i = 1。</p>
<p>因此，公式为：</p>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e064b7b72ebd445aa9865510683427a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>返回dp中最大值即为“最长不重复子字符串”的长度。这里可以借助一个变量tmp存粗dp[j]，每轮循环的时候更新最大值即可，可以省创建dp数组O(N)的空间。</li>
</ul>
<h3 data-id="heading-2">法一 动态规划 + 哈希表</h3>
<p>使用哈希表来统计<strong>各字符最后一次出现的索引位置</strong>，遍历到s[j]时，可通过哈希表dic[s[j]]获取最佳的相同字符的索引i。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">/**
  * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
  * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number&#125;</span></span>
  */</span>
 <span class="hljs-keyword">var</span> lengthOfLongestSubstring = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">s</span>) </span>&#123;
   <span class="hljs-keyword">let</span> dic = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
   <span class="hljs-keyword">let</span> res = <span class="hljs-number">0</span>,
     tmp = <span class="hljs-number">0</span>;
   <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < s.length; j++) &#123;
     <span class="hljs-keyword">let</span> i = dic.has(s[j]) ? dic.get(s[j]) : -<span class="hljs-number">1</span>;
     dic.set(s[j], j);
     tmp = tmp < j - i ? tmp + <span class="hljs-number">1</span> : j - i;
     res = <span class="hljs-built_in">Math</span>.max(res, tmp);
   &#125;
   <span class="hljs-keyword">return</span> res;
 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>时间复杂度：O(N)</li>
<li>空间复杂度：O(1)</li>
</ul>
<h3 data-id="heading-3">法二 动态规划 + 遍历</h3>
<p>遍历到s[j]时，初始化索引i = j - 1，向左遍历搜索第一个满足s[i] = s[j]字符即可。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">var</span> lengthOfLongestSubstring = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">s</span>) </span>&#123;
   <span class="hljs-keyword">let</span> res = <span class="hljs-number">0</span>, tmp = <span class="hljs-number">0</span>;
   <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < s.length; j++)&#123;
     <span class="hljs-keyword">let</span> i = j - <span class="hljs-number">1</span>;
     <span class="hljs-keyword">while</span>(i >= <span class="hljs-number">0</span> && s[i] !== s[j]) i--;
     tmp = tmp < j - i ? tmp + <span class="hljs-number">1</span> : j - i;
     res = <span class="hljs-built_in">Math</span>.max(res, tmp);
   &#125;
   <span class="hljs-keyword">return</span> res;
 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>时间复杂度：O(N^2)</li>
<li>空间复杂度：O(1)</li>
</ul>
<h3 data-id="heading-4">法三 滑动窗口</h3>
<p>使用哈希表dic统计s[j]<strong>最后一次出现的索引</strong>，步骤如下：</p>
<ul>
<li>更新左边界i，根据上轮做边界i和dic[s[j]]，每次更新左边界i都要保证[i + 1, j]内无重复字符且最大：「i=max(dic[s[j]],i)」</li>
<li>更新结果res，取上轮res和本轮滑动窗口[i +1 , j]的最大值（即j - i的最大值）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">var</span> lengthOfLongestSubstring = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">s</span>) </span>&#123;
   <span class="hljs-keyword">let</span> dic = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
   <span class="hljs-keyword">let</span> res = <span class="hljs-number">0</span>,
     i = -<span class="hljs-number">1</span>;
   <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < s.length; j++) &#123;
     <span class="hljs-keyword">if</span> (dic.has(s[j])) &#123;
       i = <span class="hljs-built_in">Math</span>.max(dic.get(s[j]), i);
     &#125;
     dic.set(s[j], j);
     res = <span class="hljs-built_in">Math</span>.max(res, j - i);
   &#125;
   <span class="hljs-keyword">return</span> res;
 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>时间复杂度：O(N)</li>
<li>空间复杂度：O(1)</li>
</ul></div>  
</div>
            