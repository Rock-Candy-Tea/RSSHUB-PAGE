
---
title: '常用浏览器API整理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9542246f1b5845b2a139fb548804adc9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 00:13:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9542246f1b5845b2a139fb548804adc9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>面向对象编程,目前还是主流,个人也比较喜欢细化组件、切割对象.这样看起来比较清晰、每个对象职责单一,不会混淆造成混乱.</p>
<p>前端经常会和浏览器打交道,在处理一些与浏览器相关的逻辑时,就会调用浏览器API,整理日常会用到的API对象.</p>
<h3 data-id="heading-0">URL</h3>
<p>构造、解析、规范化和编码URL.</p>
<h4 data-id="heading-1">创建URL对象</h4>
<p>构造参数说明</p>
<ul>
<li><code>url</code> 如果是绝对URL地址,则忽略第二个参数;如果是相对路径,则以base作为基准URL.</li>
<li><code>base</code> 基准URL,如果第一个参数url是绝对URL时,则不生效.</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 指定绝对ULR地址</span>
<span class="hljs-keyword">const</span> url = <span class="hljs-keyword">new</span> URL(<span class="hljs-string">'http://www.baidu.com'</span>)
<span class="hljs-comment">// 或者</span>
<span class="hljs-keyword">const</span> url = <span class="hljs-keyword">new</span> URL(<span class="hljs-string">''</span>,<span class="hljs-string">'http://www.baidu.com'</span>)

