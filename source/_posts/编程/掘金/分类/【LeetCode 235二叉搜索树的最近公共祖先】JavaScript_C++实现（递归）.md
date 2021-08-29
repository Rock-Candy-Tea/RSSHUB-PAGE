
---
title: '【LeetCode 235.二叉搜索树的最近公共祖先】JavaScript_C++实现（递归）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f1fc320b61e4116a7e061c5f89f5812~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 17:55:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f1fc320b61e4116a7e061c5f89f5812~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<hr>
<blockquote>
<p><strong>说明:文章部分内容及图片出自网络，如有侵权请与我本人联系(主页有公众号:小攻城狮学前端)</strong></p>
<p>作者：<strong>小只前端攻城狮</strong>、
主页：<strong><a href="https://juejin.cn/user/3747558609661213" target="_blank" title="https://juejin.cn/user/3747558609661213">小只前端攻城狮的主页</a></strong>、
来源：<strong>掘金</strong></p>
<p>GitHub：<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FP-J27" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/P-J27" ref="nofollow noopener noreferrer">P-J27</a></strong>、
CSDN：<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_43745075" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_43745075" ref="nofollow noopener noreferrer">PJ想做前端攻城狮</a></strong></p>
<p><strong>著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。</strong></p>
</blockquote>
<hr>
<h4 data-id="heading-0">【LeetCode 235.二叉搜索树的最近公共祖先】JavaScript/C++实现（递归）</h4>
<p><strong>题目描述</strong>：给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。</p>
<p><strong>说明</strong>：</p>
<ol>
<li>所有节点的值都是唯一的。</li>
<li>p、q 为不同节点且均存在于给定的二叉搜索树中。</li>
</ol>
<p>例如，给定如下二叉搜索树: <code>root = [6,2,8,0,4,7,9,null,null,3,5]</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f1fc320b61e4116a7e061c5f89f5812~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>示例：</p>
<blockquote>
<p>输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。</p>
</blockquote>
<hr>
<h4 data-id="heading-1">思路分析</h4>
<p>只要理清递归中过程即可。注意这是一棵二叉搜索树，满足 <code>node.left.val < node.val < node.right.val</code>。</p>
<p>一共 4 种情况：</p>
<ol>
<li>如果 p 和 q 的节点在 root 的两侧，那么最近公共祖先节点就是 root</li>
<li>如果 p.val 或者 q.val 等于 root.val，那么最近公共祖先节点就是 p 或 q</li>
<li>如果情况 1 和 2 都不满足，说明 p 和 q 在 root 的同一侧：
<ul>
<li>若 root.val 大于 p.val 和 q.val，那么往左侧递归</li>
<li>若 root.val 小于 p.val 和 q.val，那么往右侧递归</li>
</ul>
</li>
</ol>
<hr>
<h4 data-id="heading-2">解法 1: JavaScript 实现</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">root</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">p</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;TreeNode&#125;</span> <span class="hljs-variable">q</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;TreeNode&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> lowestCommonAncestor = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, p, q</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (
    (root.val > p.val && root.val < q.val) ||
    (root.val < p.val && root.val > q.val) ||
    root.val === p.val ||
    root.val === q.val
  ) &#123;
    <span class="hljs-keyword">return</span> root;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (root.val > q.val) &#123;
    <span class="hljs-keyword">return</span> lowestCommonAncestor(root.left, p, q);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> lowestCommonAncestor(root.right, p, q);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h4 data-id="heading-3">解法 2: C++实现</h4>
<p>由于这题的剑指 offer 的题库中没提供 js 语言环境，我用 c++实现了思路:</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Solution</span> &#123;</span>
<span class="hljs-keyword">public</span>:
    <span class="hljs-function">TreeNode* <span class="hljs-title">lowestCommonAncestor</span><span class="hljs-params">(TreeNode* root, TreeNode* p, TreeNode* q)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (
            (root->val == p->val)
            || (root->val == q->val)
            || (root->val > q->val && root->val < p->val)
            || (root->val < q->val && root->val > p->val)
        ) &#123;
            <span class="hljs-keyword">return</span> root;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (root->val > q->val) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">lowestCommonAncestor</span>(root->left, p, q);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">lowestCommonAncestor</span>(root->right, p, q);
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>感谢阅读，希望能对你有所帮助,文章若有错误或者侵权，可以在评论区留言或在我的主页添加公众号联系我。</strong></p>
<p><strong>写作不易，如果觉得不错，可以「点赞」+「评论」 谢谢支持❤</strong></p></div>  
</div>
            