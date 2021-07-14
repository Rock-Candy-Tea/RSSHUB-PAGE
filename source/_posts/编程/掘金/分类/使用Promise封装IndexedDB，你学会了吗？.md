
---
title: '使用Promise封装IndexedDB，你学会了吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fd8740d183c4a8b9139ea2445e54b66~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 19:18:13 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fd8740d183c4a8b9139ea2445e54b66~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">使用Promise封装IndexedDB</h2>
<blockquote>
<p>IndexedDB是大型NoSQL存储系统。它使你几乎可以将任何内容存储在用户的浏览器中。除了通常增删改查外，IndexedDB还支持事务。</p>
</blockquote>
<h3 data-id="heading-1">为何使用IndexdDB</h3>
<p>IndexedDB 具有以下特点</p>
<ol>
<li>IndexedDB 数据库存储键值对。 IndexedDB 内部采用对象仓库（object store）存放数据。所有类型的数据都可以直接存入，包括 JavaScript 对象。对象仓库中，数据以"键值对"的形式保存，每一个数据记录都有对应的主键，主键是独一无二的，不能有重复，否则会抛出一个错误。</li>
<li>IndexedDB API主要是异步的。 IndexedDB 操作时不会锁死浏览器，用户依然可以进行其他操作，这与 LocalStorage 形成对比，后者的操作是同步的。异步设计是为了防止大量数据的读写，拖慢网页的表现。</li>
<li>IndexedDB 构建在事务数据库模型上。 IndexedDB 支持事务（transaction），这意味着一系列操作步骤之中，只要有一步失败，整个事务就都取消，数据库回滚到事务发生之前的状态，不存在只改写一部分数据的情况。</li>
<li>同源限制 IndexedDB 受到同源限制，每一个数据库对应创建它的域名。网页只能访问自身域名下的数据库，而不能访问跨域的数据库。</li>
<li>储存空间大 IndexedDB 的储存空间比 LocalStorage 大得多，全局限制为硬盘的50%，组的限制为硬盘的20%。某些浏览器会限制每次写入130M</li>
<li>支持二进制储存。 IndexedDB 不仅可以储存字符串，还可以储存二进制数据（ArrayBuffer 对象和 Blob 对象）。</li>
</ol>
<h3 data-id="heading-2">原生过程实现</h3>
<p>IndexedDB 虽好但是用法没有LocalStorage 简单，我们先来看下步骤与写法。</p>
<ol>
<li>首先打开数据库 -> indexedDB.open() -> IDBDatabase</li>
<li>开始一个事务 -> IDBDatabase.transaction() -> IDBTransaction ->IDBObjectStore</li>
<li>新建数据库 (IDBObjectStore.createObjectStore())</li>
<li>新增数据 (IDBObjectStore.add())、读取数据 (IDBObjectStore.get())、更新数据 (IDBObjectStore.put())、删除数据 (IDBObjectStore.delete())</li>
<li>遍历数据 (IDBObjectStore.openCursor())</li>
</ol>
<h4 data-id="heading-3">1.打开数据库</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// IDBOpenDBRequest  表示打开数据库的请求</span>
<span class="hljs-keyword">const</span> request: IDBOpenDBRequest  = indexedDB.open( databaseName, version );
<span class="hljs-comment">// 版本更新，创建新的store的时候</span>
request.onupgradeneeded = <span class="hljs-function">(<span class="hljs-params"> event </span>) =></span> &#123;
 <span class="hljs-comment">// // IDBDatabase 表示与数据库的连接。这是获取数据库事务的唯一方法。</span>
 <span class="hljs-keyword">const</span> db: IDBDatabase = event.target.result;
 <span class="hljs-keyword">if</span> ( db.objectStoreNames.contains( stroeName ) === <span class="hljs-literal">false</span> ) &#123;
   db.createObjectStore( stroeName, &#123;<span class="hljs-attr">keyPath</span>: <span class="hljs-string">'key'</span>&#125; );
 &#125;
 openSuccess(db);
&#125;;
request.onsuccess = <span class="hljs-function">(<span class="hljs-params"> event </span>) =></span> &#123;
 <span class="hljs-comment">// IDBDatabase 表示与数据库的连接。这是获取数据库事务的唯一方法。</span>
 <span class="hljs-keyword">const</span> db: IDBDatabase = event.target.result;
 openSuccess(db);
&#125;;
request.onerror = <span class="hljs-function">(<span class="hljs-params"> event </span>) =></span> &#123;
 <span class="hljs-built_in">console</span>.error( <span class="hljs-string">'IndexedDB'</span>, event );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2.开始一个事务</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">openSuccess</span> (<span class="hljs-params">db: IDBDatabase</span>) </span>&#123;
 <span class="hljs-attr">transaction</span>: IDBTransaction = db.transaction( [ storeName ], <span class="hljs-string">'readwrite'</span> );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3.获取<code>IDBObjectStore</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">openSuccess</span> (<span class="hljs-params">db: IDBDatabase</span>) </span>&#123;
 <span class="hljs-attr">transaction</span>: IDBTransaction = db.transaction( [ storeName ], <span class="hljs-string">'readwrite'</span> );
 objectStore: IDBObjectStore = transaction.objectStore(storeName);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">4.<strong>增删改查以 新增为例</strong></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> request: IDBRequest = objectStore.add(data);
request.onsuccess = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"> event </span>) </span>&#123;&#125;;
request.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"> event </span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">5.遍历数据</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> request = objectStore.openCursor();
request.onsuccess = <span class="hljs-function">(<span class="hljs-params"> event </span>) =></span> &#123;
 <span class="hljs-keyword">let</span> cursor = event.target.result;
 <span class="hljs-comment">// 没有数据可遍历时 cursor === null</span>
 <span class="hljs-keyword">if</span> (cursor !== <span class="hljs-literal">null</span>) &#123;
   callback(cursor.value);
   <span class="hljs-comment">// 下一个</span>
   cursor.continue();
 &#125;
&#125;;
request.onerror = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
 callback(event)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原生写法使用效果:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fd8740d183c4a8b9139ea2445e54b66~tplv-k3u1fbpfcp-watermark.image" alt="2546b1d8ceb582a0.gif" loading="lazy" referrerpolicy="no-referrer">
<strong>原生写法缺点</strong>：</p>
<ul>
<li>获取objectStrore路径过长</li>
<li>回调函数过多</li>
<li>扩展性差</li>
</ul>
<p>所以我们来尝试使用Promise + class 封装 IndexedDB API</p>
<h3 data-id="heading-8">Promise代码实现</h3>
<p>其实关键点是 objectStore获取比较复杂，经过open，transaction。我们获取后将这个对象缓存下来，然后增删改查操作都通过一个getObjectStore方法获取ObjectStore对象。</p>
<p>整个结构如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DB</span> </span>&#123;
 <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">databaseName, version, storeOptions</span>)</span> &#123;&#125;
 <span class="hljs-comment">/**
  * 打开数据库
  */</span>
 <span class="hljs-function"><span class="hljs-title">open</span>(<span class="hljs-params">databaseName, version, storeOptions</span>)</span> &#123;&#125;
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">_getTransaction</span>(<span class="hljs-params">storeName, version</span>)</span> &#123;&#125;
 <span class="hljs-comment">/**
  * 获取store
  */</span>
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">_getObjectStore</span>(<span class="hljs-params">storeName, version</span>)</span> &#123;&#125;
 <span class="hljs-comment">/**
 * 获取一个store
 */</span>
 <span class="hljs-function"><span class="hljs-title">collection</span>(<span class="hljs-params">storeName, version</span>)</span> &#123;
   <span class="hljs-built_in">this</span>.currentStore = storeName;
   <span class="hljs-built_in">this</span>._getObjectStore(storeName, version);
   <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
 &#125;
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">data</span>)</span> &#123;&#125;
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">data</span>)</span> &#123;&#125;
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params">data</span>)</span> &#123;&#125;
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">put</span>(<span class="hljs-params">data</span>)</span> &#123;&#125;
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params">storeName</span>)</span> &#123;&#125;
 <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">each</span>(<span class="hljs-params">callback</span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面提到获取ObjectStore需要通过transaction获取，而transaction通过indexedDB.open() 获取</p>
<p>首先初始化一下重要参数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">databaseName, version, storeOptions</span>)</span> &#123;
 <span class="hljs-comment">// 缓存数据库名称：name + version为key</span>
 <span class="hljs-built_in">this</span>._dbs = &#123;&#125;;
 <span class="hljs-built_in">this</span>._databaseName = databaseName;
 <span class="hljs-built_in">this</span>.open(databaseName, version, storeOptions);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>open需要监听onupgradeneeded ，版本更新时会进入触发此事件，这种情况要创建好store和主键，不然事务那边会获取失败</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">open</span>(<span class="hljs-params">databaseName, version, storeOptions</span>)</span> &#123;
   <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
     <span class="hljs-comment">// 有缓存的情况</span>
     <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._dbs[databaseName + version]) &#123;
       resolve(<span class="hljs-built_in">this</span>._dbs[databaseName + version]);
       <span class="hljs-keyword">return</span>;
     &#125;

      <span class="hljs-keyword">const</span> request = indexedDB.open(databaseName, version);
       <span class="hljs-comment">// 版本更新，创建新的store的时候</span>
      request.onupgradeneeded = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
          <span class="hljs-comment">// IDBDatabase</span>
         <span class="hljs-keyword">const</span> database = event.target.result;
         <span class="hljs-comment">// 缓存起来</span>
         <span class="hljs-built_in">this</span>._dbs[databaseName + version] = database;
         <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> storeOptions) &#123;
           <span class="hljs-keyword">if</span> (database.objectStoreNames.contains(key) === <span class="hljs-literal">false</span>) &#123;
             <span class="hljs-keyword">const</span> keyPath = storeOptions[key] ? storeOptions[key] : [];
             database.createObjectStore(key, &#123; keyPath &#125;);
            &#125;
         &#125;
         resolve(database);
      &#125;;
     request.onsuccess = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
       <span class="hljs-comment">// IDBDatabase</span>
       <span class="hljs-keyword">const</span> database = event.target.result;
       <span class="hljs-comment">// 缓存起来</span>
       <span class="hljs-built_in">this</span>._dbs[databaseName + version] = database;
       resolve(database);
     &#125;;
     request.onerror = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
       reject(event);
       <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'IndexedDB'</span>, event);
     &#125;;
   &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来是获取事务并通过事务得到ObjectStore对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">_getTransaction</span>(<span class="hljs-params">storeName, version</span>)</span> &#123;
 <span class="hljs-keyword">let</span> db;
 <span class="hljs-comment">// 先从缓存获取</span>
 <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._dbs[<span class="hljs-built_in">this</span>._databaseName + version]) &#123;
   db = <span class="hljs-built_in">this</span>._dbs[<span class="hljs-built_in">this</span>._databaseName + version];
 &#125; <span class="hljs-keyword">else</span> &#123;
   db = <span class="hljs-built_in">this</span>.open(<span class="hljs-built_in">this</span>._databaseName, version);
 &#125;
 <span class="hljs-keyword">return</span> db.transaction( [ storeName ], <span class="hljs-string">'readwrite'</span> );
