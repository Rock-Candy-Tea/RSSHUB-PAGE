
---
title: 'JS算法-最小覆盖子串'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1235'
author: 掘金
comments: false
date: Mon, 03 May 2021 03:41:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=1235'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本题来自<code>leetcode 第 76 题</code>。</p>
<h3 data-id="heading-0">题目描述</h3>
<p>给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。</p>
<p>注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。</p>
<p>示例 1：</p>
<pre><code class="copyable">输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例 2：</p>
<pre><code class="copyable">输入：s = "a", t = "a"
输出："a"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示：</p>
<ul>
<li>1 <= s.length, t.length <= 105</li>
<li>s 和 t 由英文字母组成</li>
</ul>
<h3 data-id="heading-1">解题思路</h3>
<ul>
<li>
<p>首先遍历子串t，并且设置map值。例如：子串t = "ABC"，Map(3) &#123;"A" => 1, "B" => 1, "C" => 1&#125;。记录map的size值。</p>
</li>
<li>
<p>然后右指针开始向后走，每找到一个map中存在的字符，该字符对应的值减1，该字符的值减为0时，map的size减1。</p>
</li>
<li>
<p>直到map的size为0时，开始移动左指针，并且记录当前的子串。</p>
</li>
<li>
<p>左指针移动过程中，每找到一个字符，设置map，size加1，接着继续外层循环，移动右指针。下次map的size减为0时，再移动左指针。</p>
</li>
<li>
<p>每次开始移动左指针时，当前子串是符合题目要求的情况，比较子串长度并取最小的子串即可取到最短符合条件的子串。</p>
</li>
</ul>
<h3 data-id="heading-2">代码展示</h3>
<p>双指针 + 哈希表 + 滑动窗口 + 字符串</p>
<pre><code class="copyable">/**
 * @param &#123;string&#125; s
 * @param &#123;string&#125; t
 * @return &#123;string&#125;
 */
var minWindow = function(s, t) &#123;
    const len = s.length;
    const map = new Map();
    let l = 0, r = 0, res = '';
    for (let i = 0; i < t.length; i++) &#123;
        const c = t[i];
        map.set(c, map.get(c) ? map.get(c) + 1 : 1);
    &#125;
    let mapSize = map.size;
    while (r < len) &#123;
        const c1 = s[r];
        if (map.has(c1)) &#123;
            map.set(c1, map.get(c1) - 1)
            if (map.get(c1) === 0) mapSize -= 1;
        &#125;
        while(mapSize === 0) &#123;
            const newRes = s.substring(l, r + 1);
            if (!res || res > newRes) &#123;
                res = newRes;
            &#125;
            const c2 = s[l];
            if (map.has(c2)) &#123;
                map.set(c2, map.get(c2) + 1);
                if (map.get(c2) === 1) mapSize += 1;
            &#125;
            l += 1;
        &#125;
        r += 1;
    &#125;
    return res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>复杂度分析：</p>
<p>时间复杂度：O(m + n)。m是字符串s的长度，n是字符串t的长度。</p>
<p>空间复杂度：O(k)。k是t中不重复字符的长度。</p>
<h3 data-id="heading-3">总结</h3>
<p>这道题对于理解双指针，滑动窗口，以及map数据类型和字符串操作挺有帮助。</p></div>  
</div>
            