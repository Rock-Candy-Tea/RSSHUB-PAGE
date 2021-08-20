
---
title: '使用ReadtheDocs托管文档'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73676b60a8b5410f94ab9c0c0e0facc5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 00:42:51 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73676b60a8b5410f94ab9c0c0e0facc5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>WangScaler: 一个用心创作的作者。</p>
<p>声明：才疏学浅，如有错误，恳请指正。</p>
</blockquote>
<p>很多的技术文档都是使用的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.readthedocs.io%2Fen%2Fstable%2Findex.html%23" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.readthedocs.io/en/stable/index.html#" ref="nofollow noopener noreferrer">ReadtheDocs</a>,比如<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.python.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.python.org/" ref="nofollow noopener noreferrer">Python文档</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.tornadoweb.org%2Fen%2Fstable%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.tornadoweb.org/en/stable/" ref="nofollow noopener noreferrer">tornado文档</a>等等。虽然不是很美观,但是对于技术博文来说够用了。</p>
<h2 data-id="heading-0">一、安装Python</h2>
<p>使用ReadtheDocs需要有python3的环境,因为sphinx是基于 python3 的。那么我们首先安装python环境,如果你有python环境,可以直接跳过这一步,直接浏览<a href="https://juejin.cn/post/6998429656860852237#%E4%BA%8C%E3%80%81%E5%AE%89%E8%A3%85Sphinx" target="_blank" title="#%E4%BA%8C%E3%80%81%E5%AE%89%E8%A3%85Sphinx">安装Sphinx</a>。</p>
<h3 data-id="heading-1">1、下载python</h3>
<p>选择python<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.python.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.python.org/" ref="nofollow noopener noreferrer">官网</a>下载。可能比较慢,慢慢等待一会。选择Download下载安装包。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73676b60a8b5410f94ab9c0c0e0facc5~tplv-k3u1fbpfcp-watermark.image" alt="python2.png" loading="lazy" referrerpolicy="no-referrer">
根据你的环境下载,我这里下载的Windows的64位最新版本的安装包。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d15441bae0a4d87a3d23d6683d3ec1d~tplv-k3u1fbpfcp-watermark.image" alt="python3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">2、安装</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2664407fa9004edca5a72e4475c34391~tplv-k3u1fbpfcp-watermark.image" alt="python4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>Add python 3.8 to PATH</code> 自动给环境变量添加python的路径。相当于给你的电脑自动配置了python环境,在全局任意位置均可直接使用python。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6095f9e57654789a677bfc62ec84850~tplv-k3u1fbpfcp-watermark.image" alt="python5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>表示安装成功,那么我们的电脑到底是否具备了python环境,接下来进行验证。</p>
<h3 data-id="heading-3">3、验证</h3>
<p>Win+R 打开cmd输入python。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e010e0a4752746748ec37b552161f27f~tplv-k3u1fbpfcp-watermark.image" alt="python6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们看到了python的版本信息,恭喜你大功告成了,接下来正式进入我们的话题。</p>
<h2 data-id="heading-4">二、安装Sphinx</h2>
<p>Sphinx 是一个功能强大的文档生成器，具有许多用于编写技术文档的强大功能，Sphinx 最早只是用来生成 Python 官方文档，随着工具的完善， 越来越多的知名的项目也用他来生成文档。</p>
<h3 data-id="heading-5">1、安装Sphinx</h3>
<pre><code class="hljs language-bash copyable" lang="bash">pip install sphinx sphinx-autobuild sphinx_rtd_theme
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.初始化</h3>
<p>window下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">d:
<span class="hljs-built_in">cd</span> /wangscaler/
sphinx-quickstar
<span class="copy-code-btn">复制代码</span></code></pre>
<p>linux下</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 创建文档根目录</span>
mkdir -p /usr/<span class="hljs-built_in">local</span>/wangscaler/
<span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/wangscaler/
<span class="hljs-comment"># 可以回车按默认配置来写</span>
sphinx-quickstart
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是我填写的，其他基本上默认即可：</p>
<pre><code class="hljs language-bash copyable" lang="bash">> Separate <span class="hljs-built_in">source</span> and build directories (y/n) [n]:y
> Project name: WangScaler
> Author name(s): WangScaler
> Project version []: 0.2
> Project release [1.0]: 0.2.2
> Project language [en]: zh_CN
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">3.安装软件tree查看目录树结构：</h3>
<p>windows</p>
<pre><code class="hljs language-bash copyable" lang="bash">tree
<span class="copy-code-btn">复制代码</span></code></pre>
<p>linux</p>
<pre><code class="hljs language-bash copyable" lang="bash">yum install tree
tree -C .
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">三、支持markdown编写以及切换主题</h2>
<p>recommonmark是支持markdown的插件,而sphinx-markdown-tables则是主题,因为默认的主题是不好看的,我们可以使用这个主题来优化我们的界面。</p>
<h3 data-id="heading-9">1.安装插件</h3>
<pre><code class="hljs language-bash copyable" lang="bash">pip install recommonmark
pip install sphinx-markdown-tables
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.修改配置</h3>
<p>然后更改conf.py，我的配置如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># Configuration file for the Sphinx documentation builder.</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># This file only contains a selection of the most common options. For a full</span>
<span class="hljs-comment"># list see the documentation:</span>
<span class="hljs-comment"># https://www.sphinx-doc.org/en/master/usage/configuration.html</span>
​
<span class="hljs-comment"># -- Path setup --------------------------------------------------------------</span>
​
<span class="hljs-comment"># If extensions (or modules to document with autodoc) are in another directory,</span>
<span class="hljs-comment"># add these directories to sys.path here. If the directory is relative to the</span>
<span class="hljs-comment"># documentation root, use os.path.abspath to make it absolute, like shown here.</span>
<span class="hljs-comment">#</span>
import os
import sys
import shlex
sys.path.insert(0, os.path.abspath(<span class="hljs-string">'.'</span>))
​
import recommonmark
from recommonmark.transform import AutoStructify
<span class="hljs-comment"># -- Project information -----------------------------------------------------</span>
source_suffix = [<span class="hljs-string">'.rst'</span>, <span class="hljs-string">'.md'</span>]
​
master_doc = <span class="hljs-string">'index'</span>
​
project = <span class="hljs-string">'Interface'</span>
copyright = <span class="hljs-string">'2021, WangScaler'</span>
author = <span class="hljs-string">'WangScaler'</span>
version = recommonmark.__version__
<span class="hljs-comment"># The full version, including alpha/beta/rc tags</span>
release = recommonmark.__version__
​
​
<span class="hljs-comment"># -- General configuration ---------------------------------------------------</span>
​
<span class="hljs-comment"># Add any Sphinx extension module names here, as strings. They can be</span>
<span class="hljs-comment"># extensions coming with Sphinx (named 'sphinx.ext.*') or your custom</span>
<span class="hljs-comment"># ones.</span>
extensions = [
    <span class="hljs-string">'sphinx.ext.autodoc'</span>,
    <span class="hljs-string">'sphinx.ext.napoleon'</span>,
    <span class="hljs-string">'sphinx.ext.mathjax'</span>,
    <span class="hljs-string">'recommonmark'</span>,
    <span class="hljs-string">'sphinx_markdown_tables'</span>,
]
​
<span class="hljs-comment"># Add any paths that contain templates here, relative to this directory.</span>
templates_path = [<span class="hljs-string">'_templates'</span>]
​
<span class="hljs-comment"># The language for content autogenerated by Sphinx. Refer to documentation</span>
<span class="hljs-comment"># for a list of supported languages.</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># This is also used if you do content translation via gettext catalogs.</span>
<span class="hljs-comment"># Usually you set "language" from the command line for these cases.</span>
language = <span class="hljs-string">'zh_CN'</span>
​
<span class="hljs-comment"># List of patterns, relative to source directory, that match files and</span>
<span class="hljs-comment"># directories to ignore when looking for source files.</span>
<span class="hljs-comment"># This pattern also affects html_static_path and html_extra_path.</span>
exclude_patterns = [<span class="hljs-string">'_build'</span>]
default_role = None
pygments_style = <span class="hljs-string">'sphinx'</span>
todo_include_todos = False
<span class="hljs-comment"># -- Options for HTML output -------------------------------------------------</span>
​
<span class="hljs-comment"># The theme to use for HTML and HTML Help pages.  See the documentation for</span>
<span class="hljs-comment"># a list of builtin themes.</span>
<span class="hljs-comment">#</span>
html_theme = <span class="hljs-string">'sphinx_rtd_theme'</span>
​
<span class="hljs-comment"># Add any paths that contain custom static files (such as style sheets) here,</span>
<span class="hljs-comment"># relative to this directory. They are copied after the builtin static files,</span>
<span class="hljs-comment"># so a file named "default.css" will overwrite the builtin "default.css".</span>
html_static_path = [<span class="hljs-string">'_static'</span>]
htmlhelp_basename = <span class="hljs-string">'Recommonmarkdoc'</span>
latex_elements = &#123;
<span class="hljs-comment"># The paper size ('letterpaper' or 'a4paper').</span>
<span class="hljs-comment">#'papersize': 'letterpaper',</span>
​
<span class="hljs-comment"># The font size ('10pt', '11pt' or '12pt').</span>
<span class="hljs-comment">#'pointsize': '10pt',</span>
​
<span class="hljs-comment"># Additional stuff for the LaTeX preamble.</span>
<span class="hljs-comment">#'preamble': '',</span>
​
<span class="hljs-comment"># Latex figure (float) alignment</span>
<span class="hljs-comment">#'figure_align': 'htbp',</span>
&#125;
​
<span class="hljs-comment"># Grouping the document tree into LaTeX files. List of tuples</span>
<span class="hljs-comment"># (source start file, target name, title,</span>
<span class="hljs-comment">#  author, documentclass [howto, manual, or own class]).</span>
latex_documents = [
  (master_doc, <span class="hljs-string">'Recommonmark.tex'</span>, u<span class="hljs-string">'Recommonmark Documentation'</span>,
   u<span class="hljs-string">'Lu Zero, Eric Holscher, and contributors'</span>, <span class="hljs-string">'manual'</span>),
]
man_pages = [
    (master_doc, <span class="hljs-string">'recommonmark'</span>, u<span class="hljs-string">'Recommonmark Documentation'</span>,
     [author], 1)
]
texinfo_documents = [
  (master_doc, <span class="hljs-string">'Recommonmark'</span>, u<span class="hljs-string">'Recommonmark Documentation'</span>,
   author, <span class="hljs-string">'Recommonmark'</span>, <span class="hljs-string">'One line description of project.'</span>,
   <span class="hljs-string">'Miscellaneous'</span>),
]
​
<span class="hljs-comment"># At the bottom of conf.py</span>
<span class="hljs-comment"># def setup(app):</span>
<span class="hljs-comment">#     app.add_config_value('recommonmark_config', &#123;</span>
<span class="hljs-comment">#         #'url_resolver': lambda url: github_doc_root + url,</span>
<span class="hljs-comment">#         'auto_toc_tree_section': 'Contents',</span>
<span class="hljs-comment">#         'enable_math': False,</span>
<span class="hljs-comment">#         'enable_inline_math': False,</span>
<span class="hljs-comment">#         'enable_eval_rst': True,</span>
<span class="hljs-comment">#         'enable_auto_doc_ref': True,</span>
<span class="hljs-comment">#     &#125;, True)</span>
<span class="hljs-comment">#     app.add_transform(AutoStructify)</span>
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3、编写文件</h3>
<p>框架已经搭建的差不多了,就来写我们的第一篇文章吧。</p>
<p>在source目录下新建hello.rst，内容如下:</p>
<pre><code class="hljs language-rst copyable" lang="rst"># My New Learning
## 一、Mongo（Montor异步数据库）
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4、修改index.rst文件</h3>
<p>这个文件是我们博客的目录,当我们有了新的文章可以加入到这个目录中。</p>
<pre><code class="hljs language-rst copyable" lang="rst">.. Test documentation master file, created by
   sphinx-quickstart on Mon Jul 20 09:49:03 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
