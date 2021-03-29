
---
title: '分享15个Webpack实用的插件！！！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea184cb836354c909d2648dd56b0d9b7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 21:20:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea184cb836354c909d2648dd56b0d9b7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p><strong>初衷：</strong> 分享一下工作中实用的几个<code>Plugin</code>，希望对大家有些帮助，不喜勿喷。</p>
<h2 data-id="heading-1">html-webpack-plugin</h2>
<p><strong>用途：</strong> 将一个页面模板打包到dist目录下，默认都是自动引入js or css</p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i html-webpack-plugin@<span class="hljs-number">3.2</span><span class="hljs-number">.0</span> -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>index.html</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">'./index.html'</span>,  <span class="hljs-comment">// 以咱们本地的index.html文件为基础模板</span>
            <span class="hljs-attr">filename</span>: <span class="hljs-string">"index.html"</span>,  <span class="hljs-comment">// 输出到dist目录下的文件名称</span>
        &#125;),
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>HtmlWebpackPlugin</code>接收一个对象，里面自行进行配置，详细参见<a href="https://www.npmjs.com/package/html-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer">这里</a></p>
<h2 data-id="heading-2">clean-webpack-plugin</h2>
<p><strong>用途：</strong> 用于每次打包dist目录删除</p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i clean-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> CleanWebpackPlugin()
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">extract-text-webpack-plugin</h2>
<p><strong>用途：</strong> 将<code>css</code>样式从<code>js</code>文件中提取出来最终合成一个<code>css</code>文件，该插件只支持<code>webpack4</code>之前的版本，如果你当前是<code>webpack4</code>及以上版本那么就会报错。</p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i extract-text-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> extractTextPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'extract-text-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: extractTextPlugin.extract(&#123;
                    <span class="hljs-attr">fallback</span>: <span class="hljs-string">"style-loader"</span>, 
                    <span class="hljs-attr">use</span>: <span class="hljs-string">"css-loader"</span>
                &#125;)
            &#125;
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> extractTextPlugin(&#123;
            <span class="hljs-attr">filename</span>: <span class="hljs-string">"[name].css"</span>,
            <span class="hljs-attr">allChunks</span>: <span class="hljs-literal">true</span>
        &#125;)
    ]
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面配置中，<code>extractTextPlugin.extract</code>里面参数<code>fallback</code>是当提取不成功时，就执行<code>style-loader</code>。<code>use</code>里面是提取时使用<code>css-loader</code>进行转换，<code>plugins</code>里面的配置<code>filename</code>是最后合并完的<code>.css</code>文件名称，当<code>allChunks</code>为<code>false</code>时，只会提取初始化时的<code>css</code>文件，为<code>true</code>时会提取异步的<code>css</code>文件。</p>
<h2 data-id="heading-4">mini-css-extract-plugin</h2>
<p><strong>用途：</strong> 该插件与上面的<code>exract-text-webpack-plugin</code>的一样，都是将css样式提取出来, 唯一就是用法不同，本插件的<code>webpack4</code>版本之后推荐使用</p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i mini-css-extract-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [
                   MiniCssExtractPlugin.loader,
                   <span class="hljs-string">"css-loader"</span>
                ]
            &#125;
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
            <span class="hljs-attr">filename</span>: <span class="hljs-string">"css/[name].css"</span>,
            <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">"css/[name].css"</span>
        &#125;)
    ]
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面配置中，可以看到用法与<code>exract-text-webpack-plugin</code>不同，来看一下它们的区别。</p>
<ol>
<li><code>loader</code>配置没有<code>fallback</code></li>
<li>在<code>plugin</code>中设置<code>filename</code>同步加载资源名称，还要指定异步加载<code>css</code>资源<code>chunkFilename</code></li>
<li>该插件支持配置<code>publicPath</code>用来设置异步加载<code>css</code>的路径</li>
<li><code>exract-text-webpack-plugin</code>只会提取一个css文件，<code>mini-css-extract-plugin</code>会根据异步文件提取出来。</li>
</ol>
<h2 data-id="heading-5">webpack.optimize.CommonsChunkPlugin</h2>
<p><strong>用途：</strong> 用于将页面里的公共代码提取出来，从而进行优化加载速度，该<code>CommonsChunkPlugin</code>只支持<code>Webpack4</code>之前。</p>
<p><strong>安装</strong></p>
<pre><code class="copyable">该插件是Webpack内置的，不需要安装。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>main.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">main</span>: <span class="hljs-string">"./main.js"</span>,
        <span class="hljs-attr">vendor</span>: [<span class="hljs-string">"Vue"</span>]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> Webpack.optimize.CommonsChunkPlugin(&#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"vendor"</span>,
            <span class="hljs-attr">filename</span>: <span class="hljs-string">"[name].js"</span>
        &#125;),
        <span class="hljs-keyword">new</span> Webpack.optimize.CommonsChunkPlugin(&#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"common"</span>,
            <span class="hljs-attr">chunks</span>: [<span class="hljs-string">"vendor"</span>],
            <span class="hljs-attr">filename</span>: <span class="hljs-string">"[name].js"</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面配置中，我们把<code>main.js</code>及它里面的依赖文件把<code>Vue.js</code>提取出来进行优化，避免每次打包或者每次访问其它页面都加载一个该<code>js</code>文件, 我们先是把<code>Vue</code>基础环境提取出来，因为基础环境它几乎不会改变，从而进行提取优化是必须的。再把<code>Webpack</code>运行时的代码也提取出来,  这样<code>vendor</code>就再次打包也不会变化，可以走浏览器缓存</p>
<h2 data-id="heading-6">optimization.SplitChunks</h2>
<p><strong>用途：</strong> 该功能与上面的<code>webpack.optimize.CommonsChunkPlugin</code>一样，只不过<code>optimization.SplitChunks</code>是<code>webpack4</code>之后推荐使用的</p>
<p><strong>安装</strong></p>
<pre><code class="copyable">内置的，不需要安装。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>main.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-built_in">console</span>.log(Vue)
<span class="hljs-keyword">import</span>(<span class="hljs-string">"./news"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>news.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-built_in">console</span>.log(Vue)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">main</span>: <span class="hljs-string">"./main.js"</span>
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">"[name].js"</span>,
        <span class="hljs-attr">path</span>: __dirname + <span class="hljs-string">"/dist"</span>
    &#125;,
    <span class="hljs-attr">optimization</span>: &#123;
        <span class="hljs-attr">splitChunks</span>: &#123;
            <span class="hljs-attr">chunks</span>: <span class="hljs-string">"all"</span>
        &#125;
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面配置中，<code>splitChunks</code>的<code>chunks</code>为<code>all</code>是对所有的<code>chunk</code>都生效，默认只对<code>async</code>异步有效。</p>
<p><code>splitChunks</code>默认情况下也有自动提取，默认要求如下：</p>
<ul>
<li>被提取的模块来自<code>node_module</code>目录</li>
<li>模块大于30kb</li>
<li>按需加载时请求资源最大值小于等于5</li>
<li>首次加载时并行请求最大值小于等于3</li>
</ul>
<h2 data-id="heading-7">DefinePlugin</h2>
<p><strong>用途：</strong> 用于注入全局变量，一般用在环境变量上。</p>
<p><strong>安装</strong></p>
<pre><code class="copyable">无需安装，webpack内置
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> Webpack.DefinePlugin(&#123;
           <span class="hljs-attr">STR</span>: <span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-string">"蛙人"</span>),
           <span class="hljs-string">"process.env"</span>: <span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-string">"dev"</span>),
            <span class="hljs-attr">name</span>: <span class="hljs-string">"蛙人"</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面配置中，<code>DefinePlugin</code>接收一个对象，里面的<code>key</code>值对应一个<code>value</code>值，这个<code>value</code>值是一个代码片段，可以看上面<code>name</code>那个，会报错 <code>蛙人 is not defined</code>，<strong>这里需要注意，<code>value</code>值必须是一个变量或代码片段</strong>。</p>
<h2 data-id="heading-8">ProvidePlugin</h2>
<p><strong>用途：</strong> 用于定义全局变量，如100个页面都引入<code>vue</code>，每个页面都引入只会增加工作量，直接在<code>webpackProvide</code>挂载一个变量就行，不用再去一一引入。</p>
<p><strong>安装</strong></p>
<pre><code class="copyable">无需安装，webpack内置
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> Webpack.ProvidePlugin(&#123;
            <span class="hljs-string">"Vue"</span>: [<span class="hljs-string">"vue"</span>, <span class="hljs-string">"default"</span>] 
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面配置中，<code>ProvidePlugin</code>接收一个对象，<code>key</code>值是使用的变量，<code>value</code>值第一个参数是<code>Vue</code>模块，第二个参数默认取<code>Es Module.default</code>的属性。<code>import</code>默认引入进来是一个 <code>Es Module</code>的对象，里面有<code>default</code>这个属性就是实体对象</p>
<h2 data-id="heading-9">hot-module-replacement-plugin</h2>
<p><strong>用途：</strong> 开启热模块更新</p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">无需安装，webpack内置
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> Webpack.HotModuleReplacementPlugin()
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">IgnorePlugin</h2>
<p><strong>用途：</strong> 用于过滤打包文件，减少打包体积大小。</p>
<p><strong>安装</strong></p>
<pre><code class="copyable">无需安装，webpack内置
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> Webpack.IgnorePlugin(<span class="hljs-regexp">/.\/lib/</span>, <span class="hljs-regexp">/element-ui/</span>)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">uglifyjs-webpack-plugin</h2>
<p><strong>用途：</strong> 用于压缩<code>js</code>文件，针对<code>webpack4</code>版本以上。</p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm install uglifyjs-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> UglifyJsPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'uglifyjs-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">optimization</span>: &#123;
        <span class="hljs-attr">minimizer</span>: [
            <span class="hljs-keyword">new</span> UglifyJsPlugin(&#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js(\?.*)?$/i</span>,
                exclude: <span class="hljs-regexp">/node_modules/</span>
            &#125;)
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">copy-webpack-plugin</h2>
<p><strong>用途：</strong> 用于将文件拷贝到某个目录下</p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i  copy-webpack-plugin@<span class="hljs-number">6.4</span><span class="hljs-number">.1</span> -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> CopyWebpackPlugin=<span class="hljs-built_in">require</span>(<span class="hljs-string">'copy-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> CopyWebpackPlugin(&#123;
            <span class="hljs-attr">patterns</span>: [
                &#123;
                    <span class="hljs-attr">from</span>: <span class="hljs-string">"./main.js"</span>,
                    <span class="hljs-attr">to</span>: __dirname + <span class="hljs-string">"/dist/js"</span>,
                    <span class="hljs-attr">toType</span>: <span class="hljs-string">"dir"</span>
                &#125;
            ]
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面配置中，将<code>main.js</code>拷贝到<code>dist</code>目录下的<code>js</code>里，<code>toType</code>默认是<code>file</code>，也可以设置为<code>dir</code>，因为我这<code>dist</code>目录下没有<code>js</code>目录。</p>
<h2 data-id="heading-13">optimize-css-assets-webpack-plugin</h2>
<p><strong>用途：</strong> 用于压缩css样式</p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i optimize-css-assets-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> OptimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"optimize-css-assets-webpack-plugin"</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> OptimizeCssAssetsWebpackPlugin(),
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">imagemin-webpack-plugin</h2>
<p><strong>用途：</strong> 用于压缩图片</p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i imagemin-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ImageminPlugin =  <span class="hljs-built_in">require</span>(<span class="hljs-string">'imagemin-webpack-plugin'</span>).default
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> ImageminPlugin(&#123;
             <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpe?g|png|gif|svg)$/i</span> 
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">friendly-errors-webpack-plugin</h2>
<p><strong>用途：</strong> 美化控制台，良好的提示错误,。我们不想自己的终端启动乱糟糟的，比如这样</p>
<p><img alt="示例" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea184cb836354c909d2648dd56b0d9b7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>安装</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i friendly-errors-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p><strong>webpack.config.js</strong></p>
<pre><code class="copyable">const FriendlyErrorsWebpackPlugin = require('friendly-errors-webpack-plugin');
const devServer =  &#123;
    publicPath: "/",
    port: 9527,
    host: "localhost",
    open: true,
    hotOnly: true,
    stats: 'errors-only'
&#125;
module.exports = &#123;
plugins: [
new FriendlyErrorsWebpackPlugin(&#123;
compilationSuccessInfo: &#123;
                notes: ['蛙人你好，系统正运行在http://localhost:' + devServer.port]
            &#125;,
            clearConsole: true,
&#125;)
],
devServer
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行完上面代码。看如下结果</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d62e01b0ac844c2b4541dd7a25953e0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">感谢</h2>
<p>谢谢你读完本篇文章，希望对你能有所帮助，如有问题欢迎各位指正。</p>
<p>我是蛙人(✿◡‿◡)，如果觉得写得可以的话，请点个赞吧❤。</p>
<p>感兴趣的小伙伴可以加入 <a href="https://qinzhiying.github.io/" target="_blank" rel="nofollow noopener noreferrer">[ 前端娱乐圈交流群 ]</a> 欢迎大家一起来交流讨论</p>
<p>写作不易，<strong>「点赞」+「在看」+「转发」</strong> 谢谢支持❤</p>
<h2 data-id="heading-17">往期好文</h2>
<p><a href="https://juejin.cn/post/6943793273395740680" target="_blank">《手把手教你写一个Vue组件发布到npm且可外链引入使用》</a></p>
<p><a href="https://juejin.cn/post/6942322281913778206" target="_blank">《分享12个Webpack中常用的Loader》</a></p>
<p><a href="https://juejin.cn/post/6938581764432461854" target="_blank">《聊聊什么是CommonJs和Es Module及它们的区别》</a></p>
<p><a href="https://juejin.cn/post/6937855370220011551" target="_blank">《带你轻松理解数据结构之Map》</a></p>
<p><a href="https://juejin.cn/post/6937092511508725774" target="_blank">《这些工作中用到的JavaScript小技巧你都知道吗？》</a></p>
<p><a href="https://juejin.cn/post/6934487656873082887" target="_blank">《【建议收藏】分享一些工作中常用的Git命令及特殊问题场景怎么解决》</a></p>
<p><a href="https://juejin.cn/post/6930428551091109896" target="_blank">《你真的了解ES6中的函数特性么？》</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            