&#125;

<span class="hljs-comment">/**
 * 获取store
 * ObjectStore: 表示允许访问IndexedDB数据库中的一组数据的对象存储，
 */</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">_getObjectStore</span>(<span class="hljs-params">storeName, version</span>)</span> &#123;
 <span class="hljs-keyword">let</span> transaction = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>._getTransaction(storeName, version);
 <span class="hljs-keyword">return</span> transaction.objectStore( storeName );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拿到ObjectStore后可以直接操作增删改查了，这几个方法比较简单，通过Promise包一层就行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">data</span>)</span> &#123;
   <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
     <span class="hljs-built_in">this</span>._getObjectStore(<span class="hljs-built_in">this</span>.currentStore).then(<span class="hljs-function">(<span class="hljs-params">objectStore</span>) =></span> &#123;
       <span class="hljs-keyword">const</span> request = objectStore.get(data);
       request.onsuccess = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"> event </span>) </span>&#123;
         resolve(event.target.result);
       &#125;;
       request.onerror = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
         reject(event);
       &#125;
      &#125;);
   &#125;);
&#125;

<span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">data</span>)</span> &#123;
 <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
     <span class="hljs-built_in">this</span>._getObjectStore(<span class="hljs-built_in">this</span>.currentStore).then(<span class="hljs-function">(<span class="hljs-params">objectStore</span>) =></span> &#123;
       <span class="hljs-keyword">const</span> request = objectStore.add(data);
       request.onsuccess = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"> event </span>) </span>&#123;
         resolve(event.target.result);
       &#125;;
       request.onerror = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
         reject(event);
       &#125;
     &#125;);
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params">data</span>)</span> &#123;
 <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
     <span class="hljs-built_in">this</span>._getObjectStore(<span class="hljs-built_in">this</span>.currentStore).then(<span class="hljs-function">(<span class="hljs-params">objectStore</span>) =></span> &#123;
       <span class="hljs-keyword">const</span> request = objectStore.delete(data);
       request.onsuccess = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"> event </span>) </span>&#123;
         resolve(event.target.result);
       &#125;;
       request.onerror = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
         reject(event);
       &#125;
     &#125;);
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-title">put</span>(<span class="hljs-params">data</span>)</span> &#123;
 <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
     <span class="hljs-built_in">this</span>._getObjectStore(<span class="hljs-built_in">this</span>.currentStore).then(<span class="hljs-function">(<span class="hljs-params">objectStore</span>) =></span> &#123;
       <span class="hljs-keyword">const</span> request = objectStore.put(data);
       request.onsuccess = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"> event </span>) </span>&#123;
         resolve(event.target.result);
       &#125;;
       request.onerror = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
         reject(event);
       &#125;
     &#125;);
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params">storeName</span>)</span> &#123;
 <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
     <span class="hljs-built_in">this</span>._getObjectStore(<span class="hljs-built_in">this</span>.currentStore).then(<span class="hljs-function">(<span class="hljs-params">objectStore</span>) =></span> &#123;
       <span class="hljs-keyword">const</span> request = objectStore.clear(data);
       request.onsuccess = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"> event </span>) </span>&#123;
         resolve(event.target.result);
       &#125;;
       request.onerror = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
         reject(event);
       &#125;
     &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">成果展示</h3>
<p>最终使用起来就简洁了很多</p>
<ul>
<li>简化创建一个DB的步骤</li>
<li>缓存了objectStore</li>
<li>API Promise化，使用更简洁</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/370e6262b804478fb3546ddfc8dbee92~tplv-k3u1fbpfcp-watermark.image" alt="2cc4a1c8870e16b2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> DB <span class="hljs-keyword">from</span> <span class="hljs-string">'./BD'</span>;

<span class="hljs-comment">/* 打开数据库并开始一个事务 */</span>
<span class="hljs-comment">// open -> transaction -> objectStore</span>
<span class="hljs-keyword">const</span> db = <span class="hljs-keyword">new</span> DB(<span class="hljs-string">'db'</span>, &#123; <span class="hljs-attr">store</span>: <span class="hljs-string">'id'</span> &#125;);

<span class="hljs-keyword">const</span> store = db.collection(<span class="hljs-string">'store'</span>);

<span class="hljs-keyword">const</span> data = [
    &#123;
 <span class="hljs-attr">name</span>: <span class="hljs-string">'甲'</span>,
 <span class="hljs-attr">id</span>: <span class="hljs-number">100</span>,
    &#125;,
    &#123;
 <span class="hljs-attr">name</span>: <span class="hljs-string">'乙'</span>,
 <span class="hljs-attr">id</span>: <span class="hljs-number">1001</span>,
    &#125;,
];

<span class="hljs-comment">/* 增 */</span>
store.add(data[<span class="hljs-number">1</span>]).then(<span class="hljs-function"><span class="hljs-params">ev</span> =></span> &#123;  
 store.add(data[<span class="hljs-number">0</span>])
 store.add(data[<span class="hljs-number">1</span>])
&#125;);

<span class="hljs-comment">/* 删 */</span>
store.delete(data[<span class="hljs-number">0</span>].id).then(<span class="hljs-function"><span class="hljs-params">ev</span> =></span> &#123;
 <span class="hljs-built_in">console</span>.log(ev);
&#125;);

<span class="hljs-comment">/* 改 */</span>
store.put(data[<span class="hljs-number">0</span>]).then(<span class="hljs-function">(<span class="hljs-params">ev</span>) =></span> &#123;
 <span class="hljs-comment">// store.put(data[0]).then(ev => &#123;</span>
 <span class="hljs-comment">// &#125;);</span>
 store.get(data[<span class="hljs-number">0</span>].id).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
   <span class="hljs-built_in">console</span>.log(result);
 &#125;);
&#125;);

<span class="hljs-comment">/* 查 */</span>
store.get(data[<span class="hljs-number">0</span>].id).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
 <span class="hljs-built_in">console</span>.log(result);
&#125;);

<span class="hljs-comment">/* 遍历 */</span>
store.each(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
 <span class="hljs-built_in">console</span>.log(result);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">总结</h3>
<blockquote>
<p>如果碰到前端频繁存储操作或者大文件缓存的需求，可以考虑使用IndexedDB。当然项目中推荐直接使用第三方库<a href="https://link.juejin.cn/?target=https%3A%2F%2Ferikolson186.github.io%2Fzangodb%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://erikolson186.github.io/zangodb/" ref="nofollow noopener noreferrer">zangodb</a>、<a href="https://link.juejin.cn/?target=http%3A%2F%2Fdexie.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://dexie.org/" ref="nofollow noopener noreferrer">dexie.js</a> API更丰富。</p>
</blockquote></div>  
</div>
            