​
Welcome to Interface Document!
================================
.. toctree::
   :maxdepth: 2
   :caption: 名字:
​
​
   hello
​
Indices and tables
==================
​
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
​
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">5、编译文件</h3>
<p>在根目录执行<code>make html</code>,将我们的文件编译成网页。我们的任务就完成了,准备访问我们的博客吧。</p>
<h3 data-id="heading-14">6、预览效果</h3>
<p>进入<code>build/html</code>目录后用浏览器打开<code>index.html</code></p>
<h3 data-id="heading-15">7、静态网页的部署</h3>
<p>编译的网页,可以通过nginx部署访问,可以参考我的往期文章<a href="https://juejin.cn/post/6997739255019765773" target="_blank" title="https://juejin.cn/post/6997739255019765773">Nginx的常用操作</a>将静态网页放在指定的位置,即可轻松访问了。</p>
<h2 data-id="heading-16">四、遇到的问题</h2>
<h3 data-id="heading-17">1.图片不显示</h3>
<p>解决方案：</p>
<ul>
<li>
<p>1、图片使用图床加载</p>
</li>
<li>
<p>2、使用相对路径，如/images/a.jpg</p>
</li>
</ul>
<p>注意:<strong>路径是/而非\          第二种不可行</strong></p>
<h3 data-id="heading-18">2.表格不显示</h3>
<pre><code class="hljs language-bash copyable" lang="bash">pip install sphinx-markdown-tables
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在conf.py文件中修改</p>
<pre><code class="hljs language-python copyable" lang="python">extensions = [
    <span class="hljs-string">'sphinx.ext.autodoc'</span>,
    <span class="hljs-string">'sphinx.ext.napoleon'</span>,
    <span class="hljs-string">'sphinx.ext.mathjax'</span>,
    <span class="hljs-string">'recommonmark'</span>,
    <span class="hljs-string">'sphinx_markdown_tables'</span>,<span class="hljs-comment">#这句话支持markdown表格</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>来都来了，点个赞再走呗！</p>
<p>关注WangScaler，祝你升职、加薪、不提桶！</p>
</blockquote></div>  
</div>
            