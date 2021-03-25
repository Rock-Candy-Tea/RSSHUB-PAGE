
---
title: '⚠️ Python编写简易API'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c7104aa3f843e99118cbfb33a71011~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 16:22:37 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c7104aa3f843e99118cbfb33a71011~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="flask_restful_banner.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c7104aa3f843e99118cbfb33a71011~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>本文<strong>约550字</strong>，将耗费您<strong>约4⃣️分钟</strong>～</p>
<blockquote>
<p>所有的操作，仅在<code>mac</code>系统上实操过</p>
</blockquote>
<h3 data-id="heading-0">前期准备</h3>
<p>创建一个虚拟环境：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ mkdir flask_restful
$ <span class="hljs-built_in">cd</span> flask_restful
$ python3 -m venv venv
<span class="copy-code-btn">复制代码</span></code></pre>
<p>激活虚拟环境：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ . venv/bin/activate
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虚拟环境退出：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ deactivate
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装<code>flask</code>和<code>flask_restful</code>：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ pip install flask
$ pip install flask_restful
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">项目接口模拟</h3>
<p>在项目的根目录下面新建文件<code>api.js</code>，在此文件中进行数据的增删改查。</p>
<blockquote>
<p>⚠️ 这里使用到的数据为模拟数据，并未连接数据库</p>
</blockquote>
<pre><code class="hljs language-python copyable" lang="python"><span class="hljs-keyword">from</span> flask <span class="hljs-keyword">import</span> Flask, jsonify, request
<span class="hljs-keyword">from</span> flask_restful <span class="hljs-keyword">import</span> Api, Resource

app = Flask(__name__)
api = Api(app)

