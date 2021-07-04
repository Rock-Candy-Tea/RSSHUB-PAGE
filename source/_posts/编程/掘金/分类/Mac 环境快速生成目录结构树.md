
---
title: 'Mac 环境快速生成目录结构树'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=222'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 22:40:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=222'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style>
<h2 data-id="heading-0">前言</h2>
<p>有时候当我们再写 <code>README</code> 的的时候需要对项目的结构进行展示的话，这个时候我们就可以很好的利用 <code>Mac</code> 自带的工具 <code>tree</code>，来帮我们快速的生成。</p>
<h2 data-id="heading-1">1. 安装 tree</h2>
<pre><code class="hljs language-bash copyable" lang="bash">brew install tree
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2. 参数介绍</h2>
<pre><code class="hljs language-bash copyable" lang="bash">参数选项
-a <span class="hljs-comment"># 显示所有文件，包括隐藏文件（以  “.” 点开头的文件 ）</span>
-d <span class="hljs-comment"># 只显示目录</span>
-f <span class="hljs-comment"># 只显示每个文件的全路径</span>
-i <span class="hljs-comment"># 不显示树枝，常与-f参数配合使用</span>
-L <span class="hljs-comment"># level 遍历目录的最大层数，level 为大于0的正整数</span>
-F <span class="hljs-comment"># 在执行文件、目录、Socket符号链接、管道名称等不同类型文件的结尾，各自加上“*”、 "/"、"="、"@"、"|"号、类似ls命令的-F选项</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3. demo 目录</h2>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 测试项目的文件层级关系</span>
.
└── src
    └── components
        └── common
            ├── FootCell
            │   └── index.vue
            ├── Pagination
            │   └── index.vue
            ├── Table
            │   └── index.vue
            └── TitleCell
                └── index.vue
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4. 生成指定文件</h2>
<blockquote>
<p>进入到要生成 tree 目录: <code>tree [-d] -L $&#123;number&#125; > $&#123;文件名[.后缀]&#125;</code></p>
</blockquote>
<ul>
<li>
<p>tree -L 3 > test1.md</p>
<pre><code class="hljs language-bash copyable" lang="bash">.
└── src
    └── components
        └── common

3 directories

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>tree -d -L 3 > test2.md</p>
<pre><code class="hljs language-bash copyable" lang="bash">.
├── src
│   └── components
│       └── common

3 directories, 3 files

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-5">5. 不带任何参数，直接调用 tree</h2>
<pre><code class="hljs language-bash copyable" lang="bash">tree <span class="hljs-comment"># 会在终端直接输出上述demo结果</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">6. 以树形结构显示目录下的所有内容（-a 的功能）</h2>
<pre><code class="hljs language-text copyable" lang="text">.
├── .DS_Store
└── src
    ├── .DS_Store
    └── components
        ├── .DS_Store
        └── common
            ├── .DS_Store
            ├── FootCell
            │   └── index.vue
            ├── Pagination
            │   └── index.vue
            ├── Table
            │   └── index.vue
            └── TitleCell
                └── index.vue

7 directories, 8 files
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">7. 只列出目录下第一层目录的结构（-L 功能）</h2>
<ul>
<li>
<p>一层 <code>tree -L 1</code></p>
<pre><code class="hljs language-text copyable" lang="text">.
└── src
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>二层 <code>tree -L 2</code></p>
<pre><code class="hljs language-text copyable" lang="text">.
└── src
    └── components
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>三层 <code>tree -L 3</code></p>
<pre><code class="hljs language-text copyable" lang="text">.
└── src
    └── components
        └── common
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-8">8. 显示所有目录（但不显示文件）</h2>
<ul>
<li>
<p>不带路径 <code>tree -d</code></p>
<blockquote>
<p>显示<code>当前文件</code>的目录</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">KaKa:<span class="hljs-built_in">test</span> hhdd$ tree -d
<span class="hljs-comment"># 结果</span>
.
└── src
    └── components
        └── common
            ├── FootCell
            ├── Pagination
            ├── Table
            └── TitleCell

7 directories
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>带路径 <code>tree -d $&#123;路径&#125;</code></p>
<blockquote>
<p>显示<code>指定路径下的文件</code>的目录</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">KaKa-3:<span class="hljs-built_in">test</span> hhdd$ tree -d /Users/hhdd/Desktop/<span class="hljs-built_in">test</span>
<span class="hljs-comment"># 输出结果</span>
/Users/hhdd/Desktop/<span class="hljs-built_in">test</span>
└── src
    └── components
        └── common
            ├── FootCell
            ├── Pagination
            ├── Table
            └── TitleCell

7 directories
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>带参数 <code>tree -dL $&#123;number&#125;</code> || <code>tree -d -L $&#123;number&#125;</code><br>
-d 参数只显示目录，-L 参数显示层数</p>
<pre><code class="hljs language-bash copyable" lang="bash">KaKa-3:<span class="hljs-built_in">test</span> hhdd$ tree -dL 1
<span class="hljs-comment"># 结果</span>
.
└── src

1 directory
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-9">9. <code>-f</code>选项和<code>-i</code>选项的使用</h2>
<blockquote>
<p>使用<code>-f</code>选项可显示完整的路径名称，使用<code>-i</code>选项则不显示树枝部分，示例代码如下：</p>
</blockquote>
<ul>
<li>
<p><code>-f</code> 可显示完整的路径名称</p>
<pre><code class="hljs language-bash copyable" lang="bash">KaKa-3:<span class="hljs-built_in">test</span> hhdd$ tree -d -L 2 -f
<span class="hljs-comment"># 结果</span>
.
└── ./src
    └── ./src/components

2 directories
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>-i</code> 不显示树枝部分</p>
<pre><code class="hljs language-bash copyable" lang="bash">KaKa-3:<span class="hljs-built_in">test</span> hhdd$ tree -d -L 2 -f -i
<span class="hljs-comment"># 输出结果</span>
.
./src
./src/components

2 directories
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-10">10. 使用 tree 命令 区分 <code>目录</code>和<code>文件</code>的方法（常用）</h2>
<blockquote>
<p>使用<code>-F</code>参数会在目录后面添加 “/ ”，方便区分目录</p>
</blockquote>
<ul>
<li>
<p>形式 <code>tree -L $&#123;number&#125; -F [$&#123;路径&#125;]</code></p>
</li>
<li>
<p>有路径</p>
<pre><code class="hljs language-bash copyable" lang="bash">KaKa-3:<span class="hljs-built_in">test</span> hhdd$ tree -L 1 -F /Users

<span class="hljs-comment"># 输出结果</span>
/Users
├── Guest/
├── Shared/
└── hhdd/

3 directories, 0 files
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>无路径参数</p>
<pre><code class="hljs language-bash copyable" lang="bash">KaKa-3:<span class="hljs-built_in">test</span> hhdd$ tree -L 1 -F

<span class="hljs-comment"># 输出结果</span>
.
└── src/

1 directory, 0 files
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>对比不加 <code>-F</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">KaKa-3:<span class="hljs-built_in">test</span> hhdd$ tree -L 1

<span class="hljs-comment"># 输出结果</span>
.
└── src

1 directory, 0 files
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</div>  
</div>
            