<span class="hljs-comment">// 存在路径时</span>
<span class="hljs-keyword">const</span> url = <span class="hljs-keyword">new</span> URL(<span class="hljs-string">'http://www.baidu.com/hello'</span>)
<span class="hljs-comment">// 或</span>
<span class="hljs-keyword">const</span> url = <span class="hljs-keyword">new</span> URL(<span class="hljs-string">'/hello'</span>,<span class="hljs-string">'http://www.baidu.com'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构造完的url实例对象有哪些属性呢 , 可以从图中获取该url地址中所有的数据信息:</p>
<p><code>origin\searchParams</code> 为只读属性 , 其他的属性则可以通过变量赋值进行设置.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9542246f1b5845b2a139fb548804adc9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210821141202812.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改相关属性：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改协议</span>
url.protocol = <span class="hljs-string">"ftp:"</span>         <span class="hljs-comment">// href: 'ftp://www.baidu.com/hello',</span>
<span class="hljs-comment">// 修改路径</span>
url.pathname = <span class="hljs-string">'/admin'</span>       <span class="hljs-comment">// href: 'ftp://www.baidu.com/admin',</span>
<span class="hljs-comment">// 追加hash</span>
url.hash = <span class="hljs-string">'app'</span>            <span class="hljs-comment">// href: 'ftp://www.baidu.com/admin#app',</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">实例方法</h4>
<ul>
<li><code>toString()</code> 返回整个URL地址</li>
<li><code>toJSON()</code> , 返回整个URL地址,同<code>url.href</code></li>
</ul>
<p>以为有啥不一样的地方,发现都是返现url地址.</p>
<p>还有静态方法,创建一个唯一的资源地址链接:</p>
<ul>
<li><code>createObjectURL()</code>  <code>File、Blog或MediaSource</code> 对象,返回唯一的blog链接.</li>
<li><code>revokeObjectURL()</code> 销毁之前createObjectURL的URL实例对象.</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// File 对象,或者blob数据</span>
<span class="hljs-keyword">const</span> dataUrl = URL.createObjectURL(<span class="hljs-string">'blob:**'</span>)

<span class="hljs-comment">// 销毁创建的实例 , 访问失效</span>
URL.revokeObjectURL(dataUrl)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">URLSearchParams 对象</h4>
<p>这个应该是我们经常会用到的,用于处理url的查询字符串.</p>
<p>在实例url中,存在<code>search</code> 和<code>searchParams</code>(只读)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// url实例追加一个查询条件</span>
url.search = <span class="hljs-string">'id=45'</span>
<span class="hljs-comment">// 重新读取时会包含 ? 注意</span>
<span class="hljs-built_in">console</span>.log(url.search)       <span class="hljs-comment">// ?id=45</span>

<span class="hljs-comment">// 获取实例URL的查询参数对象</span>
<span class="hljs-keyword">const</span> searchParams = url.searchParams
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">创建实例</h5>
<ul>
<li>可选的参数 传入会被解析,比如<code>?id=45</code> \ <code>id=45</code> 会忽略开头的 <code>?</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> searchParams = <span class="hljs-keyword">new</span> URLSearchParams()
<span class="hljs-comment">// ?id=45</span>
<span class="hljs-keyword">const</span> searchParams = <span class="hljs-keyword">new</span> URLSearchParams(<span class="hljs-string">"?id=45"</span>)    <span class="hljs-comment">// &#123; 'id' => '45' &#125;</span>
<span class="hljs-comment">// id=45&name=admin</span>
<span class="hljs-keyword">const</span> searchParams = <span class="hljs-keyword">new</span> URLSearchParams(<span class="hljs-string">"id=45&name=321"</span>)     <span class="hljs-comment">// &#123; 'id' => '45', 'name' => '321' &#125;</span>
<span class="hljs-comment">// [['id',45],['name','admin']]</span>
<span class="hljs-keyword">const</span> searchParams = <span class="hljs-keyword">new</span> URLSearchParams([[<span class="hljs-string">'id'</span>,<span class="hljs-number">45</span>],[<span class="hljs-string">'name'</span>,<span class="hljs-string">"admin"</span>]])
<span class="hljs-comment">// &#123;'id':45,'name':'admin'&#125;</span>
<span class="hljs-keyword">const</span> searchParams = <span class="hljs-keyword">new</span> URLSearchParams(&#123;<span class="hljs-string">'id'</span>:<span class="hljs-number">45</span>,<span class="hljs-string">'name'</span>:<span class="hljs-string">'admin'</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例化的好处在于可以方便管理,比如添加、删除、查找等,通过实例方法很方便的管理数据.</p>
<h5 data-id="heading-5">实例方法</h5>
<ul>
<li><code>append(name,value)</code> - 添加一个数据</li>
<li><code>delete(name)</code> - 删除指定参数名的数据</li>
<li><code>entries()</code> - 迭代遍历键/值对的对象.</li>
<li><code>get(name)</code> - 获取到指定参数名的第一个值.</li>
<li><code>getAll(name)</code> - 返回指定参数名的所有值,数组</li>
<li><code>has(name)</code> - 判断是否存在某个参数.</li>
<li><code>keys()</code> - 所有参数的键的迭代对象.</li>
<li><code>set(name,value)</code> - 设置某个参数的值.</li>
<li><code>sort()</code> - 按键名排序.</li>
<li><code>toString()</code> - 返回查询字符串.</li>
<li><code>values()</code> - 包含所有值的迭代对象.</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> searchParams = <span class="hljs-keyword">new</span> URLSearchParams()

<span class="hljs-comment">// 追加一个参数</span>
searchParams.append(<span class="hljs-string">"id"</span>,<span class="hljs-string">"sv2341"</span>)      <span class="hljs-comment">// &#123; 'id' => 'sv2341' &#125;</span>
<span class="hljs-comment">// 判断是否包含某个参数</span>
searchParams.has(<span class="hljs-string">"name"</span>)           <span class="hljs-comment">// false</span>
<span class="hljs-comment">// 获取指定参数的值</span>
searchParams.get(<span class="hljs-string">"id"</span>)              <span class="hljs-comment">// sv2341</span>
<span class="hljs-comment">// 获取所有参数的值</span>
[...searchParams.values()]         <span class="hljs-comment">// ['sv2341']</span>
<span class="hljs-comment">// </span>
searchParams.toString();        <span class="hljs-comment">//. </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">处理URL地址参数</h4>
<p>不需要自己再去分隔字符串处理查询参数了,通过searchParams对象优雅处理查询参数,方便多了.</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取实例URL的查询字符串对象</span>
<span class="hljs-keyword">const</span> searchParams = url.searchParams

<span class="hljs-comment">// 追加一个name查询参数</span>
searchParams.append(<span class="hljs-string">'name'</span>,<span class="hljs-string">'admin'</span>)        <span class="hljs-comment">// href: 'ftp://www.baidu.com/admin?id=45&name=admin#app',</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是实例化的新的<code>URLSearchParams</code> , 则复制给<code>url</code>对象属性<code>search</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> url = <span class="hljs-keyword">new</span> URL(<span class="hljs-string">'http://www.baidu.com/hello'</span>)
<span class="hljs-comment">// 新实例化的对象</span>
<span class="hljs-keyword">const</span> searchParams = <span class="hljs-keyword">new</span> URLSearchParams()
searchParams.append(<span class="hljs-string">"id"</span>,<span class="hljs-string">"sv2341"</span>)
searchParams.append(<span class="hljs-string">"name"</span>,<span class="hljs-string">"test"</span>)

<span class="hljs-comment">// 设置查询参数</span>
url.search = searchParams             <span class="hljs-comment">// href: 'http://www.baidu.com/hello?id=sv2341&name=test',</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">无法处理hash与pathname的位置顺序</h4>
<p>让人头疼的是<code>hash</code>与<code>pathname</code> 的位置,hash设置总是在<code>pathname \ search</code> 后面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> url = <span class="hljs-keyword">new</span> URL(<span class="hljs-string">'http://www.baidu.com'</span>)

<span class="hljs-comment">// 赋值hash</span>
url.hash = <span class="hljs-string">'/'</span>
<span class="hljs-comment">// 赋值路径</span>
url.pathname = <span class="hljs-string">'/app'</span>
<span class="hljs-comment">// 赋值查询条件</span>
url.search = <span class="hljs-string">'id=45'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果展示为<code>http://www.baidu.com/app?id=45#/</code> 怎么调试也没能改变, 我想要的结果是<code>http://www.baidu.com/#/app?id=45</code></p>
<p>不然重新打开一个新的tab页时,会导航到初始主路由 :cry:</p>
<p>所以只能去重新拼接一下URL地址：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> url = <span class="hljs-keyword">new</span> URL(<span class="hljs-string">'http://www.baidu.com/#/app'</span>)
<span class="hljs-keyword">const</span> searchParams = <span class="hljs-keyword">new</span> URLSearchParams()

searchParams.append(<span class="hljs-string">"id"</span>,<span class="hljs-string">"sv2341"</span>)
searchParams.append(<span class="hljs-string">"name"</span>,<span class="hljs-string">"test"</span>)
<span class="hljs-comment">// 打开新的tab页面</span>
<span class="hljs-built_in">window</span>.open(url.toString()+<span class="hljs-string">"?"</span>+searchParams.toString()) <span class="hljs-comment">// http://www.baidu.com/#/app?id=sv2341&name=test</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">File</h3>
<p>处理文件相关的信息.访问文件中的数据. <code>UTF8</code>编码</p>
<h4 data-id="heading-9">构造实例</h4>
<p>参数定义:</p>
<ul>
<li><code>bits</code> 定义的文件内容,包含<code>ArrayBuffer\ArrayBufferView\Blob\DOMString[]</code>等类型</li>
<li><code>name</code> 文件名称,可以追加路径.</li>
<li><code>options</code> 可选的配置项
<ul>
<li><code>type</code> - 文件MIME类型  ,默认‘’</li>
<li><code>lastModified</code> 文件修改的时间</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> file = <span class="hljs-keyword">new</span> File(bits,name,options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可访问的属性,都为只读属性:</p>
<ul>
<li><code>lastModified</code> - 文件最后的修改时间</li>
<li><code>name</code> - 文件名称</li>
<li><code>size</code> - 文件大小</li>
<li><code>type</code> - 文件类型</li>
</ul>
<h4 data-id="heading-10">实例方法</h4>
<p>自身没有定义方法,继承自<code>Blob</code>接口,可选的参数定义:</p>
<ul>
<li><code>slice(start,end,contentType)</code> - 返回一个新的Blob对象,原始的一段数据.</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 自定义文本内容</span>
<span class="hljs-keyword">const</span> file = <span class="hljs-keyword">new</span> File([<span class="hljs-string">'hello world'</span>,<span class="hljs-string">'luck for you'</span>],<span class="hljs-string">'test.txt'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">FileReader</h4>
<p>上述只是定义个一个文件对象,我们要读取到文件的内容,则需要<code>FileReader</code> 对象读取数据.</p>
<h5 data-id="heading-12">构造实例</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fileReader = <span class="hljs-keyword">new</span> FileReader();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可访问的属性:</p>
<ul>
<li><code>error</code> - 读取文件时发生的错误</li>
<li><code>readyState</code> - 取值状态, 0-未加载任何数据; 1-数据正在加载; 2-已读取完成.</li>
<li><code>result</code> -  读取到的文件内容.</li>
</ul>
<h5 data-id="heading-13">实例方法</h5>
<p>定义实例,则可以用来读取文件,文件的读取是一个异步过程. 那么异步就会存在异步流程,对应着不同的事件.</p>
<p>先看一下实例定义的方法:</p>
<ul>
<li><code>abort()</code> 中止读取操作</li>
<li><code>readAsArrayBuffer()</code> 读取内容以ArrayBuffer格式保存数据.</li>
<li><code>readAsDataURL()</code> 读取内容,返回格式为<code>data:</code>base64数据</li>
<li><code>readAsText()</code> 读取内容,返回的内容为字符串.</li>
</ul>
<p>可以继续之前的文件数据读取;</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义文件对象</span>
<span class="hljs-keyword">const</span> file = <span class="hljs-keyword">new</span> File([<span class="hljs-string">'hello world'</span>,<span class="hljs-string">'luck for you'</span>],<span class="hljs-string">'test.txt'</span>)
<span class="hljs-comment">// 定义文件读取的实例对象</span>
<span class="hljs-keyword">const</span> fileReader = <span class="hljs-keyword">new</span> FileReader()

<span class="hljs-comment">// 通过onload事件回调获取到文件内容</span>
fileReader.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(event.target.result)        <span class="hljs-comment">// hello worldluck for you</span>
&#125;
<span class="hljs-comment">// 读取文件为字符串</span>
fileReader.readAsText(file)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里是所有的事件:</p>
<ul>
<li><code>onabort</code> 中断读取时触发.</li>
<li><code>onerror</code> 读取操作发生错误触发.</li>
<li><code>onload</code> 读取完成时触发.</li>
<li><code>onloadstart</code> 读取开始时触发</li>
<li><code>onloadend</code> 读取结束触发,成功或者失败</li>
<li><code>onprogress</code> 读取Blob对象时触发</li>
</ul>
<h4 data-id="heading-14">定义文件下载</h4>
<p>通常前端会处理一些简单的文件下载,比如文本、图片之类的. 会使用<code>a</code>标签进行下载处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 完成简单的自定义.txt文件下载</span>
<span class="hljs-keyword">const</span> file = <span class="hljs-keyword">new</span> File([<span class="hljs-string">'hello world'</span>],<span class="hljs-string">'test.txt'</span>)

<span class="hljs-comment">// 定义读取文件对象</span>
<span class="hljs-keyword">const</span> fileReader = <span class="hljs-keyword">new</span> FileReader()
<span class="hljs-comment">// 读取文件</span>
fileReader.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
    <span class="hljs-comment">// 定义a标签,追加到body中,点击进行下载</span>
    <span class="hljs-keyword">let</span> a = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>)
    a.download = <span class="hljs-string">'hello.txt'</span>
    a.href = event.target.result
    a.textContent = <span class="hljs-string">'下载'</span>
    <span class="hljs-built_in">document</span>.body.append(a)
&#125;
<span class="hljs-comment">// a标签下载接受的格式blob:或者data:</span>
<span class="hljs-comment">// 定义读取base64 格式的数据</span>
fileReader.readAsDataURL(file)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以读取远程的URL地址文件信息,在前端实现下载.</p>
<p>通常自定义实现的下载,不需要去点击,启动触发下载事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 通过click方法模拟点击事件,触发下载</span>
a.click()

<span class="hljs-comment">// 定义a标签不可见</span>
a.style.display = <span class="hljs-string">'none'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">通过<code>URL.createObjectURL</code>定义文件下载</h4>
<p>上述可以通过FileReader来读取文件内容,也可以通过URL静态方法创建<code>blob:</code>格式的URL对象,指向源内容.</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建文件内容ULR </span>
<span class="hljs-keyword">const</span> dataUrl = URL.createObjectURL(file)
<span class="hljs-comment">// 构建下载</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>)
a.download = <span class="hljs-string">'hello.txt'</span>
a.href = dataUrl
a.textContent = <span class="hljs-string">'下载'</span>
a.style.display = <span class="hljs-string">'none'</span>
<span class="hljs-built_in">document</span>.body.append(a)
a.click();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>准备写一下文件的上传、下载;主要是断点续传、分片上传等;先立个flag吧,不知道啥时候写完. :dog:</p>
<h3 data-id="heading-16">Image</h3>
<p>常用的展示形式-图片,不可或缺. 通常的网站并不会处理图片,拿到ULR地址,直接做展示就好.如果是一个专门处理图片的工程的话, 就会对图片各方面处理要求的多. 通常先获取到图片的大小,初始画布等.</p>
<h4 data-id="heading-17">构造实例</h4>
<p>实例同等于html元素<code>img</code>, 接受参数</p>
<ul>
<li><code>width</code> 宽度</li>
<li><code>height</code> 高度</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> img = <span class="hljs-keyword">new</span> Image()
<span class="hljs-comment">// 等同于</span>
img = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'img'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可访问属性:</p>
<ul>
<li><code>alt</code> 描述内容</li>
<li><code>complete</code> 表示加载正常,没有发生错误.</li>
<li><code>crossOrigin</code> 跨域设置</li>
<li><code>currentSrc</code> 表示正在加载图像的URL.</li>
<li><code>decoding</code> 图片的加载后的解码设置</li>
<li><code>height</code> css渲染的高度</li>
<li><code>width</code> css渲染的宽度</li>
<li><code>isMap</code> 是否是某一图片映射的一部分</li>
<li><code>naturalHeight</code>图片固有高度;不同于实际展示大小可能会受CSS影响.</li>
<li><code>naturalWidth</code> 图片固有宽度;不同于实际展示大小可能会受CSS影响.</li>
<li><code>referrerPolicy</code> 定时告诉用户如何获取图片资源</li>
<li><code>src</code> 图像完整的URL</li>
<li><code>useMap</code> 定义引用<code>map</code> 元素<code>#</code>开头</li>
<li><code>srcset</code> 候选图像列表,逗号分隔; <code>w</code>表示图像宽度,<code>x</code> 表示图像密度</li>
<li><code>sizes</code> 定义图像特定现实的大小;</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义实例</span>
<span class="hljs-keyword">const</span> img = <span class="hljs-keyword">new</span> Image(<span class="hljs-number">150</span>,<span class="hljs-number">160</span>)
img.src = <span class="hljs-string">'./test.png'</span>
<span class="hljs-comment">// 定义了宽度、高度,则可以直接获取到属性 img.width img.height</span>
img.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// 要获取实际的图片的大小,则必须等待图片加载完成</span>
  <span class="hljs-comment">// img.naturalWidth,img.naturalHeight</span>
&#125;

<span class="hljs-comment">// 可以像普通的img标签添加到页面中</span>
<span class="hljs-built_in">document</span>.body.appendChild(img)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">实例方法</h4>
<p>基本没什么主要的方法提供调用，</p>
<ul>
<li><code>decode()</code> 用于解码加载图片的帧，安全的加载到DOM中。返回一个<code>promise</code></li>
</ul>
<p>继承自<code>HTMLELement</code>接口，拥有常规DOM的事件</p>
<ul>
<li><code>onload</code> 加载完成</li>
<li><code>onerror</code> 加载错误时，触发调用。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 主要是onload 加载完成获取到实际图片的大小信息</span>
img.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// 要获取实际的图片的大小,则必须等待图片加载完成</span>
  <span class="hljs-comment">// img.naturalWidth,img.naturalHeight</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建实例时，没有指定大小，<code>img.widht/img.hegiht</code>即是图片的真实大小。</p>
<h4 data-id="heading-19">响应式图片大小</h4>
<p>现在的电子设备越来越多,屏幕大小、分隔各不相同,设计网站展示想达到完美的展示效果,则必须创建适合各个大小屏幕分隔的图片进行展示.</p>
<p>使用图片的<code>srcset \ sizes</code>定义图片资源</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">srcset</span>=<span class="hljs-string">"1.png 500w,
             2.png 800w,
             3.png 1200w"</span>
     <span class="hljs-attr">sizes</span>=<span class="hljs-string">"(max-width:520px) 500px,
            (max-width:820px) 800px,
            1200px"</span> 
    <span class="hljs-attr">alt</span>=<span class="hljs-string">"图像"</span>
   /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>检测设备宽度, 检查符合条件的<code>sizes</code>列表媒体查询;获取到定义的展示图片的大小,从<code>srcset</code>加载到最符合size大小的图像进行展示.</p>
<p>可以通过定义srcset <code>x</code> 不同的分辨率;</p>
<h3 data-id="heading-20">MutationObserver</h3>
<p>提供了监视对DOM树所做更改的能力 ,</p>
<p>这个是在vue指令滚动加载的时候看到源码里写的,之后就业务功能中也会使用它做一些加载的优化处理.</p>
<h4 data-id="heading-21">构造实例</h4>
<ul>
<li>参数为回调 , 即指定的节点或子节点发生dom变动时别调用.
<ul>
<li>回调第一个参数为变动的MutationRecord 对象数组.</li>
<li>实例对象observer</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 实例化observer对象</span>
<span class="hljs-keyword">const</span> observer = <span class="hljs-keyword">new</span> MutationObserver(handlerChange)

<span class="hljs-comment">// 配置监听的dom,以及监听哪些属性的变动配置</span>
<span class="hljs-keyword">const</span> options = &#123;
  <span class="hljs-attr">childList</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 观察子节点的变化,添加或删除</span>
  <span class="hljs-attr">attributes</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 观察属性变动</span>
  <span class="hljs-attr">subtree</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 观察子孙节点</span>
&#125;

<span class="hljs-comment">// 监听</span>
observe.observe(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#app"</span>),options)

<span class="hljs-comment">// 回调事件</span>
<span class="hljs-keyword">const</span> handlerChange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">mutationList,observer</span>)</span>&#123;
  <span class="hljs-comment">// 触发变动的节点、属性</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">实例方法</h4>
<ul>
<li>
<p><code>observe(dom,options)</code> - 配置监听的DOM给定选项更改时,调用回调函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> options = &#123;
  <span class="hljs-attr">attributeFiter</span>:[], <span class="hljs-comment">// 设置监听指定属性,比如width、height等.不设置则监听所有属性.</span>
  <span class="hljs-attr">attributeOldValue</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 观察节点属性变更时,记录旧值</span>
  <span class="hljs-attr">attributes</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 观察节点属性的变更</span>
  <span class="hljs-attr">characterData</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 监听文本节点文本的变化</span>
  <span class="hljs-attr">characterDataOldValue</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 监听文本节点,记录文本节点旧值</span>
  <span class="hljs-attr">childList</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 观察子孙节点的添加、删除更改</span>
  <span class="hljs-attr">subtree</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">// 观察子孙节点、属性等所有的变化</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>多次调用监听方法,会移除现有的观察目标的监听; 如果没有指定DOM,则保留现有的观察目标,并添加新的观察者.</p>
</li>
<li>
<p><code>disconnect()</code> - 停止监听DOM,回调不会在调用</p>
</li>
<li>
<p><code>takeRecords()</code> - 删除所有待处理的变更通知.</p>
</li>
</ul>
<h4 data-id="heading-23">滚动加载时加载初始数据</h4>
<p>之前看到element的滚动加载的指令<code>v-infinite-scroll</code> , 在初始加载数据时,使用API监听子节点的变化,从而加载让数据内容去出现滚动条为止. 我们的滚动加载必须要有滚动条才能出发滚动事件.</p>
<p>(当然我们可以通过递归回调的方式判定数据区的offsetHeight/clientHeight 对比是否出现滚动条,进而追加数据)</p>
<p>但自动触发处理逻辑岂不更好 :smile:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> id = <span class="hljs-number">0</span>
<span class="hljs-comment">// 加载数据的方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadChild</span>(<span class="hljs-params"></span>)</span>&#123;
    id++;
    <span class="hljs-keyword">let</span> p = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'p'</span>)
    p.textContent = <span class="hljs-string">`数据id<span class="hljs-subst">$&#123;id&#125;</span>`</span>
    <span class="hljs-comment">//</span>
    dom.appendChild(p)
&#125;

<span class="hljs-comment">// 实例化observer对象</span>
<span class="hljs-keyword">const</span> observer = <span class="hljs-keyword">new</span> MutationObserver(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 触发之后,添加子节点</span>
    loadChild()
    <span class="hljs-comment">// 判断是否出现了滚动条,</span>
    <span class="hljs-comment">// 有滚动条了则不需要监听DOM 了</span>
    <span class="hljs-keyword">if</span>(dom.scrollHeight > dom.clientHeight)&#123;
        <span class="hljs-comment">// 存在滚动条</span>
        <span class="hljs-keyword">if</span>(observer)&#123;
            observer.disconnect();
            observer = <span class="hljs-literal">null</span>;
        &#125;
    &#125;
&#125;)

<span class="hljs-comment">// 配置监听的dom,以及监听哪些属性的变动配置</span>
<span class="hljs-keyword">const</span> options = &#123;
    <span class="hljs-attr">childList</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 观察子节点的变化,添加或删除</span>
    <span class="hljs-attr">attributes</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 观察属性变动</span>
    <span class="hljs-attr">subtree</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 观察子孙节点</span>
&#125;

<span class="hljs-comment">// 监听</span>
<span class="hljs-keyword">let</span> dom = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list-box"</span>);
observer.observe(dom, options)

<span class="hljs-comment">// 初始调用一次</span>
loadChild();

<span class="hljs-comment">// 然后是正常的scroll 事件监听</span>
dom.addEventListener(<span class="hljs-string">'scroll'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 滚动距离+可视高度 <= 内容区高度-20 追加数据</span>
    <span class="hljs-keyword">let</span> scrollBottom = dom.scrollTop + dom.clientHeight
    <span class="hljs-keyword">if</span>(dom.scrollHeight - scrollBottom <= <span class="hljs-number">20</span>)&#123;
        loadChild();
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了初始触发目标节点的变动,需要手动调用一次数据加载函数<code>loadChild()</code> , 当添加第一条数据后,DOM监听回调开始执行 ;一直到出现滚动条(可视高度不等于内容区域高度时)停止检测.</p>
<p>正常的<code>scroll</code>事件被监听,滚动到底部距离小于20(阀值)时,触发数据加载函数;</p>
<p>数据加载完成时,可以在<code>loadChild</code>函数中增加取消滚动事件,停止滚动加载时间触发.</p>
<h4 data-id="heading-24">MutationRecord</h4>
<p>监听DOM 变更后回调第一个参数.</p>
<ul>
<li><code>type</code> - 变更的类型, 属性-attributes;节点文本变化 - characterData; 子节点变化 - childList</li>
<li><code>target</code> - 变更的目标节点</li>
<li><code>addedNodes</code> - 被添加的节点NodeList</li>
<li><code>removedNodes</code> - 被移除的节点NodeList</li>
<li><code>oladValue</code> - 变更前的旧值记录,需要配置属性才会有;</li>
<li>...</li>
</ul>
<h3 data-id="heading-25">FormData</h3>
<p>提供处理form表单数据的功能，form表单处理在日常开发中处处可见。现在的前端框架帮我很好的处理了这一问题，必要的学习了解还是必须的。</p>
<h4 data-id="heading-26">构造实例</h4>
<ul>
<li>参数为 <code>form</code>标签dom对象，非必选。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// </span>
<span class="hljs-keyword">const</span> form = <span class="hljs-keyword">new</span> FormData()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们传入<code>form</code> 参数时，每个form元素都需要<code>name</code>属性，这是必须的。会自动将表单值序列化</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 指定form元素，同步获取到表单里的表单属性、值。</span>
<span class="hljs-keyword">const</span> form = <span class="hljs-keyword">new</span> FormData(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#form'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">实例方法</h4>
<ul>
<li><code>append()</code> key/value 新增键值对，如果存在key，则新增一个值</li>
<li><code>delete()</code> 删除指定键</li>
<li><code>entries()</code> 所有键值对的迭代对象</li>
<li><code>get()</code> 获取到指定键的第一个值</li>
<li><code>getAll()</code> 返回指定键的包含所有值的数组</li>
<li><code>has()</code> 是否包含某个键</li>
<li><code>keys()</code> 所有属性键的迭代对象</li>
<li><code>set()</code> 设置属性值，覆盖原有的值</li>
<li><code>valuse()</code> 返回包含所有属性值得迭代对象</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"form"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"form-item"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span>></span>姓名<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"admin"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"输入姓名"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"form-item"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span>></span>年龄<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span> <span class="hljs-attr">min</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"age"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"23"</span> <span class="hljs-attr">max</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">step</span>=<span class="hljs-string">"1"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"form-item"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span>></span>性别<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"gender"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">checked</span>></span>男
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"gender"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"2"</span>></span>女
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义的form表单，创建<code>FormData</code>实例后，操作表单元素，并可增加新的属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 所有属性 ，按照表单元素的name属性序列化</span>
form.keys()         <span class="hljs-comment">// [...keys] - result:["name", "age", "gender"]</span>
<span class="hljs-comment">// 查找某个值 </span>
form.has(<span class="hljs-string">'id'</span>)          <span class="hljs-comment">// false</span>
<span class="hljs-comment">// 添加一个值,重复的name属性</span>
form.append(<span class="hljs-string">'name'</span>,<span class="hljs-string">'test'</span>)         
form.get(<span class="hljs-string">'name'</span>)               <span class="hljs-comment">// 返回第一个符合的值， 为 admin</span>
form.getAll(<span class="hljs-string">'name'</span>)               <span class="hljs-comment">// 返回所有的值得数组， ['admin','test']</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">XMLHttpRequest发送数据</h4>
<p>创建一个ajax实例，发送请求。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 直接发送数据</span>
<span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()

xhr.open(<span class="hljs-string">'post'</span>,<span class="hljs-string">'/addUserInfo'</span>)
xhr.send(form)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>File</code> 创建文件，上传文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建文件对象</span>
<span class="hljs-keyword">const</span> file = <span class="hljs-keyword">new</span> File([<span class="hljs-string">'hello world'</span>],<span class="hljs-string">'test.txt'</span>)
<span class="hljs-comment">// 定义文件读取的实例对象</span>
<span class="hljs-keyword">const</span> fileReader = <span class="hljs-keyword">new</span> FileReader()
<span class="hljs-comment">// 定义请求实例</span>
<span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
<span class="hljs-comment">// 通过onload事件回调获取到文件内容</span>
fileReader.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
    <span class="hljs-comment">// 读取到文件blob数据</span>
    form.append(<span class="hljs-string">'file'</span>,event.target.result)
    xhr.open(<span class="hljs-string">'post'</span>,<span class="hljs-string">'/addUserInfo'</span>)
    xhr.send(form)
&#125;
<span class="hljs-comment">// 读取文件为字符串</span>
fileReader.readAsDataURL(file)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">作为<code>URLSearchParams</code> 构造参数解析</h4>
<p>可直接传入<code>URLSearchParams</code>解析，然后追加到URL上。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// </span>
<span class="hljs-keyword">const</span> params = <span class="hljs-keyword">new</span> URLSearchParams(form)

<span class="hljs-comment">// 可获取使用实例的方法</span>
params.toString()                  <span class="hljs-comment">// name=admin&age=23&gender=1&name=test</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            