
---
title: 'PyFlink 开发环境利器：Zeppelin Notebook'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5696b2dcb4648e2b670f0596a2cd180~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 00:39:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5696b2dcb4648e2b670f0596a2cd180~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> 在 Zeppelin notebook 里利用 Conda 来创建 Python env 自动部署到 Yarn 集群中。</p>
<blockquote>
<p>PyFlink 作为 Flink 的 Python 语言入口，其 Python 语言的确很简单易学，但是 PyFlink 的开发环境却不容易搭建，稍有不慎，PyFlink 环境就会乱掉，而且很难排查原因。今天给大家介绍一款能够帮你解决这些问题的 PyFlink 开发环境利器：Zeppelin Notebook。主要内容为：</p>
<p>准备工作搭建 PyFlink 环境总结与未来</p>
</blockquote>
<p>也许你早就听说过 Zeppelin，但是之前的文章都偏重讲述如何在 Zeppelin 里开发 Flink SQL，今天则来介绍下如何在 Zeppelin 里高效的开发 PyFlink Job，特别是解决 PyFlink 的环境问题。</p>
<p>一句来总结这篇文章的主题，就是在 Zeppelin notebook 里利用 Conda 来创建 Python env 自动部署到 Yarn 集群中，你无需手动在集群上去安装任何 PyFlink 的包，并且你可以在一个 Yarn 集群里同时使用互相隔离的多个版本的 PyFlink。最后你能看到的效果就是这样：</p>
<p><strong>1. 能够在 PyFlink 客户端使用第三方 Python 库，比如 matplotlib：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5696b2dcb4648e2b670f0596a2cd180~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2. 可以在 PyFlink UDF 里使用第三方 Python 库，如：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9399d05829ac49dfa95f3b35dfbb5317~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来看看如何来实现。</p>
<h1 data-id="heading-0">一、准备工作</h1>
<p><strong>Step 1.</strong></p>
<p>准备好最新版本的 Zeppelin 的搭建，这个就不在这边展开了，如果有问题可以加入 Flink on Zeppelin 钉钉群 (34517043) 咨询。另外需要注意的是，Zeppelin 部署集群需要是 Linux，如果是 Mac 的话，会导致在 Mac 机器上打的 Conda 环境无法在 Yarn 集群里使用 (因为 Conda 包在不同系统间是不兼容的)。</p>
<p><strong>Step 2.</strong></p>
<p>下载 Flink 1.13， 需要注意的是，本文的功能只能用在 Flink 1.13 以上版本，然后：</p>
<ul>
<li>把 <strong>flink-Python-*.jar</strong> 这个 jar 包 copy 到 Flink 的 lib 文件夹下；</li>
<li>把 <strong>opt/Python</strong> 这个文件夹 copy 到 Flink 的 lib 文件夹下。</li>
</ul>
<p><strong>Step 3.</strong></p>
<p>安装以下软件 (这些软件是用于创建 Conda env 的)：</p>
<ul>
<li>**miniconda：**<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.conda.io%2Fen%2Flatest%2Fminiconda.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.conda.io/en/latest/miniconda.html" ref="nofollow noopener noreferrer">docs.conda.io/en/latest/m…</a></li>
<li>**conda pack：**<a href="https://link.juejin.cn/?target=https%3A%2F%2Fconda.github.io%2Fconda-pack%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://conda.github.io/conda-pack/" ref="nofollow noopener noreferrer">conda.github.io/conda-pack/</a></li>
<li>**mamba：**<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmamba-org%2Fmamba" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mamba-org/mamba" ref="nofollow noopener noreferrer">github.com/mamba-org/m…</a></li>
</ul>
<h1 data-id="heading-1">二、搭建 PyFlink 环境</h1>
<p>接下来就可以在 Zeppelin 里搭建并且使用 PyFlink 了。</p>
<p><strong>Step 1. 制作 JobManager 上的 PyFlink Conda 环境</strong></p>
<p>因为 Zeppelin 天生支持 Shell，所以可以在 Zeppelin 里用 Shell 来制作 PyFlink 环境。注意这里的 Python 第三方包是在 PyFlink 客户端 (JobManager) 需要的包，比如 Matplotlib 这些，并且确保至少安装了下面这些包：</p>
<ul>
<li>某个版本的 <strong>Python</strong> (这里用的是 3.7）</li>
<li><strong>apache-flink</strong> (这里用的是 1.13.1)</li>
<li><strong>jupyter，grpcio，protobuf</strong> (这三个包是 Zeppelin 需要的)</li>
</ul>
<p>剩下的包可以根据需要来指定：</p>
<pre><code class="copyable">%sh

# make sure you have conda and momba installed.
# install miniconda: https://docs.conda.io/en/latest/miniconda.html
# install mamba: https://github.com/mamba-org/mamba

echo "name: pyflink_env
channels:
  - conda-forge
  - defaults
dependencies:
  - Python=3.7
  - pip
  - pip:
    - apache-flink==1.13.1
  - jupyter
  - grpcio
  - protobuf
  - matplotlib
  - pandasql
  - pandas
  - scipy
  - seaborn
  - plotnine
 " > pyflink_env.yml
    
mamba env remove -n pyflink_env
mamba env create -f pyflink_env.yml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行下面的代码打包 PyFlink 的 Conda 环境并且上传到 HDFS (注意这里打包出来的文件格式是 tar.gz)：</p>
<pre><code class="copyable">%sh

rm -rf pyflink_env.tar.gz
conda pack --ignore-missing-files -n pyflink_env -o pyflink_env.tar.gz

hadoop fs -rmr /tmp/pyflink_env.tar.gz
hadoop fs -put pyflink_env.tar.gz /tmp
# The Python conda tar should be public accessible, so need to change permission here.
hadoop fs -chmod 644 /tmp/pyflink_env.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Step 2. 制作 TaskManager 上的 PyFlink Conda 环境</strong></p>
<p>运行下面的代码来创建 TaskManager 上的 PyFlink Conda 环境，TaskManager 上的 PyFlink 环境至少包含以下 2 个包：</p>
<ul>
<li>某个版本的 <strong>Python</strong> (这里用的是 3.7）</li>
<li><strong>apache-flink</strong> (这里用的是 1.13.1)</li>
</ul>
<p>剩下的包是 Python UDF 需要依赖的包，比如这里指定了 pandas：</p>
<pre><code class="copyable">echo "name: pyflink_tm_env
channels:
  - conda-forge
  - defaults
dependencies:
  - Python=3.7
  - pip
  - pip:
    - apache-flink==1.13.1
  - pandas
 " > pyflink_tm_env.yml
    
mamba env remove -n pyflink_tm_env
mamba env create -f pyflink_tm_env.yml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行下面的代码打包 PyFlink 的 conda 环境并且上传到 HDFS (注意这里使用的是 zip 格式）</p>
<pre><code class="copyable">%sh

rm -rf pyflink_tm_env.zip
conda pack --ignore-missing-files --zip-symlinks -n pyflink_tm_env -o pyflink_tm_env.zip

hadoop fs -rmr /tmp/pyflink_tm_env.zip
hadoop fs -put pyflink_tm_env.zip /tmp
# The Python conda tar should be public accessible, so need to change permission here.
hadoop fs -chmod 644 /tmp/pyflink_tm_env.zip
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Step 3. 在 PyFlink 中使用 Conda 环境</strong></p>
<p>接下来就可以在 Zeppelin 中使用上面创建的 Conda 环境了，首先需要在 Zeppelin 里配置 Flink，主要配置的选项有：</p>
<ul>
<li>
<p>flink.execution.mode 为 yarn-application, 本文所讲的方法只适用于 yarn-application 模式；</p>
</li>
<li>
<p>指定 yarn.ship-archives，zeppelin.pyflink.Python 以及 zeppelin.interpreter.conda.env.name 来配置 JobManager 侧的 PyFlink Conda 环境；</p>
</li>
<li>
<p>指定 Python.archives 以及 Python.executable 来指定 TaskManager 侧的 PyFlink Conda 环境；</p>
</li>
<li>
<p>指定其他可选的 Flink 配置，比如这里的 flink.jm.memory 和 flink.tm.memory。</p>
<p>%flink.conf</p>
<p>flink.execution.mode yarn-application</p>
<p>yarn.ship-archives /mnt/disk1/jzhang/zeppelin/pyflink_env.tar.gz
zeppelin.pyflink.Python pyflink_env.tar.gz/bin/Python
zeppelin.interpreter.conda.env.name pyflink_env.tar.gz</p>
<p>Python.archives hdfs:///tmp/pyflink_tm_env.zip
Python.executable  pyflink_tm_env.zip/bin/Python3.7</p>
<p>flink.jm.memory 2048
flink.tm.memory 2048</p>
</li>
</ul>
<p>接下来就可以如一开始所说的那样在 Zeppelin 里使用 PyFlink 以及指定的 Conda 环境了。有 2 种场景:</p>
<ul>
<li>下面的例子里，可以在 <strong>PyFlink 客户端</strong> (JobManager 侧) 使用上面创建的 JobManager 侧的 Conda 环境，比如下边使用了 Matplotlib。</li>
<li>下面的例子是在 <strong>PyFlink UDF</strong> 里使用上面创建的 TaskManager 侧 Conda 环境里的库，比如下面在 UDF 里使用 Pandas。</li>
</ul>
<h1 data-id="heading-2">三、总结与未来</h1>
<p>本文内容就是在 Zeppelin notebook 里利用 Conda 来创建 Python env 自动部署到 Yarn 集群中，无需手动在集群上去安装任何 Pyflink 的包，并且可以在一个 Yarn 集群里同时使用多个版本的 PyFlink。</p>
<p>每个 PyFlink 的环境都是隔离的，而且可以随时定制更改 Conda 环境。可以下载下面这个 note 并导入到 Zeppelin，就可以复现今天讲的内容：<a href="https://link.juejin.cn/?target=http%3A%2F%2F23.254.161.240%2F%23%2Fnotebook%2F2G8N1WTTS" target="_blank" rel="nofollow noopener noreferrer" title="http://23.254.161.240/#/notebook/2G8N1WTTS" ref="nofollow noopener noreferrer">http://23.254.161.240/#/notebook/2G8N1WTTS</a></p>
<p>此外还有很多可以改进的地方：</p>
<ul>
<li>目前我们需要创建 2 个 conda env ，原因是 Zeppelin 支持 tar.gz 格式，而 Flink 只支持 zip 格式。等后期两边统一之后，只要创建一个 conda env 就可以；</li>
<li>apache-flink 现在包含了 Flink 的 jar 包，这就导致打出来的 conda env 特别大，yarn container 在初始化的时候耗时会比较长，这个需要 Flink 社区提供一个轻量级的 Python 包 (不包含 Flink jar 包)，就可以大大减小 conda env 的大小。</li>
</ul>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000291878%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000291878/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            