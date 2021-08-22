
---
title: '细谈 JS 对象遍历的顺序问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4358'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 02:53:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=4358'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>可能有些同学听过在 JavaScript 中遍历对象顺序不固定的这一说法。事实上，这个说法不是特别准确。</p>
<p>对待遍历顺序，对象有一套自己既定的规则，在此规则下呢，对象的遍历顺序会受插入元素顺序的影响，但是不完全受插入元素先后顺序的影响。如果您有「必须按插入元素顺序遍历」的场景，可以考虑使用 <code>Map</code>。</p>
<p>遍历对象的方法有很多种，我们经常会使用的有 <code>for...in</code> ，除此之外，还有：</p>
<ol>
<li><code>Object.keys</code></li>
<li><code>Object.entries</code></li>
<li><code>Obejct.getOwnerProPertyNames</code></li>
<li><code>Reflect.ownKeys</code></li>
<li>......</li>
</ol>
<p>上面我们列的几个方法，都按照一样的规则去遍历对象。而实际的遍历规则会根据 key 值类型的不同而不同。</p>
<p>在一个对象中，如果我们的 key 值是像 <code>'1'</code>、<code>'200'</code>这种正整数格式的字符串。 遍历的顺序是按照 key 值的大小来排列的。</p>
<p>比如我们看这样的一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;&#125;

obj[<span class="hljs-string">'10'</span>] = <span class="hljs-string">'a'</span>;
obj[<span class="hljs-string">'9'</span>] = <span class="hljs-string">'b'</span>;
obj[<span class="hljs-number">8</span>] = <span class="hljs-string">'c'</span>;
obj[<span class="hljs-number">7</span>] = <span class="hljs-string">'d'</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(obj)) <span class="hljs-comment">//  ["7", "8", "9", "10"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们最后的遍历顺序完全忽视了插入顺序，并且，值得我们注意的是，在对象中，就算我们添加属性时的索引值是 Number 类型，最后的结果还是会被隐式的转为字符串。</p>
<p>数组作为对象的一种，也符合上面的规则，又或许，有上面的表现就是因为要兼容数组的缘故呢。除此之外，通过上面的规则，我们还可以推断出，对类数组（key 值是正整数且有 <code>length</code> 属性）进行遍历也是按照索引顺序的。</p>
<p>另外，如果我们的 key 值是不能转为正整数的字符串，这其中包括了可以转换为负数的字符串（ 如 <code>'-1'</code> ）、小数格式的字符串(如 <code>'1.0'</code> ) 和其他的字符串。他们的遍历顺序会比较符合直觉，就是插入对象的顺序：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj2 = &#123;&#125;

obj2[<span class="hljs-string">'1.1'</span>] = <span class="hljs-string">'a'</span>;
obj2[<span class="hljs-string">'1.0'</span>] = <span class="hljs-string">'b'</span>;
obj2[<span class="hljs-string">'-1'</span>] = <span class="hljs-string">'c'</span>;
obj2[<span class="hljs-string">'jack'</span>] = <span class="hljs-string">'d'</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(obj2)); <span class="hljs-comment">//  ["1.1", "1.0", "-1", "jack"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>事实上，对象的索引值的类型不仅可以是字符串，还可以是 <code>Symbol</code> 类型。对于 <code>Symbol</code> 类型而言，它的遍历顺序也是单纯的按照插入对象的顺序。</p>
<p>如果我们的对象综合了上面所有的情况，即一个对象的索引值出现了所有的类型（各种形式的字符串、<code>Symbol</code> 类型），它会：</p>
<ol>
<li>先按照我们上面提的关于正整数的规则遍历正整数部分</li>
<li>按接下来会插入顺序遍历剩下的字符串</li>
<li>最后再按照插入顺序遍历 <code>Symbol</code> 类型</li>
</ol>
<p>相信到这里，大家已经完全明白了对象的遍历顺序问题，最后还有一点值得大家注意的点，是 <code>for...in</code> 的遍历顺序问题。</p>
<p>最开始的时候，<code>for...in</code> 的遍历顺序并没有一个统一的标准，浏览器厂商会按照他们的喜好去设置 <code>for...in</code> 的遍历顺序。如果您对遍历顺序有要求并且要兼容老的浏览器版本，建议不使用它。后来 ES 2019 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftc39%2Fproposal-for-in-order" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tc39/proposal-for-in-order" ref="nofollow noopener noreferrer">一个提案</a> 对此现象进行了规范，现在 <code>for...in</code> 的顺序也遵循上面的规则。</p>
<p>尽管会遵循上面的规则，但是 <code>for...in</code> 还会遍历原型的属性。所以 <code>for...in</code> 的变量元素的规则是先按照我们上面讲的对象遍历规则去变量对象本身，接下来再按照此规则去遍历对象的原型，以此类推，直到遍历到顶部。</p>
<p>除了最后一个 <code>for...in</code> 的注意点之外，就没有其他的了，其实内容比较少。</p>
<p>这就是遍历对象的全部内容了，谢谢阅读。</p>
<p>祝大家周末愉快，我的外卖也到了，干饭去咯。</p></div>  
</div>
            