USER_LIST = [&#123;<span class="hljs-string">'id'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'name'</span>: <span class="hljs-string">'jimmy'</span>&#125;]

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserListApi</span>(<span class="hljs-params">Resource</span>):</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get</span>(<span class="hljs-params">self</span>):</span>
        <span class="hljs-keyword">return</span> &#123;<span class="hljs-string">'code'</span>: <span class="hljs-number">10000</span>, <span class="hljs-string">'msg'</span>: <span class="hljs-string">'get list success'</span>, <span class="hljs-string">'data'</span>: USER_LIST&#125;

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">post</span>(<span class="hljs-params">self</span>):</span>
        json_data = request.get_json()
        new_id = <span class="hljs-built_in">len</span>(USER_LIST) + <span class="hljs-number">1</span>
        USER_LIST.append(&#123;<span class="hljs-string">'id'</span>: new_id, <span class="hljs-string">'name'</span>: json_data.get(<span class="hljs-string">'name'</span>)&#125;)
        <span class="hljs-keyword">return</span> jsonify(&#123;<span class="hljs-string">'code'</span>: <span class="hljs-number">10000</span>, <span class="hljs-string">'msg'</span>: <span class="hljs-string">'add user success'</span>, <span class="hljs-string">'data'</span>: USER_LIST[new_id-<span class="hljs-number">1</span>]&#125;)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserApi</span>(<span class="hljs-params">Resource</span>):</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get</span>(<span class="hljs-params">self, <span class="hljs-built_in">id</span></span>):</span>
        <span class="hljs-keyword">return</span> &#123;<span class="hljs-string">'code'</span>: <span class="hljs-number">10000</span>, <span class="hljs-string">'msg'</span>: <span class="hljs-string">'get user success'</span>, <span class="hljs-string">'data'</span>: &#123;&#125;&#125;

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">put</span>(<span class="hljs-params">self, <span class="hljs-built_in">id</span></span>):</span>
        <span class="hljs-keyword">return</span> &#123;<span class="hljs-string">'code'</span>: <span class="hljs-number">10000</span>, <span class="hljs-string">'msg'</span>: <span class="hljs-string">'update user success'</span>, <span class="hljs-string">'data'</span>: &#123;&#125;&#125;

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">delete</span>(<span class="hljs-params">self, <span class="hljs-built_in">id</span></span>):</span>
        <span class="hljs-keyword">return</span> &#123;<span class="hljs-string">'code'</span>: <span class="hljs-number">10000</span>, <span class="hljs-string">'msg'</span>: <span class="hljs-string">'remove user success'</span>, <span class="hljs-string">'data'</span>: &#123;&#125;&#125;

api.add_resource(UserListApi, <span class="hljs-string">'/users'</span>)
api.add_resource(UserApi, <span class="hljs-string">'/users/<int:id>'</span>)

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">'__main__'</span>:
    app.run(debug=<span class="hljs-literal">True</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后运行应用：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ <span class="hljs-built_in">export</span> FLASK_APP=api.py
$ <span class="hljs-built_in">export</span> FLASK_ENV=development
$ flask run
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到下面的输出，说明运行成功了：</p>
<pre><code class="hljs language-bash copyable" lang="bash"> * Serving Flask app <span class="hljs-string">"flaskr"</span> (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with <span class="hljs-built_in">stat</span>
 * Debugger is active!
 * Debugger PIN: 577-682-777
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">项目接口验证</h3>
<p>在上面的代码中，我们对<code>users</code>进行了相关的<strong>增删改查</strong>，下面我们来验证下：</p>
<ul>
<li><strong>新增一个用户</strong></li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">$ curl http://127.0.0.1:5000/users -X POST -H <span class="hljs-string">"Content-Type:application/json"</span> -d <span class="hljs-string">'&#123;"name": "tom"&#125;'</span>

&#123;
  <span class="hljs-string">"code"</span>: 10000, 
  <span class="hljs-string">"data"</span>: &#123;
    <span class="hljs-string">"id"</span>: 2, 
    <span class="hljs-string">"name"</span>: <span class="hljs-string">"tom"</span>
  &#125;, 
  <span class="hljs-string">"msg"</span>: <span class="hljs-string">"add user success"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>查询整个用户列表</strong></li>
</ul>
<pre><code class="copyable">$ curl http://127.0.0.1:5000/users

&#123;
    "code": 10000,
    "msg": "get list success",
    "data": [
        &#123;
            "id": 1,
            "name": "jimmy"
        &#125;,
        &#123;
            "id": 2,
            "name": "tom"
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>更新一个用户</strong></li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">$ curl http://127.0.0.1:5000/users/1 -X PUT

&#123;
    <span class="hljs-string">"code"</span>: 10000,
    <span class="hljs-string">"msg"</span>: <span class="hljs-string">"update user success"</span>,
    <span class="hljs-string">"data"</span>: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>获取一个用户</strong></li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">$ curl http://127.0.0.1:5000/users/1

&#123;
    <span class="hljs-string">"code"</span>: 10000,
    <span class="hljs-string">"msg"</span>: <span class="hljs-string">"get user success"</span>,
    <span class="hljs-string">"data"</span>: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>删除一个用户</strong></li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">$ curl http://127.0.0.1:5000/users/1 -X DELETE

&#123;
    <span class="hljs-string">"code"</span>: 10000,
    <span class="hljs-string">"msg"</span>: <span class="hljs-string">"remove user success"</span>,
    <span class="hljs-string">"data"</span>: &#123;&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">后话</h3>
<ul>
<li>
<p>参考：<a href="http://www.pythondoc.com/Flask-RESTful/" target="_blank" rel="nofollow noopener noreferrer">www.pythondoc.com/Flask-RESTf…</a></p>
</li>
<li>
<p>参考：<a href="https://dormousehole.readthedocs.io/en/latest/" target="_blank" rel="nofollow noopener noreferrer">dormousehole.readthedocs.io/en/latest/</a></p>
</li>
<li>
<p>更多内容：<a href="https://github.com/reng99" target="_blank" rel="nofollow noopener noreferrer">github.com/reng99</a></p>
</li>
<li>
<p>微信小程序云开发初体验：<a href="https://juejin.cn/post/6937461043169853447" target="_blank">juejin.cn/post/693746…</a></p>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            